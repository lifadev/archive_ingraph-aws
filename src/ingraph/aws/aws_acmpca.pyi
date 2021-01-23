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

_NAMESPACE = "AWS::ACMPCA"

class Certificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html"""

    Certificate_: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CertificateAuthorityArn: str,
        CertificateSigningRequest: str,
        SigningAlgorithm: str,
        Validity: "Certificate.Validity",
        ApiPassthrough: "Certificate.ApiPassthrough" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        TemplateArn: str = ...,
        UpdateReplacePolicy: str = ...,
        ValidityNotBefore: "Certificate.Validity" = ...
    ): ...
    class ApiPassthrough:
        def __init__(
            self,
            *,
            Extensions: "Certificate.Extensions" = ...,
            Subject: "Certificate.Subject" = ...
        ): ...
    class CertificatePolicyList:
        def __init__(
            self, *, CertificatePolicyList: List["Certificate.PolicyInformation"] = ...
        ): ...
    class EdiPartyName:
        def __init__(self, *, NameAssigner: str, PartyName: str): ...
    class ExtendedKeyUsage:
        def __init__(
            self,
            *,
            ExtendedKeyUsageObjectIdentifier: str = ...,
            ExtendedKeyUsageType: str = ...
        ): ...
    class ExtendedKeyUsageList:
        def __init__(
            self, *, ExtendedKeyUsageList: List["Certificate.ExtendedKeyUsage"] = ...
        ): ...
    class Extensions:
        def __init__(
            self,
            *,
            CertificatePolicies: "Certificate.CertificatePolicyList" = ...,
            ExtendedKeyUsage: "Certificate.ExtendedKeyUsageList" = ...,
            KeyUsage: "Certificate.KeyUsage" = ...,
            SubjectAlternativeNames: "Certificate.GeneralNameList" = ...
        ): ...
    class GeneralName:
        def __init__(
            self,
            *,
            DirectoryName: "Certificate.Subject" = ...,
            DnsName: str = ...,
            EdiPartyName: "Certificate.EdiPartyName" = ...,
            IpAddress: str = ...,
            OtherName: "Certificate.OtherName" = ...,
            RegisteredId: str = ...,
            Rfc822Name: str = ...,
            UniformResourceIdentifier: str = ...
        ): ...
    class GeneralNameList:
        def __init__(
            self, *, GeneralNameList: List["Certificate.GeneralName"] = ...
        ): ...
    class KeyUsage:
        def __init__(
            self,
            *,
            CRLSign: bool = ...,
            DataEncipherment: bool = ...,
            DecipherOnly: bool = ...,
            DigitalSignature: bool = ...,
            EncipherOnly: bool = ...,
            KeyAgreement: bool = ...,
            KeyCertSign: bool = ...,
            KeyEncipherment: bool = ...,
            NonRepudiation: bool = ...
        ): ...
    class OtherName:
        def __init__(self, *, TypeId: str, Value: str): ...
    class PolicyInformation:
        def __init__(
            self,
            *,
            CertPolicyId: str,
            PolicyQualifiers: "Certificate.PolicyQualifierInfoList" = ...
        ): ...
    class PolicyQualifierInfo:
        def __init__(
            self, *, PolicyQualifierId: str, Qualifier: "Certificate.Qualifier"
        ): ...
    class PolicyQualifierInfoList:
        def __init__(
            self,
            *,
            PolicyQualifierInfoList: List["Certificate.PolicyQualifierInfo"] = ...
        ): ...
    class Qualifier:
        def __init__(self, *, CpsUri: str): ...
    class Subject:
        def __init__(
            self,
            *,
            CommonName: str = ...,
            Country: str = ...,
            DistinguishedNameQualifier: str = ...,
            GenerationQualifier: str = ...,
            GivenName: str = ...,
            Initials: str = ...,
            Locality: str = ...,
            Organization: str = ...,
            OrganizationalUnit: str = ...,
            Pseudonym: str = ...,
            SerialNumber: str = ...,
            State: str = ...,
            Surname: str = ...,
            Title: str = ...
        ): ...
    class Validity:
        def __init__(self, *, Type: str, Value: int): ...

class CertificateAuthority:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html"""

    Arn: Final[str]

    CertificateSigningRequest: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeyAlgorithm: str,
        SigningAlgorithm: str,
        Subject: "CertificateAuthority.Subject",
        Type: str,
        CsrExtensions: "CertificateAuthority.CsrExtensions" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RevocationConfiguration: "CertificateAuthority.RevocationConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessDescription:
        def __init__(
            self,
            *,
            AccessLocation: "CertificateAuthority.GeneralName",
            AccessMethod: "CertificateAuthority.AccessMethod"
        ): ...
    class AccessMethod:
        def __init__(
            self, *, AccessMethodType: str = ..., CustomObjectIdentifier: str = ...
        ): ...
    class CrlConfiguration:
        def __init__(
            self,
            *,
            CustomCname: str = ...,
            Enabled: bool = ...,
            ExpirationInDays: int = ...,
            S3BucketName: str = ...
        ): ...
    class CsrExtensions:
        def __init__(
            self,
            *,
            KeyUsage: "CertificateAuthority.KeyUsage" = ...,
            SubjectInformationAccess: "CertificateAuthority.SubjectInformationAccess" = ...
        ): ...
    class EdiPartyName:
        def __init__(self, *, NameAssigner: str, PartyName: str): ...
    class GeneralName:
        def __init__(
            self,
            *,
            DirectoryName: "CertificateAuthority.Subject" = ...,
            DnsName: str = ...,
            EdiPartyName: "CertificateAuthority.EdiPartyName" = ...,
            IpAddress: str = ...,
            OtherName: "CertificateAuthority.OtherName" = ...,
            RegisteredId: str = ...,
            Rfc822Name: str = ...,
            UniformResourceIdentifier: str = ...
        ): ...
    class KeyUsage:
        def __init__(
            self,
            *,
            CRLSign: bool = ...,
            DataEncipherment: bool = ...,
            DecipherOnly: bool = ...,
            DigitalSignature: bool = ...,
            EncipherOnly: bool = ...,
            KeyAgreement: bool = ...,
            KeyCertSign: bool = ...,
            KeyEncipherment: bool = ...,
            NonRepudiation: bool = ...
        ): ...
    class OtherName:
        def __init__(self, *, TypeId: str, Value: str): ...
    class RevocationConfiguration:
        def __init__(
            self, *, CrlConfiguration: "CertificateAuthority.CrlConfiguration" = ...
        ): ...
    class Subject:
        def __init__(
            self,
            *,
            CommonName: str = ...,
            Country: str = ...,
            DistinguishedNameQualifier: str = ...,
            GenerationQualifier: str = ...,
            GivenName: str = ...,
            Initials: str = ...,
            Locality: str = ...,
            Organization: str = ...,
            OrganizationalUnit: str = ...,
            Pseudonym: str = ...,
            SerialNumber: str = ...,
            State: str = ...,
            Surname: str = ...,
            Title: str = ...
        ): ...
    class SubjectInformationAccess:
        def __init__(
            self,
            *,
            SubjectInformationAccess: List[
                "CertificateAuthority.AccessDescription"
            ] = ...
        ): ...

class CertificateAuthorityActivation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html"""

    CompleteCertificateChain: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Certificate: str,
        CertificateAuthorityArn: str,
        CertificateChain: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
