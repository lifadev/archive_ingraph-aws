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

_NAMESPACE = "AWS::SageMaker"

class CodeRepository:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html"""

    CodeRepositoryName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GitConfig: "CodeRepository.GitConfig",
        CodeRepositoryName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GitConfig:
        def __init__(
            self, *, RepositoryUrl: str, Branch: str = ..., SecretArn: str = ...
        ): ...

class DataQualityJobDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html"""

    JobDefinitionArn: Final[str]

    CreationTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DataQualityAppSpecification: "DataQualityJobDefinition.DataQualityAppSpecification",
        DataQualityJobInput: "DataQualityJobDefinition.DataQualityJobInput",
        DataQualityJobOutputConfig: "DataQualityJobDefinition.MonitoringOutputConfig",
        JobResources: "DataQualityJobDefinition.MonitoringResources",
        RoleArn: str,
        DataQualityBaselineConfig: "DataQualityJobDefinition.DataQualityBaselineConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobDefinitionName: str = ...,
        NetworkConfig: "DataQualityJobDefinition.NetworkConfig" = ...,
        StoppingCondition: "DataQualityJobDefinition.StoppingCondition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ClusterConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            VolumeSizeInGB: int,
            VolumeKmsKeyId: str = ...
        ): ...
    class ConstraintsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class DataQualityAppSpecification:
        def __init__(
            self,
            *,
            ImageUri: str,
            ContainerArguments: List[str] = ...,
            ContainerEntrypoint: List[str] = ...,
            Environment: "DataQualityJobDefinition.Environment" = ...,
            PostAnalyticsProcessorSourceUri: str = ...,
            RecordPreprocessorSourceUri: str = ...
        ): ...
    class DataQualityBaselineConfig:
        def __init__(
            self,
            *,
            BaseliningJobName: str = ...,
            ConstraintsResource: "DataQualityJobDefinition.ConstraintsResource" = ...,
            StatisticsResource: "DataQualityJobDefinition.StatisticsResource" = ...
        ): ...
    class DataQualityJobInput:
        def __init__(
            self, *, EndpointInput: "DataQualityJobDefinition.EndpointInput"
        ): ...
    class EndpointInput:
        def __init__(
            self,
            *,
            EndpointName: str,
            LocalPath: str,
            S3DataDistributionType: str = ...,
            S3InputMode: str = ...
        ): ...
    class Environment:
        def __init__(self) -> None: ...
    class MonitoringOutput:
        def __init__(self, *, S3Output: "DataQualityJobDefinition.S3Output"): ...
    class MonitoringOutputConfig:
        def __init__(
            self,
            *,
            MonitoringOutputs: List["DataQualityJobDefinition.MonitoringOutput"],
            KmsKeyId: str = ...
        ): ...
    class MonitoringResources:
        def __init__(
            self, *, ClusterConfig: "DataQualityJobDefinition.ClusterConfig"
        ): ...
    class NetworkConfig:
        def __init__(
            self,
            *,
            EnableInterContainerTrafficEncryption: bool = ...,
            EnableNetworkIsolation: bool = ...,
            VpcConfig: "DataQualityJobDefinition.VpcConfig" = ...
        ): ...
    class S3Output:
        def __init__(self, *, LocalPath: str, S3Uri: str, S3UploadMode: str = ...): ...
    class StatisticsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class StoppingCondition:
        def __init__(self, *, MaxRuntimeInSeconds: int): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class Device:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceFleetName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Device: "Device.Device_" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Device_:
        def __init__(
            self, *, DeviceName: str, Description: str = ..., IotThingName: str = ...
        ): ...

class DeviceFleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: "DeviceFleet.EdgeOutputConfig",
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EdgeOutputConfig:
        def __init__(self, *, S3OutputLocation: str, KmsKeyId: str = ...): ...

class Endpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html"""

    EndpointName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndpointConfigName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentConfig: "Endpoint.DeploymentConfig" = ...,
        EndpointName: str = ...,
        ExcludeRetainedVariantProperties: List["Endpoint.VariantProperty"] = ...,
        RetainAllVariantProperties: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Alarm:
        def __init__(self, *, AlarmName: str): ...
    class AutoRollbackConfig:
        def __init__(self, *, Alarms: List["Endpoint.Alarm"]): ...
    class BlueGreenUpdatePolicy:
        def __init__(
            self,
            *,
            TrafficRoutingConfiguration: "Endpoint.TrafficRoutingConfig",
            MaximumExecutionTimeoutInSeconds: int = ...,
            TerminationWaitInSeconds: int = ...
        ): ...
    class CapacitySize:
        def __init__(self, *, Type: str, Value: int): ...
    class DeploymentConfig:
        def __init__(
            self,
            *,
            BlueGreenUpdatePolicy: "Endpoint.BlueGreenUpdatePolicy",
            AutoRollbackConfiguration: "Endpoint.AutoRollbackConfig" = ...
        ): ...
    class TrafficRoutingConfig:
        def __init__(
            self,
            *,
            Type: str,
            CanarySize: "Endpoint.CapacitySize" = ...,
            WaitIntervalInSeconds: int = ...
        ): ...
    class VariantProperty:
        def __init__(self, *, VariantPropertyType: str = ...): ...

class EndpointConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html"""

    EndpointConfigName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ProductionVariants: List["EndpointConfig.ProductionVariant"],
        DataCaptureConfig: "EndpointConfig.DataCaptureConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointConfigName: str = ...,
        KmsKeyId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CaptureContentTypeHeader:
        def __init__(
            self, *, CsvContentTypes: List[str] = ..., JsonContentTypes: List[str] = ...
        ): ...
    class CaptureOption:
        def __init__(self, *, CaptureMode: str): ...
    class DataCaptureConfig:
        def __init__(
            self,
            *,
            CaptureOptions: List["EndpointConfig.CaptureOption"],
            DestinationS3Uri: str,
            InitialSamplingPercentage: int,
            CaptureContentTypeHeader: "EndpointConfig.CaptureContentTypeHeader" = ...,
            EnableCapture: bool = ...,
            KmsKeyId: str = ...
        ): ...
    class ProductionVariant:
        def __init__(
            self,
            *,
            InitialInstanceCount: int,
            InitialVariantWeight: float,
            InstanceType: str,
            ModelName: str,
            VariantName: str,
            AcceleratorType: str = ...
        ): ...

class FeatureGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        EventTimeFeatureName: str,
        FeatureDefinitions: List["FeatureGroup.FeatureDefinition"],
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        OfflineStoreConfig: Any = ...,
        OnlineStoreConfig: Any = ...,
        RoleArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class FeatureDefinition:
        def __init__(self, *, FeatureName: str, FeatureType: str): ...

