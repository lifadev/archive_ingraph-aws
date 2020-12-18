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

_NAMESPACE = "AWS::IoTSiteWise"

class AccessPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html"""

    AccessPolicyId: Final[str]

    AccessPolicyArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccessPolicyIdentity: "AccessPolicy.AccessPolicyIdentity",
        AccessPolicyPermission: str,
        AccessPolicyResource: "AccessPolicy.AccessPolicyResource",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessPolicyIdentity:
        def __init__(self, *, User: "AccessPolicy.User" = ...): ...
    class AccessPolicyResource:
        def __init__(
            self,
            *,
            Portal: "AccessPolicy.Portal" = ...,
            Project: "AccessPolicy.Project" = ...
        ): ...
    class Portal:
        def __init__(self, *, id: str = ...): ...
    class Project:
        def __init__(self, *, id: str = ...): ...
    class User:
        def __init__(self, *, id: str = ...): ...

class Asset:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html"""

    AssetId: Final[str]

    AssetArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AssetModelId: str,
        AssetName: str,
        AssetHierarchies: List["Asset.AssetHierarchy"] = ...,
        AssetProperties: List["Asset.AssetProperty"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AssetHierarchy:
        def __init__(self, *, ChildAssetId: str, LogicalId: str): ...
    class AssetProperty:
        def __init__(
            self, *, LogicalId: str, Alias: str = ..., NotificationState: str = ...
        ): ...

class AssetModel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html"""

    AssetModelId: Final[str]

    AssetModelArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AssetModelName: str,
        AssetModelDescription: str = ...,
        AssetModelHierarchies: List["AssetModel.AssetModelHierarchy"] = ...,
        AssetModelProperties: List["AssetModel.AssetModelProperty"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AssetModelHierarchy:
        def __init__(self, *, ChildAssetModelId: str, LogicalId: str, Name: str): ...
    class AssetModelProperty:
        def __init__(
            self,
            *,
            DataType: str,
            LogicalId: str,
            Name: str,
            Type: "AssetModel.PropertyType",
            Unit: str = ...
        ): ...
    class Attribute:
        def __init__(self, *, DefaultValue: str = ...): ...
    class ExpressionVariable:
        def __init__(self, *, Name: str, Value: "AssetModel.VariableValue"): ...
    class Metric:
        def __init__(
            self,
            *,
            Expression: str,
            Variables: List["AssetModel.ExpressionVariable"],
            Window: "AssetModel.MetricWindow"
        ): ...
    class MetricWindow:
        def __init__(self, *, Tumbling: "AssetModel.TumblingWindow" = ...): ...
    class PropertyType:
        def __init__(
            self,
            *,
            TypeName: str,
            Attribute: "AssetModel.Attribute" = ...,
            Metric: "AssetModel.Metric" = ...,
            Transform: "AssetModel.Transform" = ...
        ): ...
    class Transform:
        def __init__(
            self, *, Expression: str, Variables: List["AssetModel.ExpressionVariable"]
        ): ...
    class TumblingWindow:
        def __init__(self, *, Interval: str): ...
    class VariableValue:
        def __init__(
            self, *, PropertyLogicalId: str, HierarchyLogicalId: str = ...
        ): ...

class Dashboard:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html"""

    DashboardId: Final[str]

    DashboardArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DashboardDefinition: str,
        DashboardDescription: str,
        DashboardName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ProjectId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Gateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html"""

    GatewayId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GatewayName: str,
        GatewayPlatform: "Gateway.GatewayPlatform",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GatewayCapabilitySummaries: List["Gateway.GatewayCapabilitySummary"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GatewayCapabilitySummary:
        def __init__(
            self, *, CapabilityNamespace: str, CapabilityConfiguration: str = ...
        ): ...
    class GatewayPlatform:
        def __init__(self, *, Greengrass: "Gateway.Greengrass"): ...
    class Greengrass:
        def __init__(self, *, GroupArn: str): ...

class Portal:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html"""

    PortalArn: Final[str]

    PortalClientId: Final[str]

    PortalId: Final[str]

    PortalStartUrl: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortalContactEmail: str,
        PortalName: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PortalDescription: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MonitorErrorDetails:
        def __init__(self, *, code: str = ..., message: str = ...): ...
    class PortalStatus:
        def __init__(
            self, *, state: str, error: "Portal.MonitorErrorDetails" = ...
        ): ...

class Project:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html"""

    ProjectId: Final[str]

    ProjectArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortalId: str,
        ProjectName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ProjectDescription: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
