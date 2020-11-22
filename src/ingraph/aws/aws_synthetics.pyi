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

_NAMESPACE = "AWS::Synthetics"

class Canary:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html"""

    Id: Final[str]

    State: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ArtifactS3Location: str,
        Code: "Canary.Code",
        ExecutionRoleArn: str,
        Name: str,
        RuntimeVersion: str,
        Schedule: "Canary.Schedule",
        StartCanaryAfterCreation: bool,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FailureRetentionPeriod: int = ...,
        RunConfig: "Canary.RunConfig" = ...,
        SuccessRetentionPeriod: int = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VPCConfig: "Canary.VPCConfig" = ...
    ): ...
    class Code:
        def __init__(
            self,
            *,
            Handler: str = ...,
            S3Bucket: str = ...,
            S3Key: str = ...,
            S3ObjectVersion: str = ...,
            Script: str = ...
        ): ...
    class RunConfig:
        def __init__(
            self,
            *,
            TimeoutInSeconds: int,
            ActiveTracing: bool = ...,
            EnvironmentVariables: Dict[str, str] = ...,
            MemoryInMB: int = ...
        ): ...
    class Schedule:
        def __init__(self, *, Expression: str, DurationInSeconds: str = ...): ...
    class VPCConfig:
        def __init__(
            self, *, SecurityGroupIds: List[str], SubnetIds: List[str], VpcId: str = ...
        ): ...
