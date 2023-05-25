# cloudquery sync . --log-level debug --log-console
from concurrent import futures
import json
import grpc
import pyarrow as pa
import cq.v1.source_pb2 as pb2
import cq.v1.source_pb2_grpc as pb2_grpc
import cq.discovery.discovery_pb2 as d_pb2
import cq.discovery.discovery_pb2_grpc as d_pb2_grpc
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException
import time
import uuid

import cq.types as cq_types

PLUGIN_NAME = "test"
PLUGIN_VERSION = "v2"
TABLE_NAME = PLUGIN_NAME

# https://github.com/cloudquery/plugin-sdk/blob/main/internal/servers/destination/v0/schemav2tov3.go


class DiscoveryV1Handler(d_pb2_grpc.DiscoveryServicer):
    def GetVersions(self, request, context):
        return d_pb2.GetVersions.Response(versions=["v1"])


class SourceV1Handler(pb2_grpc.SourceServicer):
    def GetName(self, request, context):
        return pb2.GetName.Response(name=PLUGIN_NAME)

    def GetMetrics(self, request, context):
        return pb2.GetMetrics.Response(
            metrics=bytes(
                json.dumps(
                    {
                        "TableClient": {
                            TABLE_NAME: {
                                "": {
                                    "Resources": 1,
                                    "Errors": 0,
                                    "Panics": 0,
                                    "StartTime": "0001-01-01T00:00:00Z",
                                    "EndTime": "0001-01-01T00:00:00Z",
                                }
                            }
                        }
                    }
                ),
                "utf8",
            )
        )

    def GetVersion(self, request, context):
        return pb2.GetVersion.Response(version=PLUGIN_VERSION)


    def GetTables(self, request, context):
        # For some reason this is not called with v1?
        return pb2.GetTables.Response(
            name=PLUGIN_NAME,
            version=PLUGIN_VERSION,
            tables=bytes(
                "null",
                "utf8",
            ),
        )

    def GetDynamicTables(self, request, context):
        return pb2.GetDynamicTables.Response(
            tables=bytes(
                json.dumps(
                    [
                        {
                            "name": TABLE_NAME,
                            "title": TABLE_NAME,
                            "description": "....",
                            "relations": None,
                            "IsIncremental": True,
                            "ignore_in_tests": True,
                            "pk_constraint_name": "",
                            "columns": [
                                {
                                    "name": "_cq_id",
                                    "type": cq_types.CQ_TYPE_MAP["TypeUUID"],
                                    "creation_options": {
                                        "not_null": True,
                                        "incremental_key": False,
                                        "unique": True,
                                    },
                                },
                                {
                                    "name": "_cq_parent_id",
                                    "type": cq_types.CQ_TYPE_MAP["TypeUUID"],
                                    "creation_options": {"incremental_key": False},
                                },
                                {
                                    "name": "test",
                                    "type": cq_types.CQ_TYPE_MAP["TypeString"],
                                    "creation_options": {
                                        "not_null": False,
                                        "incremental_key": False,
                                        "unique": False,
                                    },
                                },
                            ],
                        }
                    ]
                ),
                "utf8",
            ),
        )

    def Init(self, request, context):
        spec = json.loads(request.spec)
        print(spec)
        print(context.peer())
        return pb2.Init.Response()

    def Sync(self, request, context):
        # https://github.com/cloudquery/plugin-sdk/tree/main/schema
        for x in range(0, 10):
            time.sleep(1)
            yield pb2.Sync.Response(
                resource=bytes(
                    json.dumps(
                        {
                            "table_name": TABLE_NAME,
                            "data": [
                                cq_types.cq_serialize(uuid.uuid4()),
                                {
                                    "type": "UUID",
                                    "value": {
                                        "Bytes": [
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                            0,
                                        ],
                                        "Status": 1,
                                    },
                                },
                                {
                                    "type": "Text",
                                    "value": {
                                        "Str": "Test data goes here?",
                                        "Status": 2,
                                    },
                                },
                            ],
                        }
                    ),
                    "utf8",
                )
            )


class ExceptionToStatusInterceptor(ServerInterceptor):
    def intercept(
        self,
        method,
        request,
        context,
        method_name,
    ):
        print(method_name)
        try:
            x = method(request, context)
            print(x)
            return x
        except GrpcException as e:
            print(e)
            print(e.details)
            context.set_code(e.status_code)
            context.set_details(e.details)
            raise


def serve():
    interceptors = [ExceptionToStatusInterceptor()]

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    pb2_grpc.add_SourceServicer_to_server(SourceV1Handler(), server)
    d_pb2_grpc.add_DiscoveryServicer_to_server(DiscoveryV1Handler(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
