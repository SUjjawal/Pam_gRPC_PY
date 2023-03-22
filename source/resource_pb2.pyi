import util_pb2 as _util_pb2
import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountDetail(_message.Message):
    __slots__ = ["accountId", "certDetail", "grcpUser", "ipAddress", "resourceId"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    accountId: int
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceId: _Optional[int] = ..., accountId: _Optional[int] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class AccountMap(_message.Message):
    __slots__ = ["accountName", "accountPassPolicy", "customField", "notes", "password"]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTPASSPOLICY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    accountName: str
    accountPassPolicy: str
    customField: _containers.RepeatedCompositeFieldContainer[_util_pb2.FieldMap]
    notes: str
    password: str
    def __init__(self, accountName: _Optional[str] = ..., password: _Optional[str] = ..., accountPassPolicy: _Optional[str] = ..., notes: _Optional[str] = ..., customField: _Optional[_Iterable[_Union[_util_pb2.FieldMap, _Mapping]]] = ...) -> None: ...

class AccountPassword(_message.Message):
    __slots__ = ["accountId", "certDetail", "grcpUser", "ipAddress", "reason", "resourceId", "ticketId"]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    TICKETID_FIELD_NUMBER: _ClassVar[int]
    accountId: int
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    reason: str
    resourceId: int
    ticketId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceId: _Optional[int] = ..., accountId: _Optional[int] = ..., reason: _Optional[str] = ..., ticketId: _Optional[int] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class CreateAccount(_message.Message):
    __slots__ = ["accountDetails", "certDetail", "grcpUser", "ipAddress", "resourceId"]
    ACCOUNTDETAILS_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    accountDetails: _containers.RepeatedCompositeFieldContainer[AccountMap]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceId: _Optional[int] = ..., accountDetails: _Optional[_Iterable[_Union[AccountMap, _Mapping]]] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ["accountCustomField", "accountName", "accountPasswordPolicy", "certDetail", "department", "dnsName", "domainName", "grcpUser", "ipAddress", "isPrivatekeyEnabled", "location", "notes", "ownerName", "passWord", "resourceCustomField", "resourceDesc", "resourceName", "resourcePasswordPolicy", "resourceType", "resourceUrl"]
    ACCOUNTCUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTPASSWORDPOLICY_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    DNSNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAINNAME_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    ISPRIVATEKEYENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    OWNERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RESOURCECUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    RESOURCEDESC_FIELD_NUMBER: _ClassVar[int]
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCEPASSWORDPOLICY_FIELD_NUMBER: _ClassVar[int]
    RESOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    accountCustomField: _containers.RepeatedCompositeFieldContainer[_util_pb2.FieldMap]
    accountName: str
    accountPasswordPolicy: str
    certDetail: _util_pb2.CertificateDetail
    department: str
    dnsName: str
    domainName: str
    grcpUser: str
    ipAddress: str
    isPrivatekeyEnabled: bool
    location: str
    notes: str
    ownerName: str
    passWord: str
    resourceCustomField: _containers.RepeatedCompositeFieldContainer[_util_pb2.FieldMap]
    resourceDesc: str
    resourceName: str
    resourcePasswordPolicy: str
    resourceType: str
    resourceUrl: str
    def __init__(self, resourceName: _Optional[str] = ..., resourceType: _Optional[str] = ..., accountName: _Optional[str] = ..., passWord: _Optional[str] = ..., notes: _Optional[str] = ..., grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourcePasswordPolicy: _Optional[str] = ..., accountPasswordPolicy: _Optional[str] = ..., isPrivatekeyEnabled: bool = ..., location: _Optional[str] = ..., department: _Optional[str] = ..., dnsName: _Optional[str] = ..., domainName: _Optional[str] = ..., resourceDesc: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., ownerName: _Optional[str] = ..., resourceCustomField: _Optional[_Iterable[_Union[_util_pb2.FieldMap, _Mapping]]] = ..., accountCustomField: _Optional[_Iterable[_Union[_util_pb2.FieldMap, _Mapping]]] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "resourceId"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceId: int
    def __init__(self, resourceId: _Optional[int] = ..., ipAddress: _Optional[str] = ..., grcpUser: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class EditAccount(_message.Message):
    __slots__ = ["accountDetails", "accountId", "certDetail", "grcpUser", "ipAddress", "resourceId"]
    ACCOUNTDETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    accountDetails: AccountMap
    accountId: int
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceId: _Optional[int] = ..., accountId: _Optional[int] = ..., accountDetails: _Optional[_Union[AccountMap, _Mapping]] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class EditRequest(_message.Message):
    __slots__ = ["certDetail", "department", "dnsName", "grcpUser", "ipAddress", "location", "ownerName", "resPasswordPolicy", "resourceCustomField", "resourceDesc", "resourceId", "resourceName", "resourceType", "resourceUrl"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    DNSNAME_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OWNERNAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCECUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    RESOURCEDESC_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    RESPASSWORDPOLICY_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    department: str
    dnsName: str
    grcpUser: str
    ipAddress: str
    location: str
    ownerName: str
    resPasswordPolicy: str
    resourceCustomField: _containers.RepeatedCompositeFieldContainer[_util_pb2.FieldMap]
    resourceDesc: str
    resourceId: int
    resourceName: str
    resourceType: str
    resourceUrl: str
    def __init__(self, resourceName: _Optional[str] = ..., resourceDesc: _Optional[str] = ..., dnsName: _Optional[str] = ..., location: _Optional[str] = ..., department: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceType: _Optional[str] = ..., ownerName: _Optional[str] = ..., resPasswordPolicy: _Optional[str] = ..., resourceCustomField: _Optional[_Iterable[_Union[_util_pb2.FieldMap, _Mapping]]] = ..., grcpUser: _Optional[str] = ..., resourceId: _Optional[int] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class GetResourceIDReq(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "resourceName"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceName: str
    def __init__(self, resourceName: _Optional[str] = ..., grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class GetResourceRequest(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class ResAccountList(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "resourceId"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceId: _Optional[int] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class ResourceIdAccountId(_message.Message):
    __slots__ = ["accountName", "certDetail", "grcpUser", "ipAddress", "resourceName"]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    accountName: str
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    resourceName: str
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceName: _Optional[str] = ..., accountName: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class ResourceTypeArray(_message.Message):
    __slots__ = ["resourceType"]
    RESOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    resourceType: str
    def __init__(self, resourceType: _Optional[str] = ...) -> None: ...

class ResourceTypes(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "orgName", "resourceType"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORGNAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    orgName: str
    resourceType: _containers.RepeatedCompositeFieldContainer[ResourceTypeArray]
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., resourceType: _Optional[_Iterable[_Union[ResourceTypeArray, _Mapping]]] = ..., orgName: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...
