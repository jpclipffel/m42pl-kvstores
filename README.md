# M42PL - Key/value stores

Core [M42PL] key/value stores.

## What are M42PL dispatchers ?

M42PL KVStore read and write key/value pairs from a KVStore (e.g. Redis).
As other M42PL components, multiples KVStore backend are supported.

## Dispatchers list

| Aliases | Class   | Module      | Description                   | Status |
|---------|---------|-------------|-------------------------------|--------|
| `local` | `Local` | `local.py`  | Use a local `dict` as backend | Alpha  |
| `redis` | `Redis` | `_redis.py` | Use Redis as backend          | Alpha  |

## Installation

```Bash
git clone https://github.com/jpclipffel/m42pl-kvstores
pip install -e m42pl-kvstores
```

## Usage

One can select the dispatcher to use with the `-k` or `--kvstore` parameter
when calling `m42pl`.

Examples to use the `redis` dispatcher:

* To run a pipeline: `m42pl -k redis run <path/to/pipeline.mpl>`
* In a REPL: `m42pl -k redis repl`

---

[M42PL]: https://github.com/jpclipffel/m42pl-core
