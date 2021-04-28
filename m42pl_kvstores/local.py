from m42pl.kvstores import KVStore

from typing import Any


class LocalKVStore(KVStore):
    """A simplisitc and temporary KVStore implementation.
    
    This KVSotre exists only during a pipeline execution and does not
    preserve its state once destroyed.
    """

    _aliases_ = ['local',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kvs = {}
    
    async def read(self, key: str, default: Any = None) -> Any:
        return self.kvs.get(key, default)
    
    async def write(self, key: str, value: Any = None) -> None:
        self.kvs[key] = value

    async def delete(self, key: str = None, default: Any = None) -> Any:
        return self.kvs.pop(key, default)
