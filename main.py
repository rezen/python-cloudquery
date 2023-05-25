import json
import grpc
import cq.v1.source_pb2 as pb2
import cq.v1.source_pb2_grpc as pb2_grpc

# import cq.discovery.discovery_pb2 as d_pb2
# import cq.discovery.discovery_pb2_grpc as d_pb2_grpc

import cq.types as cq_types


host = "localhost"
server_port = 50051

channel = grpc.insecure_channel("{}:{}".format(host, server_port))
client = pb2_grpc.SourceStub(channel)
# client2 = d_pb2_grpc.DiscoveryStub(channel)

# Get name of plugin
# result = client.GetMetrics(pb2.GetMetrics())
# print(result.metrics)

# result = client2.GetVersions(d_pb2.GetVersions())
# print(result)

# Get name of plugin
# result = client.GetName(pb2.GetName())
# print(result.name)

# Get version of plugin
# result = client.GetVersion(pb2.GetVersion())
# print(result.version)

result = client.GetDynamicTables(pb2.GetDynamicTables())
print(result)
tables = json.loads(result.tables)

# Get names of tables
result = client.GetTables(pb2.GetTables())
print(result)
tables = json.loads(result.tables)
print(json.dumps(tables, indent=True))
for table in tables:
    print(json.dumps(table, indent=True))


# Initialize interaction with plugin
request = pb2.Init.Request(
    spec=bytes(
        json.dumps(
            {
                "version": "v_",
                "name": "_",
                "path": "_",
                "tables": ["*"],
                "destinations": [
                    "sqlite",
                ],
                "spec": {

                },
            }
        ),
        "utf-8",
    )
)

result = client.Init(request)





# Start syncing
result = client.Sync(pb2.Sync())

# Read data ...
for response in result:
    try:
        data = json.loads(response.resource)
    except:
        continue

    print(json.dumps(data, indent=True))
    exit()

