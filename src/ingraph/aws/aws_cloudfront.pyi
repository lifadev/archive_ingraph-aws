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

_NAMESPACE = "AWS::CloudFront"

class CachePolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html"""

    Id: Final[str]

    LastModifiedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CachePolicyConfig: "CachePolicy.CachePolicyConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CachePolicyConfig:
        def __init__(
            self,
            *,
            DefaultTTL: float,
            MaxTTL: float,
            MinTTL: float,
            Name: str,
            ParametersInCacheKeyAndForwardedToOrigin: "CachePolicy.ParametersInCacheKeyAndForwardedToOrigin",
            Comment: str = ...
        ): ...
    class CookiesConfig:
        def __init__(self, *, CookieBehavior: str, Cookies: List[str] = ...): ...
    class HeadersConfig:
        def __init__(self, *, HeaderBehavior: str, Headers: List[str] = ...): ...
    class ParametersInCacheKeyAndForwardedToOrigin:
        def __init__(
            self,
            *,
            CookiesConfig: "CachePolicy.CookiesConfig",
            EnableAcceptEncodingGzip: bool,
            HeadersConfig: "CachePolicy.HeadersConfig",
            QueryStringsConfig: "CachePolicy.QueryStringsConfig",
            EnableAcceptEncodingBrotli: bool = ...
        ): ...
    class QueryStringsConfig:
        def __init__(
            self, *, QueryStringBehavior: str, QueryStrings: List[str] = ...
        ): ...

class CloudFrontOriginAccessIdentity:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html"""

    S3CanonicalUserId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudFrontOriginAccessIdentityConfig:
        def __init__(self, *, Comment: str): ...

class Distribution:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html"""

    DomainName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DistributionConfig: "Distribution.DistributionConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CacheBehavior:
        def __init__(
            self,
            *,
            PathPattern: str,
            TargetOriginId: str,
            ViewerProtocolPolicy: str,
            AllowedMethods: List[str] = ...,
            CachePolicyId: str = ...,
            CachedMethods: List[str] = ...,
            Compress: bool = ...,
            DefaultTTL: float = ...,
            FieldLevelEncryptionId: str = ...,
            ForwardedValues: "Distribution.ForwardedValues" = ...,
            LambdaFunctionAssociations: List[
                "Distribution.LambdaFunctionAssociation"
            ] = ...,
            MaxTTL: float = ...,
            MinTTL: float = ...,
            OriginRequestPolicyId: str = ...,
            RealtimeLogConfigArn: str = ...,
            SmoothStreaming: bool = ...,
            TrustedKeyGroups: List[str] = ...,
            TrustedSigners: List[str] = ...
        ): ...
    class Cookies:
        def __init__(self, *, Forward: str, WhitelistedNames: List[str] = ...): ...
    class CustomErrorResponse:
        def __init__(
            self,
            *,
            ErrorCode: int,
            ErrorCachingMinTTL: float = ...,
            ResponseCode: int = ...,
            ResponsePagePath: str = ...
        ): ...
    class CustomOriginConfig:
        def __init__(
            self,
            *,
            OriginProtocolPolicy: str,
            HTTPPort: int = ...,
            HTTPSPort: int = ...,
            OriginKeepaliveTimeout: int = ...,
            OriginReadTimeout: int = ...,
            OriginSSLProtocols: List[str] = ...
        ): ...
    class DefaultCacheBehavior:
        def __init__(
            self,
            *,
            TargetOriginId: str,
            ViewerProtocolPolicy: str,
            AllowedMethods: List[str] = ...,
            CachePolicyId: str = ...,
            CachedMethods: List[str] = ...,
            Compress: bool = ...,
            DefaultTTL: float = ...,
            FieldLevelEncryptionId: str = ...,
            ForwardedValues: "Distribution.ForwardedValues" = ...,
            LambdaFunctionAssociations: List[
                "Distribution.LambdaFunctionAssociation"
            ] = ...,
            MaxTTL: float = ...,
            MinTTL: float = ...,
            OriginRequestPolicyId: str = ...,
            RealtimeLogConfigArn: str = ...,
            SmoothStreaming: bool = ...,
            TrustedKeyGroups: List[str] = ...,
            TrustedSigners: List[str] = ...
        ): ...
    class DistributionConfig:
        def __init__(
            self,
            *,
            Enabled: bool,
            Aliases: List[str] = ...,
            CacheBehaviors: List["Distribution.CacheBehavior"] = ...,
            Comment: str = ...,
            CustomErrorResponses: List["Distribution.CustomErrorResponse"] = ...,
            DefaultCacheBehavior: "Distribution.DefaultCacheBehavior" = ...,
            DefaultRootObject: str = ...,
            HttpVersion: str = ...,
            IPV6Enabled: bool = ...,
            Logging: "Distribution.Logging" = ...,
            OriginGroups: "Distribution.OriginGroups" = ...,
            Origins: List["Distribution.Origin"] = ...,
            PriceClass: str = ...,
            Restrictions: "Distribution.Restrictions" = ...,
            ViewerCertificate: "Distribution.ViewerCertificate" = ...,
            WebACLId: str = ...
        ): ...
    class ForwardedValues:
        def __init__(
            self,
            *,
            QueryString: bool,
            Cookies: "Distribution.Cookies" = ...,
            Headers: List[str] = ...,
            QueryStringCacheKeys: List[str] = ...
        ): ...
    class GeoRestriction:
        def __init__(self, *, RestrictionType: str, Locations: List[str] = ...): ...
    class LambdaFunctionAssociation:
        def __init__(
            self,
            *,
            EventType: str = ...,
            IncludeBody: bool = ...,
            LambdaFunctionARN: str = ...
        ): ...
    class Logging:
        def __init__(
            self, *, Bucket: str, IncludeCookies: bool = ..., Prefix: str = ...
        ): ...
    class Origin:
        def __init__(
            self,
            *,
            DomainName: str,
            Id: str,
            ConnectionAttempts: int = ...,
            ConnectionTimeout: int = ...,
            CustomOriginConfig: "Distribution.CustomOriginConfig" = ...,
            OriginCustomHeaders: List["Distribution.OriginCustomHeader"] = ...,
            OriginPath: str = ...,
            OriginShield: "Distribution.OriginShield" = ...,
            S3OriginConfig: "Distribution.S3OriginConfig" = ...
        ): ...
    class OriginCustomHeader:
        def __init__(self, *, HeaderName: str, HeaderValue: str): ...
    class OriginGroup:
        def __init__(
            self,
            *,
            FailoverCriteria: "Distribution.OriginGroupFailoverCriteria",
            Id: str,
            Members: "Distribution.OriginGroupMembers"
        ): ...
    class OriginGroupFailoverCriteria:
        def __init__(self, *, StatusCodes: "Distribution.StatusCodes"): ...
    class OriginGroupMember:
        def __init__(self, *, OriginId: str): ...
    class OriginGroupMembers:
        def __init__(
            self, *, Items: List["Distribution.OriginGroupMember"], Quantity: int
        ): ...
    class OriginGroups:
        def __init__(
            self, *, Quantity: int, Items: List["Distribution.OriginGroup"] = ...
        ): ...
    class OriginShield:
        def __init__(self, *, Enabled: bool, OriginShieldRegion: str = ...): ...
    class Restrictions:
        def __init__(self, *, GeoRestriction: "Distribution.GeoRestriction"): ...
    class S3OriginConfig:
        def __init__(self, *, OriginAccessIdentity: str = ...): ...
    class StatusCodes:
        def __init__(self, *, Items: List[int], Quantity: int): ...
    class ViewerCertificate:
        def __init__(
            self,
            *,
            AcmCertificateArn: str = ...,
            CloudFrontDefaultCertificate: bool = ...,
            IamCertificateId: str = ...,
            MinimumProtocolVersion: str = ...,
            SslSupportMethod: str = ...
        ): ...

class KeyGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html"""

    Id: Final[str]

    LastModifiedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeyGroupConfig: "KeyGroup.KeyGroupConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class KeyGroupConfig:
        def __init__(self, *, Items: List[str], Name: str, Comment: str = ...): ...

class OriginRequestPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html"""

    Id: Final[str]

    LastModifiedTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        OriginRequestPolicyConfig: "OriginRequestPolicy.OriginRequestPolicyConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CookiesConfig:
        def __init__(self, *, CookieBehavior: str, Cookies: List[str] = ...): ...
    class HeadersConfig:
        def __init__(self, *, HeaderBehavior: str, Headers: List[str] = ...): ...
    class OriginRequestPolicyConfig:
        def __init__(
            self,
            *,
            CookiesConfig: "OriginRequestPolicy.CookiesConfig",
            HeadersConfig: "OriginRequestPolicy.HeadersConfig",
            Name: str,
            QueryStringsConfig: "OriginRequestPolicy.QueryStringsConfig",
            Comment: str = ...
        ): ...
    class QueryStringsConfig:
        def __init__(
            self, *, QueryStringBehavior: str, QueryStrings: List[str] = ...
        ): ...

class PublicKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html"""

    CreatedTime: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PublicKeyConfig: "PublicKey.PublicKeyConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class PublicKeyConfig:
        def __init__(
            self,
            *,
            CallerReference: str,
            EncodedKey: str,
            Name: str,
            Comment: str = ...
        ): ...

class RealtimeLogConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndPoints: List["RealtimeLogConfig.EndPoint"],
        Fields: List[str],
        Name: str,
        SamplingRate: float,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EndPoint:
        def __init__(
            self,
            *,
            KinesisStreamConfig: "RealtimeLogConfig.KinesisStreamConfig",
            StreamType: str
        ): ...
    class KinesisStreamConfig:
        def __init__(self, *, RoleArn: str, StreamArn: str): ...

class StreamingDistribution:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html"""

    DomainName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        StreamingDistributionConfig: "StreamingDistribution.StreamingDistributionConfig",
        Tags: List["Tag"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Logging:
        def __init__(self, *, Bucket: str, Enabled: bool, Prefix: str): ...
    class S3Origin:
        def __init__(self, *, DomainName: str, OriginAccessIdentity: str): ...
    class StreamingDistributionConfig:
        def __init__(
            self,
            *,
            Comment: str,
            Enabled: bool,
            S3Origin: "StreamingDistribution.S3Origin",
            TrustedSigners: "StreamingDistribution.TrustedSigners",
            Aliases: List[str] = ...,
            Logging: "StreamingDistribution.Logging" = ...,
            PriceClass: str = ...
        ): ...
    class TrustedSigners:
        def __init__(self, *, Enabled: bool, AwsAccountNumbers: List[str] = ...): ...