class Model:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html"""

    ModelName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ExecutionRoleArn: str,
        Containers: List["Model.ContainerDefinition"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnableNetworkIsolation: bool = ...,
        ModelName: str = ...,
        PrimaryContainer: "Model.ContainerDefinition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Model.VpcConfig" = ...
    ): ...
    class ContainerDefinition:
        def __init__(
            self,
            *,
            ContainerHostname: str = ...,
            Environment: Any = ...,
            Image: str = ...,
            ImageConfig: "Model.ImageConfig" = ...,
            Mode: str = ...,
            ModelDataUrl: str = ...,
            ModelPackageName: str = ...,
            MultiModelConfig: "Model.MultiModelConfig" = ...
        ): ...
    class ImageConfig:
        def __init__(self, *, RepositoryAccessMode: str): ...
    class MultiModelConfig:
        def __init__(self, *, ModelCacheSetting: str = ...): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class ModelBiasJobDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html"""

    JobDefinitionArn: Final[str]

    CreationTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        JobResources: "ModelBiasJobDefinition.MonitoringResources",
        ModelBiasAppSpecification: "ModelBiasJobDefinition.ModelBiasAppSpecification",
        ModelBiasJobInput: "ModelBiasJobDefinition.ModelBiasJobInput",
        ModelBiasJobOutputConfig: "ModelBiasJobDefinition.MonitoringOutputConfig",
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobDefinitionName: str = ...,
        ModelBiasBaselineConfig: "ModelBiasJobDefinition.ModelBiasBaselineConfig" = ...,
        NetworkConfig: "ModelBiasJobDefinition.NetworkConfig" = ...,
        StoppingCondition: "ModelBiasJobDefinition.StoppingCondition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ClusterConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            VolumeSizeInGB: int,
            VolumeKmsKeyId: str = ...
        ): ...
    class ConstraintsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class EndpointInput:
        def __init__(
            self,
            *,
            EndpointName: str,
            LocalPath: str,
            EndTimeOffset: str = ...,
            FeaturesAttribute: str = ...,
            InferenceAttribute: str = ...,
            ProbabilityAttribute: str = ...,
            ProbabilityThresholdAttribute: float = ...,
            S3DataDistributionType: str = ...,
            S3InputMode: str = ...,
            StartTimeOffset: str = ...
        ): ...
    class Environment:
        def __init__(self) -> None: ...
    class ModelBiasAppSpecification:
        def __init__(
            self,
            *,
            ConfigUri: str,
            ImageUri: str,
            Environment: "ModelBiasJobDefinition.Environment" = ...
        ): ...
    class ModelBiasBaselineConfig:
        def __init__(
            self,
            *,
            BaseliningJobName: str = ...,
            ConstraintsResource: "ModelBiasJobDefinition.ConstraintsResource" = ...
        ): ...
    class ModelBiasJobInput:
        def __init__(
            self,
            *,
            EndpointInput: "ModelBiasJobDefinition.EndpointInput",
            GroundTruthS3Input: "ModelBiasJobDefinition.MonitoringGroundTruthS3Input"
        ): ...
    class MonitoringGroundTruthS3Input:
        def __init__(self, *, S3Uri: str): ...
    class MonitoringOutput:
        def __init__(self, *, S3Output: "ModelBiasJobDefinition.S3Output"): ...
    class MonitoringOutputConfig:
        def __init__(
            self,
            *,
            MonitoringOutputs: List["ModelBiasJobDefinition.MonitoringOutput"],
            KmsKeyId: str = ...
        ): ...
    class MonitoringResources:
        def __init__(
            self, *, ClusterConfig: "ModelBiasJobDefinition.ClusterConfig"
        ): ...
    class NetworkConfig:
        def __init__(
            self,
            *,
            EnableInterContainerTrafficEncryption: bool = ...,
            EnableNetworkIsolation: bool = ...,
            VpcConfig: "ModelBiasJobDefinition.VpcConfig" = ...
        ): ...
    class S3Output:
        def __init__(self, *, LocalPath: str, S3Uri: str, S3UploadMode: str = ...): ...
    class StoppingCondition:
        def __init__(self, *, MaxRuntimeInSeconds: int): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class ModelExplainabilityJobDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html"""

    JobDefinitionArn: Final[str]

    CreationTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        JobResources: "ModelExplainabilityJobDefinition.MonitoringResources",
        ModelExplainabilityAppSpecification: "ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification",
        ModelExplainabilityJobInput: "ModelExplainabilityJobDefinition.ModelExplainabilityJobInput",
        ModelExplainabilityJobOutputConfig: "ModelExplainabilityJobDefinition.MonitoringOutputConfig",
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobDefinitionName: str = ...,
        ModelExplainabilityBaselineConfig: "ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig" = ...,
        NetworkConfig: "ModelExplainabilityJobDefinition.NetworkConfig" = ...,
        StoppingCondition: "ModelExplainabilityJobDefinition.StoppingCondition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ClusterConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            VolumeSizeInGB: int,
            VolumeKmsKeyId: str = ...
        ): ...
    class ConstraintsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class EndpointInput:
        def __init__(
            self,
            *,
            EndpointName: str,
            LocalPath: str,
            FeaturesAttribute: str = ...,
            InferenceAttribute: str = ...,
            ProbabilityAttribute: str = ...,
            S3DataDistributionType: str = ...,
            S3InputMode: str = ...
        ): ...
    class Environment:
        def __init__(self) -> None: ...
    class ModelExplainabilityAppSpecification:
        def __init__(
            self,
            *,
            ConfigUri: str,
            ImageUri: str,
            Environment: "ModelExplainabilityJobDefinition.Environment" = ...
        ): ...
    class ModelExplainabilityBaselineConfig:
        def __init__(
            self,
            *,
            BaseliningJobName: str = ...,
            ConstraintsResource: "ModelExplainabilityJobDefinition.ConstraintsResource" = ...
        ): ...
    class ModelExplainabilityJobInput:
        def __init__(
            self, *, EndpointInput: "ModelExplainabilityJobDefinition.EndpointInput"
        ): ...
    class MonitoringOutput:
        def __init__(
            self, *, S3Output: "ModelExplainabilityJobDefinition.S3Output"
        ): ...
    class MonitoringOutputConfig:
        def __init__(
            self,
            *,
            MonitoringOutputs: List[
                "ModelExplainabilityJobDefinition.MonitoringOutput"
            ],
            KmsKeyId: str = ...
        ): ...
    class MonitoringResources:
        def __init__(
            self, *, ClusterConfig: "ModelExplainabilityJobDefinition.ClusterConfig"
        ): ...
    class NetworkConfig:
        def __init__(
            self,
            *,
            EnableInterContainerTrafficEncryption: bool = ...,
            EnableNetworkIsolation: bool = ...,
            VpcConfig: "ModelExplainabilityJobDefinition.VpcConfig" = ...
        ): ...
    class S3Output:
        def __init__(self, *, LocalPath: str, S3Uri: str, S3UploadMode: str = ...): ...
    class StoppingCondition:
        def __init__(self, *, MaxRuntimeInSeconds: int): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class ModelPackageGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html"""

    ModelPackageGroupArn: Final[str]

    CreationTime: Final[str]

    ModelPackageGroupStatus: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ModelPackageGroupName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModelPackageGroupDescription: str = ...,
        ModelPackageGroupPolicy: Any = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ModelQualityJobDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html"""

    JobDefinitionArn: Final[str]

    CreationTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        JobResources: "ModelQualityJobDefinition.MonitoringResources",
        ModelQualityAppSpecification: "ModelQualityJobDefinition.ModelQualityAppSpecification",
        ModelQualityJobInput: "ModelQualityJobDefinition.ModelQualityJobInput",
        ModelQualityJobOutputConfig: "ModelQualityJobDefinition.MonitoringOutputConfig",
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobDefinitionName: str = ...,
        ModelQualityBaselineConfig: "ModelQualityJobDefinition.ModelQualityBaselineConfig" = ...,
        NetworkConfig: "ModelQualityJobDefinition.NetworkConfig" = ...,
        StoppingCondition: "ModelQualityJobDefinition.StoppingCondition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ClusterConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            VolumeSizeInGB: int,
            VolumeKmsKeyId: str = ...
        ): ...
    class ConstraintsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class EndpointInput:
        def __init__(
            self,
            *,
            EndpointName: str,
            LocalPath: str,
            EndTimeOffset: str = ...,
            InferenceAttribute: str = ...,
            ProbabilityAttribute: str = ...,
            ProbabilityThresholdAttribute: float = ...,
            S3DataDistributionType: str = ...,
            S3InputMode: str = ...,
            StartTimeOffset: str = ...
        ): ...
    class Environment:
        def __init__(self) -> None: ...
    class ModelQualityAppSpecification:
        def __init__(
            self,
            *,
            ImageUri: str,
            ProblemType: str,
            ContainerArguments: List[str] = ...,
            ContainerEntrypoint: List[str] = ...,
            Environment: "ModelQualityJobDefinition.Environment" = ...,
            PostAnalyticsProcessorSourceUri: str = ...,
            RecordPreprocessorSourceUri: str = ...
        ): ...
    class ModelQualityBaselineConfig:
        def __init__(
            self,
            *,
            BaseliningJobName: str = ...,
            ConstraintsResource: "ModelQualityJobDefinition.ConstraintsResource" = ...
        ): ...
    class ModelQualityJobInput:
        def __init__(
            self,
            *,
            EndpointInput: "ModelQualityJobDefinition.EndpointInput",
            GroundTruthS3Input: "ModelQualityJobDefinition.MonitoringGroundTruthS3Input"
        ): ...
    class MonitoringGroundTruthS3Input:
        def __init__(self, *, S3Uri: str): ...
    class MonitoringOutput:
        def __init__(self, *, S3Output: "ModelQualityJobDefinition.S3Output"): ...
    class MonitoringOutputConfig:
        def __init__(
            self,
            *,
            MonitoringOutputs: List["ModelQualityJobDefinition.MonitoringOutput"],
            KmsKeyId: str = ...
        ): ...
    class MonitoringResources:
        def __init__(
            self, *, ClusterConfig: "ModelQualityJobDefinition.ClusterConfig"
        ): ...
    class NetworkConfig:
        def __init__(
            self,
            *,
            EnableInterContainerTrafficEncryption: bool = ...,
            EnableNetworkIsolation: bool = ...,
            VpcConfig: "ModelQualityJobDefinition.VpcConfig" = ...
        ): ...
    class S3Output:
        def __init__(self, *, LocalPath: str, S3Uri: str, S3UploadMode: str = ...): ...
    class StoppingCondition:
        def __init__(self, *, MaxRuntimeInSeconds: int): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class MonitoringSchedule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html"""

    MonitoringScheduleArn: Final[str]

    CreationTime: Final[str]

    LastModifiedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MonitoringScheduleConfig: "MonitoringSchedule.MonitoringScheduleConfig",
        MonitoringScheduleName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointName: str = ...,
        FailureReason: str = ...,
        LastMonitoringExecutionSummary: "MonitoringSchedule.MonitoringExecutionSummary" = ...,
        MonitoringScheduleStatus: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BaselineConfig:
        def __init__(
            self,
            *,
            ConstraintsResource: "MonitoringSchedule.ConstraintsResource" = ...,
            StatisticsResource: "MonitoringSchedule.StatisticsResource" = ...
        ): ...
    class ClusterConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            VolumeSizeInGB: int,
            VolumeKmsKeyId: str = ...
        ): ...
    class ConstraintsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class EndpointInput:
        def __init__(
            self,
            *,
            EndpointName: str,
            LocalPath: str,
            S3DataDistributionType: str = ...,
            S3InputMode: str = ...
        ): ...
    class Environment:
        def __init__(self) -> None: ...
    class MonitoringAppSpecification:
        def __init__(
            self,
            *,
            ImageUri: str,
            ContainerArguments: List[str] = ...,
            ContainerEntrypoint: List[str] = ...,
            PostAnalyticsProcessorSourceUri: str = ...,
            RecordPreprocessorSourceUri: str = ...
        ): ...
    class MonitoringExecutionSummary:
        def __init__(
            self,
            *,
            CreationTime: str,
            LastModifiedTime: str,
            MonitoringExecutionStatus: str,
            MonitoringScheduleName: str,
            ScheduledTime: str,
            EndpointName: str = ...,
            FailureReason: str = ...,
            ProcessingJobArn: str = ...
        ): ...
    class MonitoringInput:
        def __init__(self, *, EndpointInput: "MonitoringSchedule.EndpointInput"): ...
    class MonitoringInputs:
        def __init__(
            self, *, MonitoringInputs: List["MonitoringSchedule.MonitoringInput"] = ...
        ): ...
    class MonitoringJobDefinition:
        def __init__(
            self,
            *,
            MonitoringAppSpecification: "MonitoringSchedule.MonitoringAppSpecification",
            MonitoringInputs: "MonitoringSchedule.MonitoringInputs",
            MonitoringOutputConfig: "MonitoringSchedule.MonitoringOutputConfig",
            MonitoringResources: "MonitoringSchedule.MonitoringResources",
            RoleArn: str,
            BaselineConfig: "MonitoringSchedule.BaselineConfig" = ...,
            Environment: "MonitoringSchedule.Environment" = ...,
            NetworkConfig: "MonitoringSchedule.NetworkConfig" = ...,
            StoppingCondition: "MonitoringSchedule.StoppingCondition" = ...
        ): ...
    class MonitoringOutput:
        def __init__(self, *, S3Output: "MonitoringSchedule.S3Output"): ...
    class MonitoringOutputConfig:
        def __init__(
            self,
            *,
            MonitoringOutputs: List["MonitoringSchedule.MonitoringOutput"],
            KmsKeyId: str = ...
        ): ...
    class MonitoringResources:
        def __init__(self, *, ClusterConfig: "MonitoringSchedule.ClusterConfig"): ...
    class MonitoringScheduleConfig:
        def __init__(
            self,
            *,
            MonitoringJobDefinition: "MonitoringSchedule.MonitoringJobDefinition" = ...,
            MonitoringJobDefinitionName: str = ...,
            MonitoringType: str = ...,
            ScheduleConfig: "MonitoringSchedule.ScheduleConfig" = ...
        ): ...
    class NetworkConfig:
        def __init__(
            self,
            *,
            EnableInterContainerTrafficEncryption: bool = ...,
            EnableNetworkIsolation: bool = ...,
            VpcConfig: "MonitoringSchedule.VpcConfig" = ...
        ): ...
    class S3Output:
        def __init__(self, *, LocalPath: str, S3Uri: str, S3UploadMode: str = ...): ...
    class ScheduleConfig:
        def __init__(self, *, ScheduleExpression: str): ...
    class StatisticsResource:
        def __init__(self, *, S3Uri: str = ...): ...
    class StoppingCondition:
        def __init__(self, *, MaxRuntimeInSeconds: int): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class NotebookInstance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html"""

    NotebookInstanceName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceType: str,
        RoleArn: str,
        AcceleratorTypes: List[str] = ...,
        AdditionalCodeRepositories: List[str] = ...,
        DefaultCodeRepository: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DirectInternetAccess: str = ...,
        KmsKeyId: str = ...,
        LifecycleConfigName: str = ...,
        NotebookInstanceName: str = ...,
        RootAccess: str = ...,
        SecurityGroupIds: List[str] = ...,
        SubnetId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VolumeSizeInGB: int = ...
    ): ...

class NotebookInstanceLifecycleConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html"""

    NotebookInstanceLifecycleConfigName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotebookInstanceLifecycleConfigName: str = ...,
        OnCreate: List[
            "NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook"
        ] = ...,
        OnStart: List[
            "NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook"
        ] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NotebookInstanceLifecycleHook:
        def __init__(self, *, Content: str = ...): ...

class Pipeline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PipelineDefinition: Any,
        PipelineName: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PipelineDescription: str = ...,
        PipelineDisplayName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Project:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html"""

    ProjectArn: Final[str]

    ProjectId: Final[str]

    CreationTime: Final[str]

    ServiceCatalogProvisionedProductDetails: Final[str]

    ProjectStatus: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ProjectName: str,
        ServiceCatalogProvisioningDetails: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ProjectDescription: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Workteam:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html"""

    WorkteamName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        MemberDefinitions: List["Workteam.MemberDefinition"] = ...,
        NotificationConfiguration: "Workteam.NotificationConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        WorkteamName: str = ...
    ): ...
    class CognitoMemberDefinition:
        def __init__(
            self, *, CognitoClientId: str, CognitoUserGroup: str, CognitoUserPool: str
        ): ...
    class MemberDefinition:
        def __init__(
            self, *, CognitoMemberDefinition: "Workteam.CognitoMemberDefinition"
        ): ...
    class NotificationConfiguration:
        def __init__(self, *, NotificationTopicArn: str): ...
