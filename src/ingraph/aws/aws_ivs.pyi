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

_NAMESPACE = "AWS::IVS"

class Channel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html"""

    Arn: Final[str]

    PlaybackUrl: Final[str]

    IngestEndpoint: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Authorized: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LatencyMode: str = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PlaybackKeyPair:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html"""

    Fingerprint: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PublicKeyMaterial: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class StreamKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html"""

    Arn: Final[str]

    Value: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ChannelArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
