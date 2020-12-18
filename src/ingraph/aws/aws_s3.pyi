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

_NAMESPACE = "AWS::S3"

class AccessPoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Bucket: str,
        CreationDate: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        NetworkOrigin: str = ...,
        Policy: Any = ...,
        PolicyStatus: Any = ...,
        PublicAccessBlockConfiguration: "AccessPoint.PublicAccessBlockConfiguration" = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfiguration: "AccessPoint.VpcConfiguration" = ...
    ): ...
    class PublicAccessBlockConfiguration:
        def __init__(
            self,
            *,
            BlockPublicAcls: bool = ...,
            BlockPublicPolicy: bool = ...,
            IgnorePublicAcls: bool = ...,
            RestrictPublicBuckets: bool = ...
        ): ...
    class VpcConfiguration:
        def __init__(self, *, VpcId: str = ...): ...

class Bucket:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html"""

    Arn: Final[str]

    DomainName: Final[str]

    DualStackDomainName: Final[str]

    RegionalDomainName: Final[str]

    WebsiteURL: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccelerateConfiguration: "Bucket.AccelerateConfiguration" = ...,
        AccessControl: str = ...,
        AnalyticsConfigurations: List["Bucket.AnalyticsConfiguration"] = ...,
        BucketEncryption: "Bucket.BucketEncryption" = ...,
        BucketName: str = ...,
        CorsConfiguration: "Bucket.CorsConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IntelligentTieringConfigurations: List[
            "Bucket.IntelligentTieringConfiguration"
        ] = ...,
        InventoryConfigurations: List["Bucket.InventoryConfiguration"] = ...,
        LifecycleConfiguration: "Bucket.LifecycleConfiguration" = ...,
        LoggingConfiguration: "Bucket.LoggingConfiguration" = ...,
        MetricsConfigurations: List["Bucket.MetricsConfiguration"] = ...,
        NotificationConfiguration: "Bucket.NotificationConfiguration" = ...,
        ObjectLockConfiguration: "Bucket.ObjectLockConfiguration" = ...,
        ObjectLockEnabled: bool = ...,
        OwnershipControls: "Bucket.OwnershipControls" = ...,
        PublicAccessBlockConfiguration: "Bucket.PublicAccessBlockConfiguration" = ...,
        ReplicationConfiguration: "Bucket.ReplicationConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VersioningConfiguration: "Bucket.VersioningConfiguration" = ...,
        WebsiteConfiguration: "Bucket.WebsiteConfiguration" = ...
    ): ...
    class AbortIncompleteMultipartUpload:
        def __init__(self, *, DaysAfterInitiation: int): ...
    class AccelerateConfiguration:
        def __init__(self, *, AccelerationStatus: str): ...
    class AccessControlTranslation:
        def __init__(self, *, Owner: str): ...
    class AnalyticsConfiguration:
        def __init__(
            self,
            *,
            Id: str,
            StorageClassAnalysis: "Bucket.StorageClassAnalysis",
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class BucketEncryption:
        def __init__(
            self,
            *,
            ServerSideEncryptionConfiguration: List["Bucket.ServerSideEncryptionRule"]
        ): ...
    class CorsConfiguration:
        def __init__(self, *, CorsRules: List["Bucket.CorsRule"]): ...
    class CorsRule:
        def __init__(
            self,
            *,
            AllowedMethods: List[str],
            AllowedOrigins: List[str],
            AllowedHeaders: List[str] = ...,
            ExposedHeaders: List[str] = ...,
            Id: str = ...,
            MaxAge: int = ...
        ): ...
    class DataExport:
        def __init__(
            self, *, Destination: "Bucket.Destination", OutputSchemaVersion: str
        ): ...
    class DefaultRetention:
        def __init__(self, *, Days: int = ..., Mode: str = ..., Years: int = ...): ...
    class DeleteMarkerReplication:
        def __init__(self, *, Status: str = ...): ...
    class Destination:
        def __init__(
            self,
            *,
            BucketArn: str,
            Format: str,
            BucketAccountId: str = ...,
            Prefix: str = ...
        ): ...
    class EncryptionConfiguration:
        def __init__(self, *, ReplicaKmsKeyID: str): ...
    class FilterRule:
        def __init__(self, *, Name: str, Value: str): ...
    class IntelligentTieringConfiguration:
        def __init__(
            self,
            *,
            Id: str,
            Status: str,
            Tierings: List["Bucket.Tiering"],
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class InventoryConfiguration:
        def __init__(
            self,
            *,
            Destination: "Bucket.Destination",
            Enabled: bool,
            Id: str,
            IncludedObjectVersions: str,
            ScheduleFrequency: str,
            OptionalFields: List[str] = ...,
            Prefix: str = ...
        ): ...
    class LambdaConfiguration:
        def __init__(
            self,
            *,
            Event: str,
            Function: str,
            Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class LifecycleConfiguration:
        def __init__(self, *, Rules: List["Bucket.Rule"]): ...
    class LoggingConfiguration:
        def __init__(
            self, *, DestinationBucketName: str = ..., LogFilePrefix: str = ...
        ): ...
    class Metrics:
        def __init__(
            self, *, Status: str, EventThreshold: "Bucket.ReplicationTimeValue" = ...
        ): ...
    class MetricsConfiguration:
        def __init__(
            self,
            *,
            Id: str,
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class NoncurrentVersionTransition:
        def __init__(self, *, StorageClass: str, TransitionInDays: int): ...
    class NotificationConfiguration:
        def __init__(
            self,
            *,
            LambdaConfigurations: List["Bucket.LambdaConfiguration"] = ...,
            QueueConfigurations: List["Bucket.QueueConfiguration"] = ...,
            TopicConfigurations: List["Bucket.TopicConfiguration"] = ...
        ): ...
    class NotificationFilter:
        def __init__(self, *, S3Key: "Bucket.S3KeyFilter"): ...
    class ObjectLockConfiguration:
        def __init__(
            self, *, ObjectLockEnabled: str = ..., Rule: "Bucket.ObjectLockRule" = ...
        ): ...
    class ObjectLockRule:
        def __init__(self, *, DefaultRetention: "Bucket.DefaultRetention" = ...): ...
    class OwnershipControls:
        def __init__(self, *, Rules: List["Bucket.OwnershipControlsRule"]): ...
    class OwnershipControlsRule:
        def __init__(self, *, ObjectOwnership: str = ...): ...
    class PublicAccessBlockConfiguration:
        def __init__(
            self,
            *,
            BlockPublicAcls: bool = ...,
            BlockPublicPolicy: bool = ...,
            IgnorePublicAcls: bool = ...,
            RestrictPublicBuckets: bool = ...
        ): ...
    class QueueConfiguration:
        def __init__(
            self, *, Event: str, Queue: str, Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class RedirectAllRequestsTo:
        def __init__(self, *, HostName: str, Protocol: str = ...): ...
    class RedirectRule:
        def __init__(
            self,
            *,
            HostName: str = ...,
            HttpRedirectCode: str = ...,
            Protocol: str = ...,
            ReplaceKeyPrefixWith: str = ...,
            ReplaceKeyWith: str = ...
        ): ...
    class ReplicaModifications:
        def __init__(self, *, Status: str): ...
    class ReplicationConfiguration:
        def __init__(self, *, Role: str, Rules: List["Bucket.ReplicationRule"]): ...
    class ReplicationDestination:
        def __init__(
            self,
            *,
            Bucket: str,
            AccessControlTranslation: "Bucket.AccessControlTranslation" = ...,
            Account: str = ...,
            EncryptionConfiguration: "Bucket.EncryptionConfiguration" = ...,
            Metrics: "Bucket.Metrics" = ...,
            ReplicationTime: "Bucket.ReplicationTime" = ...,
            StorageClass: str = ...
        ): ...
    class ReplicationRule:
        def __init__(
            self,
            *,
            Destination: "Bucket.ReplicationDestination",
            Status: str,
            DeleteMarkerReplication: "Bucket.DeleteMarkerReplication" = ...,
            Filter: "Bucket.ReplicationRuleFilter" = ...,
            Id: str = ...,
            Prefix: str = ...,
            Priority: int = ...,
            SourceSelectionCriteria: "Bucket.SourceSelectionCriteria" = ...
        ): ...
    class ReplicationRuleAndOperator:
        def __init__(
            self, *, Prefix: str = ..., TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class ReplicationRuleFilter:
        def __init__(
            self,
            *,
            And: "Bucket.ReplicationRuleAndOperator" = ...,
            Prefix: str = ...,
            TagFilter: "Bucket.TagFilter" = ...
        ): ...
    class ReplicationTime:
        def __init__(self, *, Status: str, Time: "Bucket.ReplicationTimeValue"): ...
    class ReplicationTimeValue:
        def __init__(self, *, Minutes: int): ...
    class RoutingRule:
        def __init__(
            self,
            *,
            RedirectRule: "Bucket.RedirectRule",
            RoutingRuleCondition: "Bucket.RoutingRuleCondition" = ...
        ): ...
    class RoutingRuleCondition:
        def __init__(
            self, *, HttpErrorCodeReturnedEquals: str = ..., KeyPrefixEquals: str = ...
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            Status: str,
            AbortIncompleteMultipartUpload: "Bucket.AbortIncompleteMultipartUpload" = ...,
            ExpirationDate: str = ...,
            ExpirationInDays: int = ...,
            Id: str = ...,
            NoncurrentVersionExpirationInDays: int = ...,
            NoncurrentVersionTransition: "Bucket.NoncurrentVersionTransition" = ...,
            NoncurrentVersionTransitions: List[
                "Bucket.NoncurrentVersionTransition"
            ] = ...,
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...,
            Transition: "Bucket.Transition" = ...,
            Transitions: List["Bucket.Transition"] = ...
        ): ...
    class S3KeyFilter:
        def __init__(self, *, Rules: List["Bucket.FilterRule"]): ...
    class ServerSideEncryptionByDefault:
        def __init__(self, *, SSEAlgorithm: str, KMSMasterKeyID: str = ...): ...
    class ServerSideEncryptionRule:
        def __init__(
            self,
            *,
            BucketKeyEnabled: bool = ...,
            ServerSideEncryptionByDefault: "Bucket.ServerSideEncryptionByDefault" = ...
        ): ...
    class SourceSelectionCriteria:
        def __init__(
            self,
            *,
            ReplicaModifications: "Bucket.ReplicaModifications" = ...,
            SseKmsEncryptedObjects: "Bucket.SseKmsEncryptedObjects" = ...
        ): ...
    class SseKmsEncryptedObjects:
        def __init__(self, *, Status: str): ...
    class StorageClassAnalysis:
        def __init__(self, *, DataExport: "Bucket.DataExport" = ...): ...
    class TagFilter:
        def __init__(self, *, Key: str, Value: str): ...
    class Tiering:
        def __init__(self, *, AccessTier: str, Days: int): ...
    class TopicConfiguration:
        def __init__(
            self, *, Event: str, Topic: str, Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class Transition:
        def __init__(
            self,
            *,
            StorageClass: str,
            TransitionDate: str = ...,
            TransitionInDays: int = ...
        ): ...
    class VersioningConfiguration:
        def __init__(self, *, Status: str): ...
    class WebsiteConfiguration:
        def __init__(
            self,
            *,
            ErrorDocument: str = ...,
            IndexDocument: str = ...,
            RedirectAllRequestsTo: "Bucket.RedirectAllRequestsTo" = ...,
            RoutingRules: List["Bucket.RoutingRule"] = ...
        ): ...

class BucketPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Bucket: str,
        PolicyDocument: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class StorageLens:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html"""

    StorageLensArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        StorageLensConfiguration: "StorageLens.StorageLensConfiguration",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccountLevel:
        def __init__(
            self,
            *,
            BucketLevel: "StorageLens.BucketLevel",
            ActivityMetrics: "StorageLens.ActivityMetrics" = ...
        ): ...
    class ActivityMetrics:
        def __init__(self, *, IsEnabled: bool = ...): ...
    class AwsOrg:
        def __init__(self, *, Arn: str): ...
    class BucketLevel:
        def __init__(
            self,
            *,
            ActivityMetrics: "StorageLens.ActivityMetrics" = ...,
            PrefixLevel: "StorageLens.PrefixLevel" = ...
        ): ...
    class BucketsAndRegions:
        def __init__(self, *, Buckets: List[str] = ..., Regions: List[str] = ...): ...
    class DataExport:
        def __init__(
            self, *, S3BucketDestination: "StorageLens.S3BucketDestination"
        ): ...
    class Encryption:
        def __init__(self) -> None: ...
    class PrefixLevel:
        def __init__(
            self, *, StorageMetrics: "StorageLens.PrefixLevelStorageMetrics"
        ): ...
    class PrefixLevelStorageMetrics:
        def __init__(
            self,
            *,
            IsEnabled: bool = ...,
            SelectionCriteria: "StorageLens.SelectionCriteria" = ...
        ): ...
    class S3BucketDestination:
        def __init__(
            self,
            *,
            AccountId: str,
            Arn: str,
            Format: str,
            OutputSchemaVersion: str,
            Encryption: "StorageLens.Encryption" = ...,
            Prefix: str = ...
        ): ...
    class SelectionCriteria:
        def __init__(
            self,
            *,
            Delimiter: str = ...,
            MaxDepth: int = ...,
            MinStorageBytesPercentage: float = ...
        ): ...
    class StorageLensConfiguration:
        def __init__(
            self,
            *,
            AccountLevel: "StorageLens.AccountLevel",
            Id: str,
            IsEnabled: bool,
            AwsOrg: "StorageLens.AwsOrg" = ...,
            DataExport: "StorageLens.DataExport" = ...,
            Exclude: "StorageLens.BucketsAndRegions" = ...,
            Include: "StorageLens.BucketsAndRegions" = ...,
            StorageLensArn: str = ...
        ): ...
