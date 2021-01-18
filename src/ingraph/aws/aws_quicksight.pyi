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

_NAMESPACE = "AWS::QuickSight"

class Analysis:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html"""

    Arn: Final[str]

    CreatedTime: Final[str]

    DataSetArns: Final[List[str]]

    LastUpdatedTime: Final[str]

    Sheets: Final[List]

    Status: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AnalysisId: str,
        AwsAccountId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Errors: List["Analysis.AnalysisError"] = ...,
        Name: str = ...,
        Parameters: "Analysis.Parameters" = ...,
        Permissions: List["Analysis.ResourcePermission"] = ...,
        SourceEntity: "Analysis.AnalysisSourceEntity" = ...,
        Tags: List["Tag"] = ...,
        ThemeArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AnalysisError:
        def __init__(self, *, Message: str = ..., Type: str = ...): ...
    class AnalysisSourceEntity:
        def __init__(
            self, *, SourceTemplate: "Analysis.AnalysisSourceTemplate" = ...
        ): ...
    class AnalysisSourceTemplate:
        def __init__(
            self, *, Arn: str, DataSetReferences: List["Analysis.DataSetReference"]
        ): ...
    class DataSetReference:
        def __init__(self, *, DataSetArn: str, DataSetPlaceholder: str): ...
    class DateTimeParameter:
        def __init__(self, *, Name: str, Values: List[str]): ...
    class DecimalParameter:
        def __init__(self, *, Name: str, Values: List[float]): ...
    class IntegerParameter:
        def __init__(self, *, Name: str, Values: List[float]): ...
    class Parameters:
        def __init__(
            self,
            *,
            DateTimeParameters: List["Analysis.DateTimeParameter"] = ...,
            DecimalParameters: List["Analysis.DecimalParameter"] = ...,
            IntegerParameters: List["Analysis.IntegerParameter"] = ...,
            StringParameters: List["Analysis.StringParameter"] = ...
        ): ...
    class ResourcePermission:
        def __init__(self, *, Actions: List[str], Principal: str): ...
    class Sheet:
        def __init__(self, *, Name: str = ..., SheetId: str = ...): ...
    class StringParameter:
        def __init__(self, *, Name: str, Values: List[str]): ...

class Dashboard:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html"""

    Arn: Final[str]

    CreatedTime: Final[str]

    LastPublishedTime: Final[str]

    LastUpdatedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        DashboardPublishOptions: "Dashboard.DashboardPublishOptions" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Parameters: "Dashboard.Parameters" = ...,
        Permissions: List["Dashboard.ResourcePermission"] = ...,
        SourceEntity: "Dashboard.DashboardSourceEntity" = ...,
        Tags: List["Tag"] = ...,
        ThemeArn: str = ...,
        UpdateReplacePolicy: str = ...,
        VersionDescription: str = ...
    ): ...
    class AdHocFilteringOption:
        def __init__(self, *, AvailabilityStatus: str = ...): ...
    class DashboardError:
        def __init__(self, *, Message: str = ..., Type: str = ...): ...
    class DashboardPublishOptions:
        def __init__(
            self,
            *,
            AdHocFilteringOption: "Dashboard.AdHocFilteringOption" = ...,
            ExportToCSVOption: "Dashboard.ExportToCSVOption" = ...,
            SheetControlsOption: "Dashboard.SheetControlsOption" = ...
        ): ...
    class DashboardSourceEntity:
        def __init__(
            self, *, SourceTemplate: "Dashboard.DashboardSourceTemplate" = ...
        ): ...
    class DashboardSourceTemplate:
        def __init__(
            self, *, Arn: str, DataSetReferences: List["Dashboard.DataSetReference"]
        ): ...
    class DashboardVersion:
        def __init__(
            self,
            *,
            Arn: str = ...,
            CreatedTime: str = ...,
            DataSetArns: List[str] = ...,
            Description: str = ...,
            Errors: List["Dashboard.DashboardError"] = ...,
            Sheets: List["Dashboard.Sheet"] = ...,
            SourceEntityArn: str = ...,
            Status: str = ...,
            ThemeArn: str = ...,
            VersionNumber: float = ...
        ): ...
    class DataSetReference:
        def __init__(self, *, DataSetArn: str, DataSetPlaceholder: str): ...
    class DateTimeParameter:
        def __init__(self, *, Name: str, Values: List[str]): ...
    class DecimalParameter:
        def __init__(self, *, Name: str, Values: List[float]): ...
    class ExportToCSVOption:
        def __init__(self, *, AvailabilityStatus: str = ...): ...
    class IntegerParameter:
        def __init__(self, *, Name: str, Values: List[float]): ...
    class Parameters:
        def __init__(
            self,
            *,
            DateTimeParameters: List["Dashboard.DateTimeParameter"] = ...,
            DecimalParameters: List["Dashboard.DecimalParameter"] = ...,
            IntegerParameters: List["Dashboard.IntegerParameter"] = ...,
            StringParameters: List["Dashboard.StringParameter"] = ...
        ): ...
    class ResourcePermission:
        def __init__(self, *, Actions: List[str], Principal: str): ...
    class Sheet:
        def __init__(self, *, Name: str = ..., SheetId: str = ...): ...
    class SheetControlsOption:
        def __init__(self, *, VisibilityState: str = ...): ...
    class StringParameter:
        def __init__(self, *, Name: str, Values: List[str]): ...

