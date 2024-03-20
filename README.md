
# pyballc

[![PyPI version](https://badge.fury.io/py/pyballc.svg)](https://badge.fury.io/py/pyballc)


Pyballc is a python wrapper to read/manipulate BAllC files. It is based on the [BAllCools](https://github.com/jksr/ballcools).


## Dependency
```BAllCools >= 0.9.3``` (https://github.com/jksr/ballcools)

## Installation
**Notice:** You NEED to install BAllCools separately.

**Installing from pypi**
```bash
pip install pyballc
```

**Installing from github**
```shell
git clone https://jksr@github.com/jksr/pyballc
cd pyballc
pip install .
```
or 
```shell
pip install git+https://jksr@github.com/jksr/pyballc
```

## Usage

An example of how to use pyballc

```python
from pyballc import PyBallC
ballcools_folder = ''
## You don't need to add "ballcools" when specifying the installation path
## for example if you call ballcools with "/path/to/ballcools/folder/ballcools" in the shell,
## you can use "ballcpath = '/path/to/ballcools/folder'"
pyballc = PyBAllC(ballcools_folder)

ballc_path = '/path/to/a/ballc/file'
pyballc.query(ballc_path, 'chr1:170000000-175635089')
```
The results will look like
```jupyter
| chr  | pos       | mc | cov |
|------|-----------|----|-----|
| chr1 | 175635056 | 1  | 1   |
| chr1 | 175635058 | 1  | 1   |
| chr1 | 175635071 | 1  | 1   |
| chr1 | 175635088 | 1  | 1   |
| chr1 | 175635089 | 1  | 1   |
```

All ballcools functions (view, query, a2b, b2a, merge, meta, index) are fully supported. 
Usage details of each function can be checked with
```ballcools -h``` in shell

