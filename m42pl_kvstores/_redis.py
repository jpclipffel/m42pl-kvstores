import aioredis
import msgpack

from typing import Any

from m42pl.kvstores import KVStore


class Redis(KVStore):
    """A Redis-backed KVStore implementation.
    """

    _aliases_ = ['redis',]

    def __init__(self, url: str = 'redis://127.0.0.1:6379',
                    prefix: str = 'm42pl.', *args, **kwargs):
        """
        :param url:     Redis URL
        :param prefix:  Redis keys prefix; Default to 'm42pl.'
        """
        super().__init__(url, prefix, *args, **kwargs)
        self.url = url
        self.prefix = prefix
        self.collections = {}
        self.redis = None

    def make_key(self, key: str):
        return f'{self.prefix}{key}'

    async def __aenter__(self):
        self.redis = await aioredis.create_redis_pool(self.url)
        return self

    async def __aexit__(self, *args, **kwargs):
        if self.redis is not None:
            self.redis.close()
            await self.redis.wait_closed()

    async def read(self, key: str = None, default: Any = None) -> Any:
        try:
            return msgpack.unpackb(
                await self.redis.get(self.make_key(key))
            )
        except Exception:
            return default
    
    async def write(self, key: str, value: Any = None) -> None:
        await self.redis.set(
            self.make_key(key),
            msgpack.packb(value or '')
        )
