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

_NAMESPACE = "AWS::CodeCommit"

class Repository:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html"""

    CloneUrlHttp: Final[str]

    CloneUrlSsh: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RepositoryName: str,
        Code: "Repository.Code" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RepositoryDescription: str = ...,
        Tags: List["Tag"] = ...,
        Triggers: List["Repository.RepositoryTrigger"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Code:
        def __init__(self, *, S3: "Repository.S3", BranchName: str = ...): ...
    class RepositoryTrigger:
        def __init__(
            self,
            *,
            DestinationArn: str,
            Events: List[str],
            Name: str,
            Branches: List[str] = ...,
            CustomData: str = ...
        ): ...
    class S3:
        def __init__(self, *, Bucket: str, Key: str, ObjectVersion: str = ...): ...
