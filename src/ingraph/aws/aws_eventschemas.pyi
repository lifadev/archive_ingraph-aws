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

_NAMESPACE = "AWS::EventSchemas"

class Discoverer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html"""

    DiscovererArn: Final[str]

    DiscovererId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        SourceArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Discoverer.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...

class Registry:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html"""

    RegistryName: Final[str]

    RegistryArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RegistryName: str = ...,
        Tags: List["Registry.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...

class RegistryPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html"""

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Policy: Any,
        RegistryName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RevisionId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Schema:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html"""

    SchemaVersion: Final[str]

    SchemaArn: Final[str]

    SchemaName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Content: str,
        RegistryName: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        SchemaName: str = ...,
        Tags: List["Schema.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...
