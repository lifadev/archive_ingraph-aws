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

_NAMESPACE = "AWS::GreengrassV2"

class ComponentVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html"""

    Arn: Final[str]

    ComponentName: Final[str]

    ComponentVersion_: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InlineRecipe: str = ...,
        LambdaFunction: "ComponentVersion.LambdaFunctionRecipeSource" = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ComponentDependencyRequirement:
        def __init__(
            self, *, DependencyType: str = ..., VersionRequirement: str = ...
        ): ...
    class ComponentPlatform:
        def __init__(self, *, Attributes: Dict[str, str] = ..., Name: str = ...): ...
    class LambdaContainerParams:
        def __init__(
            self,
            *,
            Devices: List["ComponentVersion.LambdaDeviceMount"] = ...,
            MemorySizeInKB: int = ...,
            MountROSysfs: bool = ...,
            Volumes: List["ComponentVersion.LambdaVolumeMount"] = ...
        ): ...
    class LambdaDeviceMount:
        def __init__(
            self, *, AddGroupOwner: bool = ..., Path: str = ..., Permission: str = ...
        ): ...
    class LambdaEventSource:
        def __init__(self, *, Topic: str = ..., Type: str = ...): ...
    class LambdaExecutionParameters:
        def __init__(
            self,
            *,
            EnvironmentVariables: Dict[str, str] = ...,
            EventSources: List["ComponentVersion.LambdaEventSource"] = ...,
            ExecArgs: List[str] = ...,
            InputPayloadEncodingType: str = ...,
            LinuxProcessParams: "ComponentVersion.LambdaLinuxProcessParams" = ...,
            MaxIdleTimeInSeconds: int = ...,
            MaxInstancesCount: int = ...,
            MaxQueueSize: int = ...,
            Pinned: bool = ...,
            StatusTimeoutInSeconds: int = ...,
            TimeoutInSeconds: int = ...
        ): ...
    class LambdaFunctionRecipeSource:
        def __init__(
            self,
            *,
            ComponentDependencies: Dict[
                str, "ComponentVersion.ComponentDependencyRequirement"
            ] = ...,
            ComponentLambdaParameters: "ComponentVersion.LambdaExecutionParameters" = ...,
            ComponentName: str = ...,
            ComponentPlatforms: List["ComponentVersion.ComponentPlatform"] = ...,
            ComponentVersion: str = ...,
            LambdaArn: str = ...
        ): ...
    class LambdaLinuxProcessParams:
        def __init__(
            self,
            *,
            ContainerParams: "ComponentVersion.LambdaContainerParams" = ...,
            IsolationMode: str = ...
        ): ...
    class LambdaVolumeMount:
        def __init__(
            self,
            *,
            AddGroupOwner: bool = ...,
            DestinationPath: str = ...,
            Permission: str = ...,
            SourcePath: str = ...
        ): ...
