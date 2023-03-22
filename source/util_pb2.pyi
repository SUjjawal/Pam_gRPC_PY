from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CertificateDetail(_message.Message):
    __slots__ = ["pfxPassword", "thumbPrint"]
    PFXPASSWORD_FIELD_NUMBER: _ClassVar[int]
    THUMBPRINT_FIELD_NUMBER: _ClassVar[int]
    pfxPassword: str
    thumbPrint: str
    def __init__(self, thumbPrint: _Optional[str] = ..., pfxPassword: _Optional[str] = ...) -> None: ...

class FieldMap(_message.Message):
    __slots__ = ["customLabel", "customValue"]
    CUSTOMLABEL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMVALUE_FIELD_NUMBER: _ClassVar[int]
    customLabel: str
    customValue: str
    def __init__(self, customLabel: _Optional[str] = ..., customValue: _Optional[str] = ...) -> None: ...
