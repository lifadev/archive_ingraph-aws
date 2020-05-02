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

_NAMESPACE = "AWS::IoTEvents"

class DetectorModel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DetectorModelDefinition: "DetectorModel.DetectorModelDefinition" = ...,
        DetectorModelDescription: str = ...,
        DetectorModelName: str = ...,
        EvaluationMethod: str = ...,
        Key: str = ...,
        RoleArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            ClearTimer: "DetectorModel.ClearTimer" = ...,
            DynamoDB: "DetectorModel.DynamoDB" = ...,
            DynamoDBv2: "DetectorModel.DynamoDBv2" = ...,
            Firehose: "DetectorModel.Firehose" = ...,
            IotEvents: "DetectorModel.IotEvents" = ...,
            IotSiteWise: "DetectorModel.IotSiteWise" = ...,
            IotTopicPublish: "DetectorModel.IotTopicPublish" = ...,
            Lambda: "DetectorModel.Lambda" = ...,
            ResetTimer: "DetectorModel.ResetTimer" = ...,
            SetTimer: "DetectorModel.SetTimer" = ...,
            SetVariable: "DetectorModel.SetVariable" = ...,
            Sns: "DetectorModel.Sns" = ...,
            Sqs: "DetectorModel.Sqs" = ...
        ): ...
    class AssetPropertyTimestamp:
        def __init__(self, *, OffsetInNanos: str = ..., TimeInSeconds: str = ...): ...
    class AssetPropertyValue:
        def __init__(
            self,
            *,
            Quality: str = ...,
            Timestamp: "DetectorModel.AssetPropertyTimestamp" = ...,
            Value: "DetectorModel.AssetPropertyVariant" = ...
        ): ...
    class AssetPropertyVariant:
        def __init__(
            self,
            *,
            BooleanValue: str = ...,
            DoubleValue: str = ...,
            IntegerValue: str = ...,
            StringValue: str = ...
        ): ...
    class ClearTimer:
        def __init__(self, *, TimerName: str = ...): ...
    class DetectorModelDefinition:
        def __init__(
            self,
            *,
            InitialStateName: str = ...,
            States: List["DetectorModel.State"] = ...
        ): ...
    class DynamoDB:
        def __init__(
            self,
            *,
            HashKeyField: str = ...,
            HashKeyType: str = ...,
            HashKeyValue: str = ...,
            Operation: str = ...,
            Payload: "DetectorModel.Payload" = ...,
            PayloadField: str = ...,
            RangeKeyField: str = ...,
            RangeKeyType: str = ...,
            RangeKeyValue: str = ...,
            TableName: str = ...
        ): ...
    class DynamoDBv2:
        def __init__(
            self, *, Payload: "DetectorModel.Payload" = ..., TableName: str = ...
        ): ...
    class Event:
        def __init__(
            self,
            *,
            Actions: List["DetectorModel.Action"] = ...,
            Condition: str = ...,
            EventName: str = ...
        ): ...
    class Firehose:
        def __init__(
            self,
            *,
            DeliveryStreamName: str = ...,
            Payload: "DetectorModel.Payload" = ...,
            Separator: str = ...
        ): ...
    class IotEvents:
        def __init__(
            self, *, InputName: str = ..., Payload: "DetectorModel.Payload" = ...
        ): ...
    class IotSiteWise:
        def __init__(
            self,
            *,
            AssetId: str = ...,
            EntryId: str = ...,
            PropertyAlias: str = ...,
            PropertyId: str = ...,
            PropertyValue: "DetectorModel.AssetPropertyValue" = ...
        ): ...
    class IotTopicPublish:
        def __init__(
            self, *, MqttTopic: str = ..., Payload: "DetectorModel.Payload" = ...
        ): ...
    class Lambda:
        def __init__(
            self, *, FunctionArn: str = ..., Payload: "DetectorModel.Payload" = ...
        ): ...
    class OnEnter:
        def __init__(self, *, Events: List["DetectorModel.Event"] = ...): ...
    class OnExit:
        def __init__(self, *, Events: List["DetectorModel.Event"] = ...): ...
    class OnInput:
        def __init__(
            self,
            *,
            Events: List["DetectorModel.Event"] = ...,
            TransitionEvents: List["DetectorModel.TransitionEvent"] = ...
        ): ...
    class Payload:
        def __init__(self, *, ContentExpression: str = ..., Type: str = ...): ...
    class ResetTimer:
        def __init__(self, *, TimerName: str = ...): ...
    class SetTimer:
        def __init__(
            self,
            *,
            DurationExpression: str = ...,
            Seconds: int = ...,
            TimerName: str = ...
        ): ...
    class SetVariable:
        def __init__(self, *, Value: str = ..., VariableName: str = ...): ...
    class Sns:
        def __init__(
            self, *, Payload: "DetectorModel.Payload" = ..., TargetArn: str = ...
        ): ...
    class Sqs:
        def __init__(
            self,
            *,
            Payload: "DetectorModel.Payload" = ...,
            QueueUrl: str = ...,
            UseBase64: bool = ...
        ): ...
    class State:
        def __init__(
            self,
            *,
            OnEnter: "DetectorModel.OnEnter" = ...,
            OnExit: "DetectorModel.OnExit" = ...,
            OnInput: "DetectorModel.OnInput" = ...,
            StateName: str = ...
        ): ...
    class TransitionEvent:
        def __init__(
            self,
            *,
            Actions: List["DetectorModel.Action"] = ...,
            Condition: str = ...,
            EventName: str = ...,
            NextState: str = ...
        ): ...

class Input:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InputDefinition: "Input.InputDefinition" = ...,
        InputDescription: str = ...,
        InputName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Attribute:
        def __init__(self, *, JsonPath: str = ...): ...
    class InputDefinition:
        def __init__(self, *, Attributes: List["Input.Attribute"] = ...): ...
