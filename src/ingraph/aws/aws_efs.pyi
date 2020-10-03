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

_NAMESPACE = "AWS::EFS"

class AccessPoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html"""

    AccessPointId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FileSystemId: str,
        AccessPointTags: List["AccessPoint.AccessPointTag"] = ...,
        ClientToken: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PosixUser: "AccessPoint.PosixUser" = ...,
        RootDirectory: "AccessPoint.RootDirectory" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessPointTag:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class CreationInfo:
        def __init__(self, *, OwnerGid: str, OwnerUid: str, Permissions: str): ...
    class PosixUser:
        def __init__(self, *, Gid: str, Uid: str, SecondaryGids: List[str] = ...): ...
    class RootDirectory:
        def __init__(
            self, *, CreationInfo: "AccessPoint.CreationInfo" = ..., Path: str = ...
        ): ...

class FileSystem:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html"""

    FileSystemId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        BackupPolicy: "FileSystem.BackupPolicy" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Encrypted: bool = ...,
        FileSystemPolicy: Any = ...,
        FileSystemTags: List["FileSystem.ElasticFileSystemTag"] = ...,
        KmsKeyId: str = ...,
        LifecyclePolicies: List["FileSystem.LifecyclePolicy"] = ...,
        PerformanceMode: str = ...,
        ProvisionedThroughputInMibps: float = ...,
        ThroughputMode: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BackupPolicy:
        def __init__(self, *, Status: str): ...
    class ElasticFileSystemTag:
        def __init__(self, *, Key: str, Value: str): ...
    class LifecyclePolicy:
        def __init__(self, *, TransitionToIA: str): ...

class MountTarget:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html"""

    IpAddress: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FileSystemId: str,
        SecurityGroups: List[str],
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IpAddress: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
