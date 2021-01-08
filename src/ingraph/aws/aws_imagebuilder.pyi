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

_NAMESPACE = "AWS::ImageBuilder"

class Component:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html"""

    Arn: Final[str]

    Type: Final[str]

    Encrypted: Final[bool]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Platform: str,
        Version: str,
        ChangeDescription: str = ...,
        Data: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        KmsKeyId: str = ...,
        SupportedOsVersions: List[str] = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...,
        Uri: str = ...
    ): ...

class DistributionConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Distributions: List["DistributionConfiguration.Distribution"],
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Distribution:
        def __init__(
            self,
            *,
            Region: str,
            AmiDistributionConfiguration: Any = ...,
            ContainerDistributionConfiguration: Any = ...,
            LicenseConfigurationArns: List[str] = ...
        ): ...

class Image:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html"""

    Arn: Final[str]

    Name: Final[str]

    ImageId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ImageRecipeArn: str,
        InfrastructureConfigurationArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DistributionConfigurationArn: str = ...,
        EnhancedImageMetadataEnabled: bool = ...,
        ImageTestsConfiguration: "Image.ImageTestsConfiguration" = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ImageTestsConfiguration:
        def __init__(
            self, *, ImageTestsEnabled: bool = ..., TimeoutMinutes: int = ...
        ): ...

class ImagePipeline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ImageRecipeArn: str,
        InfrastructureConfigurationArn: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DistributionConfigurationArn: str = ...,
        EnhancedImageMetadataEnabled: bool = ...,
        ImageTestsConfiguration: "ImagePipeline.ImageTestsConfiguration" = ...,
        Schedule: "ImagePipeline.Schedule" = ...,
        Status: str = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ImageTestsConfiguration:
        def __init__(
            self, *, ImageTestsEnabled: bool = ..., TimeoutMinutes: int = ...
        ): ...
    class Schedule:
        def __init__(
            self,
            *,
            PipelineExecutionStartCondition: str = ...,
            ScheduleExpression: str = ...
        ): ...

class ImageRecipe:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Components: List["ImageRecipe.ComponentConfiguration"],
        Name: str,
        ParentImage: str,
        Version: str,
        BlockDeviceMappings: List["ImageRecipe.InstanceBlockDeviceMapping"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...,
        WorkingDirectory: str = ...
    ): ...
    class ComponentConfiguration:
        def __init__(self, *, ComponentArn: str = ...): ...
    class EbsInstanceBlockDeviceSpecification:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Encrypted: bool = ...,
            Iops: int = ...,
            KmsKeyId: str = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class InstanceBlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str = ...,
            Ebs: "ImageRecipe.EbsInstanceBlockDeviceSpecification" = ...,
            NoDevice: str = ...,
            VirtualName: str = ...
        ): ...

class InfrastructureConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceProfileName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        InstanceTypes: List[str] = ...,
        KeyPair: str = ...,
        Logging: "InfrastructureConfiguration.Logging" = ...,
        ResourceTags: Dict[str, str] = ...,
        SecurityGroupIds: List[str] = ...,
        SnsTopicArn: str = ...,
        SubnetId: str = ...,
        Tags: Dict[str, str] = ...,
        TerminateInstanceOnFailure: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Logging:
        def __init__(self, *, S3Logs: "InfrastructureConfiguration.S3Logs" = ...): ...
    class S3Logs:
        def __init__(self, *, S3BucketName: str = ..., S3KeyPrefix: str = ...): ...
