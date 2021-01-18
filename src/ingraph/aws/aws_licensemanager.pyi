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
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GrantName: str = ...,
        HomeRegion: str = ...,
        LicenseArn: str = ...,
        Principals: List[str] = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

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
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LicenseMetadata: List["License.Metadata"] = ...,
        ProductSKU: str = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
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
            MaxCount: int = ...,
            Overage: bool = ...,
            Value: str = ...
        ): ...
    class IssuerData:
        def __init__(self, *, Name: str, SignKey: str = ...): ...
    class Metadata:
        def __init__(self, *, Name: str, Value: str): ...
    class ProvisionalConfiguration:
        def __init__(self, *, MaxTimeToLiveInMinutes: int): ...
    class ValidityDateFormat:
        def __init__(self, *, Begin: str, End: str): ...
