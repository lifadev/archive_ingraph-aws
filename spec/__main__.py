# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gzip
import io
import json
from functools import reduce
from pathlib import Path
from typing import Any, Dict, Mapping
from urllib.request import Request, urlopen

import jinja2

HERE = Path(__file__).parent

ENDPOINT = (
    "https://cfn-resource-specifications-{region}-prod.s3.{region}.amazonaws.com"
    "/latest/gzip/CloudFormationResourceSpecification.json"
)
REGIONS = {
    # Africa
    "af-south-1": "Africa (Cape Town)",
    # Asia Pacific
    "ap-east-1": "Asia Pacific (Hong Kong)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-northeast-3": "Asia Pacific (Osaka-Local)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    # Canada
    "ca-central-1": "Canada (Central)",
    # China
    "cn-north-1": "China (Beijing)",
    "cn-northwest-1": "China (Ningxia)",
    # Europe
    "eu-central-1": "EU (Frankfurt)",
    "eu-north-1": "EU (Stockholm)",
    "eu-south-1": "EU (Milan)",
    "eu-west-1": "EU (Ireland)",
    "eu-west-2": "EU (London)",
    "eu-west-3": "EU (Paris)",
    # Middle East
    "me-south-1": "Middle East (Bahrain)",
    # South America
    "sa-east-1": "South America (São Paulo)",
    # United States
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    # GovCloud
    "us-gov-east-1": "AWS GovCloud (US-East)",
    "us-gov-west-1": "AWS GovCloud (US-West)",
}


_PTSKEY = "PropertyTypes"
_RTSKEY = "ResourceTypes"
_ASKEY = "Attributes"
_PSKEY = "Properties"


def _download() -> Mapping[str, Any]:
    res: Dict[str, Any] = {}
    for region in REGIONS:
        print(region)
        res[region] = json.loads(_getdata(_geturl(region)))
    return res


def _getdata(url: str) -> str:
    req = Request(url)
    req.add_header("Accept-encoding", "gzip")
    res = urlopen(req)
    if res.info().get("Content-Encoding") == "gzip":
        buf = io.BytesIO(res.read())
        f = gzip.GzipFile(fileobj=buf)
        return f.read().decode()
    return res.read().decode()


def _geturl(region: str) -> str:
    """Returns a region specific specification url."""
    url = ENDPOINT.format(region=region)
    if region.startswith("cn-"):
        url = url.replace("amazonaws.com", "amazonaws.com.cn")
    return url


def _getversions(data: Mapping[str, Any]) -> Mapping[str, str]:
    """Returns all regions specification versions."""
    return {k: v["ResourceSpecificationVersion"] for k, v in data.items()}


def _merge(data: Mapping[str, Any]) -> Any:
    """Merges all regions resources."""
    ref: Any = {_PTSKEY: {}, _RTSKEY: {}}
    for region, datum in data.items():
        for part in (_PTSKEY, _RTSKEY):
            for key, value in datum[part].items():
                if key not in ref[part]:
                    ref[part][key] = value
                else:
                    for subpart in ("Attributes", "Properties"):
                        if subpart in value:
                            ref[part][key].setdefault(subpart, {}).update(
                                value[subpart]
                            )
                if part == _RTSKEY:
                    ref[part][key].setdefault("Attributes", {}).update(
                        Ref=dict(PrimitiveType="String")
                    )
    return ref


