# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import services_pb2 as services__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in services_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProducerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/ProducerService/Generate',
                request_serializer=services__pb2.Empty.SerializeToString,
                response_deserializer=services__pb2.Data.FromString,
                _registered_method=True)


class ProducerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProducerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=services__pb2.Empty.FromString,
                    response_serializer=services__pb2.Data.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProducerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ProducerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProducerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProducerService/Generate',
            services__pb2.Empty.SerializeToString,
            services__pb2.Data.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ProcessorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Process = channel.unary_unary(
                '/ProcessorService/Process',
                request_serializer=services__pb2.Data.SerializeToString,
                response_deserializer=services__pb2.ProcessedData.FromString,
                _registered_method=True)


class ProcessorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Process(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProcessorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Process': grpc.unary_unary_rpc_method_handler(
                    servicer.Process,
                    request_deserializer=services__pb2.Data.FromString,
                    response_serializer=services__pb2.ProcessedData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProcessorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ProcessorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProcessorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Process(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProcessorService/Process',
            services__pb2.Data.SerializeToString,
            services__pb2.ProcessedData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class AggregatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Aggregate = channel.stream_unary(
                '/AggregatorService/Aggregate',
                request_serializer=services__pb2.ProcessedData.SerializeToString,
                response_deserializer=services__pb2.Summary.FromString,
                _registered_method=True)


class AggregatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Aggregate(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AggregatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Aggregate': grpc.stream_unary_rpc_method_handler(
                    servicer.Aggregate,
                    request_deserializer=services__pb2.ProcessedData.FromString,
                    response_serializer=services__pb2.Summary.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AggregatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('AggregatorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AggregatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Aggregate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/AggregatorService/Aggregate',
            services__pb2.ProcessedData.SerializeToString,
            services__pb2.Summary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
