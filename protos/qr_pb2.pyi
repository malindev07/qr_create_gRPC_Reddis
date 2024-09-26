from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QR(_message.Message):
    __slots__ = ("id", "title", "url", "completed")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    url: str
    completed: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., completed: bool = ...) -> None: ...

class CreateQRRequest(_message.Message):
    __slots__ = ("title", "url", "completed")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    title: str
    url: str
    completed: bool
    def __init__(self, title: _Optional[str] = ..., url: _Optional[str] = ..., completed: bool = ...) -> None: ...

class CreateQRResponse(_message.Message):
    __slots__ = ("qr",)
    QR_FIELD_NUMBER: _ClassVar[int]
    qr: QR
    def __init__(self, qr: _Optional[_Union[QR, _Mapping]] = ...) -> None: ...
