"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CreateStorageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINK_FIELD_NUMBER: builtins.int
    EXPENSES_TABLE_LINK_FIELD_NUMBER: builtins.int
    INCOMES_TABLE_LINK_FIELD_NUMBER: builtins.int
    link: builtins.str
    expenses_table_link: builtins.str
    incomes_table_link: builtins.str
    def __init__(
        self,
        *,
        link: builtins.str = ...,
        expenses_table_link: builtins.str = ...,
        incomes_table_link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expenses_table_link", b"expenses_table_link", "incomes_table_link", b"incomes_table_link", "link", b"link"]) -> None: ...

global___CreateStorageRequest = CreateStorageRequest

@typing_extensions.final
class CreateStorageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_ID_FIELD_NUMBER: builtins.int
    storage_id: builtins.str
    def __init__(
        self,
        *,
        storage_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["storage_id", b"storage_id"]) -> None: ...

global___CreateStorageResponse = CreateStorageResponse

@typing_extensions.final
class GetStorageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_ID_FIELD_NUMBER: builtins.int
    storage_id: builtins.str
    def __init__(
        self,
        *,
        storage_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["storage_id", b"storage_id"]) -> None: ...

global___GetStorageRequest = GetStorageRequest

@typing_extensions.final
class GetStorageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINK_FIELD_NUMBER: builtins.int
    EXPENSES_TABLE_LINK_FIELD_NUMBER: builtins.int
    INCOMES_TABLE_LINK_FIELD_NUMBER: builtins.int
    link: builtins.str
    expenses_table_link: builtins.str
    incomes_table_link: builtins.str
    def __init__(
        self,
        *,
        link: builtins.str = ...,
        expenses_table_link: builtins.str = ...,
        incomes_table_link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expenses_table_link", b"expenses_table_link", "incomes_table_link", b"incomes_table_link", "link", b"link"]) -> None: ...

global___GetStorageResponse = GetStorageResponse