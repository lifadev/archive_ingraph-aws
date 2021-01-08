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

_NAMESPACE = "AWS::IoTWireless"

class Destination:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Expression: str,
        ExpressionType: str,
        Name: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        NextToken: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DeviceProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LoRaWANDeviceProfile: "DeviceProfile.LoRaWANDeviceProfile" = ...,
        Name: str = ...,
        NextToken: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LoRaWANDeviceProfile:
        def __init__(
            self,
            *,
            ClassBTimeout: int = ...,
            ClassCTimeout: int = ...,
            MacVersion: str = ...,
            MaxDutyCycle: int = ...,
            MaxEirp: int = ...,
            PingSlotDr: int = ...,
            PingSlotFreq: int = ...,
            PingSlotPeriod: int = ...,
            RegParamsRevision: str = ...,
            RfRegion: str = ...,
            Supports32BitFCnt: bool = ...,
            SupportsClassB: bool = ...,
            SupportsClassC: bool = ...,
            SupportsJoin: bool = ...
        ): ...

class ServiceProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LoRaWANGetServiceProfileInfo: "ServiceProfile.LoRaWANGetServiceProfileInfo" = ...,
        LoRaWANServiceProfile: "ServiceProfile.LoRaWANServiceProfile" = ...,
        Name: str = ...,
        NextToken: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LoRaWANGetServiceProfileInfo:
        def __init__(
            self,
            *,
            AddGwMetadata: bool = ...,
            ChannelMask: str = ...,
            DevStatusReqFreq: int = ...,
            DlBucketSize: int = ...,
            DlRate: int = ...,
            DlRatePolicy: str = ...,
            DrMax: int = ...,
            DrMin: int = ...,
            HrAllowed: bool = ...,
            MinGwDiversity: int = ...,
            NwkGeoLoc: bool = ...,
            PrAllowed: bool = ...,
            RaAllowed: bool = ...,
            ReportDevStatusBattery: bool = ...,
            ReportDevStatusMargin: bool = ...,
            TargetPer: int = ...,
            UlBucketSize: int = ...,
            UlRate: int = ...,
            UlRatePolicy: str = ...
        ): ...
    class LoRaWANServiceProfile:
        def __init__(self, *, AddGwMetadata: bool = ...): ...

class WirelessDevice:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html"""

    Arn: Final[str]

    Id: Final[str]

    ThingArn: Final[str]

    ThingName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationName: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LoRaWANDevice: "WirelessDevice.LoRaWANDevice" = ...,
        Name: str = ...,
        NextToken: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AbpV10X:
        def __init__(
            self, *, DevAddr: str, SessionKeys: "WirelessDevice.SessionKeysAbpV10X"
        ): ...
    class AbpV11:
        def __init__(
            self, *, DevAddr: str, SessionKeys: "WirelessDevice.SessionKeysAbpV11"
        ): ...
    class LoRaWANDevice:
        def __init__(
            self,
            *,
            AbpV10X: "WirelessDevice.AbpV10X" = ...,
            AbpV11: "WirelessDevice.AbpV11" = ...,
            DevEui: str = ...,
            DeviceProfileId: str = ...,
            OtaaV10X: "WirelessDevice.OtaaV10X" = ...,
            OtaaV11: "WirelessDevice.OtaaV11" = ...,
            ServiceProfileId: str = ...
        ): ...
    class OtaaV10X:
        def __init__(self, *, AppEui: str, AppKey: str): ...
    class OtaaV11:
        def __init__(self, *, AppKey: str, JoinEui: str, NwkKey: str): ...
    class SessionKeysAbpV10X:
        def __init__(self, *, AppSKey: str, NwkSKey: str): ...
    class SessionKeysAbpV11:
        def __init__(
            self, *, AppSKey: str, FNwkSIntKey: str, NwkSEncKey: str, SNwkSIntKey: str
        ): ...

class WirelessGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html"""

    Arn: Final[str]

    Id: Final[str]

    ThingArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        LoRaWANGateway: "WirelessGateway.LoRaWANGateway",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        NextToken: str = ...,
        Tags: List["Tag"] = ...,
        ThingName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LoRaWANGateway:
        def __init__(self, *, GatewayEui: str, RfRegion: str): ...
