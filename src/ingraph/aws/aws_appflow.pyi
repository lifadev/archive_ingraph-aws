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

_NAMESPACE = "AWS::AppFlow"

class ConnectorProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html"""

    ConnectorProfileArn: Final[str]

    CredentialsArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConnectionMode: str,
        ConnectorProfileName: str,
        ConnectorType: str,
        ConnectorProfileConfig: "ConnectorProfile.ConnectorProfileConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        KMSArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AmplitudeConnectorProfileCredentials:
        def __init__(self, *, ApiKey: str, SecretKey: str): ...
    class ConnectorOAuthRequest:
        def __init__(self, *, AuthCode: str = ..., RedirectUri: str = ...): ...
    class ConnectorProfileConfig:
        def __init__(
            self,
            *,
            ConnectorProfileCredentials: "ConnectorProfile.ConnectorProfileCredentials",
            ConnectorProfileProperties: "ConnectorProfile.ConnectorProfileProperties" = ...
        ): ...
    class ConnectorProfileCredentials:
        def __init__(
            self,
            *,
            Amplitude: "ConnectorProfile.AmplitudeConnectorProfileCredentials" = ...,
            Datadog: "ConnectorProfile.DatadogConnectorProfileCredentials" = ...,
            Dynatrace: "ConnectorProfile.DynatraceConnectorProfileCredentials" = ...,
            GoogleAnalytics: "ConnectorProfile.GoogleAnalyticsConnectorProfileCredentials" = ...,
            InforNexus: "ConnectorProfile.InforNexusConnectorProfileCredentials" = ...,
            Marketo: "ConnectorProfile.MarketoConnectorProfileCredentials" = ...,
            Redshift: "ConnectorProfile.RedshiftConnectorProfileCredentials" = ...,
            Salesforce: "ConnectorProfile.SalesforceConnectorProfileCredentials" = ...,
            ServiceNow: "ConnectorProfile.ServiceNowConnectorProfileCredentials" = ...,
            Singular: "ConnectorProfile.SingularConnectorProfileCredentials" = ...,
            Slack: "ConnectorProfile.SlackConnectorProfileCredentials" = ...,
            Snowflake: "ConnectorProfile.SnowflakeConnectorProfileCredentials" = ...,
            Trendmicro: "ConnectorProfile.TrendmicroConnectorProfileCredentials" = ...,
            Veeva: "ConnectorProfile.VeevaConnectorProfileCredentials" = ...,
            Zendesk: "ConnectorProfile.ZendeskConnectorProfileCredentials" = ...
        ): ...
    class ConnectorProfileProperties:
        def __init__(
            self,
            *,
            Datadog: "ConnectorProfile.DatadogConnectorProfileProperties" = ...,
            Dynatrace: "ConnectorProfile.DynatraceConnectorProfileProperties" = ...,
            InforNexus: "ConnectorProfile.InforNexusConnectorProfileProperties" = ...,
            Marketo: "ConnectorProfile.MarketoConnectorProfileProperties" = ...,
            Redshift: "ConnectorProfile.RedshiftConnectorProfileProperties" = ...,
            Salesforce: "ConnectorProfile.SalesforceConnectorProfileProperties" = ...,
            ServiceNow: "ConnectorProfile.ServiceNowConnectorProfileProperties" = ...,
            Slack: "ConnectorProfile.SlackConnectorProfileProperties" = ...,
            Snowflake: "ConnectorProfile.SnowflakeConnectorProfileProperties" = ...,
            Veeva: "ConnectorProfile.VeevaConnectorProfileProperties" = ...,
            Zendesk: "ConnectorProfile.ZendeskConnectorProfileProperties" = ...
        ): ...
    class DatadogConnectorProfileCredentials:
        def __init__(self, *, ApiKey: str, ApplicationKey: str): ...
    class DatadogConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class DynatraceConnectorProfileCredentials:
        def __init__(self, *, ApiToken: str): ...
    class DynatraceConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class GoogleAnalyticsConnectorProfileCredentials:
        def __init__(
            self,
            *,
            ClientId: str,
            ClientSecret: str,
            AccessToken: str = ...,
            ConnectorOAuthRequest: "ConnectorProfile.ConnectorOAuthRequest" = ...,
            RefreshToken: str = ...
        ): ...
    class InforNexusConnectorProfileCredentials:
        def __init__(
            self, *, AccessKeyId: str, Datakey: str, SecretAccessKey: str, UserId: str
        ): ...
    class InforNexusConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class MarketoConnectorProfileCredentials:
        def __init__(
            self,
            *,
            ClientId: str,
            ClientSecret: str,
            AccessToken: str = ...,
            ConnectorOAuthRequest: "ConnectorProfile.ConnectorOAuthRequest" = ...
        ): ...
    class MarketoConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class RedshiftConnectorProfileCredentials:
        def __init__(self, *, Password: str, Username: str): ...
    class RedshiftConnectorProfileProperties:
        def __init__(
            self,
            *,
            BucketName: str,
            DatabaseUrl: str,
            RoleArn: str,
            BucketPrefix: str = ...
        ): ...
    class SalesforceConnectorProfileCredentials:
        def __init__(
            self,
            *,
            AccessToken: str = ...,
            ClientCredentialsArn: str = ...,
            ConnectorOAuthRequest: "ConnectorProfile.ConnectorOAuthRequest" = ...,
            RefreshToken: str = ...
        ): ...
    class SalesforceConnectorProfileProperties:
        def __init__(
            self, *, InstanceUrl: str = ..., isSandboxEnvironment: bool = ...
        ): ...
    class ServiceNowConnectorProfileCredentials:
        def __init__(self, *, Password: str, Username: str): ...
    class ServiceNowConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class SingularConnectorProfileCredentials:
        def __init__(self, *, ApiKey: str): ...
    class SlackConnectorProfileCredentials:
        def __init__(
            self,
            *,
            ClientId: str,
            ClientSecret: str,
            AccessToken: str = ...,
            ConnectorOAuthRequest: "ConnectorProfile.ConnectorOAuthRequest" = ...
        ): ...
    class SlackConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class SnowflakeConnectorProfileCredentials:
        def __init__(self, *, Password: str, Username: str): ...
    class SnowflakeConnectorProfileProperties:
        def __init__(
            self,
            *,
            BucketName: str,
            Stage: str,
            Warehouse: str,
            AccountName: str = ...,
            BucketPrefix: str = ...,
            PrivateLinkServiceName: str = ...,
            Region: str = ...
        ): ...
    class TrendmicroConnectorProfileCredentials:
        def __init__(self, *, ApiSecretKey: str): ...
    class VeevaConnectorProfileCredentials:
        def __init__(self, *, Password: str, Username: str): ...
    class VeevaConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...
    class ZendeskConnectorProfileCredentials:
        def __init__(
            self,
            *,
            ClientId: str,
            ClientSecret: str,
            AccessToken: str = ...,
            ConnectorOAuthRequest: "ConnectorProfile.ConnectorOAuthRequest" = ...
        ): ...
    class ZendeskConnectorProfileProperties:
        def __init__(self, *, InstanceUrl: str): ...

class Flow:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html"""

    FlowArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationFlowConfigList: List["Flow.DestinationFlowConfig"],
        FlowName: str,
        SourceFlowConfig: "Flow.SourceFlowConfig",
        Tasks: List["Flow.Task"],
        TriggerConfig: "Flow.TriggerConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        KMSArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AggregationConfig:
        def __init__(self, *, AggregationType: str = ...): ...
    class AmplitudeSourceProperties:
        def __init__(self, *, Object: str): ...
    class ConnectorOperator:
        def __init__(
            self,
            *,
            Amplitude: str = ...,
            Datadog: str = ...,
            Dynatrace: str = ...,
            GoogleAnalytics: str = ...,
            InforNexus: str = ...,
            Marketo: str = ...,
            S3: str = ...,
            Salesforce: str = ...,
            ServiceNow: str = ...,
            Singular: str = ...,
            Slack: str = ...,
            Trendmicro: str = ...,
            Veeva: str = ...,
            Zendesk: str = ...
        ): ...
    class DatadogSourceProperties:
        def __init__(self, *, Object: str): ...
    class DestinationConnectorProperties:
        def __init__(
            self,
            *,
            EventBridge: "Flow.EventBridgeDestinationProperties" = ...,
            Redshift: "Flow.RedshiftDestinationProperties" = ...,
            S3: "Flow.S3DestinationProperties" = ...,
            Salesforce: "Flow.SalesforceDestinationProperties" = ...,
            Snowflake: "Flow.SnowflakeDestinationProperties" = ...,
            Upsolver: "Flow.UpsolverDestinationProperties" = ...
        ): ...
    class DestinationFlowConfig:
        def __init__(
            self,
            *,
            ConnectorType: str,
            DestinationConnectorProperties: "Flow.DestinationConnectorProperties",
            ConnectorProfileName: str = ...
        ): ...
    class DynatraceSourceProperties:
        def __init__(self, *, Object: str): ...
    class ErrorHandlingConfig:
        def __init__(
            self,
            *,
            BucketName: str = ...,
            BucketPrefix: str = ...,
            FailOnFirstError: bool = ...
        ): ...
    class EventBridgeDestinationProperties:
        def __init__(
            self, *, Object: str, ErrorHandlingConfig: "Flow.ErrorHandlingConfig" = ...
        ): ...
    class GoogleAnalyticsSourceProperties:
        def __init__(self, *, Object: str): ...
    class IncrementalPullConfig:
        def __init__(self, *, DatetimeTypeFieldName: str = ...): ...
    class InforNexusSourceProperties:
        def __init__(self, *, Object: str): ...
    class MarketoSourceProperties:
        def __init__(self, *, Object: str): ...
    class PrefixConfig:
        def __init__(self, *, PrefixFormat: str = ..., PrefixType: str = ...): ...
    class RedshiftDestinationProperties:
        def __init__(
            self,
            *,
            IntermediateBucketName: str,
            Object: str,
            BucketPrefix: str = ...,
            ErrorHandlingConfig: "Flow.ErrorHandlingConfig" = ...
        ): ...
    class S3DestinationProperties:
        def __init__(
            self,
            *,
            BucketName: str,
            BucketPrefix: str = ...,
            S3OutputFormatConfig: "Flow.S3OutputFormatConfig" = ...
        ): ...
    class S3OutputFormatConfig:
        def __init__(
            self,
            *,
            AggregationConfig: "Flow.AggregationConfig" = ...,
            FileType: str = ...,
            PrefixConfig: "Flow.PrefixConfig" = ...
        ): ...
    class S3SourceProperties:
        def __init__(self, *, BucketName: str, BucketPrefix: str): ...
    class SalesforceDestinationProperties:
        def __init__(
            self, *, Object: str, ErrorHandlingConfig: "Flow.ErrorHandlingConfig" = ...
        ): ...
    class SalesforceSourceProperties:
        def __init__(
            self,
            *,
            Object: str,
            EnableDynamicFieldUpdate: bool = ...,
            IncludeDeletedRecords: bool = ...
        ): ...
    class ScheduledTriggerProperties:
        def __init__(
            self,
            *,
            ScheduleExpression: str,
            DataPullMode: str = ...,
            ScheduleEndTime: float = ...,
            ScheduleStartTime: float = ...,
            TimeZone: str = ...
        ): ...
    class ServiceNowSourceProperties:
        def __init__(self, *, Object: str): ...
    class SingularSourceProperties:
        def __init__(self, *, Object: str): ...
    class SlackSourceProperties:
        def __init__(self, *, Object: str): ...
    class SnowflakeDestinationProperties:
        def __init__(
            self,
            *,
            IntermediateBucketName: str,
            Object: str,
            BucketPrefix: str = ...,
            ErrorHandlingConfig: "Flow.ErrorHandlingConfig" = ...
        ): ...
    class SourceConnectorProperties:
        def __init__(
            self,
            *,
            Amplitude: "Flow.AmplitudeSourceProperties" = ...,
            Datadog: "Flow.DatadogSourceProperties" = ...,
            Dynatrace: "Flow.DynatraceSourceProperties" = ...,
            GoogleAnalytics: "Flow.GoogleAnalyticsSourceProperties" = ...,
            InforNexus: "Flow.InforNexusSourceProperties" = ...,
            Marketo: "Flow.MarketoSourceProperties" = ...,
            S3: "Flow.S3SourceProperties" = ...,
            Salesforce: "Flow.SalesforceSourceProperties" = ...,
            ServiceNow: "Flow.ServiceNowSourceProperties" = ...,
            Singular: "Flow.SingularSourceProperties" = ...,
            Slack: "Flow.SlackSourceProperties" = ...,
            Trendmicro: "Flow.TrendmicroSourceProperties" = ...,
            Veeva: "Flow.VeevaSourceProperties" = ...,
            Zendesk: "Flow.ZendeskSourceProperties" = ...
        ): ...
    class SourceFlowConfig:
        def __init__(
            self,
            *,
            ConnectorType: str,
            SourceConnectorProperties: "Flow.SourceConnectorProperties",
            ConnectorProfileName: str = ...,
            IncrementalPullConfig: "Flow.IncrementalPullConfig" = ...
        ): ...
    class Task:
        def __init__(
            self,
            *,
            SourceFields: List[str],
            TaskType: str,
            ConnectorOperator: "Flow.ConnectorOperator" = ...,
            DestinationField: str = ...,
            TaskProperties: List["Flow.TaskPropertiesObject"] = ...
        ): ...
    class TaskPropertiesObject:
        def __init__(self, *, Key: str, Value: str): ...
    class TrendmicroSourceProperties:
        def __init__(self, *, Object: str): ...
    class TriggerConfig:
        def __init__(
            self,
            *,
            TriggerType: str,
            TriggerProperties: "Flow.ScheduledTriggerProperties" = ...
        ): ...
    class UpsolverDestinationProperties:
        def __init__(
            self,
            *,
            BucketName: str,
            S3OutputFormatConfig: "Flow.UpsolverS3OutputFormatConfig",
            BucketPrefix: str = ...
        ): ...
    class UpsolverS3OutputFormatConfig:
        def __init__(
            self,
            *,
            PrefixConfig: "Flow.PrefixConfig",
            AggregationConfig: "Flow.AggregationConfig" = ...,
            FileType: str = ...
        ): ...
    class VeevaSourceProperties:
        def __init__(self, *, Object: str): ...
    class ZendeskSourceProperties:
        def __init__(self, *, Object: str): ...
