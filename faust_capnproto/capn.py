from typing import Any
from faust.serializers import codecs


class ProtobufSerializer(codecs.Codec):
    def __init__(self, capn_type: Any):
        self.capn_type = capn_type
        super().__init__()

    def _dumps(self, capn_proto: Any) -> bytes:
        """ dump data to byte string """
        return capn_proto.to_bytes_packed()

    def _loads(self, bytestream: bytes) -> Any:
        """ return object from byte stream"""
        return self.capn_type.from_bytes_packed(bytestream)
