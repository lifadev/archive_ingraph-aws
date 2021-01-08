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

    delegations: Final[List]

    creationTime: Final[float]

    Ref: Final[str]

    FrameworkId: Final[str]

    AssessmentId: Final[str]

    Arn: Final[str]

    Delegations: Final[List]

    CreationTime: Final[float]
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
        UpdateReplacePolicy: str = ...,
        assessmentReportsDestination: "Assessment.AssessmentReportsDestination" = ...,
        awsAccount: "Assessment.AWSAccount" = ...,
        description: str = ...,
        frameworkId: str = ...,
        name: str = ...,
        roles: List["Assessment.Role"] = ...,
        scope: "Assessment.Scope" = ...,
        status: str = ...,
        tags: List["Tag"] = ...
    ): ...
    class AWSAccount:
        def __init__(
            self,
            *,
            EmailAddress: str = ...,
            Id: str = ...,
            Name: str = ...,
            emailAddress: str = ...,
            id: str = ...,
            name: str = ...
        ): ...
    class AWSAccounts:
        def __init__(self, *, AWSAccounts: List["Assessment.AWSAccount"] = ...): ...
    class AWSService:
        def __init__(self, *, ServiceName: str = ..., serviceName: str = ...): ...
    class AWSServices:
        def __init__(self, *, AWSServices: List["Assessment.AWSService"] = ...): ...
    class AssessmentReportsDestination:
        def __init__(
            self,
            *,
            Destination: str = ...,
            DestinationType: str = ...,
            destination: str = ...,
            destinationType: str = ...
        ): ...
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
            Status: str = ...,
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
    class Role:
        def __init__(
            self,
            *,
            RoleArn: str = ...,
            RoleType: str = ...,
            roleArn: str = ...,
            roleType: str = ...
        ): ...
    class Scope:
        def __init__(
            self,
            *,
            AwsAccounts: List["Assessment.AWSAccount"] = ...,
            AwsServices: List["Assessment.AWSService"] = ...,
            awsAccounts: "Assessment.AWSAccounts" = ...,
            awsServices: "Assessment.AWSServices" = ...
        ): ...
