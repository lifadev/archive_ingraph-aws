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

_NAMESPACE = "AWS::MediaStore"

class Container:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html"""

    Endpoint: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ContainerName: str,
        AccessLoggingEnabled: bool = ...,
        CorsPolicy: List["Container.CorsRule"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LifecyclePolicy: str = ...,
        MetricPolicy: "Container.MetricPolicy" = ...,
        Policy: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CorsRule:
        def __init__(
            self,
            *,
            AllowedHeaders: List[str] = ...,
            AllowedMethods: List[str] = ...,
            AllowedOrigins: List[str] = ...,
            ExposeHeaders: List[str] = ...,
            MaxAgeSeconds: int = ...
        ): ...
    class MetricPolicy:
        def __init__(
            self,
            *,
            ContainerLevelMetrics: str,
            MetricPolicyRules: List["Container.MetricPolicyRule"] = ...
        ): ...
    class MetricPolicyRule:
        def __init__(self, *, ObjectGroup: str, ObjectGroupName: str): ...
