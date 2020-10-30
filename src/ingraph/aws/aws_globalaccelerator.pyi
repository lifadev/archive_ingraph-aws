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

_NAMESPACE = "AWS::GlobalAccelerator"

class Accelerator:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html"""

    DnsName: Final[str]

    AcceleratorArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        IpAddressType: str = ...,
        IpAddresses: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EndpointGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html"""

    EndpointGroupArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndpointGroupRegion: str,
        ListenerArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointConfigurations: List["EndpointGroup.EndpointConfiguration"] = ...,
        HealthCheckIntervalSeconds: int = ...,
        HealthCheckPath: str = ...,
        HealthCheckPort: int = ...,
        HealthCheckProtocol: str = ...,
        PortOverrides: List["EndpointGroup.PortOverride"] = ...,
        ThresholdCount: int = ...,
        TrafficDialPercentage: float = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EndpointConfiguration:
        def __init__(
            self,
            *,
            EndpointId: str,
            ClientIPPreservationEnabled: bool = ...,
            Weight: int = ...
        ): ...
    class PortOverride:
        def __init__(self, *, EndpointPort: int, ListenerPort: int): ...

class Listener:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html"""

    ListenerArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AcceleratorArn: str,
        PortRanges: List["Listener.PortRange"],
        Protocol: str,
        ClientAffinity: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class PortRange:
        def __init__(self, *, FromPort: int, ToPort: int): ...
