import util_pb2 as _util_pb2
import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUser(_message.Message):
    __slots__ = ["certDetail", "department", "email", "expiryDate", "firstName", "fullName", "grcpUser", "hostName", "ipAddress", "isApiUser", "isSupperAdmin", "lastName", "location", "password", "policy", "role", "userName"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EXPIRYDATE_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    ISAPIUSER_FIELD_NUMBER: _ClassVar[int]
    ISSUPPERADMIN_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    department: str
    email: str
    expiryDate: str
    firstName: str
    fullName: str
    grcpUser: str
    hostName: str
    ipAddress: str
    isApiUser: bool
    isSupperAdmin: bool
    lastName: str
    location: str
    password: str
    policy: str
    role: str
    userName: str
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., userName: _Optional[str] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., fullName: _Optional[str] = ..., email: _Optional[str] = ..., policy: _Optional[str] = ..., role: _Optional[str] = ..., isSupperAdmin: bool = ..., password: _Optional[str] = ..., department: _Optional[str] = ..., location: _Optional[str] = ..., isApiUser: bool = ..., hostName: _Optional[str] = ..., expiryDate: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class UserID(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "userId"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    userId: int
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., userId: _Optional[int] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...

class UserName(_message.Message):
    __slots__ = ["certDetail", "grcpUser", "ipAddress", "userName"]
    CERTDETAIL_FIELD_NUMBER: _ClassVar[int]
    GRCPUSER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    certDetail: _util_pb2.CertificateDetail
    grcpUser: str
    ipAddress: str
    userName: str
    def __init__(self, grcpUser: _Optional[str] = ..., ipAddress: _Optional[str] = ..., userName: _Optional[str] = ..., certDetail: _Optional[_Union[_util_pb2.CertificateDetail, _Mapping]] = ...) -> None: ...
