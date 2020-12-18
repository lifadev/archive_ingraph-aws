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

_NAMESPACE = "AWS::CloudFormation"

class CustomResource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ServiceToken: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...,
        **kwargs: Any
    ): ...

class Macro:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LogGroupName: str = ...,
        LogRoleARN: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ModuleDefaultVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Arn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModuleName: str = ...,
        UpdateReplacePolicy: str = ...,
        VersionId: str = ...
    ): ...

class ModuleVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html"""

    Arn: Final[str]

    Description: Final[str]

    DocumentationUrl: Final[str]

    IsDefaultVersion: Final[bool]

    Schema: Final[str]

    TimeCreated: Final[str]

    VersionId: Final[str]

    Visibility: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ModuleName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModulePackage: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Stack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TemplateURL: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotificationARNs: List[str] = ...,
        Parameters: Dict[str, str] = ...,
        Tags: List["Tag"] = ...,
        TimeoutInMinutes: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class StackSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html"""

    StackSetId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PermissionModel: str,
        StackSetName: str,
        AdministrationRoleARN: str = ...,
        AutoDeployment: "StackSet.AutoDeployment" = ...,
        Capabilities: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ExecutionRoleName: str = ...,
        OperationPreferences: "StackSet.OperationPreferences" = ...,
        Parameters: List["StackSet.Parameter"] = ...,
        StackInstancesGroup: List["StackSet.StackInstances"] = ...,
        Tags: List["Tag"] = ...,
        TemplateBody: str = ...,
        TemplateURL: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AutoDeployment:
        def __init__(
            self, *, Enabled: bool = ..., RetainStacksOnAccountRemoval: bool = ...
        ): ...
    class DeploymentTargets:
        def __init__(
            self, *, Accounts: List[str] = ..., OrganizationalUnitIds: List[str] = ...
        ): ...
    class OperationPreferences:
        def __init__(
            self,
            *,
            FailureToleranceCount: int = ...,
            FailureTolerancePercentage: int = ...,
            MaxConcurrentCount: int = ...,
            MaxConcurrentPercentage: int = ...,
            RegionOrder: List[str] = ...
        ): ...
    class Parameter:
        def __init__(self, *, ParameterKey: str, ParameterValue: str): ...
    class StackInstances:
        def __init__(
            self,
            *,
            DeploymentTargets: "StackSet.DeploymentTargets",
            Regions: List[str],
            ParameterOverrides: List["StackSet.Parameter"] = ...
        ): ...

class WaitCondition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html"""

    Data: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Count: int = ...,
        CreationPolicy: "WaitCondition.CreationPolicy" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Handle: str = ...,
        Timeout: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CreationPolicy:
        def __init__(self, *, ResourceSignal: "WaitCondition.ResourceSignal" = ...): ...
    class ResourceSignal:
        def __init__(self, *, Count: int = ..., Timeout: str = ...): ...

class WaitConditionHandle:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
