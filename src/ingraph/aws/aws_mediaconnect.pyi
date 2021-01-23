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

_NAMESPACE = "AWS::MediaConnect"

class Flow:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html"""

    FlowArn: Final[str]

    FlowAvailabilityZone: Final[str]

    SourceArn: Final[str]

    IngestIp: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Source: "Flow.Source",
        AvailabilityZone: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SourceFailoverConfig: "Flow.FailoverConfig" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Encryption:
        def __init__(
            self,
            *,
            Algorithm: str,
            RoleArn: str,
            ConstantInitializationVector: str = ...,
            DeviceId: str = ...,
            KeyType: str = ...,
            Region: str = ...,
            ResourceId: str = ...,
            SecretArn: str = ...,
            Url: str = ...
        ): ...
    class FailoverConfig:
        def __init__(self, *, RecoveryWindow: int = ..., State: str = ...): ...
    class Source:
        def __init__(
            self,
            *,
            Decryption: "Flow.Encryption" = ...,
            Description: str = ...,
            EntitlementArn: str = ...,
            IngestIp: str = ...,
            IngestPort: int = ...,
            MaxBitrate: int = ...,
            MaxLatency: int = ...,
            Name: str = ...,
            Protocol: str = ...,
            SourceArn: str = ...,
            StreamId: str = ...,
            VpcInterfaceName: str = ...,
            WhitelistCidr: str = ...
        ): ...

class FlowEntitlement:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html"""

    EntitlementArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        FlowArn: str,
        Name: str,
        Subscribers: List[str],
        DataTransferSubscriberFeePercent: int = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Encryption: "FlowEntitlement.Encryption" = ...,
        EntitlementStatus: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Encryption:
        def __init__(
            self,
            *,
            Algorithm: str,
            RoleArn: str,
            ConstantInitializationVector: str = ...,
            DeviceId: str = ...,
            KeyType: str = ...,
            Region: str = ...,
            ResourceId: str = ...,
            SecretArn: str = ...,
            Url: str = ...
        ): ...

class FlowOutput:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html"""

    OutputArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FlowArn: str,
        Protocol: str,
        CidrAllowList: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Destination: str = ...,
        Encryption: "FlowOutput.Encryption" = ...,
        MaxLatency: int = ...,
        Name: str = ...,
        Port: int = ...,
        RemoteId: str = ...,
        SmoothingLatency: int = ...,
        StreamId: str = ...,
        UpdateReplacePolicy: str = ...,
        VpcInterfaceAttachment: "FlowOutput.VpcInterfaceAttachment" = ...
    ): ...
    class Encryption:
        def __init__(
            self, *, Algorithm: str, RoleArn: str, SecretArn: str, KeyType: str = ...
        ): ...
    class VpcInterfaceAttachment:
        def __init__(self, *, VpcInterfaceName: str = ...): ...

class FlowSource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html"""

    SourceArn: Final[str]

    IngestIp: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        Name: str,
        Decryption: "FlowSource.Encryption" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EntitlementArn: str = ...,
        FlowArn: str = ...,
        IngestPort: int = ...,
        MaxBitrate: int = ...,
        MaxLatency: int = ...,
        Protocol: str = ...,
        StreamId: str = ...,
        UpdateReplacePolicy: str = ...,
        VpcInterfaceName: str = ...,
        WhitelistCidr: str = ...
    ): ...
    class Encryption:
        def __init__(
            self,
            *,
            Algorithm: str,
            RoleArn: str,
            ConstantInitializationVector: str = ...,
            DeviceId: str = ...,
            KeyType: str = ...,
            Region: str = ...,
            ResourceId: str = ...,
            SecretArn: str = ...,
            Url: str = ...
        ): ...

class FlowVpcInterface:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html"""

    NetworkInterfaceIds: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FlowArn: str,
        Name: str,
        RoleArn: str,
        SecurityGroupIds: List[str],
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