def _add_policies(data: Any) -> None:
    """Extends resources properties to include the lifecycle policies."""
    policies = json.loads((HERE / "policies.json").read_text())
    for key, value in policies[_RTSKEY].items():
        datum = data[_RTSKEY][key]
        if set(value[_PSKEY]) & set(datum[_PSKEY]):
            raise NotImplementedError("policy overwrites existing property")
        datum[_PSKEY].update(value[_PSKEY])
    if any(k in data[_PTSKEY] for k in policies[_PTSKEY]):
        raise NotImplementedError("policy overwrites existing property")
    data[_PTSKEY].update(policies[_PTSKEY])
    coms = dict(
        DeletionPolicy=dict(PrimitiveType="String", Required=False),
        UpdateReplacePolicy=dict(PrimitiveType="String", Required=False),
        DependsOn=dict(Type="List", PrimitiveItemType="Json", Required=False),
    )
    for value in data[_RTSKEY].values():
        if any(c in value[_PSKEY] for c in coms):
            raise NotImplementedError("policy overwrites existing property")
        value[_PSKEY].update(coms)


def _colocate(data: Any) -> Any:
    """Moves property types next to their resource types."""
    res: Any = data[_RTSKEY]
    for key, value in data[_PTSKEY].items():
        if "." in key:
            resc, prop = key.split(".")
            curr = res[resc]
            curr.setdefault(_PTSKEY, {})[prop] = value
    for value in res.values():
        value.setdefault(_PTSKEY, {})
    return res


_RESERVED = {"None"}


def _nomalize_attrs(data: Any) -> None:
    """Renames illegal attributes."""
    for name, value in data.items():
        coms = {name.rpartition("::")[-1]} | _RESERVED
        value[_ASKEY] = {
            k.replace(".", "_") + ("_" if k in coms else ""): v
            for k, v in value[_ASKEY].items()
        }
        # patch 16.0.0
        if name == "AWS::ServiceCatalog::CloudFormationProvisionedProduct":
            bad = value[_ASKEY].get("Outputs", {})
            if bad.get("Type") == "Map" and bad.get("PrimitiveItemType") == "String":
                del value[_ASKEY]["Outputs"]
            else:
                raise NotImplementedError("patch outdated")


def _normalize_props(data: Any) -> None:
    """Renames illegal properties."""
    for name, value in data.items():
        coms = _RESERVED
        value[_PSKEY] = {
            k + ("_" if k in coms else ""): v for k, v in value[_PSKEY].items()
        }
        # patch 12.3.0
        if name == "AWS::ImageBuilder::InfrastructureConfiguration":
            bad = value[_PSKEY].get("Logging", {})
            if bad.get("Type") == "Logging" and bad.get("PrimitiveType") == "Json":
                del bad["PrimitiveType"]
            else:
                raise NotImplementedError("patch outdated")


def _normalize_proptypes(data: Any) -> None:
    """Renames illegal property types."""
    for name, value in data.items():
        coms = {name.rpartition("::")[-1]} | _RESERVED | set(value[_ASKEY])
        ptypes = {}
        ptrans = {}
        for k, v in value[_PTSKEY].items():
            # patch 16.3.0
            if name == "AWS::ECS::TaskDefinition" and k == "EFSVolumeConfiguration":
                bad = v[_PSKEY].get("AuthorizationConfig")
                if (
                    bad.get("Type") == "AuthorizationConfig"
                    and bad.get("PrimitiveType") == "Json"
                ):
                    del bad["PrimitiveType"]
                else:
                    raise NotImplementedError("patch outdated")
            if k not in coms:
                ptypes[k] = v
                continue
            alias = f"{k}_"
            ptrans[k] = alias
            ptypes[alias] = v
        value[_PTSKEY] = ptypes
        for orig, alias in ptrans.items():
            entries = list(value[_PSKEY].values())
            for ptype in value.get(_PTSKEY, {}).values():
                entries.extend(ptype[_PSKEY].values() if _PSKEY in ptype else [ptype])
            for entry in entries:
                for k, v in entry.items():
                    entry[k] = v if v != orig else alias


def _normalize_proptypes_props(data: Any) -> None:
    """Renames illegal property types properties."""
    for name, entry in data.items():
        for value in entry[_PTSKEY].values():
            if _PSKEY not in value:
                continue
            coms = _RESERVED
            postfix = "_"
            value[_PSKEY] = {
                **{k: v for k, v in value[_PSKEY].items() if k not in coms},
                **{f"{k}{postfix}": v for k, v in value[_PSKEY].items() if k in coms},
            }


