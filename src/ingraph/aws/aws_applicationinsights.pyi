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

_NAMESPACE = "AWS::ApplicationInsights"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html"""

    ApplicationARN: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceGroupName: str,
        AutoConfigurationEnabled: bool = ...,
        CWEMonitorEnabled: bool = ...,
        ComponentMonitoringSettings: List[
            "Application.ComponentMonitoringSetting"
        ] = ...,
        CustomComponents: List["Application.CustomComponent"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LogPatternSets: List["Application.LogPatternSet"] = ...,
        OpsCenterEnabled: bool = ...,
        OpsItemSNSTopicArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Alarm:
        def __init__(self, *, AlarmName: str, Severity: str = ...): ...
    class AlarmMetric:
        def __init__(self, *, AlarmMetricName: str): ...
    class ComponentConfiguration:
        def __init__(
            self,
            *,
            ConfigurationDetails: "Application.ConfigurationDetails" = ...,
            SubComponentTypeConfigurations: List[
                "Application.SubComponentTypeConfiguration"
            ] = ...
        ): ...
    class ComponentMonitoringSetting:
        def __init__(
            self,
            *,
            ComponentARN: str = ...,
            ComponentConfigurationMode: str = ...,
            ComponentName: str = ...,
            CustomComponentConfiguration: "Application.ComponentConfiguration" = ...,
            DefaultOverwriteComponentConfiguration: "Application.ComponentConfiguration" = ...,
            Tier: str = ...
        ): ...
    class ConfigurationDetails:
        def __init__(
            self,
            *,
            AlarmMetrics: List["Application.AlarmMetric"] = ...,
            Alarms: List["Application.Alarm"] = ...,
            JMXPrometheusExporter: "Application.JMXPrometheusExporter" = ...,
            Logs: List["Application.Log"] = ...,
            WindowsEvents: List["Application.WindowsEvent"] = ...
        ): ...
    class CustomComponent:
        def __init__(self, *, ComponentName: str, ResourceList: List[str]): ...
    class JMXPrometheusExporter:
        def __init__(
            self, *, HostPort: str = ..., JMXURL: str = ..., PrometheusPort: str = ...
        ): ...
    class Log:
        def __init__(
            self,
            *,
            LogType: str,
            Encoding: str = ...,
            LogGroupName: str = ...,
            LogPath: str = ...,
            PatternSet: str = ...
        ): ...
    class LogPattern:
        def __init__(self, *, Pattern: str, PatternName: str, Rank: int): ...
    class LogPatternSet:
        def __init__(
            self, *, LogPatterns: List["Application.LogPattern"], PatternSetName: str
        ): ...
    class SubComponentConfigurationDetails:
        def __init__(
            self,
            *,
            AlarmMetrics: List["Application.AlarmMetric"] = ...,
            Logs: List["Application.Log"] = ...,
            WindowsEvents: List["Application.WindowsEvent"] = ...
        ): ...
    class SubComponentTypeConfiguration:
        def __init__(
            self,
            *,
            SubComponentConfigurationDetails: "Application.SubComponentConfigurationDetails",
            SubComponentType: str
        ): ...
    class WindowsEvent:
        def __init__(
            self,
            *,
            EventLevels: List[str],
            EventName: str,
            LogGroupName: str,
            PatternSet: str = ...
        ): ...
