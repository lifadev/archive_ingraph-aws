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

_NAMESPACE = "AWS::Batch"

class ComputeEnvironment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ServiceRole: str,
        Type: str,
        ComputeEnvironmentName: str = ...,
        ComputeResources: "ComputeEnvironment.ComputeResources" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        State: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ComputeResources:
        def __init__(
            self,
            *,
            MaxvCpus: int,
            Subnets: List[str],
            Type: str,
            AllocationStrategy: str = ...,
            BidPercentage: int = ...,
            DesiredvCpus: int = ...,
            Ec2Configuration: List["ComputeEnvironment.Ec2ConfigurationObject"] = ...,
            Ec2KeyPair: str = ...,
            ImageId: str = ...,
            InstanceRole: str = ...,
            InstanceTypes: List[str] = ...,
            LaunchTemplate: "ComputeEnvironment.LaunchTemplateSpecification" = ...,
            MinvCpus: int = ...,
            PlacementGroup: str = ...,
            SecurityGroupIds: List[str] = ...,
            SpotIamFleetRole: str = ...,
            Tags: Any = ...
        ): ...
    class Ec2ConfigurationObject:
        def __init__(self, *, ImageType: str, ImageIdOverride: str = ...): ...
    class LaunchTemplateSpecification:
        def __init__(
            self,
            *,
            LaunchTemplateId: str = ...,
            LaunchTemplateName: str = ...,
            Version: str = ...
        ): ...

class JobDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Type: str,
        ContainerProperties: "JobDefinition.ContainerProperties" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobDefinitionName: str = ...,
        NodeProperties: "JobDefinition.NodeProperties" = ...,
        Parameters: Any = ...,
        PlatformCapabilities: List[str] = ...,
        PropagateTags: bool = ...,
        RetryStrategy: "JobDefinition.RetryStrategy" = ...,
        Tags: Any = ...,
        Timeout: "JobDefinition.Timeout" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ContainerProperties:
        def __init__(
            self,
            *,
            Image: str,
            Command: List[str] = ...,
            Environment: List["JobDefinition.Environment"] = ...,
            ExecutionRoleArn: str = ...,
            FargatePlatformConfiguration: "JobDefinition.FargatePlatformConfiguration" = ...,
            InstanceType: str = ...,
            JobRoleArn: str = ...,
            LinuxParameters: "JobDefinition.LinuxParameters" = ...,
            LogConfiguration: "JobDefinition.LogConfiguration" = ...,
            Memory: int = ...,
            MountPoints: List["JobDefinition.MountPoints"] = ...,
            NetworkConfiguration: "JobDefinition.NetworkConfiguration" = ...,
            Privileged: bool = ...,
            ReadonlyRootFilesystem: bool = ...,
            ResourceRequirements: List["JobDefinition.ResourceRequirement"] = ...,
            Secrets: List["JobDefinition.Secret"] = ...,
            Ulimits: List["JobDefinition.Ulimit"] = ...,
            User: str = ...,
            Vcpus: int = ...,
            Volumes: List["JobDefinition.Volumes"] = ...
        ): ...
    class Device:
        def __init__(
            self,
            *,
            ContainerPath: str = ...,
            HostPath: str = ...,
            Permissions: List[str] = ...
        ): ...
    class Environment:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...
    class EvaluateOnExit:
        def __init__(
            self,
            *,
            Action: str,
            OnExitCode: str = ...,
            OnReason: str = ...,
            OnStatusReason: str = ...
        ): ...
    class FargatePlatformConfiguration:
        def __init__(self, *, PlatformVersion: str = ...): ...
    class LinuxParameters:
        def __init__(
            self,
            *,
            Devices: List["JobDefinition.Device"] = ...,
            InitProcessEnabled: bool = ...,
            MaxSwap: int = ...,
            SharedMemorySize: int = ...,
            Swappiness: int = ...,
            Tmpfs: List["JobDefinition.Tmpfs"] = ...
        ): ...
    class LogConfiguration:
        def __init__(
            self,
            *,
            LogDriver: str,
            Options: Any = ...,
            SecretOptions: List["JobDefinition.Secret"] = ...
        ): ...
    class MountPoints:
        def __init__(
            self,
            *,
            ContainerPath: str = ...,
            ReadOnly: bool = ...,
            SourceVolume: str = ...
        ): ...
    class NetworkConfiguration:
        def __init__(self, *, AssignPublicIp: str = ...): ...
    class NodeProperties:
        def __init__(
            self,
            *,
            MainNode: int,
            NodeRangeProperties: List["JobDefinition.NodeRangeProperty"],
            NumNodes: int
        ): ...
    class NodeRangeProperty:
        def __init__(
            self,
            *,
            TargetNodes: str,
            Container: "JobDefinition.ContainerProperties" = ...
        ): ...
    class ResourceRequirement:
        def __init__(self, *, Type: str = ..., Value: str = ...): ...
    class RetryStrategy:
        def __init__(
            self,
            *,
            Attempts: int = ...,
            EvaluateOnExit: List["JobDefinition.EvaluateOnExit"] = ...
        ): ...
    class Secret:
        def __init__(self, *, Name: str, ValueFrom: str): ...
    class Timeout:
        def __init__(self, *, AttemptDurationSeconds: int = ...): ...
    class Tmpfs:
        def __init__(
            self, *, ContainerPath: str, Size: int, MountOptions: List[str] = ...
        ): ...
    class Ulimit:
        def __init__(self, *, HardLimit: int, Name: str, SoftLimit: int): ...
    class Volumes:
        def __init__(
            self, *, Host: "JobDefinition.VolumesHost" = ..., Name: str = ...
        ): ...
    class VolumesHost:
        def __init__(self, *, SourcePath: str = ...): ...

class JobQueue:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ComputeEnvironmentOrder: List["JobQueue.ComputeEnvironmentOrder"],
        Priority: int,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobQueueName: str = ...,
        State: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ComputeEnvironmentOrder:
        def __init__(self, *, ComputeEnvironment: str, Order: int): ...
