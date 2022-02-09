Cython package example
======================

Purpose
-------

The purpose of this package is to demonstrate how to organize a project developed using Cython.
It shows a suitable folder structure according to the best practices, how to create extension modules with Cython, how to implement functions in C and make them available to Cython, how to include package data, how to write a `setup.py` script that allows users without Cython to install the package nonetheless.

Installation
------------

### From a repository checkout

```bash
make install
```
or
```bash
CYTHONIZE=1 pip install --user .
```

### From PyPi

```bash
pip install --user cython-package-example
```
