from __future__ import annotations

import pathlib
import shelve

from m42pl.kvstores import KVStore

from typing import Any


class LocalKVStore(KVStore):
    """A simplisitc and temporary KVStore implementation.
    
    This KVSotre exists only during a pipeline execution and does not
    preserve its state once destroyed.
    """

    _aliases_ = ['local', 'shelve']

    def __init__(self, path: None|str = None, *args, **kwargs):
        """
        :param path:    KVStore shelf path
        """
        super().__init__(path, *args, **kwargs)
        self.path = str(pathlib.Path(path or '~/.m42pl_kvstore').expanduser().absolute())
        self.shelve = None
    
    async def __aenter__(self):
        # Try to open in read+write+create
        try:
            self.logger.info('attempting to open shelve')
            self.shelve = shelve.open(self.path, flag='c')
        # Retry to open in read only
        except Exception:
            try:
                self.logger.info('attempting to open shelve in read-only mode')
                self.shelve = self.shelve(self.path, flag='r')
            except Exception:
                raise
        self.logger.info(f'shelve opened')
        return self

    async def __aexit__(self, *args, **kwargs):
        try:
            self.logger.info('closing shelve')
            self.shelve.close()
            self.logger.info(f'shelve closed')
        except Exception as error:
            self.logger.warn(f'failed to close shelve: {str(error)}')
            self.logger.exception(error)

    async def read(self, key: str, default: Any = None) -> Any:
        try:
            return self.shelve[key]
        except KeyError:
            return default
    
    async def write(self, key: str, value: Any = None) -> None:
        self.shelve[key] = value

    async def remove(self, key: str = None, default: Any = None) -> Any:
        try:
            del self.shelve[key]
        except Exception:
            pass
        return default
