# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: W.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='W.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x07W.proto\"\xd6\x02\n\rServerRequest\x12\"\n\x05\x63\x61rds\x18\x01 \x03(\x0b\x32\x13.ServerRequest.Card\x1a\xa0\x02\n\x04\x43\x61rd\x12\x10\n\x08gpu_name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x13\n\x0btemperature\x18\x03 \x01(\x05\x12\x11\n\tfan_speed\x18\x04 \x01(\x05\x12\x13\n\x0bmemory_used\x18\x05 \x01(\x05\x12\x14\n\x0cmemory_total\x18\x06 \x01(\x05\x12\x13\n\x0butilization\x18\x07 \x01(\x05\x12\x0c\n\x04uuid\x18\x08 \x01(\t\x12,\n\x07process\x18\t \x03(\x0b\x32\x1b.ServerRequest.Card.Process\x1aS\n\x07Process\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x18\n\x10gpu_memory_usage\x18\x03 \x01(\x05\x12\x0b\n\x03pid\x18\x04 \x01(\x05\"!\n\x0eServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\t27\n\x04gRPC\x12/\n\nGetMessage\x12\x0e.ServerRequest\x1a\x0f.ServerResponse\"\x00\x62\x06proto3')
)




_SERVERREQUEST_CARD_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='ServerRequest.Card.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='ServerRequest.Card.Process.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='ServerRequest.Card.Process.command', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_memory_usage', full_name='ServerRequest.Card.Process.gpu_memory_usage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='ServerRequest.Card.Process.pid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=271,
  serialized_end=354,
)

_SERVERREQUEST_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='ServerRequest.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpu_name', full_name='ServerRequest.Card.gpu_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='ServerRequest.Card.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='ServerRequest.Card.temperature', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fan_speed', full_name='ServerRequest.Card.fan_speed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_used', full_name='ServerRequest.Card.memory_used', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_total', full_name='ServerRequest.Card.memory_total', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utilization', full_name='ServerRequest.Card.utilization', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ServerRequest.Card.uuid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process', full_name='ServerRequest.Card.process', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVERREQUEST_CARD_PROCESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=354,
)

_SERVERREQUEST = _descriptor.Descriptor(
  name='ServerRequest',
  full_name='ServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cards', full_name='ServerRequest.cards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVERREQUEST_CARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=354,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ServerResponse.success', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=356,
  serialized_end=389,
)

_SERVERREQUEST_CARD_PROCESS.containing_type = _SERVERREQUEST_CARD
_SERVERREQUEST_CARD.fields_by_name['process'].message_type = _SERVERREQUEST_CARD_PROCESS
_SERVERREQUEST_CARD.containing_type = _SERVERREQUEST
_SERVERREQUEST.fields_by_name['cards'].message_type = _SERVERREQUEST_CARD
DESCRIPTOR.message_types_by_name['ServerRequest'] = _SERVERREQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), dict(

  Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), dict(

    Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), dict(
      DESCRIPTOR = _SERVERREQUEST_CARD_PROCESS,
      __module__ = 'W_pb2'
      # @@protoc_insertion_point(class_scope:ServerRequest.Card.Process)
      ))
    ,
    DESCRIPTOR = _SERVERREQUEST_CARD,
    __module__ = 'W_pb2'
    # @@protoc_insertion_point(class_scope:ServerRequest.Card)
    ))
  ,
  DESCRIPTOR = _SERVERREQUEST,
  __module__ = 'W_pb2'
  # @@protoc_insertion_point(class_scope:ServerRequest)
  ))
_sym_db.RegisterMessage(ServerRequest)
_sym_db.RegisterMessage(ServerRequest.Card)
_sym_db.RegisterMessage(ServerRequest.Card.Process)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRESPONSE,
  __module__ = 'W_pb2'
  # @@protoc_insertion_point(class_scope:ServerResponse)
  ))
_sym_db.RegisterMessage(ServerResponse)



_GRPC = _descriptor.ServiceDescriptor(
  name='gRPC',
  full_name='gRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=391,
  serialized_end=446,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMessage',
    full_name='gRPC.GetMessage',
    index=0,
    containing_service=None,
    input_type=_SERVERREQUEST,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPC)

DESCRIPTOR.services_by_name['gRPC'] = _GRPC

# @@protoc_insertion_point(module_scope)
