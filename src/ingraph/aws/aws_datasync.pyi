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

_NAMESPACE = "AWS::DataSync"

class Agent:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html"""

    EndpointType: Final[str]

    AgentArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ActivationKey: str,
        AgentName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SecurityGroupArns: List[str] = ...,
        SubnetArns: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcEndpointId: str = ...
    ): ...

class LocationEFS:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Ec2Config: "LocationEFS.Ec2Config",
        EfsFilesystemArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Subdirectory: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Ec2Config:
        def __init__(self, *, SecurityGroupArns: List[str], SubnetArn: str): ...

class LocationFSxWindows:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FsxFilesystemArn: str,
        Password: str,
        SecurityGroupArns: List[str],
        User: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Domain: str = ...,
        Subdirectory: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LocationNFS:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        OnPremConfig: "LocationNFS.OnPremConfig",
        ServerHostname: str,
        Subdirectory: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MountOptions: "LocationNFS.MountOptions" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MountOptions:
        def __init__(self, *, Version: str = ...): ...
    class OnPremConfig:
        def __init__(self, *, AgentArns: List[str]): ...

class LocationObjectStorage:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AgentArns: List[str],
        BucketName: str,
        ServerHostname: str,
        AccessKey: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SecretKey: str = ...,
        ServerPort: int = ...,
        ServerProtocol: str = ...,
        Subdirectory: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LocationS3:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        S3BucketArn: str,
        S3Config: "LocationS3.S3Config",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        S3StorageClass: str = ...,
        Subdirectory: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class S3Config:
        def __init__(self, *, BucketAccessRoleArn: str): ...

class LocationSMB:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html"""

    LocationArn: Final[str]

    LocationUri: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AgentArns: List[str],
        Password: str,
        ServerHostname: str,
        Subdirectory: str,
        User: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Domain: str = ...,
        MountOptions: "LocationSMB.MountOptions" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MountOptions:
        def __init__(self, *, Version: str = ...): ...

class Task:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html"""

    TaskArn: Final[str]

    ErrorCode: Final[str]

    ErrorDetail: Final[str]

    Status: Final[str]

    SourceNetworkInterfaceArns: Final[List[str]]

    DestinationNetworkInterfaceArns: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationLocationArn: str,
        SourceLocationArn: str,
        CloudWatchLogGroupArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Excludes: List["Task.FilterRule"] = ...,
        Name: str = ...,
        Options: "Task.Options" = ...,
        Schedule: "Task.TaskSchedule" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class FilterRule:
        def __init__(self, *, FilterType: str = ..., Value: str = ...): ...
    class Options:
        def __init__(
            self,
            *,
            Atime: str = ...,
            BytesPerSecond: int = ...,
            Gid: str = ...,
            LogLevel: str = ...,
            Mtime: str = ...,
            OverwriteMode: str = ...,
            PosixPermissions: str = ...,
            PreserveDeletedFiles: str = ...,
            PreserveDevices: str = ...,
            TaskQueueing: str = ...,
            TransferMode: str = ...,
            Uid: str = ...,
            VerifyMode: str = ...
        ): ...
    class TaskSchedule:
        def __init__(self, *, ScheduleExpression: str): ...
