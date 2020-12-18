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

    frameworkId: Final[str]

    assessmentId: Final[str]

    arn: Final[str]

    creationTime: Final[float]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...,
        assessmentReportsDestination: "Assessment.AssessmentReportsDestination" = ...,
        awsAccount: "Assessment.AWSAccount" = ...,
        description: str = ...,
        frameworkId: str = ...,
        name: str = ...,
        roles: "Assessment.Roles" = ...,
        scope: "Assessment.Scope" = ...,
        status: str = ...,
        tags: "Assessment.Tags" = ...
    ): ...
    class AWSAccount:
        def __init__(
            self, *, emailAddress: str = ..., id: str = ..., name: str = ...
        ): ...
    class AWSAccounts:
        def __init__(self, *, AWSAccounts: List["Assessment.AWSAccount"] = ...): ...
    class AWSService:
        def __init__(self, *, serviceName: str = ...): ...
    class AWSServices:
        def __init__(self, *, AWSServices: List["Assessment.AWSService"] = ...): ...
    class AssessmentReportsDestination:
        def __init__(self, *, destination: str = ..., destinationType: str = ...): ...
    class Delegation:
        def __init__(
            self,
            *,
            assessmentId: str = ...,
            assessmentName: str = ...,
            comment: str = ...,
            controlSetId: str = ...,
            createdBy: str = ...,
            creationTime: float = ...,
            id: str = ...,
            lastUpdated: float = ...,
            roleArn: str = ...,
            roleType: str = ...,
            status: str = ...
        ): ...
    class Delegations:
        def __init__(self, *, Delegations: List["Assessment.Delegation"] = ...): ...
    class Role:
        def __init__(self, *, roleArn: str = ..., roleType: str = ...): ...
    class Roles:
        def __init__(self, *, Roles: List["Assessment.Role"] = ...): ...
    class Scope:
        def __init__(
            self,
            *,
            awsAccounts: "Assessment.AWSAccounts" = ...,
            awsServices: "Assessment.AWSServices" = ...
        ): ...
    class Tags:
        def __init__(self, *, Tags: List["Tag"] = ...): ...