def _flatten(data: Any) -> Any:
    """Moves all 'VND::SVC::COMS' to the 'VND::SVC' level."""
    res: Any = {}
    for key, value in data.items():
        pkg, _, com = key.rpartition("::")
        res.setdefault(pkg, {})[com] = value
    return res


def _generate(data: Any) -> None:
    src = HERE.parent / "src" / "ingraph" / "aws"
    tpl = jinja2.Template((HERE / "module.py.j2").read_text())
    for key, value in data.items():
        vnd, svc = key.split("::")
        path = src / f"{vnd.lower()}_{svc.lower()}.pyi"
        path.write_text(
            tpl.render(
                sorted=sorted,
                namespace=key,
                data=value,
                getproptype=_getproptype,
                getattrtype=_getattrtype,
            )
        )


_PTYPES = dict(
    Boolean="bool",
    Double="float",
    Integer="int",
    Json="Any",
    Long="int",
    String="str",
    Timestamp="str",
)


def _getproptype(data: Any, spec: Any, parent: str) -> str:
    hint = {k for k in spec.keys() if k.endswith("Type") and k != "UpdateType"}
    if "PrimitiveType" in spec:
        if hint != {"PrimitiveType"}:
            raise NotImplementedError(f"unknown hint: {hint}")
        return _PTYPES[spec["PrimitiveType"]]
    if "PrimitiveItemType" in spec:
        if hint != {"Type", "PrimitiveItemType"}:
            raise NotImplementedError(f"unknown hint: {hint}")
        cnt = spec["Type"]
        typ = _PTYPES[spec["PrimitiveItemType"]]
        if cnt == "List":
            return f"List[{typ}]"
        if cnt == "Map":
            return f"Dict[str, {typ}]"
        raise NotImplementedError(f"unknown container type: {cnt}")
    if "ItemType" in spec:
        if hint != {"Type", "ItemType"}:
            raise NotImplementedError(f"unknown hint: {hint}")
        cnt = spec["Type"]
        typ = spec["ItemType"]
        if typ in data and "Properties" not in data[typ]:
            typ = _getproptype(data, data[typ], parent)
        elif typ in _PTYPES:
            typ = _PTYPES[typ]
        else:
            typ = f'"{parent}.{typ}"' if typ != "Tag" else f'"{typ}"'
        if cnt == "List":
            return f"List[{typ}]"
        if cnt == "Map":
            return f"Dict[str, {typ}]"
        raise NotImplementedError(f"unknown container type: {cnt}")
    if hint != {"Type"}:
        raise NotImplementedError(f"unknown hint: {hint}")
    typ = spec["Type"]
    if typ in data and "Properties" not in data[typ]:
        return _getproptype(data, data[typ], parent)
    return f'"{parent}.{typ}"' if typ != "Tag" else f'"{typ}"'


_ATYPES = dict(Boolean="bool", Integer="int", Json="str", List="List", String="str")


def _getattrtype(spec: Any) -> str:
    return reduce(
        lambda c, p: f"{p}[{c}]",
        reversed(
            [
                _ATYPES[spec[t]]
                for t in ("PrimitiveType", "Type", "PrimitiveItemType")
                if t in spec
            ]
        ),
    )


if __name__ == "__main__":
    data = _download()
    versions = _getversions(data)
    data = _merge(data)
    _add_policies(data)
    data = _colocate(data)
    _nomalize_attrs(data)
    _normalize_props(data)
    _normalize_proptypes(data)
    _normalize_proptypes_props(data)
    data = _flatten(data)
    (HERE / "versions.json").write_text(json.dumps(versions))
    _generate(data)
    (HERE / "VERSION").write_text(max(versions.values()))
