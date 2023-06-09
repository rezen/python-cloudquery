# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csource.proto\x12\x14\x63loudquery.source.v1\".\n\x07GetName\x1a\t\n\x07Request\x1a\x18\n\x08Response\x12\x0c\n\x04name\x18\x01 \x01(\t\"4\n\nGetVersion\x1a\t\n\x07Request\x1a\x1b\n\x08Response\x12\x0f\n\x07version\x18\x01 \x01(\t\"+\n\x04Init\x1a\x17\n\x07Request\x12\x0c\n\x04spec\x18\x01 \x01(\x0c\x1a\n\n\x08Response\"9\n\x10GetDynamicTables\x1a\t\n\x07Request\x1a\x1a\n\x08Response\x12\x0e\n\x06tables\x18\x01 \x01(\x0c\"/\n\x04Sync\x1a\t\n\x07Request\x1a\x1c\n\x08Response\x12\x10\n\x08resource\x18\x01 \x01(\x0c\"Q\n\tGetTables\x1a\t\n\x07Request\x1a\x39\n\x08Response\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06tables\x18\x03 \x01(\x0c\"4\n\nGetMetrics\x1a\t\n\x07Request\x1a\x1b\n\x08Response\x12\x0f\n\x07metrics\x18\x01 \x01(\x0c\"\x86\x01\n\x07GenDocs\x1aM\n\x07Request\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x34\n\x06\x66ormat\x18\x02 \x01(\x0e\x32$.cloudquery.source.v1.GenDocs.FORMAT\x1a\n\n\x08Response\" \n\x06\x46ORMAT\x12\x0c\n\x08markdown\x10\x00\x12\x08\n\x04json\x10\x01\x32\xfb\x05\n\x06Source\x12X\n\x07GetName\x12%.cloudquery.source.v1.GetName.Request\x1a&.cloudquery.source.v1.GetName.Response\x12\x61\n\nGetVersion\x12(.cloudquery.source.v1.GetVersion.Request\x1a).cloudquery.source.v1.GetVersion.Response\x12^\n\tGetTables\x12\'.cloudquery.source.v1.GetTables.Request\x1a(.cloudquery.source.v1.GetTables.Response\x12\x61\n\nGetMetrics\x12(.cloudquery.source.v1.GetMetrics.Request\x1a).cloudquery.source.v1.GetMetrics.Response\x12O\n\x04Init\x12\".cloudquery.source.v1.Init.Request\x1a#.cloudquery.source.v1.Init.Response\x12s\n\x10GetDynamicTables\x12..cloudquery.source.v1.GetDynamicTables.Request\x1a/.cloudquery.source.v1.GetDynamicTables.Response\x12Q\n\x04Sync\x12\".cloudquery.source.v1.Sync.Request\x1a#.cloudquery.source.v1.Sync.Response0\x01\x12X\n\x07GenDocs\x12%.cloudquery.source.v1.GenDocs.Request\x1a&.cloudquery.source.v1.GenDocs.ResponseB8Z6github.com/cloudquery/plugin-pb-go/pb/source/v1;sourceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'source_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/cloudquery/plugin-pb-go/pb/source/v1;source'
  _GETNAME._serialized_start=38
  _GETNAME._serialized_end=84
  _GETNAME_REQUEST._serialized_start=49
  _GETNAME_REQUEST._serialized_end=58
  _GETNAME_RESPONSE._serialized_start=60
  _GETNAME_RESPONSE._serialized_end=84
  _GETVERSION._serialized_start=86
  _GETVERSION._serialized_end=138
  _GETVERSION_REQUEST._serialized_start=49
  _GETVERSION_REQUEST._serialized_end=58
  _GETVERSION_RESPONSE._serialized_start=111
  _GETVERSION_RESPONSE._serialized_end=138
  _INIT._serialized_start=140
  _INIT._serialized_end=183
  _INIT_REQUEST._serialized_start=148
  _INIT_REQUEST._serialized_end=171
  _INIT_RESPONSE._serialized_start=60
  _INIT_RESPONSE._serialized_end=70
  _GETDYNAMICTABLES._serialized_start=185
  _GETDYNAMICTABLES._serialized_end=242
  _GETDYNAMICTABLES_REQUEST._serialized_start=49
  _GETDYNAMICTABLES_REQUEST._serialized_end=58
  _GETDYNAMICTABLES_RESPONSE._serialized_start=216
  _GETDYNAMICTABLES_RESPONSE._serialized_end=242
  _SYNC._serialized_start=244
  _SYNC._serialized_end=291
  _SYNC_REQUEST._serialized_start=49
  _SYNC_REQUEST._serialized_end=58
  _SYNC_RESPONSE._serialized_start=263
  _SYNC_RESPONSE._serialized_end=291
  _GETTABLES._serialized_start=293
  _GETTABLES._serialized_end=374
  _GETTABLES_REQUEST._serialized_start=49
  _GETTABLES_REQUEST._serialized_end=58
  _GETTABLES_RESPONSE._serialized_start=317
  _GETTABLES_RESPONSE._serialized_end=374
  _GETMETRICS._serialized_start=376
  _GETMETRICS._serialized_end=428
  _GETMETRICS_REQUEST._serialized_start=49
  _GETMETRICS_REQUEST._serialized_end=58
  _GETMETRICS_RESPONSE._serialized_start=401
  _GETMETRICS_RESPONSE._serialized_end=428
  _GENDOCS._serialized_start=431
  _GENDOCS._serialized_end=565
  _GENDOCS_REQUEST._serialized_start=442
  _GENDOCS_REQUEST._serialized_end=519
  _GENDOCS_RESPONSE._serialized_start=60
  _GENDOCS_RESPONSE._serialized_end=70
  _GENDOCS_FORMAT._serialized_start=533
  _GENDOCS_FORMAT._serialized_end=565
  _SOURCE._serialized_start=568
  _SOURCE._serialized_end=1331
# @@protoc_insertion_point(module_scope)
