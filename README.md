# M42PL - Key/value stores

M42PL KVStores read and write key/value pairs from a KVStore (e.g. Redis).
As other M42PL components, multiples KVStore backends are supported.

## Installation

```Bash
git clone https://github.com/jpclipffel/m42pl-kvstores
pip install -e m42pl-kvstores
```

## KVStores list

| Aliases | Module      | Description                   |
|---------|-------------|-------------------------------|
| `local` | `local.py`  | Use a local `dict` as backend |
| `redis` | `_redis.py` | Use Redis as backend          |

## Usage

One can select the dispatcher to use with the `-k` or `--kvstore` parameter
when calling `m42pl`.

Examples to use the `redis` dispatcher:

* To run a pipeline: `m42pl -k redis run <path/to/pipeline.mpl>`
* In a REPL: `m42pl -k redis repl`

---

[M42PL]: https://github.com/jpclipffel/m42pl-core
