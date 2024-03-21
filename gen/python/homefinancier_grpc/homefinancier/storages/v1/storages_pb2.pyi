from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateStorageRequest(_message.Message):
    __slots__ = ("link", "expenses_table_link", "incomes_table_link")
    LINK_FIELD_NUMBER: _ClassVar[int]
    EXPENSES_TABLE_LINK_FIELD_NUMBER: _ClassVar[int]
    INCOMES_TABLE_LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    expenses_table_link: str
    incomes_table_link: str
    def __init__(self, link: _Optional[str] = ..., expenses_table_link: _Optional[str] = ..., incomes_table_link: _Optional[str] = ...) -> None: ...

class CreateStorageResponse(_message.Message):
    __slots__ = ("storage_id",)
    STORAGE_ID_FIELD_NUMBER: _ClassVar[int]
    storage_id: str
    def __init__(self, storage_id: _Optional[str] = ...) -> None: ...

class GetStorageRequest(_message.Message):
    __slots__ = ("storage_id",)
    STORAGE_ID_FIELD_NUMBER: _ClassVar[int]
    storage_id: str
    def __init__(self, storage_id: _Optional[str] = ...) -> None: ...

class GetStorageResponse(_message.Message):
    __slots__ = ("link", "expenses_table_link", "incomes_table_link")
    LINK_FIELD_NUMBER: _ClassVar[int]
    EXPENSES_TABLE_LINK_FIELD_NUMBER: _ClassVar[int]
    INCOMES_TABLE_LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    expenses_table_link: str
    incomes_table_link: str
    def __init__(self, link: _Optional[str] = ..., expenses_table_link: _Optional[str] = ..., incomes_table_link: _Optional[str] = ...) -> None: ...
