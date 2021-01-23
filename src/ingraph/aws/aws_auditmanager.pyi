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

_NAMESPACE = "AWS::AuditManager"

class Assessment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html"""

    FrameworkId: Final[str]

    AssessmentId: Final[str]

    Arn: Final[str]

    Delegations: Final[List]

    CreationTime: Final[float]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AssessmentReportsDestination: "Assessment.AssessmentReportsDestination" = ...,
        AwsAccount: "Assessment.AWSAccount" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        FrameworkId: str = ...,
        Name: str = ...,
        Roles: List["Assessment.Role"] = ...,
        Scope: "Assessment.Scope" = ...,
        Status: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AWSAccount:
        def __init__(
            self, *, EmailAddress: str = ..., Id: str = ..., Name: str = ...
        ): ...
    class AWSService:
        def __init__(self, *, ServiceName: str = ...): ...
    class AssessmentReportsDestination:
        def __init__(self, *, Destination: str = ..., DestinationType: str = ...): ...
    class Delegation:
        def __init__(
            self,
            *,
            AssessmentId: str = ...,
            AssessmentName: str = ...,
            Comment: str = ...,
            ControlSetId: str = ...,
            CreatedBy: str = ...,
            CreationTime: float = ...,
            Id: str = ...,
            LastUpdated: float = ...,
            RoleArn: str = ...,
            RoleType: str = ...,
            Status: str = ...
        ): ...
    class Role:
        def __init__(self, *, RoleArn: str = ..., RoleType: str = ...): ...
    class Scope:
        def __init__(
            self,
            *,
            AwsAccounts: List["Assessment.AWSAccount"] = ...,
            AwsServices: List["Assessment.AWSService"] = ...
        ): ...
