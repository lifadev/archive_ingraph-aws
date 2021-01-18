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

_NAMESPACE = "AWS::Kendra"

class DataSource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        IndexId: str,
        Name: str,
        Type: str,
        DataSourceConfiguration: "DataSource.DataSourceConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RoleArn: str = ...,
        Schedule: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessControlListConfiguration:
        def __init__(self, *, KeyPath: str = ...): ...
    class AclConfiguration:
        def __init__(self, *, AllowedGroupsColumnName: str): ...
    class ChangeDetectingColumns:
        def __init__(self, *, ChangeDetectingColumns: List[str] = ...): ...
    class ColumnConfiguration:
        def __init__(
            self,
            *,
            ChangeDetectingColumns: "DataSource.ChangeDetectingColumns",
            DocumentDataColumnName: str,
            DocumentIdColumnName: str,
            DocumentTitleColumnName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...
        ): ...
    class ConfluenceAttachmentConfiguration:
        def __init__(
            self,
            *,
            AttachmentFieldMappings: "DataSource.ConfluenceAttachmentFieldMappingsList" = ...,
            CrawlAttachments: bool = ...
        ): ...
    class ConfluenceAttachmentFieldMappingsList:
        def __init__(
            self,
            *,
            ConfluenceAttachmentFieldMappingsList: List[
                "DataSource.ConfluenceAttachmentToIndexFieldMapping"
            ] = ...
        ): ...
    class ConfluenceAttachmentToIndexFieldMapping:
        def __init__(
            self,
            *,
            DataSourceFieldName: str,
            IndexFieldName: str,
            DateFieldFormat: str = ...
        ): ...
    class ConfluenceBlogConfiguration:
        def __init__(
            self,
            *,
            BlogFieldMappings: "DataSource.ConfluenceBlogFieldMappingsList" = ...
        ): ...
    class ConfluenceBlogFieldMappingsList:
        def __init__(
            self,
            *,
            ConfluenceBlogFieldMappingsList: List[
                "DataSource.ConfluenceBlogToIndexFieldMapping"
            ] = ...
        ): ...
    class ConfluenceBlogToIndexFieldMapping:
        def __init__(
            self,
            *,
            DataSourceFieldName: str,
            IndexFieldName: str,
            DateFieldFormat: str = ...
        ): ...
    class ConfluenceConfiguration:
        def __init__(
            self,
            *,
            SecretArn: str,
            ServerUrl: str,
            Version: str,
            AttachmentConfiguration: "DataSource.ConfluenceAttachmentConfiguration" = ...,
            BlogConfiguration: "DataSource.ConfluenceBlogConfiguration" = ...,
            ExclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            InclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            PageConfiguration: "DataSource.ConfluencePageConfiguration" = ...,
            SpaceConfiguration: "DataSource.ConfluenceSpaceConfiguration" = ...,
            VpcConfiguration: "DataSource.DataSourceVpcConfiguration" = ...
        ): ...
    class ConfluencePageConfiguration:
        def __init__(
            self,
            *,
            PageFieldMappings: "DataSource.ConfluencePageFieldMappingsList" = ...
        ): ...
    class ConfluencePageFieldMappingsList:
        def __init__(
            self,
            *,
            ConfluencePageFieldMappingsList: List[
                "DataSource.ConfluencePageToIndexFieldMapping"
            ] = ...
        ): ...
    class ConfluencePageToIndexFieldMapping:
        def __init__(
            self,
            *,
            DataSourceFieldName: str,
            IndexFieldName: str,
            DateFieldFormat: str = ...
        ): ...
    class ConfluenceSpaceConfiguration:
        def __init__(
            self,
            *,
            CrawlArchivedSpaces: bool = ...,
            CrawlPersonalSpaces: bool = ...,
            ExcludeSpaces: "DataSource.ConfluenceSpaceList" = ...,
            IncludeSpaces: "DataSource.ConfluenceSpaceList" = ...,
            SpaceFieldMappings: "DataSource.ConfluenceSpaceFieldMappingsList" = ...
        ): ...
    class ConfluenceSpaceFieldMappingsList:
        def __init__(
            self,
            *,
            ConfluenceSpaceFieldMappingsList: List[
                "DataSource.ConfluenceSpaceToIndexFieldMapping"
            ] = ...
        ): ...
    class ConfluenceSpaceList:
        def __init__(self, *, ConfluenceSpaceList: List[str] = ...): ...
    class ConfluenceSpaceToIndexFieldMapping:
        def __init__(
            self,
            *,
            DataSourceFieldName: str,
            IndexFieldName: str,
            DateFieldFormat: str = ...
        ): ...
    class ConnectionConfiguration:
        def __init__(
            self,
            *,
            DatabaseHost: str,
            DatabaseName: str,
            DatabasePort: int,
            SecretArn: str,
            TableName: str
        ): ...
    class DataSourceConfiguration:
        def __init__(
            self,
            *,
            ConfluenceConfiguration: "DataSource.ConfluenceConfiguration" = ...,
            DatabaseConfiguration: "DataSource.DatabaseConfiguration" = ...,
            GoogleDriveConfiguration: "DataSource.GoogleDriveConfiguration" = ...,
            OneDriveConfiguration: "DataSource.OneDriveConfiguration" = ...,
            S3Configuration: "DataSource.S3DataSourceConfiguration" = ...,
            SalesforceConfiguration: "DataSource.SalesforceConfiguration" = ...,
            ServiceNowConfiguration: "DataSource.ServiceNowConfiguration" = ...,
            SharePointConfiguration: "DataSource.SharePointConfiguration" = ...
        ): ...
    class DataSourceInclusionsExclusionsStrings:
        def __init__(
            self, *, DataSourceInclusionsExclusionsStrings: List[str] = ...
        ): ...
    class DataSourceToIndexFieldMapping:
        def __init__(
            self,
            *,
            DataSourceFieldName: str,
            IndexFieldName: str,
            DateFieldFormat: str = ...
        ): ...
    class DataSourceToIndexFieldMappingList:
        def __init__(
            self,
            *,
            DataSourceToIndexFieldMappingList: List[
                "DataSource.DataSourceToIndexFieldMapping"
            ] = ...
        ): ...
    class DataSourceVpcConfiguration:
        def __init__(self, *, SecurityGroupIds: List[str], SubnetIds: List[str]): ...
    class DatabaseConfiguration:
        def __init__(
            self,
            *,
            ColumnConfiguration: "DataSource.ColumnConfiguration",
            ConnectionConfiguration: "DataSource.ConnectionConfiguration",
            DatabaseEngineType: str,
            AclConfiguration: "DataSource.AclConfiguration" = ...,
            SqlConfiguration: "DataSource.SqlConfiguration" = ...,
            VpcConfiguration: "DataSource.DataSourceVpcConfiguration" = ...
        ): ...
    class DocumentsMetadataConfiguration:
        def __init__(self, *, S3Prefix: str = ...): ...
    class ExcludeMimeTypesList:
        def __init__(self, *, ExcludeMimeTypesList: List[str] = ...): ...
    class ExcludeSharedDrivesList:
        def __init__(self, *, ExcludeSharedDrivesList: List[str] = ...): ...
    class ExcludeUserAccountsList:
        def __init__(self, *, ExcludeUserAccountsList: List[str] = ...): ...
    class GoogleDriveConfiguration:
        def __init__(
            self,
            *,
            SecretArn: str,
            ExcludeMimeTypes: "DataSource.ExcludeMimeTypesList" = ...,
            ExcludeSharedDrives: "DataSource.ExcludeSharedDrivesList" = ...,
            ExcludeUserAccounts: "DataSource.ExcludeUserAccountsList" = ...,
            ExclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            InclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...
        ): ...
    class OneDriveConfiguration:
        def __init__(
            self,
            *,
            OneDriveUsers: "DataSource.OneDriveUsers",
            SecretArn: str,
            TenantDomain: str,
            DisableLocalGroups: bool = ...,
            ExclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            InclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...
        ): ...
    class OneDriveUserList:
        def __init__(self, *, OneDriveUserList: List[str] = ...): ...
    class OneDriveUsers:
        def __init__(
            self,
            *,
            OneDriveUserList: "DataSource.OneDriveUserList" = ...,
            OneDriveUserS3Path: "DataSource.S3Path" = ...
        ): ...
    class S3DataSourceConfiguration:
        def __init__(
            self,
            *,
            BucketName: str,
            AccessControlListConfiguration: "DataSource.AccessControlListConfiguration" = ...,
            DocumentsMetadataConfiguration: "DataSource.DocumentsMetadataConfiguration" = ...,
            ExclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            InclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            InclusionPrefixes: "DataSource.DataSourceInclusionsExclusionsStrings" = ...
        ): ...
    class S3Path:
        def __init__(self, *, Bucket: str, Key: str): ...
    class SalesforceChatterFeedConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            DocumentTitleFieldName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            IncludeFilterTypes: "DataSource.SalesforceChatterFeedIncludeFilterTypes" = ...
        ): ...
    class SalesforceChatterFeedIncludeFilterTypes:
        def __init__(
            self, *, SalesforceChatterFeedIncludeFilterTypes: List[str] = ...
        ): ...
    class SalesforceConfiguration:
        def __init__(
            self,
            *,
            SecretArn: str,
            ServerUrl: str,
            ChatterFeedConfiguration: "DataSource.SalesforceChatterFeedConfiguration" = ...,
            CrawlAttachments: bool = ...,
            ExcludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            IncludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            KnowledgeArticleConfiguration: "DataSource.SalesforceKnowledgeArticleConfiguration" = ...,
            StandardObjectAttachmentConfiguration: "DataSource.SalesforceStandardObjectAttachmentConfiguration" = ...,
            StandardObjectConfigurations: "DataSource.SalesforceStandardObjectConfigurationList" = ...
        ): ...
    class SalesforceCustomKnowledgeArticleTypeConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            Name: str,
            DocumentTitleFieldName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...
        ): ...
    class SalesforceCustomKnowledgeArticleTypeConfigurationList:
        def __init__(
            self,
            *,
            SalesforceCustomKnowledgeArticleTypeConfigurationList: List[
                "DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration"
            ] = ...
        ): ...
    class SalesforceKnowledgeArticleConfiguration:
        def __init__(
            self,
            *,
            IncludedStates: "DataSource.SalesforceKnowledgeArticleStateList",
            CustomKnowledgeArticleTypeConfigurations: "DataSource.SalesforceCustomKnowledgeArticleTypeConfigurationList" = ...,
            StandardKnowledgeArticleTypeConfiguration: "DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration" = ...
        ): ...
    class SalesforceKnowledgeArticleStateList:
        def __init__(self, *, SalesforceKnowledgeArticleStateList: List[str] = ...): ...
    class SalesforceStandardKnowledgeArticleTypeConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            DocumentTitleFieldName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...
        ): ...
    class SalesforceStandardObjectAttachmentConfiguration:
        def __init__(
            self,
            *,
            DocumentTitleFieldName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...
        ): ...
    class SalesforceStandardObjectConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            Name: str,
            DocumentTitleFieldName: str = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...
        ): ...
    class SalesforceStandardObjectConfigurationList:
        def __init__(
            self,
            *,
            SalesforceStandardObjectConfigurationList: List[
                "DataSource.SalesforceStandardObjectConfiguration"
            ] = ...
        ): ...
    class ServiceNowConfiguration:
        def __init__(
            self,
            *,
            HostUrl: str,
            SecretArn: str,
            ServiceNowBuildVersion: str,
            KnowledgeArticleConfiguration: "DataSource.ServiceNowKnowledgeArticleConfiguration" = ...,
            ServiceCatalogConfiguration: "DataSource.ServiceNowServiceCatalogConfiguration" = ...
        ): ...
    class ServiceNowKnowledgeArticleConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            CrawlAttachments: bool = ...,
            DocumentTitleFieldName: str = ...,
            ExcludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            IncludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...
        ): ...
    class ServiceNowServiceCatalogConfiguration:
        def __init__(
            self,
            *,
            DocumentDataFieldName: str,
            CrawlAttachments: bool = ...,
            DocumentTitleFieldName: str = ...,
            ExcludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            IncludeAttachmentFilePatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...
        ): ...
    class SharePointConfiguration:
        def __init__(
            self,
            *,
            SecretArn: str,
            SharePointVersion: str,
            Urls: List[str],
            CrawlAttachments: bool = ...,
            DisableLocalGroups: bool = ...,
            DocumentTitleFieldName: str = ...,
            ExclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            FieldMappings: "DataSource.DataSourceToIndexFieldMappingList" = ...,
            InclusionPatterns: "DataSource.DataSourceInclusionsExclusionsStrings" = ...,
            UseChangeLog: bool = ...,
            VpcConfiguration: "DataSource.DataSourceVpcConfiguration" = ...
        ): ...
    class SqlConfiguration:
        def __init__(self, *, QueryIdentifiersEnclosingOption: str = ...): ...

