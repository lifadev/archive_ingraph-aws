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

_NAMESPACE = "AWS::DevOpsGuru"

class NotificationChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html"""

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Config: "NotificationChannel.NotificationChannelConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NotificationChannelConfig:
        def __init__(self, *, Sns: "NotificationChannel.SnsChannelConfig" = ...): ...
    class SnsChannelConfig:
        def __init__(self, *, TopicArn: str = ...): ...

class ResourceCollection:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html"""

    ResourceCollectionType: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceCollectionFilter: "ResourceCollection.ResourceCollectionFilter",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudFormationCollectionFilter:
        def __init__(self, *, StackNames: List[str] = ...): ...
    class ResourceCollectionFilter:
        def __init__(
            self,
            *,
            CloudFormation: "ResourceCollection.CloudFormationCollectionFilter" = ...
        ): ...
