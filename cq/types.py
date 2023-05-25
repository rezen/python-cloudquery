import struct
from uuid import UUID
import pyarrow as pa

# https://github.com/cloudquery/cq-provider-sdk/blob/main/provider/schema/column.go#L69
CQ_TYPE_MAP = {
    "TypeInvalid": 0,
    "TypeBool": 1,
    "TypeInt": 2,
    "TypeFloat": 3,
    "TypeUUID": 4,
    "TypeString": 5,
    "TypeByteArray": 6,
    "TypeStringArray": 7,
    "TypeIntArray": 8,
    "TypeTimestamp": 9,
    "TypeJSON": 10,
    "TypeUUIDArray": 11,
    "TypeInet": 12,
    "TypeInetArray": 13,
    "TypeCIDR": 14,
    "TypeCIDRArray": 15,
    "TypeMacAddr": 16,
    "TypeMacAddrArray": 17,
    "TypeTimeIntervalDeprecated": 18,
    "TypeEnd": 19,
}

# https://github.com/apache/arrow/blob/main/go/arrow/datatype.go
ARROW_TYPE_MAP = {
    "null": pa.null(),
    "bool": pa.bool_(),
    "int8": pa.int8(),
    "int16": pa.int16(),
    "int32": pa.int32(),
    "int64": pa.int64(),
    "uint8": pa.uint8(),
    "uint16": pa.uint16(),
    "uint32": pa.uint32(),
    "uint64": pa.uint64(),
    "float16": pa.float16(),
    "float32": pa.float32(),
    "float64": pa.float64(),
    "time32": pa.time32("s"),
    "time64": pa.time64("ns"),
    "timestamp": pa.timestamp("s"),
    "date32": pa.date32(),
    "date64": pa.date64(),
    "duration": pa.duration("s"),
    "month_day_nano_interval": pa.month_day_nano_interval(),
    "binary": pa.binary(),
    "string": pa.string(),
    "utf8": pa.utf8(),
    "large_binary": pa.large_binary(),
    "large_string": pa.large_string(),
    "large_utf8": pa.large_utf8(),
    "decimal128": pa.decimal128(2),
    "list": pa.list_(pa.string()),
    "large_list": pa.large_list(pa.string()),
    "map": pa.map_(pa.string(), pa.string()),
    "dictionary": pa.dictionary(pa.int8(), pa.string()),
    # "run_end_encoded": pa.run_end_encoded(pa.int16(), pa.int16()),
}

ARROW_ID_TO_LABEL = {ARROW_TYPE_MAP[k].id: k for k in ARROW_TYPE_MAP}


def to_bytes_array(val):
    if isinstance(val, str):
        val = bytes(val, "utf8")

    ints = struct.unpack("B" * len(val), val)
    return list(ints)


def from_bytes_array(val):
    return struct.pack("B" * len(val), *val)


SCHEMA_PRESENT = 2
SCHEMA_OTHER = 1


def cq_serialize(val):
    if isinstance(val, str):
        return {
            "type": "Text",
            "value": {"Str": val, "Status": SCHEMA_PRESENT},
        }
    elif isinstance(val, bool):
        return {
            "type": "Bool",
            "value": {"Bool": val, "Status": SCHEMA_PRESENT},
        }
    elif isinstance(val, dict):
        return {
            "type": "JSON",
            "value": {"Bytes": to_bytes_array(val), "Status": SCHEMA_PRESENT},
        }
    elif isinstance(val, UUID):
        return {
            "type": "UUID",
            "value": {"Bytes": to_bytes_array(val.bytes), "Status": SCHEMA_PRESENT},
        }
    elif isinstance(val, list):
        return {
            "type": "TextArray",
            "value": {
                "Elements": [{"Str": v, "Status": SCHEMA_PRESENT} for v in val],
                "Status": SCHEMA_PRESENT,
            },
        }
    return {
        "type": str(type(val)),
        "value": {
            "Status": SCHEMA_PRESENT,
        },
    }

