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

_NAMESPACE = "AWS::MediaPackage"

class Asset:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html"""

    Arn: Final[str]

    CreatedAt: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EgressEndpoints: List["Asset.EgressEndpoint"] = ...,
        ResourceId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EgressEndpoint:
        def __init__(self, *, PackagingConfigurationId: str, Url: str): ...

class Channel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Id: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class HlsIngest:
        def __init__(
            self, *, ingestEndpoints: List["Channel.IngestEndpoint"] = ...
        ): ...
    class IngestEndpoint:
        def __init__(
            self,
            *,
            Id: str = ...,
            Password: str = ...,
            Url: str = ...,
            Username: str = ...
        ): ...

class OriginEndpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html"""

    Arn: Final[str]

    Url: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ChannelId: str,
        Id: str,
        Authorization: "OriginEndpoint.Authorization" = ...,
        CmafPackage: "OriginEndpoint.CmafPackage" = ...,
        DashPackage: "OriginEndpoint.DashPackage" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        HlsPackage: "OriginEndpoint.HlsPackage" = ...,
        ManifestName: str = ...,
        MssPackage: "OriginEndpoint.MssPackage" = ...,
        Origination: str = ...,
        StartoverWindowSeconds: int = ...,
        Tags: List["Tag"] = ...,
        TimeDelaySeconds: int = ...,
        UpdateReplacePolicy: str = ...,
        Whitelist: List[str] = ...
    ): ...
    class Authorization:
        def __init__(self, *, CdnIdentifierSecret: str, SecretsRoleArn: str): ...
    class CmafEncryption:
        def __init__(
            self,
            *,
            SpekeKeyProvider: "OriginEndpoint.SpekeKeyProvider",
            KeyRotationIntervalSeconds: int = ...
        ): ...
    class CmafPackage:
        def __init__(
            self,
            *,
            Encryption: "OriginEndpoint.CmafEncryption" = ...,
            HlsManifests: List["OriginEndpoint.HlsManifest"] = ...,
            SegmentDurationSeconds: int = ...,
            SegmentPrefix: str = ...,
            StreamSelection: "OriginEndpoint.StreamSelection" = ...
        ): ...
    class DashEncryption:
        def __init__(
            self,
            *,
            SpekeKeyProvider: "OriginEndpoint.SpekeKeyProvider",
            KeyRotationIntervalSeconds: int = ...
        ): ...
    class DashPackage:
        def __init__(
            self,
            *,
            AdTriggers: List[str] = ...,
            AdsOnDeliveryRestrictions: str = ...,
            Encryption: "OriginEndpoint.DashEncryption" = ...,
            ManifestLayout: str = ...,
            ManifestWindowSeconds: int = ...,
            MinBufferTimeSeconds: int = ...,
            MinUpdatePeriodSeconds: int = ...,
            PeriodTriggers: List[str] = ...,
            Profile: str = ...,
            SegmentDurationSeconds: int = ...,
            SegmentTemplateFormat: str = ...,
            StreamSelection: "OriginEndpoint.StreamSelection" = ...,
            SuggestedPresentationDelaySeconds: int = ...
        ): ...
    class HlsEncryption:
        def __init__(
            self,
            *,
            SpekeKeyProvider: "OriginEndpoint.SpekeKeyProvider",
            ConstantInitializationVector: str = ...,
            EncryptionMethod: str = ...,
            KeyRotationIntervalSeconds: int = ...,
            RepeatExtXKey: bool = ...
        ): ...
    class HlsManifest:
        def __init__(
            self,
            *,
            Id: str,
            AdMarkers: str = ...,
            AdTriggers: List[str] = ...,
            AdsOnDeliveryRestrictions: str = ...,
            IncludeIframeOnlyStream: bool = ...,
            ManifestName: str = ...,
            PlaylistType: str = ...,
            PlaylistWindowSeconds: int = ...,
            ProgramDateTimeIntervalSeconds: int = ...,
            Url: str = ...
        ): ...
    class HlsPackage:
        def __init__(
            self,
            *,
            AdMarkers: str = ...,
            AdTriggers: List[str] = ...,
            AdsOnDeliveryRestrictions: str = ...,
            Encryption: "OriginEndpoint.HlsEncryption" = ...,
            IncludeIframeOnlyStream: bool = ...,
            PlaylistType: str = ...,
            PlaylistWindowSeconds: int = ...,
            ProgramDateTimeIntervalSeconds: int = ...,
            SegmentDurationSeconds: int = ...,
            StreamSelection: "OriginEndpoint.StreamSelection" = ...,
            UseAudioRenditionGroup: bool = ...
        ): ...
    class MssEncryption:
        def __init__(self, *, SpekeKeyProvider: "OriginEndpoint.SpekeKeyProvider"): ...
    class MssPackage:
        def __init__(
            self,
            *,
            Encryption: "OriginEndpoint.MssEncryption" = ...,
            ManifestWindowSeconds: int = ...,
            SegmentDurationSeconds: int = ...,
            StreamSelection: "OriginEndpoint.StreamSelection" = ...
        ): ...
    class SpekeKeyProvider:
        def __init__(
            self,
            *,
            ResourceId: str,
            RoleArn: str,
            SystemIds: List[str],
            Url: str,
            CertificateArn: str = ...
        ): ...
    class StreamSelection:
        def __init__(
            self,
            *,
            MaxVideoBitsPerSecond: int = ...,
            MinVideoBitsPerSecond: int = ...,
            StreamOrder: str = ...
        ): ...

class PackagingConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: "PackagingConfiguration.CmafPackage" = ...,
        DashPackage: "PackagingConfiguration.DashPackage" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HlsPackage: "PackagingConfiguration.HlsPackage" = ...,
        MssPackage: "PackagingConfiguration.MssPackage" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CmafEncryption:
        def __init__(self, *, SpekeKeyProvider: Any): ...
    class CmafPackage:
        def __init__(
            self,
            *,
            HlsManifests: List["PackagingConfiguration.HlsManifest"],
            Encryption: "PackagingConfiguration.CmafEncryption" = ...,
            SegmentDurationSeconds: int = ...
        ): ...
    class DashEncryption:
        def __init__(self, *, SpekeKeyProvider: Any): ...
    class DashManifest:
        def __init__(
            self,
            *,
            ManifestLayout: str = ...,
            ManifestName: str = ...,
            MinBufferTimeSeconds: int = ...,
            Profile: str = ...,
            StreamSelection: "PackagingConfiguration.StreamSelection" = ...
        ): ...
    class DashPackage:
        def __init__(
            self,
            *,
            DashManifests: List["PackagingConfiguration.DashManifest"],
            Encryption: "PackagingConfiguration.DashEncryption" = ...,
            PeriodTriggers: List[str] = ...,
            SegmentDurationSeconds: int = ...,
            SegmentTemplateFormat: str = ...
        ): ...
    class HlsEncryption:
        def __init__(
            self,
            *,
            SpekeKeyProvider: Any,
            ConstantInitializationVector: str = ...,
            EncryptionMethod: str = ...
        ): ...
    class HlsManifest:
        def __init__(
            self,
            *,
            AdMarkers: str = ...,
            IncludeIframeOnlyStream: bool = ...,
            ManifestName: str = ...,
            ProgramDateTimeIntervalSeconds: int = ...,
            RepeatExtXKey: bool = ...,
            StreamSelection: "PackagingConfiguration.StreamSelection" = ...
        ): ...
    class HlsPackage:
        def __init__(
            self,
            *,
            HlsManifests: List["PackagingConfiguration.HlsManifest"],
            Encryption: "PackagingConfiguration.HlsEncryption" = ...,
            SegmentDurationSeconds: int = ...,
            UseAudioRenditionGroup: bool = ...
        ): ...
    class MssEncryption:
        def __init__(self, *, SpekeKeyProvider: Any): ...
    class MssManifest:
        def __init__(
            self,
            *,
            ManifestName: str = ...,
            StreamSelection: "PackagingConfiguration.StreamSelection" = ...
        ): ...
    class MssPackage:
        def __init__(
            self,
            *,
            MssManifests: List["PackagingConfiguration.MssManifest"],
            Encryption: "PackagingConfiguration.MssEncryption" = ...,
            SegmentDurationSeconds: int = ...
        ): ...
    class SpekeKeyProvider:
        def __init__(self, *, RoleArn: str, SystemIds: List[str], Url: str): ...
    class StreamSelection:
        def __init__(
            self,
            *,
            MaxVideoBitsPerSecond: int = ...,
            MinVideoBitsPerSecond: int = ...,
            StreamOrder: str = ...
        ): ...

class PackagingGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html"""

    Arn: Final[str]

    DomainName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Id: str,
        Authorization: "PackagingGroup.Authorization" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Authorization:
        def __init__(self, *, CdnIdentifierSecret: str, SecretsRoleArn: str): ...
