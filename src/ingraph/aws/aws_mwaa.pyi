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

_NAMESPACE = "AWS::MWAA"

class Environment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html"""

    Name: Final[str]

    Status: Final[str]

    Arn: Final[str]

    CreatedAt: Final[str]

    ServiceRoleArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AirflowConfigurationOptions: "Environment.AirflowConfigurationOptions" = ...,
        AirflowVersion: str = ...,
        DagS3Path: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnvironmentClass: str = ...,
        ExecutionRoleArn: str = ...,
        KmsKey: str = ...,
        LoggingConfiguration: "Environment.LoggingConfiguration" = ...,
        MaxWorkers: int = ...,
        NetworkConfiguration: "Environment.NetworkConfiguration" = ...,
        PluginsS3ObjectVersion: str = ...,
        PluginsS3Path: str = ...,
        RequirementsS3ObjectVersion: str = ...,
        RequirementsS3Path: str = ...,
        SourceBucketArn: str = ...,
        Tags: "Environment.TagMap" = ...,
        UpdateReplacePolicy: str = ...,
        WebserverAccessMode: str = ...,
        WebserverUrl: str = ...,
        WeeklyMaintenanceWindowStart: str = ...
    ): ...
    class AirflowConfigurationOptions:
        def __init__(self) -> None: ...
    class LastUpdate:
        def __init__(
            self,
            *,
            CreatedAt: str = ...,
            Error: "Environment.UpdateError" = ...,
            Status: str = ...
        ): ...
    class LoggingConfiguration:
        def __init__(
            self,
            *,
            DagProcessingLogs: "Environment.ModuleLoggingConfiguration" = ...,
            SchedulerLogs: "Environment.ModuleLoggingConfiguration" = ...,
            TaskLogs: "Environment.ModuleLoggingConfiguration" = ...,
            WebserverLogs: "Environment.ModuleLoggingConfiguration" = ...,
            WorkerLogs: "Environment.ModuleLoggingConfiguration" = ...
        ): ...
    class ModuleLoggingConfiguration:
        def __init__(
            self,
            *,
            CloudWatchLogGroupArn: str = ...,
            Enabled: bool = ...,
            LogLevel: str = ...
        ): ...
    class NetworkConfiguration:
        def __init__(
            self,
            *,
            SecurityGroupIds: "Environment.SecurityGroupList" = ...,
            SubnetIds: "Environment.SubnetList" = ...
        ): ...
    class SecurityGroupList:
        def __init__(self, *, SecurityGroupList: List[str] = ...): ...
    class SubnetList:
        def __init__(self, *, SubnetList: List[str] = ...): ...
    class TagMap:
        def __init__(self) -> None: ...
    class UpdateError:
        def __init__(self, *, ErrorCode: str = ..., ErrorMessage: str = ...): ...
