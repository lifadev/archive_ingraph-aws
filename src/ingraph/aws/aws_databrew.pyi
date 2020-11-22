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

_NAMESPACE = "AWS::DataBrew"

class Dataset:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Input: Any,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FormatOptions: Any = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Job:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        RoleArn: str,
        Type: str,
        DatasetName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EncryptionKeyArn: str = ...,
        EncryptionMode: str = ...,
        LogSubscription: str = ...,
        MaxCapacity: int = ...,
        MaxRetries: int = ...,
        OutputLocation: Any = ...,
        Outputs: List["Job.Output"] = ...,
        ProjectName: str = ...,
        Recipe: Any = ...,
        Tags: List["Tag"] = ...,
        Timeout: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Output:
        def __init__(
            self,
            *,
            Location: "Job.S3Location",
            CompressionFormat: str = ...,
            Format: str = ...,
            Overwrite: bool = ...,
            PartitionColumns: List[str] = ...
        ): ...
    class S3Location:
        def __init__(self, *, Bucket: str, Key: str = ...): ...

class Project:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DatasetName: str,
        Name: str,
        RecipeName: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Sample: Any = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Recipe:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Steps: List["Recipe.RecipeStep"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(self, *, Operation: str, Parameters: Any = ...): ...
    class ConditionExpression:
        def __init__(self, *, Condition: str, TargetColumn: str, Value: str = ...): ...
    class DataCatalogInputDefinition:
        def __init__(
            self,
            *,
            CatalogId: str = ...,
            DatabaseName: str = ...,
            TableName: str = ...,
            TempDirectory: "Recipe.S3Location" = ...
        ): ...
    class RecipeParameters:
        def __init__(
            self,
            *,
            AggregateFunction: str = ...,
            Base: str = ...,
            CaseStatement: str = ...,
            CategoryMap: str = ...,
            CharsToRemove: str = ...,
            CollapseConsecutiveWhitespace: str = ...,
            ColumnDataType: str = ...,
            ColumnRange: str = ...,
            Count: str = ...,
            CustomCharacters: str = ...,
            CustomStopWords: str = ...,
            CustomValue: str = ...,
            DatasetsColumns: str = ...,
            DateAddValue: str = ...,
            DateTimeFormat: str = ...,
            DateTimeParameters: str = ...,
            DeleteOtherRows: str = ...,
            Delimiter: str = ...,
            EndPattern: str = ...,
            EndPosition: str = ...,
            EndValue: str = ...,
            ExpandContractions: str = ...,
            Exponent: str = ...,
            FalseString: str = ...,
            GroupByAggFunctionOptions: str = ...,
            GroupByColumns: str = ...,
            HiddenColumns: str = ...,
            IgnoreCase: str = ...,
            IncludeInSplit: str = ...,
            Input: Any = ...,
            Interval: str = ...,
            IsText: str = ...,
            JoinKeys: str = ...,
            JoinType: str = ...,
            LeftColumns: str = ...,
            Limit: str = ...,
            LowerBound: str = ...,
            MapType: str = ...,
            ModeType: str = ...,
            MultiLine: bool = ...,
            NumRows: str = ...,
            NumRowsAfter: str = ...,
            NumRowsBefore: str = ...,
            OrderByColumn: str = ...,
            OrderByColumns: str = ...,
            Other: str = ...,
            Pattern: str = ...,
            PatternOption1: str = ...,
            PatternOption2: str = ...,
            PatternOptions: str = ...,
            Period: str = ...,
            Position: str = ...,
            RemoveAllPunctuation: str = ...,
            RemoveAllQuotes: str = ...,
            RemoveAllWhitespace: str = ...,
            RemoveCustomCharacters: str = ...,
            RemoveCustomValue: str = ...,
            RemoveLeadingAndTrailingPunctuation: str = ...,
            RemoveLeadingAndTrailingQuotes: str = ...,
            RemoveLeadingAndTrailingWhitespace: str = ...,
            RemoveLetters: str = ...,
            RemoveNumbers: str = ...,
            RemoveSourceColumn: str = ...,
            RemoveSpecialCharacters: str = ...,
            RightColumns: str = ...,
            SampleSize: str = ...,
            SampleType: str = ...,
            SecondInput: str = ...,
            SecondaryInputs: List["Recipe.SecondaryInput"] = ...,
            SheetIndexes: List[int] = ...,
            SheetNames: List[str] = ...,
            SourceColumn: str = ...,
            SourceColumn1: str = ...,
            SourceColumn2: str = ...,
            SourceColumns: str = ...,
            StartColumnIndex: str = ...,
            StartPattern: str = ...,
            StartPosition: str = ...,
            StartValue: str = ...,
            StemmingMode: str = ...,
            StepCount: str = ...,
            StepIndex: str = ...,
            StopWordsMode: str = ...,
            Strategy: str = ...,
            TargetColumn: str = ...,
            TargetColumnNames: str = ...,
            TargetDateFormat: str = ...,
            TargetIndex: str = ...,
            TimeZone: str = ...,
            TokenizerPattern: str = ...,
            TrueString: str = ...,
            UdfLang: str = ...,
            Units: str = ...,
            UnpivotColumn: str = ...,
            UpperBound: str = ...,
            UseNewDataFrame: str = ...,
            Value: str = ...,
            Value1: str = ...,
            Value2: str = ...,
            ValueColumn: str = ...,
            ViewFrame: str = ...
        ): ...
    class RecipeStep:
        def __init__(
            self,
            *,
            Action: "Recipe.Action",
            ConditionExpressions: List["Recipe.ConditionExpression"] = ...
        ): ...
    class S3Location:
        def __init__(self, *, Bucket: str, Key: str = ...): ...
    class SecondaryInput:
        def __init__(
            self,
            *,
            DataCatalogInputDefinition: "Recipe.DataCatalogInputDefinition" = ...,
            S3InputDefinition: "Recipe.S3Location" = ...
        ): ...

class Schedule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CronExpression: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        JobNames: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
