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

_NAMESPACE = "AWS::NetworkFirewall"

class Firewall:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html"""

    FirewallArn: Final[str]

    FirewallId: Final[str]

    EndpointIds: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FirewallName: str,
        FirewallPolicyArn: str,
        SubnetMappings: List["Firewall.SubnetMapping"],
        VpcId: str,
        DeleteProtection: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        FirewallPolicyChangeProtection: bool = ...,
        SubnetChangeProtection: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class SubnetMapping:
        def __init__(self, *, SubnetId: str): ...

class FirewallPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html"""

    FirewallPolicyArn: Final[str]

    FirewallPolicyId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FirewallPolicy: "FirewallPolicy.FirewallPolicy_",
        FirewallPolicyName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ActionDefinition:
        def __init__(
            self, *, PublishMetricAction: "FirewallPolicy.PublishMetricAction" = ...
        ): ...
    class CustomAction:
        def __init__(
            self,
            *,
            ActionDefinition: "FirewallPolicy.ActionDefinition",
            ActionName: str
        ): ...
    class Dimension:
        def __init__(self, *, Value: str): ...
    class FirewallPolicy_:
        def __init__(
            self,
            *,
            StatelessDefaultActions: List[str],
            StatelessFragmentDefaultActions: List[str],
            StatefulRuleGroupReferences: List[
                "FirewallPolicy.StatefulRuleGroupReference"
            ] = ...,
            StatelessCustomActions: List["FirewallPolicy.CustomAction"] = ...,
            StatelessRuleGroupReferences: List[
                "FirewallPolicy.StatelessRuleGroupReference"
            ] = ...
        ): ...
    class PublishMetricAction:
        def __init__(self, *, Dimensions: List["FirewallPolicy.Dimension"]): ...
    class StatefulRuleGroupReference:
        def __init__(self, *, ResourceArn: str): ...
    class StatelessRuleGroupReference:
        def __init__(self, *, Priority: int, ResourceArn: str): ...

class LoggingConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FirewallArn: str,
        LoggingConfiguration: "LoggingConfiguration.LoggingConfiguration_",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FirewallName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LogDestinationConfig:
        def __init__(
            self,
            *,
            LogDestination: Dict[str, str],
            LogDestinationType: str,
            LogType: str
        ): ...
    class LoggingConfiguration_:
        def __init__(
            self,
            *,
            LogDestinationConfigs: List["LoggingConfiguration.LogDestinationConfig"]
        ): ...

class RuleGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html"""

    RuleGroupArn: Final[str]

    RuleGroupId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Capacity: int,
        RuleGroupName: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RuleGroup: "RuleGroup.RuleGroup_" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ActionDefinition:
        def __init__(
            self, *, PublishMetricAction: "RuleGroup.PublishMetricAction" = ...
        ): ...
    class Address:
        def __init__(self, *, AddressDefinition: str): ...
    class CustomAction:
        def __init__(
            self, *, ActionDefinition: "RuleGroup.ActionDefinition", ActionName: str
        ): ...
    class Dimension:
        def __init__(self, *, Value: str): ...
    class Header:
        def __init__(
            self,
            *,
            Destination: str,
            DestinationPort: str,
            Direction: str,
            Protocol: str,
            Source: str,
            SourcePort: str
        ): ...
    class IPSet:
        def __init__(self, *, Definition: List[str] = ...): ...
    class MatchAttributes:
        def __init__(
            self,
            *,
            DestinationPorts: List["RuleGroup.PortRange"] = ...,
            Destinations: List["RuleGroup.Address"] = ...,
            Protocols: List[int] = ...,
            SourcePorts: List["RuleGroup.PortRange"] = ...,
            Sources: List["RuleGroup.Address"] = ...,
            TCPFlags: List["RuleGroup.TCPFlagField"] = ...
        ): ...
    class PortRange:
        def __init__(self, *, FromPort: int, ToPort: int): ...
    class PortSet:
        def __init__(self, *, Definition: List[str] = ...): ...
    class PublishMetricAction:
        def __init__(self, *, Dimensions: List["RuleGroup.Dimension"]): ...
    class RuleDefinition:
        def __init__(
            self, *, Actions: List[str], MatchAttributes: "RuleGroup.MatchAttributes"
        ): ...
    class RuleGroup_:
        def __init__(
            self,
            *,
            RulesSource: "RuleGroup.RulesSource",
            RuleVariables: "RuleGroup.RuleVariables" = ...
        ): ...
    class RuleOption:
        def __init__(self, *, Keyword: str, Settings: List[str] = ...): ...
    class RuleVariables:
        def __init__(
            self,
            *,
            IPSets: Dict[str, "RuleGroup.IPSet"] = ...,
            PortSets: Dict[str, "RuleGroup.PortSet"] = ...
        ): ...
    class RulesSource:
        def __init__(
            self,
            *,
            RulesSourceList: "RuleGroup.RulesSourceList" = ...,
            RulesString: str = ...,
            StatefulRules: List["RuleGroup.StatefulRule"] = ...,
            StatelessRulesAndCustomActions: "RuleGroup.StatelessRulesAndCustomActions" = ...
        ): ...
    class RulesSourceList:
        def __init__(
            self, *, GeneratedRulesType: str, TargetTypes: List[str], Targets: List[str]
        ): ...
    class StatefulRule:
        def __init__(
            self,
            *,
            Action: str,
            Header: "RuleGroup.Header",
            RuleOptions: List["RuleGroup.RuleOption"]
        ): ...
    class StatelessRule:
        def __init__(
            self, *, Priority: int, RuleDefinition: "RuleGroup.RuleDefinition"
        ): ...
    class StatelessRulesAndCustomActions:
        def __init__(
            self,
            *,
            StatelessRules: List["RuleGroup.StatelessRule"],
            CustomActions: List["RuleGroup.CustomAction"] = ...
        ): ...
    class TCPFlagField:
        def __init__(self, *, Flags: List[str], Masks: List[str] = ...): ...