class Faq:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        IndexId: str,
        Name: str,
        RoleArn: str,
        S3Path: "Faq.S3Path",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        FileFormat: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class S3Path:
        def __init__(self, *, Bucket: str, Key: str): ...

class Index:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Edition: str,
        Name: str,
        RoleArn: str,
        CapacityUnits: "Index.CapacityUnitsConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DocumentMetadataConfigurations: List[
            "Index.DocumentMetadataConfiguration"
        ] = ...,
        ServerSideEncryptionConfiguration: "Index.ServerSideEncryptionConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UserContextPolicy: str = ...,
        UserTokenConfigurations: List["Index.UserTokenConfiguration"] = ...
    ): ...
    class CapacityUnitsConfiguration:
        def __init__(self, *, QueryCapacityUnits: int, StorageCapacityUnits: int): ...
    class DocumentMetadataConfiguration:
        def __init__(
            self,
            *,
            Name: str,
            Type: str,
            Relevance: "Index.Relevance" = ...,
            Search: "Index.Search" = ...
        ): ...
    class JsonTokenTypeConfiguration:
        def __init__(
            self, *, GroupAttributeField: str, UserNameAttributeField: str
        ): ...
    class JwtTokenTypeConfiguration:
        def __init__(
            self,
            *,
            KeyLocation: str,
            ClaimRegex: str = ...,
            GroupAttributeField: str = ...,
            Issuer: str = ...,
            SecretManagerArn: str = ...,
            URL: str = ...,
            UserNameAttributeField: str = ...
        ): ...
    class Relevance:
        def __init__(
            self,
            *,
            Duration: str = ...,
            Freshness: bool = ...,
            Importance: int = ...,
            RankOrder: str = ...,
            ValueImportanceItems: "Index.ValueImportanceItems" = ...
        ): ...
    class Search:
        def __init__(
            self,
            *,
            Displayable: bool = ...,
            Facetable: bool = ...,
            Searchable: bool = ...,
            Sortable: bool = ...
        ): ...
    class ServerSideEncryptionConfiguration:
        def __init__(self, *, KmsKeyId: str = ...): ...
    class UserTokenConfiguration:
        def __init__(
            self,
            *,
            JsonTokenTypeConfiguration: "Index.JsonTokenTypeConfiguration" = ...,
            JwtTokenTypeConfiguration: "Index.JwtTokenTypeConfiguration" = ...
        ): ...
    class ValueImportanceItem:
        def __init__(self, *, Key: str = ..., Value: int = ...): ...
    class ValueImportanceItems:
        def __init__(
            self, *, ValueImportanceItems: List["Index.ValueImportanceItem"] = ...
        ): ...
