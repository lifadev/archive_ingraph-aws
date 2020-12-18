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

_NAMESPACE = "AWS::Lambda"

class Alias:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        FunctionVersion: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ProvisionedConcurrencyConfig: "Alias.ProvisionedConcurrencyConfiguration" = ...,
        RoutingConfig: "Alias.AliasRoutingConfiguration" = ...,
        UpdatePolicy: "Alias.UpdatePolicy" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AliasRoutingConfiguration:
        def __init__(
            self, *, AdditionalVersionWeights: List["Alias.VersionWeight"]
        ): ...
    class ProvisionedConcurrencyConfiguration:
        def __init__(self, *, ProvisionedConcurrentExecutions: int): ...
    class UpdatePolicy:
        def __init__(
            self,
            *,
            ApplicationName: str,
            DeploymentGroupName: str,
            AfterAllowTrafficHook: str = ...,
            BeforeAllowTrafficHook: str = ...
        ): ...
    class VersionWeight:
        def __init__(self, *, FunctionVersion: str, FunctionWeight: float): ...

class CodeSigningConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html"""

    CodeSigningConfigId: Final[str]

    CodeSigningConfigArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllowedPublishers: "CodeSigningConfig.AllowedPublishers",
        CodeSigningPolicies: "CodeSigningConfig.CodeSigningPolicies" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AllowedPublishers:
        def __init__(self, *, SigningProfileVersionArns: List[str]): ...
    class CodeSigningPolicies:
        def __init__(self, *, UntrustedArtifactOnDeployment: str): ...

class EventInvokeConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationConfig: "EventInvokeConfig.DestinationConfig" = ...,
        MaximumEventAgeInSeconds: int = ...,
        MaximumRetryAttempts: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DestinationConfig:
        def __init__(
            self,
            *,
            OnFailure: "EventInvokeConfig.OnFailure" = ...,
            OnSuccess: "EventInvokeConfig.OnSuccess" = ...
        ): ...
    class OnFailure:
        def __init__(self, *, Destination: str): ...
    class OnSuccess:
        def __init__(self, *, Destination: str): ...

class EventSourceMapping:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html"""

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        BatchSize: int = ...,
        BisectBatchOnFunctionError: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationConfig: "EventSourceMapping.DestinationConfig" = ...,
        Enabled: bool = ...,
        EventSourceArn: str = ...,
        FunctionResponseTypes: List[str] = ...,
        MaximumBatchingWindowInSeconds: int = ...,
        MaximumRecordAgeInSeconds: int = ...,
        MaximumRetryAttempts: int = ...,
        ParallelizationFactor: int = ...,
        PartialBatchResponse: bool = ...,
        Queues: List[str] = ...,
        SelfManagedEventSource: "EventSourceMapping.SelfManagedEventSource" = ...,
        SourceAccessConfigurations: List[
            "EventSourceMapping.SourceAccessConfiguration"
        ] = ...,
        StartingPosition: str = ...,
        Topics: List[str] = ...,
        TumblingWindowInSeconds: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DestinationConfig:
        def __init__(self, *, OnFailure: "EventSourceMapping.OnFailure" = ...): ...
    class Endpoints:
        def __init__(self, *, KafkaBootstrapServers: List[str] = ...): ...
    class OnFailure:
        def __init__(self, *, Destination: str = ...): ...
    class SelfManagedEventSource:
        def __init__(self, *, Endpoints: "EventSourceMapping.Endpoints" = ...): ...
    class SourceAccessConfiguration:
        def __init__(self, *, Type: str = ..., URI: str = ...): ...

class Function:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Code: "Function.Code",
        Role: str,
        CodeSigningConfigArn: str = ...,
        DeadLetterConfig: "Function.DeadLetterConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Environment: "Function.Environment" = ...,
        FileSystemConfigs: List["Function.FileSystemConfig"] = ...,
        FunctionName: str = ...,
        Handler: str = ...,
        ImageConfig: "Function.ImageConfig" = ...,
        KmsKeyArn: str = ...,
        Layers: List[str] = ...,
        MemorySize: int = ...,
        PackageType: str = ...,
        ReservedConcurrentExecutions: int = ...,
        Runtime: str = ...,
        Tags: List["Tag"] = ...,
        Timeout: int = ...,
        TracingConfig: "Function.TracingConfig" = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Function.VpcConfig" = ...
    ): ...
    class Code:
        def __init__(
            self,
            *,
            ImageUri: str = ...,
            S3Bucket: str = ...,
            S3Key: str = ...,
            S3ObjectVersion: str = ...,
            ZipFile: str = ...
        ): ...
    class DeadLetterConfig:
        def __init__(self, *, TargetArn: str = ...): ...
    class Environment:
        def __init__(self, *, Variables: Dict[str, str] = ...): ...
    class FileSystemConfig:
        def __init__(self, *, Arn: str, LocalMountPath: str): ...
    class ImageConfig:
        def __init__(
            self,
            *,
            Command: List[str] = ...,
            EntryPoint: List[str] = ...,
            WorkingDirectory: str = ...
        ): ...
    class TracingConfig:
        def __init__(self, *, Mode: str = ...): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], SubnetIds: List[str]): ...

class LayerVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Content: "LayerVersion.Content",
        CompatibleRuntimes: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LayerName: str = ...,
        LicenseInfo: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Content:
        def __init__(
            self, *, S3Bucket: str, S3Key: str, S3ObjectVersion: str = ...
        ): ...

class LayerVersionPermission:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        LayerVersionArn: str,
        Principal: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        OrganizationId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Permission:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        FunctionName: str,
        Principal: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EventSourceToken: str = ...,
        SourceAccount: str = ...,
        SourceArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Version:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html"""

    Version_: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        CodeSha256: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ProvisionedConcurrencyConfig: "Version.ProvisionedConcurrencyConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ProvisionedConcurrencyConfiguration:
        def __init__(self, *, ProvisionedConcurrentExecutions: int): ...
