# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/qr.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 2, "", "protos/qr.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fprotos/qr.proto\x12\x02qr"?\n\x02QR\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x11\n\tcompleted\x18\x04 \x01(\x08"@\n\x0f\x43reateQRRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\tcompleted\x18\x03 \x01(\x08"&\n\x10\x43reateQRResponse\x12\x12\n\x02qr\x18\x01 \x01(\x0b\x32\x06.qr.QR2B\n\tQRService\x12\x35\n\x08\x43reateQR\x12\x13.qr.CreateQRRequest\x1a\x14.qr.CreateQRResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "protos.qr_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_QR"]._serialized_start = 23
    _globals["_QR"]._serialized_end = 86
    _globals["_CREATEQRREQUEST"]._serialized_start = 88
    _globals["_CREATEQRREQUEST"]._serialized_end = 152
    _globals["_CREATEQRRESPONSE"]._serialized_start = 154
    _globals["_CREATEQRRESPONSE"]._serialized_end = 192
    _globals["_QRSERVICE"]._serialized_start = 194
    _globals["_QRSERVICE"]._serialized_end = 260
# @@protoc_insertion_point(module_scope)
