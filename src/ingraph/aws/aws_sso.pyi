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

_NAMESPACE = "AWS::SSO"

class Assignment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PrincipalId: str,
        PrincipalType: str,
        TargetId: str,
        TargetType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class InstanceAccessControlAttributeConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceArn: str,
        AccessControlAttributes: List[
            "InstanceAccessControlAttributeConfiguration.AccessControlAttribute"
        ] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InstanceAccessControlAttributeConfiguration: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessControlAttribute:
        def __init__(
            self,
            *,
            Key: str,
            Value: "InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue"
        ): ...
    class AccessControlAttributeValue:
        def __init__(
            self,
            *,
            Source: "InstanceAccessControlAttributeConfiguration.AccessControlAttributeValueSourceList"
        ): ...
    class AccessControlAttributeValueSourceList:
        def __init__(
            self, *, AccessControlAttributeValueSourceList: List[str] = ...
        ): ...

class PermissionSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html"""

    PermissionSetArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceArn: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        InlinePolicy: Any = ...,
        ManagedPolicies: List[str] = ...,
        RelayStateType: str = ...,
        SessionDuration: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
