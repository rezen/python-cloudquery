# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import v.v1.source_pb2 as source__pb2


class SourceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetName = channel.unary_unary(
                '/cloudquery.source.v1.Source/GetName',
                request_serializer=source__pb2.GetName.Request.SerializeToString,
                response_deserializer=source__pb2.GetName.Response.FromString,
                )
        self.GetVersion = channel.unary_unary(
                '/cloudquery.source.v1.Source/GetVersion',
                request_serializer=source__pb2.GetVersion.Request.SerializeToString,
                response_deserializer=source__pb2.GetVersion.Response.FromString,
                )
        self.GetTables = channel.unary_unary(
                '/cloudquery.source.v1.Source/GetTables',
                request_serializer=source__pb2.GetTables.Request.SerializeToString,
                response_deserializer=source__pb2.GetTables.Response.FromString,
                )
        self.GetMetrics = channel.unary_unary(
                '/cloudquery.source.v1.Source/GetMetrics',
                request_serializer=source__pb2.GetMetrics.Request.SerializeToString,
                response_deserializer=source__pb2.GetMetrics.Response.FromString,
                )
        self.Init = channel.unary_unary(
                '/cloudquery.source.v1.Source/Init',
                request_serializer=source__pb2.Init.Request.SerializeToString,
                response_deserializer=source__pb2.Init.Response.FromString,
                )
        self.GetDynamicTables = channel.unary_unary(
                '/cloudquery.source.v1.Source/GetDynamicTables',
                request_serializer=source__pb2.GetDynamicTables.Request.SerializeToString,
                response_deserializer=source__pb2.GetDynamicTables.Response.FromString,
                )
        self.Sync = channel.unary_stream(
                '/cloudquery.source.v1.Source/Sync',
                request_serializer=source__pb2.Sync.Request.SerializeToString,
                response_deserializer=source__pb2.Sync.Response.FromString,
                )
        self.GenDocs = channel.unary_unary(
                '/cloudquery.source.v1.Source/GenDocs',
                request_serializer=source__pb2.GenDocs.Request.SerializeToString,
                response_deserializer=source__pb2.GenDocs.Response.FromString,
                )


class SourceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetName(self, request, context):
        """Get the name of the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Get the current version of the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTables(self, request, context):
        """Get all static tables the source plugin supports
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Get metrics for the source plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Configure the plugin with the given credentials and mode
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDynamicTables(self, request, context):
        """Get all tables the source plugin supports. Must be called after Init
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Start the sync the source plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenDocs(self, request, context):
        """Generate documentation for the source plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetName,
                    request_deserializer=source__pb2.GetName.Request.FromString,
                    response_serializer=source__pb2.GetName.Response.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=source__pb2.GetVersion.Request.FromString,
                    response_serializer=source__pb2.GetVersion.Response.SerializeToString,
            ),
            'GetTables': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTables,
                    request_deserializer=source__pb2.GetTables.Request.FromString,
                    response_serializer=source__pb2.GetTables.Response.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=source__pb2.GetMetrics.Request.FromString,
                    response_serializer=source__pb2.GetMetrics.Response.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=source__pb2.Init.Request.FromString,
                    response_serializer=source__pb2.Init.Response.SerializeToString,
            ),
            'GetDynamicTables': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDynamicTables,
                    request_deserializer=source__pb2.GetDynamicTables.Request.FromString,
                    response_serializer=source__pb2.GetDynamicTables.Response.SerializeToString,
            ),
            'Sync': grpc.unary_stream_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=source__pb2.Sync.Request.FromString,
                    response_serializer=source__pb2.Sync.Response.SerializeToString,
            ),
            'GenDocs': grpc.unary_unary_rpc_method_handler(
                    servicer.GenDocs,
                    request_deserializer=source__pb2.GenDocs.Request.FromString,
                    response_serializer=source__pb2.GenDocs.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cloudquery.source.v1.Source', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Source(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GetName',
            source__pb2.GetName.Request.SerializeToString,
            source__pb2.GetName.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GetVersion',
            source__pb2.GetVersion.Request.SerializeToString,
            source__pb2.GetVersion.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GetTables',
            source__pb2.GetTables.Request.SerializeToString,
            source__pb2.GetTables.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GetMetrics',
            source__pb2.GetMetrics.Request.SerializeToString,
            source__pb2.GetMetrics.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/Init',
            source__pb2.Init.Request.SerializeToString,
            source__pb2.Init.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDynamicTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GetDynamicTables',
            source__pb2.GetDynamicTables.Request.SerializeToString,
            source__pb2.GetDynamicTables.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/cloudquery.source.v1.Source/Sync',
            source__pb2.Sync.Request.SerializeToString,
            source__pb2.Sync.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenDocs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.source.v1.Source/GenDocs',
            source__pb2.GenDocs.Request.SerializeToString,
            source__pb2.GenDocs.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
