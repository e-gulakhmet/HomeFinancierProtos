# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: homefinancier/storages/v1/storages.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(homefinancier/storages/v1/storages.proto\x12\x19homefinancier.storages.v1\"\x88\x01\n\x14\x43reateStorageRequest\x12\x12\n\x04link\x18\x01 \x01(\tR\x04link\x12.\n\x13\x65xpenses_table_link\x18\x02 \x01(\tR\x11\x65xpensesTableLink\x12,\n\x12incomes_table_link\x18\x03 \x01(\tR\x10incomesTableLink\"6\n\x15\x43reateStorageResponse\x12\x1d\n\nstorage_id\x18\x01 \x01(\tR\tstorageId\"2\n\x11GetStorageRequest\x12\x1d\n\nstorage_id\x18\x01 \x01(\tR\tstorageId\"\x86\x01\n\x12GetStorageResponse\x12\x12\n\x04link\x18\x01 \x01(\tR\x04link\x12.\n\x13\x65xpenses_table_link\x18\x02 \x01(\tR\x11\x65xpensesTableLink\x12,\n\x12incomes_table_link\x18\x03 \x01(\tR\x10incomesTableLink2\xf4\x01\n\x0fStoragesService\x12t\n\rCreateStorage\x12/.homefinancier.storages.v1.CreateStorageRequest\x1a\x30.homefinancier.storages.v1.CreateStorageResponse\"\x00\x12k\n\nGetStorage\x12,.homefinancier.storages.v1.GetStorageRequest\x1a-.homefinancier.storages.v1.GetStorageResponse\"\x00\x42\xb4\x01\n\x1d\x63om.homefinancier.storages.v1B\rStoragesProtoP\x01\xa2\x02\x03HSX\xaa\x02\x19Homefinancier.Storages.V1\xca\x02\x19Homefinancier\\Storages\\V1\xe2\x02%Homefinancier\\Storages\\V1\\GPBMetadata\xea\x02\x1bHomefinancier::Storages::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'homefinancier.storages.v1.storages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.homefinancier.storages.v1B\rStoragesProtoP\001\242\002\003HSX\252\002\031Homefinancier.Storages.V1\312\002\031Homefinancier\\Storages\\V1\342\002%Homefinancier\\Storages\\V1\\GPBMetadata\352\002\033Homefinancier::Storages::V1'
  _globals['_CREATESTORAGEREQUEST']._serialized_start=72
  _globals['_CREATESTORAGEREQUEST']._serialized_end=208
  _globals['_CREATESTORAGERESPONSE']._serialized_start=210
  _globals['_CREATESTORAGERESPONSE']._serialized_end=264
  _globals['_GETSTORAGEREQUEST']._serialized_start=266
  _globals['_GETSTORAGEREQUEST']._serialized_end=316
  _globals['_GETSTORAGERESPONSE']._serialized_start=319
  _globals['_GETSTORAGERESPONSE']._serialized_end=453
  _globals['_STORAGESSERVICE']._serialized_start=456
  _globals['_STORAGESSERVICE']._serialized_end=700
# @@protoc_insertion_point(module_scope)