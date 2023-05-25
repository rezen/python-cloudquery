# python-cloudquery
Demonstrates how to interact with cloudquery plugin using python!

**Download a plugin**  
```sh
curl -L -o plugins/hackernews.zip https://github.com/cloudquery/cloudquery/releases/download/plugins-source-hackernews-v1.3.1/hackernews_darwin_arm64.zip
unzip plugins/hackernews.zip
mv plugins/source/hackernews plugins/hackernews
cd plugins && rm -rf source 
rm hackernews.zip
cd ..
./plugins/hackernews serve  --address localhost:7778
```

**Adding new protobuf version**  
```sh
pip3 install grpcio-tools

version=v1
vdir="./cq/$version"
mkdir -p $vdir
curl https://raw.githubusercontent.com/cloudquery/plugin-pb/main/source/$version/source.proto > "${vdir}/source.proto"
python3 -m grpc_tools.protoc --proto_path=$vdir $vdir/source.proto --python_out=$vdir --grpc_python_out=$vdir
sed -i '' "s/import source_pb2/import cq.${version}.source_pb2/" $vdir/source_pb2_grpc.py
```


## Resources
**protobuf**  
- https://www.datadoghq.com/blog/engineering/protobuf-parsing-in-python/
- https://velotio.medium.com/implementing-grpc-in-python-a-step-by-step-guide-e9733871acb0

**debugging**  
```
export GRPC_VERBOSITY=debug
export GRPC_TRACE=executor,api,call
```