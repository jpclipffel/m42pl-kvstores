from __future__ import annotations

import pathlib
import shelve

from m42pl.kvstores import KVStore

from typing import Any


class LocalKVStore(KVStore):
    """A fake KVStore.

    This KVStore never write anything and read nothing.
    To be usde for debug purposes.
    """

    _aliases_ = ['fake',]

    def __init__(self, *args, **kwargs):
        """
        :param path:    KVStore shelf path
        """
        super().__init__(*args, **kwargs)
