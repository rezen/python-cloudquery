# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cq.discovery.discovery_pb2 as discovery__pb2


class DiscoveryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVersions = channel.unary_unary(
                '/cloudquery.discovery.v0.Discovery/GetVersions',
                request_serializer=discovery__pb2.GetVersions.Request.SerializeToString,
                response_deserializer=discovery__pb2.GetVersions.Response.FromString,
                )


class DiscoveryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetVersions(self, request, context):
        """Get the name of the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiscoveryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersions,
                    request_deserializer=discovery__pb2.GetVersions.Request.FromString,
                    response_serializer=discovery__pb2.GetVersions.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cloudquery.discovery.v0.Discovery', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Discovery(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cloudquery.discovery.v0.Discovery/GetVersions',
            discovery__pb2.GetVersions.Request.SerializeToString,
            discovery__pb2.GetVersions.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
