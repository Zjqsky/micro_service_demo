# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/base.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/base.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11protos/base.proto\x12\x06protos\"\t\n\x07\x42\x61seReq\"-\n\nCommonResp\x12\x1f\n\x04resp\x18\xff\x01 \x01(\x0b\x32\x10.protos.BaseResp\"F\n\x08\x42\x61seResp\x12\x16\n\x0estatus_message\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.protos.StatusCode\"\x14\n\x06IdData\x12\n\n\x02id\x18\x01 \x01(\x03\"\x16\n\x07NumData\x12\x0b\n\x03num\x18\x01 \x01(\x03*>\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\x05\x45RROR\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x14\n\x07WARNING\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x62\x06proto3'
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='protos.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=-1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=-2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=205,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
ERROR = -1
WARNING = -2



_BASEREQ = _descriptor.Descriptor(
  name='BaseReq',
  full_name='protos.BaseReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=38,
)


_COMMONRESP = _descriptor.Descriptor(
  name='CommonResp',
  full_name='protos.CommonResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='protos.CommonResp.resp', index=0,
      number=255, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=85,
)


_BASERESP = _descriptor.Descriptor(
  name='BaseResp',
  full_name='protos.BaseResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_message', full_name='protos.BaseResp.status_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='protos.BaseResp.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=157,
)


_IDDATA = _descriptor.Descriptor(
  name='IdData',
  full_name='protos.IdData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.IdData.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=179,
)


_NUMDATA = _descriptor.Descriptor(
  name='NumData',
  full_name='protos.NumData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='protos.NumData.num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=203,
)

_COMMONRESP.fields_by_name['resp'].message_type = _BASERESP
_BASERESP.fields_by_name['status'].enum_type = _STATUSCODE
DESCRIPTOR.message_types_by_name['BaseReq'] = _BASEREQ
DESCRIPTOR.message_types_by_name['CommonResp'] = _COMMONRESP
DESCRIPTOR.message_types_by_name['BaseResp'] = _BASERESP
DESCRIPTOR.message_types_by_name['IdData'] = _IDDATA
DESCRIPTOR.message_types_by_name['NumData'] = _NUMDATA
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseReq = _reflection.GeneratedProtocolMessageType('BaseReq', (_message.Message,), {
  'DESCRIPTOR' : _BASEREQ,
  '__module__' : 'protos.base_pb2'
  # @@protoc_insertion_point(class_scope:protos.BaseReq)
  })
_sym_db.RegisterMessage(BaseReq)

CommonResp = _reflection.GeneratedProtocolMessageType('CommonResp', (_message.Message,), {
  'DESCRIPTOR' : _COMMONRESP,
  '__module__' : 'protos.base_pb2'
  # @@protoc_insertion_point(class_scope:protos.CommonResp)
  })
_sym_db.RegisterMessage(CommonResp)

BaseResp = _reflection.GeneratedProtocolMessageType('BaseResp', (_message.Message,), {
  'DESCRIPTOR' : _BASERESP,
  '__module__' : 'protos.base_pb2'
  # @@protoc_insertion_point(class_scope:protos.BaseResp)
  })
_sym_db.RegisterMessage(BaseResp)

IdData = _reflection.GeneratedProtocolMessageType('IdData', (_message.Message,), {
  'DESCRIPTOR' : _IDDATA,
  '__module__' : 'protos.base_pb2'
  # @@protoc_insertion_point(class_scope:protos.IdData)
  })
_sym_db.RegisterMessage(IdData)

NumData = _reflection.GeneratedProtocolMessageType('NumData', (_message.Message,), {
  'DESCRIPTOR' : _NUMDATA,
  '__module__' : 'protos.base_pb2'
  # @@protoc_insertion_point(class_scope:protos.NumData)
  })
_sym_db.RegisterMessage(NumData)


# @@protoc_insertion_point(module_scope)
