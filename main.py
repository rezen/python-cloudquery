import json
import grpc
import v.v1.source_pb2 as pb2
import v.v1.source_pb2_grpc as pb2_grpc


host = 'localhost'
server_port = 7778

channel = grpc.insecure_channel('{}:{}'.format(host, server_port))
client = pb2_grpc.SourceStub(channel)

# Get name of plugin
result = client.GetName(pb2.GetName())
print(result.name)

# Get version of plugin
result = client.GetVersion(pb2.GetVersion())
print(result.version)

# Get names of tables
result = client.GetTables(pb2.GetTables())
tables = json.loads(result.tables)

for table in tables:
    print(table)

# Initialize interaction with plugin
request = pb2.Init.Request(spec=bytes(json.dumps({
    "version": "v_",
    "name": "_",
    "path": "_",
    "tables": ["*"],
    "destinations": [
        "sqlite",
    ]
}), 'utf-8'))

result = client.Init(request)

# Start syncing
result = client.Sync(pb2.Sync())

# Read data ...
for response in result:
    try:
        data = json.loads(response.resource)
    except:
        continue

    print(data)
    print()
