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

_NAMESPACE = "AWS::MediaLive"

class Channel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html"""

    Arn: Final[str]

    Inputs: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CdiInputSpecification: "Channel.CdiInputSpecification" = ...,
        ChannelClass: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Destinations: List["Channel.OutputDestination"] = ...,
        EncoderSettings: "Channel.EncoderSettings" = ...,
        InputAttachments: List["Channel.InputAttachment"] = ...,
        InputSpecification: "Channel.InputSpecification" = ...,
        LogLevel: str = ...,
        Name: str = ...,
        RoleArn: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AacSettings:
        def __init__(
            self,
            *,
            Bitrate: float = ...,
            CodingMode: str = ...,
            InputType: str = ...,
            Profile: str = ...,
            RateControlMode: str = ...,
            RawFormat: str = ...,
            SampleRate: float = ...,
            Spec: str = ...,
            VbrQuality: str = ...
        ): ...
    class Ac3Settings:
        def __init__(
            self,
            *,
            Bitrate: float = ...,
            BitstreamMode: str = ...,
            CodingMode: str = ...,
            Dialnorm: int = ...,
            DrcProfile: str = ...,
            LfeFilter: str = ...,
            MetadataControl: str = ...
        ): ...
    class AncillarySourceSettings:
        def __init__(self, *, SourceAncillaryChannelNumber: int = ...): ...
    class ArchiveContainerSettings:
        def __init__(
            self,
            *,
            M2tsSettings: "Channel.M2tsSettings" = ...,
            RawSettings: "Channel.RawSettings" = ...
        ): ...
    class ArchiveGroupSettings:
        def __init__(
            self,
            *,
            Destination: "Channel.OutputLocationRef" = ...,
            RolloverInterval: int = ...
        ): ...
    class ArchiveOutputSettings:
        def __init__(
            self,
            *,
            ContainerSettings: "Channel.ArchiveContainerSettings" = ...,
            Extension: str = ...,
            NameModifier: str = ...
        ): ...
    class AribDestinationSettings:
        def __init__(self) -> None: ...
    class AribSourceSettings:
        def __init__(self) -> None: ...
    class AudioChannelMapping:
        def __init__(
            self,
            *,
            InputChannelLevels: List["Channel.InputChannelLevel"] = ...,
            OutputChannel: int = ...
        ): ...
    class AudioCodecSettings:
        def __init__(
            self,
            *,
            AacSettings: "Channel.AacSettings" = ...,
            Ac3Settings: "Channel.Ac3Settings" = ...,
            Eac3Settings: "Channel.Eac3Settings" = ...,
            Mp2Settings: "Channel.Mp2Settings" = ...,
            PassThroughSettings: "Channel.PassThroughSettings" = ...,
            WavSettings: "Channel.WavSettings" = ...
        ): ...
    class AudioDescription:
        def __init__(
            self,
            *,
            AudioNormalizationSettings: "Channel.AudioNormalizationSettings" = ...,
            AudioSelectorName: str = ...,
            AudioType: str = ...,
            AudioTypeControl: str = ...,
            CodecSettings: "Channel.AudioCodecSettings" = ...,
            LanguageCode: str = ...,
            LanguageCodeControl: str = ...,
            Name: str = ...,
            RemixSettings: "Channel.RemixSettings" = ...,
            StreamName: str = ...
        ): ...
    class AudioLanguageSelection:
        def __init__(
            self, *, LanguageCode: str = ..., LanguageSelectionPolicy: str = ...
        ): ...
    class AudioNormalizationSettings:
        def __init__(
            self,
            *,
            Algorithm: str = ...,
            AlgorithmControl: str = ...,
            TargetLkfs: float = ...
        ): ...
    class AudioOnlyHlsSettings:
        def __init__(
            self,
            *,
            AudioGroupId: str = ...,
            AudioOnlyImage: "Channel.InputLocation" = ...,
            AudioTrackType: str = ...,
            SegmentType: str = ...
        ): ...
    class AudioPidSelection:
        def __init__(self, *, Pid: int = ...): ...
    class AudioSelector:
        def __init__(
            self,
            *,
            Name: str = ...,
            SelectorSettings: "Channel.AudioSelectorSettings" = ...
        ): ...
    class AudioSelectorSettings:
        def __init__(
            self,
            *,
            AudioLanguageSelection: "Channel.AudioLanguageSelection" = ...,
            AudioPidSelection: "Channel.AudioPidSelection" = ...,
            AudioTrackSelection: "Channel.AudioTrackSelection" = ...
        ): ...
    class AudioSilenceFailoverSettings:
        def __init__(
            self, *, AudioSelectorName: str = ..., AudioSilenceThresholdMsec: int = ...
        ): ...
    class AudioTrack:
        def __init__(self, *, Track: int = ...): ...
    class AudioTrackSelection:
        def __init__(self, *, Tracks: List["Channel.AudioTrack"] = ...): ...
    class AutomaticInputFailoverSettings:
        def __init__(
            self,
            *,
            ErrorClearTimeMsec: int = ...,
            FailoverConditions: List["Channel.FailoverCondition"] = ...,
            InputPreference: str = ...,
            SecondaryInputId: str = ...
        ): ...
    class AvailBlanking:
        def __init__(
            self, *, AvailBlankingImage: "Channel.InputLocation" = ..., State: str = ...
        ): ...
    class AvailConfiguration:
        def __init__(self, *, AvailSettings: "Channel.AvailSettings" = ...): ...
    class AvailSettings:
        def __init__(
            self,
            *,
            Scte35SpliceInsert: "Channel.Scte35SpliceInsert" = ...,
            Scte35TimeSignalApos: "Channel.Scte35TimeSignalApos" = ...
        ): ...
    class BlackoutSlate:
        def __init__(
            self,
            *,
            BlackoutSlateImage: "Channel.InputLocation" = ...,
            NetworkEndBlackout: str = ...,
            NetworkEndBlackoutImage: "Channel.InputLocation" = ...,
            NetworkId: str = ...,
            State: str = ...
        ): ...
    class BurnInDestinationSettings:
        def __init__(
            self,
            *,
            Alignment: str = ...,
            BackgroundColor: str = ...,
            BackgroundOpacity: int = ...,
            Font: "Channel.InputLocation" = ...,
            FontColor: str = ...,
            FontOpacity: int = ...,
            FontResolution: int = ...,
            FontSize: str = ...,
            OutlineColor: str = ...,
            OutlineSize: int = ...,
            ShadowColor: str = ...,
            ShadowOpacity: int = ...,
            ShadowXOffset: int = ...,
            ShadowYOffset: int = ...,
            TeletextGridControl: str = ...,
            XPosition: int = ...,
            YPosition: int = ...
        ): ...
    class CaptionDescription:
        def __init__(
            self,
            *,
            CaptionSelectorName: str = ...,
            DestinationSettings: "Channel.CaptionDestinationSettings" = ...,
            LanguageCode: str = ...,
            LanguageDescription: str = ...,
            Name: str = ...
        ): ...
    class CaptionDestinationSettings:
        def __init__(
            self,
            *,
            AribDestinationSettings: "Channel.AribDestinationSettings" = ...,
            BurnInDestinationSettings: "Channel.BurnInDestinationSettings" = ...,
            DvbSubDestinationSettings: "Channel.DvbSubDestinationSettings" = ...,
            EbuTtDDestinationSettings: "Channel.EbuTtDDestinationSettings" = ...,
            EmbeddedDestinationSettings: "Channel.EmbeddedDestinationSettings" = ...,
            EmbeddedPlusScte20DestinationSettings: "Channel.EmbeddedPlusScte20DestinationSettings" = ...,
            RtmpCaptionInfoDestinationSettings: "Channel.RtmpCaptionInfoDestinationSettings" = ...,
            Scte20PlusEmbeddedDestinationSettings: "Channel.Scte20PlusEmbeddedDestinationSettings" = ...,
            Scte27DestinationSettings: "Channel.Scte27DestinationSettings" = ...,
            SmpteTtDestinationSettings: "Channel.SmpteTtDestinationSettings" = ...,
            TeletextDestinationSettings: "Channel.TeletextDestinationSettings" = ...,
            TtmlDestinationSettings: "Channel.TtmlDestinationSettings" = ...,
            WebvttDestinationSettings: "Channel.WebvttDestinationSettings" = ...
        ): ...
    class CaptionLanguageMapping:
        def __init__(
            self,
            *,
            CaptionChannel: int = ...,
            LanguageCode: str = ...,
            LanguageDescription: str = ...
        ): ...
    class CaptionSelector:
        def __init__(
            self,
            *,
            LanguageCode: str = ...,
            Name: str = ...,
            SelectorSettings: "Channel.CaptionSelectorSettings" = ...
        ): ...
    class CaptionSelectorSettings:
        def __init__(
            self,
            *,
            AncillarySourceSettings: "Channel.AncillarySourceSettings" = ...,
            AribSourceSettings: "Channel.AribSourceSettings" = ...,
            DvbSubSourceSettings: "Channel.DvbSubSourceSettings" = ...,
            EmbeddedSourceSettings: "Channel.EmbeddedSourceSettings" = ...,
            Scte20SourceSettings: "Channel.Scte20SourceSettings" = ...,
            Scte27SourceSettings: "Channel.Scte27SourceSettings" = ...,
            TeletextSourceSettings: "Channel.TeletextSourceSettings" = ...
        ): ...
    class CdiInputSpecification:
        def __init__(self, *, Resolution: str = ...): ...
    class ColorSpacePassthroughSettings:
        def __init__(self) -> None: ...
    class DvbNitSettings:
        def __init__(
            self,
            *,
            NetworkId: int = ...,
            NetworkName: str = ...,
            RepInterval: int = ...
        ): ...
    class DvbSdtSettings:
        def __init__(
            self,
            *,
            OutputSdt: str = ...,
            RepInterval: int = ...,
            ServiceName: str = ...,
            ServiceProviderName: str = ...
        ): ...
    class DvbSubDestinationSettings:
        def __init__(
            self,
            *,
            Alignment: str = ...,
            BackgroundColor: str = ...,
            BackgroundOpacity: int = ...,
            Font: "Channel.InputLocation" = ...,
            FontColor: str = ...,
            FontOpacity: int = ...,
            FontResolution: int = ...,
            FontSize: str = ...,
            OutlineColor: str = ...,
            OutlineSize: int = ...,
            ShadowColor: str = ...,
            ShadowOpacity: int = ...,
            ShadowXOffset: int = ...,
            ShadowYOffset: int = ...,
            TeletextGridControl: str = ...,
            XPosition: int = ...,
            YPosition: int = ...
        ): ...
    class DvbSubSourceSettings:
        def __init__(self, *, Pid: int = ...): ...
    class DvbTdtSettings:
        def __init__(self, *, RepInterval: int = ...): ...
    class Eac3Settings:
        def __init__(
            self,
            *,
            AttenuationControl: str = ...,
            Bitrate: float = ...,
            BitstreamMode: str = ...,
            CodingMode: str = ...,
            DcFilter: str = ...,
            Dialnorm: int = ...,
            DrcLine: str = ...,
            DrcRf: str = ...,
            LfeControl: str = ...,
            LfeFilter: str = ...,
            LoRoCenterMixLevel: float = ...,
            LoRoSurroundMixLevel: float = ...,
            LtRtCenterMixLevel: float = ...,
            LtRtSurroundMixLevel: float = ...,
            MetadataControl: str = ...,
            PassthroughControl: str = ...,
            PhaseControl: str = ...,
            StereoDownmix: str = ...,
            SurroundExMode: str = ...,
            SurroundMode: str = ...
        ): ...
    class EbuTtDDestinationSettings:
        def __init__(
            self,
            *,
            FillLineGap: str = ...,
            FontFamily: str = ...,
            StyleControl: str = ...
        ): ...
    class EmbeddedDestinationSettings:
        def __init__(self) -> None: ...
    class EmbeddedPlusScte20DestinationSettings:
        def __init__(self) -> None: ...
    class EmbeddedSourceSettings:
        def __init__(
            self,
            *,
            Convert608To708: str = ...,
            Scte20Detection: str = ...,
            Source608ChannelNumber: int = ...,
            Source608TrackNumber: int = ...
        ): ...
    class EncoderSettings:
        def __init__(
            self,
            *,
            AudioDescriptions: List["Channel.AudioDescription"] = ...,
            AvailBlanking: "Channel.AvailBlanking" = ...,
            AvailConfiguration: "Channel.AvailConfiguration" = ...,
            BlackoutSlate: "Channel.BlackoutSlate" = ...,
            CaptionDescriptions: List["Channel.CaptionDescription"] = ...,
            FeatureActivations: "Channel.FeatureActivations" = ...,
            GlobalConfiguration: "Channel.GlobalConfiguration" = ...,
            NielsenConfiguration: "Channel.NielsenConfiguration" = ...,
            OutputGroups: List["Channel.OutputGroup"] = ...,
            TimecodeConfig: "Channel.TimecodeConfig" = ...,
            VideoDescriptions: List["Channel.VideoDescription"] = ...
        ): ...
    class FailoverCondition:
        def __init__(
            self,
            *,
            FailoverConditionSettings: "Channel.FailoverConditionSettings" = ...
        ): ...
    class FailoverConditionSettings:
        def __init__(
            self,
            *,
            AudioSilenceSettings: "Channel.AudioSilenceFailoverSettings" = ...,
            InputLossSettings: "Channel.InputLossFailoverSettings" = ...,
            VideoBlackSettings: "Channel.VideoBlackFailoverSettings" = ...
        ): ...
    class FeatureActivations:
        def __init__(self, *, InputPrepareScheduleActions: str = ...): ...
    class FecOutputSettings:
        def __init__(
            self, *, ColumnDepth: int = ..., IncludeFec: str = ..., RowLength: int = ...
        ): ...
    class Fmp4HlsSettings:
        def __init__(
            self,
            *,
            AudioRenditionSets: str = ...,
            NielsenId3Behavior: str = ...,
            TimedMetadataBehavior: str = ...
        ): ...
    class FrameCaptureGroupSettings:
        def __init__(self, *, Destination: "Channel.OutputLocationRef" = ...): ...
    class FrameCaptureOutputSettings:
        def __init__(self, *, NameModifier: str = ...): ...
    class FrameCaptureSettings:
        def __init__(
            self, *, CaptureInterval: int = ..., CaptureIntervalUnits: str = ...
        ): ...
    class GlobalConfiguration:
        def __init__(
            self,
            *,
            InitialAudioGain: int = ...,
            InputEndAction: str = ...,
            InputLossBehavior: "Channel.InputLossBehavior" = ...,
            OutputLockingMode: str = ...,
            OutputTimingSource: str = ...,
            SupportLowFramerateInputs: str = ...
        ): ...
    class H264ColorSpaceSettings:
        def __init__(
            self,
            *,
            ColorSpacePassthroughSettings: "Channel.ColorSpacePassthroughSettings" = ...,
            Rec601Settings: "Channel.Rec601Settings" = ...,
            Rec709Settings: "Channel.Rec709Settings" = ...
        ): ...
    class H264FilterSettings:
        def __init__(
            self, *, TemporalFilterSettings: "Channel.TemporalFilterSettings" = ...
        ): ...
    class H264Settings:
        def __init__(
            self,
            *,
            AdaptiveQuantization: str = ...,
            AfdSignaling: str = ...,
            Bitrate: int = ...,
            BufFillPct: int = ...,
            BufSize: int = ...,
            ColorMetadata: str = ...,
            ColorSpaceSettings: "Channel.H264ColorSpaceSettings" = ...,
            EntropyEncoding: str = ...,
            FilterSettings: "Channel.H264FilterSettings" = ...,
            FixedAfd: str = ...,
            FlickerAq: str = ...,
            ForceFieldPictures: str = ...,
            FramerateControl: str = ...,
            FramerateDenominator: int = ...,
            FramerateNumerator: int = ...,
            GopBReference: str = ...,
            GopClosedCadence: int = ...,
            GopNumBFrames: int = ...,
            GopSize: float = ...,
            GopSizeUnits: str = ...,
            Level: str = ...,
            LookAheadRateControl: str = ...,
            MaxBitrate: int = ...,
            MinIInterval: int = ...,
            NumRefFrames: int = ...,
            ParControl: str = ...,
            ParDenominator: int = ...,
            ParNumerator: int = ...,
            Profile: str = ...,
            QualityLevel: str = ...,
            QvbrQualityLevel: int = ...,
            RateControlMode: str = ...,
            ScanType: str = ...,
            SceneChangeDetect: str = ...,
            Slices: int = ...,
            Softness: int = ...,
            SpatialAq: str = ...,
            SubgopLength: str = ...,
            Syntax: str = ...,
            TemporalAq: str = ...,
            TimecodeInsertion: str = ...
        ): ...
    class H265ColorSpaceSettings:
        def __init__(
            self,
            *,
            ColorSpacePassthroughSettings: "Channel.ColorSpacePassthroughSettings" = ...,
            Hdr10Settings: "Channel.Hdr10Settings" = ...,
            Rec601Settings: "Channel.Rec601Settings" = ...,
            Rec709Settings: "Channel.Rec709Settings" = ...
        ): ...
    class H265FilterSettings:
        def __init__(
            self, *, TemporalFilterSettings: "Channel.TemporalFilterSettings" = ...
        ): ...
    class H265Settings:
        def __init__(
            self,
            *,
            AdaptiveQuantization: str = ...,
            AfdSignaling: str = ...,
            AlternativeTransferFunction: str = ...,
            Bitrate: int = ...,
            BufSize: int = ...,
            ColorMetadata: str = ...,
            ColorSpaceSettings: "Channel.H265ColorSpaceSettings" = ...,
            FilterSettings: "Channel.H265FilterSettings" = ...,
            FixedAfd: str = ...,
            FlickerAq: str = ...,
            FramerateDenominator: int = ...,
            FramerateNumerator: int = ...,
            GopClosedCadence: int = ...,
            GopSize: float = ...,
            GopSizeUnits: str = ...,
            Level: str = ...,
            LookAheadRateControl: str = ...,
            MaxBitrate: int = ...,
            MinIInterval: int = ...,
            ParDenominator: int = ...,
            ParNumerator: int = ...,
            Profile: str = ...,
            QvbrQualityLevel: int = ...,
            RateControlMode: str = ...,
            ScanType: str = ...,
            SceneChangeDetect: str = ...,
            Slices: int = ...,
            Tier: str = ...,
            TimecodeInsertion: str = ...
        ): ...
    class Hdr10Settings:
        def __init__(self, *, MaxCll: int = ..., MaxFall: int = ...): ...
    class HlsAkamaiSettings:
        def __init__(
            self,
            *,
            ConnectionRetryInterval: int = ...,
            FilecacheDuration: int = ...,
            HttpTransferMode: str = ...,
            NumRetries: int = ...,
            RestartDelay: int = ...,
            Salt: str = ...,
            Token: str = ...
        ): ...
    class HlsBasicPutSettings:
        def __init__(
            self,
            *,
            ConnectionRetryInterval: int = ...,
            FilecacheDuration: int = ...,
            NumRetries: int = ...,
            RestartDelay: int = ...
        ): ...
    class HlsCdnSettings:
        def __init__(
            self,
            *,
            HlsAkamaiSettings: "Channel.HlsAkamaiSettings" = ...,
            HlsBasicPutSettings: "Channel.HlsBasicPutSettings" = ...,
            HlsMediaStoreSettings: "Channel.HlsMediaStoreSettings" = ...,
            HlsWebdavSettings: "Channel.HlsWebdavSettings" = ...
        ): ...
    class HlsGroupSettings:
        def __init__(
            self,
            *,
            AdMarkers: List[str] = ...,
            BaseUrlContent: str = ...,
            BaseUrlContent1: str = ...,
            BaseUrlManifest: str = ...,
            BaseUrlManifest1: str = ...,
            CaptionLanguageMappings: List["Channel.CaptionLanguageMapping"] = ...,
            CaptionLanguageSetting: str = ...,
            ClientCache: str = ...,
            CodecSpecification: str = ...,
            ConstantIv: str = ...,
            Destination: "Channel.OutputLocationRef" = ...,
            DirectoryStructure: str = ...,
            DiscontinuityTags: str = ...,
            EncryptionType: str = ...,
            HlsCdnSettings: "Channel.HlsCdnSettings" = ...,
            HlsId3SegmentTagging: str = ...,
            IFrameOnlyPlaylists: str = ...,
            IncompleteSegmentBehavior: str = ...,
            IndexNSegments: int = ...,
            InputLossAction: str = ...,
            IvInManifest: str = ...,
            IvSource: str = ...,
            KeepSegments: int = ...,
            KeyFormat: str = ...,
            KeyFormatVersions: str = ...,
            KeyProviderSettings: "Channel.KeyProviderSettings" = ...,
            ManifestCompression: str = ...,
            ManifestDurationFormat: str = ...,
            MinSegmentLength: int = ...,
            Mode: str = ...,
            OutputSelection: str = ...,
            ProgramDateTime: str = ...,
            ProgramDateTimePeriod: int = ...,
            RedundantManifest: str = ...,
            SegmentLength: int = ...,
            SegmentationMode: str = ...,
            SegmentsPerSubdirectory: int = ...,
            StreamInfResolution: str = ...,
            TimedMetadataId3Frame: str = ...,
            TimedMetadataId3Period: int = ...,
            TimestampDeltaMilliseconds: int = ...,
            TsFileMode: str = ...
        ): ...
    class HlsInputSettings:
        def __init__(
            self,
            *,
            Bandwidth: int = ...,
            BufferSegments: int = ...,
            Retries: int = ...,
            RetryInterval: int = ...
        ): ...
    class HlsMediaStoreSettings:
        def __init__(
            self,
            *,
            ConnectionRetryInterval: int = ...,
            FilecacheDuration: int = ...,
            MediaStoreStorageClass: str = ...,
            NumRetries: int = ...,
            RestartDelay: int = ...
        ): ...
    class HlsOutputSettings:
        def __init__(
            self,
            *,
            H265PackagingType: str = ...,
            HlsSettings: "Channel.HlsSettings" = ...,
            NameModifier: str = ...,
            SegmentModifier: str = ...
        ): ...
    class HlsSettings:
        def __init__(
            self,
            *,
            AudioOnlyHlsSettings: "Channel.AudioOnlyHlsSettings" = ...,
            Fmp4HlsSettings: "Channel.Fmp4HlsSettings" = ...,
            StandardHlsSettings: "Channel.StandardHlsSettings" = ...
        ): ...
    class HlsWebdavSettings:
        def __init__(
            self,
            *,
            ConnectionRetryInterval: int = ...,
            FilecacheDuration: int = ...,
            HttpTransferMode: str = ...,
            NumRetries: int = ...,
            RestartDelay: int = ...
        ): ...
    class InputAttachment:
        def __init__(
            self,
            *,
            AutomaticInputFailoverSettings: "Channel.AutomaticInputFailoverSettings" = ...,
            InputAttachmentName: str = ...,
            InputId: str = ...,
            InputSettings: "Channel.InputSettings" = ...
        ): ...
    class InputChannelLevel:
        def __init__(self, *, Gain: int = ..., InputChannel: int = ...): ...
    class InputLocation:
        def __init__(
            self, *, PasswordParam: str = ..., Uri: str = ..., Username: str = ...
        ): ...
    class InputLossBehavior:
        def __init__(
            self,
            *,
            BlackFrameMsec: int = ...,
            InputLossImageColor: str = ...,
            InputLossImageSlate: "Channel.InputLocation" = ...,
            InputLossImageType: str = ...,
            RepeatFrameMsec: int = ...
        ): ...
    class InputLossFailoverSettings:
        def __init__(self, *, InputLossThresholdMsec: int = ...): ...
    class InputSettings:
        def __init__(
            self,
            *,
            AudioSelectors: List["Channel.AudioSelector"] = ...,
            CaptionSelectors: List["Channel.CaptionSelector"] = ...,
            DeblockFilter: str = ...,
            DenoiseFilter: str = ...,
            FilterStrength: int = ...,
            InputFilter: str = ...,
            NetworkInputSettings: "Channel.NetworkInputSettings" = ...,
            Smpte2038DataPreference: str = ...,
            SourceEndBehavior: str = ...,
            VideoSelector: "Channel.VideoSelector" = ...
        ): ...
    class InputSpecification:
        def __init__(
            self, *, Codec: str = ..., MaximumBitrate: str = ..., Resolution: str = ...
        ): ...
    class KeyProviderSettings:
        def __init__(self, *, StaticKeySettings: "Channel.StaticKeySettings" = ...): ...
    class M2tsSettings:
        def __init__(
            self,
            *,
            AbsentInputAudioBehavior: str = ...,
            Arib: str = ...,
            AribCaptionsPid: str = ...,
            AribCaptionsPidControl: str = ...,
            AudioBufferModel: str = ...,
            AudioFramesPerPes: int = ...,
            AudioPids: str = ...,
            AudioStreamType: str = ...,
            Bitrate: int = ...,
            BufferModel: str = ...,
            CcDescriptor: str = ...,
            DvbNitSettings: "Channel.DvbNitSettings" = ...,
            DvbSdtSettings: "Channel.DvbSdtSettings" = ...,
            DvbSubPids: str = ...,
            DvbTdtSettings: "Channel.DvbTdtSettings" = ...,
            DvbTeletextPid: str = ...,
            Ebif: str = ...,
            EbpAudioInterval: str = ...,
            EbpLookaheadMs: int = ...,
            EbpPlacement: str = ...,
            EcmPid: str = ...,
            EsRateInPes: str = ...,
            EtvPlatformPid: str = ...,
            EtvSignalPid: str = ...,
            FragmentTime: float = ...,
            Klv: str = ...,
            KlvDataPids: str = ...,
            NielsenId3Behavior: str = ...,
            NullPacketBitrate: float = ...,
            PatInterval: int = ...,
            PcrControl: str = ...,
            PcrPeriod: int = ...,
            PcrPid: str = ...,
            PmtInterval: int = ...,
            PmtPid: str = ...,
            ProgramNum: int = ...,
            RateMode: str = ...,
            Scte27Pids: str = ...,
            Scte35Control: str = ...,
            Scte35Pid: str = ...,
            SegmentationMarkers: str = ...,
            SegmentationStyle: str = ...,
            SegmentationTime: float = ...,
            TimedMetadataBehavior: str = ...,
            TimedMetadataPid: str = ...,
            TransportStreamId: int = ...,
            VideoPid: str = ...
        ): ...
    class M3u8Settings:
        def __init__(
            self,
            *,
            AudioFramesPerPes: int = ...,
            AudioPids: str = ...,
            EcmPid: str = ...,
            NielsenId3Behavior: str = ...,
            PatInterval: int = ...,
            PcrControl: str = ...,
            PcrPeriod: int = ...,
            PcrPid: str = ...,
            PmtInterval: int = ...,
            PmtPid: str = ...,
            ProgramNum: int = ...,
            Scte35Behavior: str = ...,
            Scte35Pid: str = ...,
            TimedMetadataBehavior: str = ...,
            TimedMetadataPid: str = ...,
            TransportStreamId: int = ...,
            VideoPid: str = ...
        ): ...
    class MediaPackageGroupSettings:
        def __init__(self, *, Destination: "Channel.OutputLocationRef" = ...): ...
    class MediaPackageOutputDestinationSettings:
        def __init__(self, *, ChannelId: str = ...): ...
    class MediaPackageOutputSettings:
        def __init__(self) -> None: ...
    class Mp2Settings:
        def __init__(
            self,
            *,
            Bitrate: float = ...,
            CodingMode: str = ...,
            SampleRate: float = ...
        ): ...
    class Mpeg2FilterSettings:
        def __init__(
            self, *, TemporalFilterSettings: "Channel.TemporalFilterSettings" = ...
        ): ...
    class Mpeg2Settings:
        def __init__(
            self,
            *,
            AdaptiveQuantization: str = ...,
            AfdSignaling: str = ...,
            ColorMetadata: str = ...,
            ColorSpace: str = ...,
            DisplayAspectRatio: str = ...,
            FilterSettings: "Channel.Mpeg2FilterSettings" = ...,
            FixedAfd: str = ...,
            FramerateDenominator: int = ...,
            FramerateNumerator: int = ...,
            GopClosedCadence: int = ...,
            GopNumBFrames: int = ...,
            GopSize: float = ...,
            GopSizeUnits: str = ...,
            ScanType: str = ...,
            SubgopLength: str = ...,
            TimecodeInsertion: str = ...
        ): ...
    class MsSmoothGroupSettings:
        def __init__(
            self,
            *,
            AcquisitionPointId: str = ...,
            AudioOnlyTimecodeControl: str = ...,
            CertificateMode: str = ...,
            ConnectionRetryInterval: int = ...,
            Destination: "Channel.OutputLocationRef" = ...,
            EventId: str = ...,
            EventIdMode: str = ...,
            EventStopBehavior: str = ...,
            FilecacheDuration: int = ...,
            FragmentLength: int = ...,
            InputLossAction: str = ...,
            NumRetries: int = ...,
            RestartDelay: int = ...,
            SegmentationMode: str = ...,
            SendDelayMs: int = ...,
            SparseTrackType: str = ...,
            StreamManifestBehavior: str = ...,
            TimestampOffset: str = ...,
            TimestampOffsetMode: str = ...
        ): ...
    class MsSmoothOutputSettings:
        def __init__(
            self, *, H265PackagingType: str = ..., NameModifier: str = ...
        ): ...
    class MultiplexGroupSettings:
        def __init__(self) -> None: ...
    class MultiplexOutputSettings:
        def __init__(self, *, Destination: "Channel.OutputLocationRef" = ...): ...
    class MultiplexProgramChannelDestinationSettings:
        def __init__(self, *, MultiplexId: str = ..., ProgramName: str = ...): ...
    class NetworkInputSettings:
        def __init__(
            self,
            *,
            HlsInputSettings: "Channel.HlsInputSettings" = ...,
            ServerValidation: str = ...
        ): ...
    class NielsenConfiguration:
        def __init__(
            self, *, DistributorId: str = ..., NielsenPcmToId3Tagging: str = ...
        ): ...
    class Output:
        def __init__(
            self,
            *,
            AudioDescriptionNames: List[str] = ...,
            CaptionDescriptionNames: List[str] = ...,
            OutputName: str = ...,
            OutputSettings: "Channel.OutputSettings" = ...,
            VideoDescriptionName: str = ...
        ): ...
    class OutputDestination:
        def __init__(
            self,
            *,
            Id: str = ...,
            MediaPackageSettings: List[
                "Channel.MediaPackageOutputDestinationSettings"
            ] = ...,
            MultiplexSettings: "Channel.MultiplexProgramChannelDestinationSettings" = ...,
            Settings: List["Channel.OutputDestinationSettings"] = ...
        ): ...
    class OutputDestinationSettings:
        def __init__(
            self,
            *,
            PasswordParam: str = ...,
            StreamName: str = ...,
            Url: str = ...,
            Username: str = ...
        ): ...
    class OutputGroup:
        def __init__(
            self,
            *,
            Name: str = ...,
            OutputGroupSettings: "Channel.OutputGroupSettings" = ...,
            Outputs: List["Channel.Output"] = ...
        ): ...
    class OutputGroupSettings:
        def __init__(
            self,
            *,
            ArchiveGroupSettings: "Channel.ArchiveGroupSettings" = ...,
            FrameCaptureGroupSettings: "Channel.FrameCaptureGroupSettings" = ...,
            HlsGroupSettings: "Channel.HlsGroupSettings" = ...,
            MediaPackageGroupSettings: "Channel.MediaPackageGroupSettings" = ...,
            MsSmoothGroupSettings: "Channel.MsSmoothGroupSettings" = ...,
            MultiplexGroupSettings: "Channel.MultiplexGroupSettings" = ...,
            RtmpGroupSettings: "Channel.RtmpGroupSettings" = ...,
            UdpGroupSettings: "Channel.UdpGroupSettings" = ...
        ): ...
    class OutputLocationRef:
        def __init__(self, *, DestinationRefId: str = ...): ...
    class OutputSettings:
        def __init__(
            self,
            *,
            ArchiveOutputSettings: "Channel.ArchiveOutputSettings" = ...,
            FrameCaptureOutputSettings: "Channel.FrameCaptureOutputSettings" = ...,
            HlsOutputSettings: "Channel.HlsOutputSettings" = ...,
            MediaPackageOutputSettings: "Channel.MediaPackageOutputSettings" = ...,
            MsSmoothOutputSettings: "Channel.MsSmoothOutputSettings" = ...,
            MultiplexOutputSettings: "Channel.MultiplexOutputSettings" = ...,
            RtmpOutputSettings: "Channel.RtmpOutputSettings" = ...,
            UdpOutputSettings: "Channel.UdpOutputSettings" = ...
        ): ...
    class PassThroughSettings:
        def __init__(self) -> None: ...
    class RawSettings:
        def __init__(self) -> None: ...
    class Rec601Settings:
        def __init__(self) -> None: ...
    class Rec709Settings:
        def __init__(self) -> None: ...
    class RemixSettings:
        def __init__(
            self,
            *,
            ChannelMappings: List["Channel.AudioChannelMapping"] = ...,
            ChannelsIn: int = ...,
            ChannelsOut: int = ...
        ): ...
    class RtmpCaptionInfoDestinationSettings:
        def __init__(self) -> None: ...
    class RtmpGroupSettings:
        def __init__(
            self,
            *,
            AdMarkers: List[str] = ...,
            AuthenticationScheme: str = ...,
            CacheFullBehavior: str = ...,
            CacheLength: int = ...,
            CaptionData: str = ...,
            InputLossAction: str = ...,
            RestartDelay: int = ...
        ): ...
    class RtmpOutputSettings:
        def __init__(
            self,
            *,
            CertificateMode: str = ...,
            ConnectionRetryInterval: int = ...,
            Destination: "Channel.OutputLocationRef" = ...,
            NumRetries: int = ...
        ): ...
    class Scte20PlusEmbeddedDestinationSettings:
        def __init__(self) -> None: ...
    class Scte20SourceSettings:
        def __init__(
            self, *, Convert608To708: str = ..., Source608ChannelNumber: int = ...
        ): ...
    class Scte27DestinationSettings:
        def __init__(self) -> None: ...
    class Scte27SourceSettings:
        def __init__(self, *, Pid: int = ...): ...
    class Scte35SpliceInsert:
        def __init__(
            self,
            *,
            AdAvailOffset: int = ...,
            NoRegionalBlackoutFlag: str = ...,
            WebDeliveryAllowedFlag: str = ...
        ): ...
    class Scte35TimeSignalApos:
        def __init__(
            self,
            *,
            AdAvailOffset: int = ...,
            NoRegionalBlackoutFlag: str = ...,
            WebDeliveryAllowedFlag: str = ...
        ): ...
    class SmpteTtDestinationSettings:
        def __init__(self) -> None: ...
    class StandardHlsSettings:
        def __init__(
            self,
            *,
            AudioRenditionSets: str = ...,
            M3u8Settings: "Channel.M3u8Settings" = ...
        ): ...
    class StaticKeySettings:
        def __init__(
            self,
            *,
            KeyProviderServer: "Channel.InputLocation" = ...,
            StaticKeyValue: str = ...
        ): ...
    class TeletextDestinationSettings:
        def __init__(self) -> None: ...
    class TeletextSourceSettings:
        def __init__(self, *, PageNumber: str = ...): ...
    class TemporalFilterSettings:
        def __init__(self, *, PostFilterSharpening: str = ..., Strength: str = ...): ...
    class TimecodeConfig:
        def __init__(self, *, Source: str = ..., SyncThreshold: int = ...): ...
    class TtmlDestinationSettings:
        def __init__(self, *, StyleControl: str = ...): ...
    class UdpContainerSettings:
        def __init__(self, *, M2tsSettings: "Channel.M2tsSettings" = ...): ...
    class UdpGroupSettings:
        def __init__(
            self,
            *,
            InputLossAction: str = ...,
            TimedMetadataId3Frame: str = ...,
            TimedMetadataId3Period: int = ...
        ): ...
    class UdpOutputSettings:
        def __init__(
            self,
            *,
            BufferMsec: int = ...,
            ContainerSettings: "Channel.UdpContainerSettings" = ...,
            Destination: "Channel.OutputLocationRef" = ...,
            FecOutputSettings: "Channel.FecOutputSettings" = ...
        ): ...
    class VideoBlackFailoverSettings:
        def __init__(
            self,
            *,
            BlackDetectThreshold: float = ...,
            VideoBlackThresholdMsec: int = ...
        ): ...
    class VideoCodecSettings:
        def __init__(
            self,
            *,
            FrameCaptureSettings: "Channel.FrameCaptureSettings" = ...,
            H264Settings: "Channel.H264Settings" = ...,
            H265Settings: "Channel.H265Settings" = ...,
            Mpeg2Settings: "Channel.Mpeg2Settings" = ...
        ): ...
    class VideoDescription:
        def __init__(
            self,
            *,
            CodecSettings: "Channel.VideoCodecSettings" = ...,
            Height: int = ...,
            Name: str = ...,
            RespondToAfd: str = ...,
            ScalingBehavior: str = ...,
            Sharpness: int = ...,
            Width: int = ...
        ): ...
    class VideoSelector:
        def __init__(
            self,
            *,
            ColorSpace: str = ...,
            ColorSpaceUsage: str = ...,
            SelectorSettings: "Channel.VideoSelectorSettings" = ...
        ): ...
    class VideoSelectorPid:
        def __init__(self, *, Pid: int = ...): ...
    class VideoSelectorProgramId:
        def __init__(self, *, ProgramId: int = ...): ...
    class VideoSelectorSettings:
        def __init__(
            self,
            *,
            VideoSelectorPid: "Channel.VideoSelectorPid" = ...,
            VideoSelectorProgramId: "Channel.VideoSelectorProgramId" = ...
        ): ...
    class WavSettings:
        def __init__(
            self,
            *,
            BitDepth: float = ...,
            CodingMode: str = ...,
            SampleRate: float = ...
        ): ...
    class WebvttDestinationSettings:
        def __init__(self) -> None: ...

class Input:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html"""

    Destinations: Final[List[str]]

    Arn: Final[str]

    Sources: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Destinations: List["Input.InputDestinationRequest"] = ...,
        InputDevices: List["Input.InputDeviceSettings"] = ...,
        InputSecurityGroups: List[str] = ...,
        MediaConnectFlows: List["Input.MediaConnectFlowRequest"] = ...,
        Name: str = ...,
        RoleArn: str = ...,
        Sources: List["Input.InputSourceRequest"] = ...,
        Tags: Any = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...,
        Vpc: "Input.InputVpcRequest" = ...
    ): ...
    class InputDestinationRequest:
        def __init__(self, *, StreamName: str = ...): ...
    class InputDeviceRequest:
        def __init__(self, *, Id: str = ...): ...
    class InputDeviceSettings:
        def __init__(self, *, Id: str = ...): ...
    class InputSourceRequest:
        def __init__(
            self, *, PasswordParam: str = ..., Url: str = ..., Username: str = ...
        ): ...
    class InputVpcRequest:
        def __init__(
            self, *, SecurityGroupIds: List[str] = ..., SubnetIds: List[str] = ...
        ): ...
    class MediaConnectFlowRequest:
        def __init__(self, *, FlowArn: str = ...): ...

class InputSecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...,
        WhitelistRules: List["InputSecurityGroup.InputWhitelistRuleCidr"] = ...
    ): ...
    class InputWhitelistRuleCidr:
        def __init__(self, *, Cidr: str = ...): ...