class Template:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html"""

    Arn: Final[str]

    CreatedTime: Final[str]

    LastUpdatedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Permissions: List["Template.ResourcePermission"] = ...,
        SourceEntity: "Template.TemplateSourceEntity" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VersionDescription: str = ...
    ): ...
    class ColumnGroupColumnSchema:
        def __init__(self, *, Name: str = ...): ...
    class ColumnGroupSchema:
        def __init__(
            self,
            *,
            ColumnGroupColumnSchemaList: List["Template.ColumnGroupColumnSchema"] = ...,
            Name: str = ...
        ): ...
    class ColumnSchema:
        def __init__(
            self, *, DataType: str = ..., GeographicRole: str = ..., Name: str = ...
        ): ...
    class DataSetConfiguration:
        def __init__(
            self,
            *,
            ColumnGroupSchemaList: List["Template.ColumnGroupSchema"] = ...,
            DataSetSchema: "Template.DataSetSchema" = ...,
            Placeholder: str = ...
        ): ...
    class DataSetReference:
        def __init__(self, *, DataSetArn: str, DataSetPlaceholder: str): ...
    class DataSetSchema:
        def __init__(
            self, *, ColumnSchemaList: List["Template.ColumnSchema"] = ...
        ): ...
    class ResourcePermission:
        def __init__(self, *, Actions: List[str], Principal: str): ...
    class Sheet:
        def __init__(self, *, Name: str = ..., SheetId: str = ...): ...
    class TemplateError:
        def __init__(self, *, Message: str = ..., Type: str = ...): ...
    class TemplateSourceAnalysis:
        def __init__(
            self, *, Arn: str, DataSetReferences: List["Template.DataSetReference"]
        ): ...
    class TemplateSourceEntity:
        def __init__(
            self,
            *,
            SourceAnalysis: "Template.TemplateSourceAnalysis" = ...,
            SourceTemplate: "Template.TemplateSourceTemplate" = ...
        ): ...
    class TemplateSourceTemplate:
        def __init__(self, *, Arn: str): ...
    class TemplateVersion:
        def __init__(
            self,
            *,
            CreatedTime: str = ...,
            DataSetConfigurations: List["Template.DataSetConfiguration"] = ...,
            Description: str = ...,
            Errors: List["Template.TemplateError"] = ...,
            Sheets: List["Template.Sheet"] = ...,
            SourceEntityArn: str = ...,
            Status: str = ...,
            ThemeArn: str = ...,
            VersionNumber: float = ...
        ): ...

class Theme:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html"""

    Arn: Final[str]

    CreatedTime: Final[str]

    LastUpdatedTime: Final[str]

    Type: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        BaseThemeId: str = ...,
        Configuration: "Theme.ThemeConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Permissions: List["Theme.ResourcePermission"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VersionDescription: str = ...
    ): ...
    class BorderStyle:
        def __init__(self, *, Show: bool = ...): ...
    class DataColorPalette:
        def __init__(
            self,
            *,
            Colors: List[str] = ...,
            EmptyFillColor: str = ...,
            MinMaxGradient: List[str] = ...
        ): ...
    class Font:
        def __init__(self, *, FontFamily: str = ...): ...
    class GutterStyle:
        def __init__(self, *, Show: bool = ...): ...
    class MarginStyle:
        def __init__(self, *, Show: bool = ...): ...
    class ResourcePermission:
        def __init__(self, *, Actions: List[str], Principal: str): ...
    class SheetStyle:
        def __init__(
            self,
            *,
            Tile: "Theme.TileStyle" = ...,
            TileLayout: "Theme.TileLayoutStyle" = ...
        ): ...
    class ThemeConfiguration:
        def __init__(
            self,
            *,
            DataColorPalette: "Theme.DataColorPalette" = ...,
            Sheet: "Theme.SheetStyle" = ...,
            Typography: "Theme.Typography" = ...,
            UIColorPalette: "Theme.UIColorPalette" = ...
        ): ...
    class ThemeError:
        def __init__(self, *, Message: str = ..., Type: str = ...): ...
    class ThemeVersion:
        def __init__(
            self,
            *,
            Arn: str = ...,
            BaseThemeId: str = ...,
            Configuration: "Theme.ThemeConfiguration" = ...,
            CreatedTime: str = ...,
            Description: str = ...,
            Errors: List["Theme.ThemeError"] = ...,
            Status: str = ...,
            VersionNumber: float = ...
        ): ...
    class TileLayoutStyle:
        def __init__(
            self,
            *,
            Gutter: "Theme.GutterStyle" = ...,
            Margin: "Theme.MarginStyle" = ...
        ): ...
    class TileStyle:
        def __init__(self, *, Border: "Theme.BorderStyle" = ...): ...
    class Typography:
        def __init__(self, *, FontFamilies: List["Theme.Font"] = ...): ...
    class UIColorPalette:
        def __init__(
            self,
            *,
            Accent: str = ...,
            AccentForeground: str = ...,
            Danger: str = ...,
            DangerForeground: str = ...,
            Dimension: str = ...,
            DimensionForeground: str = ...,
            Measure: str = ...,
            MeasureForeground: str = ...,
            PrimaryBackground: str = ...,
            PrimaryForeground: str = ...,
            SecondaryBackground: str = ...,
            SecondaryForeground: str = ...,
            Success: str = ...,
            SuccessForeground: str = ...,
            Warning: str = ...,
            WarningForeground: str = ...
        ): ...
