# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'services.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\"\x07\n\x05\x45mpty\"\x17\n\x04\x44\x61ta\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x1f\n\rProcessedData\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1a\n\x07Summary\x12\x0f\n\x07summary\x18\x01 \x01(\t2,\n\x0fProducerService\x12\x19\n\x08Generate\x12\x06.Empty\x1a\x05.Data24\n\x10ProcessorService\x12 \n\x07Process\x12\x05.Data\x1a\x0e.ProcessedData2<\n\x11\x41ggregatorService\x12\'\n\tAggregate\x12\x0e.ProcessedData\x1a\x08.Summary(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=18
  _globals['_EMPTY']._serialized_end=25
  _globals['_DATA']._serialized_start=27
  _globals['_DATA']._serialized_end=50
  _globals['_PROCESSEDDATA']._serialized_start=52
  _globals['_PROCESSEDDATA']._serialized_end=83
  _globals['_SUMMARY']._serialized_start=85
  _globals['_SUMMARY']._serialized_end=111
  _globals['_PRODUCERSERVICE']._serialized_start=113
  _globals['_PRODUCERSERVICE']._serialized_end=157
  _globals['_PROCESSORSERVICE']._serialized_start=159
  _globals['_PROCESSORSERVICE']._serialized_end=211
  _globals['_AGGREGATORSERVICE']._serialized_start=213
  _globals['_AGGREGATORSERVICE']._serialized_end=273
# @@protoc_insertion_point(module_scope)
