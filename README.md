# Angel

#### Usage

Before you run `angel` for the first time, you must install the required libraries.

```
$ pip install -r requirements.txt
```


`angel` takes a single file as an argument. This file should be a JSON representation of a job candidate. See [`sample.json`](sample.json) for an example.

```
Usage: angel.py [OPTIONS] INPUT

Options:
  --pretty / --no-pretty  Pretty print output.
  --help                  Show this message and exit.
```