# M42PL - Key/value stores

M42PL KVStores read and write key/value pairs from a KVStore (e.g. Redis).
As other M42PL components, multiples KVStore backends are supported.

## Installation

```Bash
git clone https://github.com/jpclipffel/m42pl-kvstores
pip install -e m42pl-kvstores
```

## Usage

One can select the dispatcher to use with the `-k` or `--kvstore` parameter
when calling `m42pl`.

One can pass arguments to the KVStore using `--kvstore-kwargs`

Examples to use the `redis` KVStore:

* To run a pipeline: `m42pl run -k redis <path/to/pipeline.mpl>`
* In a REPL: `m42pl repl -k redis`
* REPL with custom arguments: `m42pl repl -k redis --kvstore-kwargs '{"url": "redis://127.0.0.1:6379"}'`

## KVStores list

| Aliases | Module      | Description                     |
|---------|-------------|---------------------------------|
| `local` | `local.py`  | Use a local `Shelve` as backend |
| `redis` | `_redis.py` | Use Redis as backend            |

### `local`

This KVStore uses a Python's `Shelve`.
As a `Shelve` does not support concurrent access, one may **not** use it
with a multiprocessing dispatcher such as `mpi`.

| Argument | Required | Default            | Description                |
|----------|----------|--------------------|----------------------------|
| `path`   | No       | `~/.m42pl_kvstore` | Path to the KVStore shelve |

### `redis`

This KVStore uses a Redis server.

| Argument | Required | Default                  | Description           |
|----------|----------|--------------------------|-----------------------|
| `url`    | No       | `redis://127.0.0.1:6379` | Redis server URL      |
| `prefix` | No       | `m42pl.`                 | KVStore's keys prefix |

---

[M42PL]: https://github.com/jpclipffel/m42pl-core
