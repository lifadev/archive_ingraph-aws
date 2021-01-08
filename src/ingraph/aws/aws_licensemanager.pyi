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

from typing import Any, Dict, Final, List

from . import Tag

_NAMESPACE = "AWS::LicenseManager"

class Grant:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html"""

    GrantArn: Final[str]

    Version: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllowedOperations: List[str] = ...,
        ClientToken: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Filters: List["Grant.Filter"] = ...,
        GrantArns: List[str] = ...,
        GrantName: str = ...,
        GrantStatus: str = ...,
        GrantedOperations: List[str] = ...,
        GranteePrincipalArn: str = ...,
        HomeRegion: str = ...,
        LicenseArn: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        ParentArn: str = ...,
        Principals: List[str] = ...,
        SourceVersion: str = ...,
        Status: str = ...,
        StatusReason: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class Filter:
        def __init__(self, *, Name: str, Values: "Grant.StringList"): ...
    class StringList:
        def __init__(self, *, StringList: List[str] = ...): ...

class License:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html"""

    LicenseArn: Final[str]

    Version: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConsumptionConfiguration: "License.ConsumptionConfiguration",
        Entitlements: List["License.Entitlement"],
        HomeRegion: str,
        Issuer: "License.IssuerData",
        LicenseName: str,
        ProductName: str,
        Validity: "License.ValidityDateFormat",
        Beneficiary: str = ...,
        ClientToken: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Filters: List["License.Filter"] = ...,
        LicenseArns: List[str] = ...,
        LicenseMetadata: List["License.Metadata"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        ProductSKU: str = ...,
        SourceVersion: str = ...,
        Status: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class BorrowConfiguration:
        def __init__(self, *, AllowEarlyCheckIn: bool, MaxTimeToLiveInMinutes: int): ...
    class ConsumptionConfiguration:
        def __init__(
            self,
            *,
            BorrowConfiguration: "License.BorrowConfiguration" = ...,
            ProvisionalConfiguration: "License.ProvisionalConfiguration" = ...,
            RenewType: str = ...
        ): ...
    class Entitlement:
        def __init__(
            self,
            *,
            Name: str,
            Unit: str,
            AllowCheckIn: bool = ...,
            CheckoutRules: "License.RuleList" = ...,
            MaxCount: int = ...,
            Overage: bool = ...,
            Value: str = ...
        ): ...
    class Filter:
        def __init__(self, *, Name: str, Values: "License.StringList"): ...
    class IssuerData:
        def __init__(self, *, Name: str, SignKey: str = ...): ...
    class Metadata:
        def __init__(self, *, Name: str, Value: str): ...
    class ProvisionalConfiguration:
        def __init__(self, *, MaxTimeToLiveInMinutes: int): ...
    class Rule:
        def __init__(self, *, Name: str, Unit: str, Value: str): ...
    class RuleList:
        def __init__(self, *, RuleList: List["License.Rule"] = ...): ...
    class StringList:
        def __init__(self, *, StringList: List[str] = ...): ...
    class ValidityDateFormat:
        def __init__(self, *, Begin: str, End: str): ...
