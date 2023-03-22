from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApiResponse(_message.Message):
    __slots__ = ["responseCode", "responseMessage"]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    responseCode: int
    responseMessage: str
    def __init__(self, responseMessage: _Optional[str] = ..., responseCode: _Optional[int] = ...) -> None: ...
