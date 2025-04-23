from .utils cimport axpy

import importlib.resources
import hashlib

cpdef the_answer():
    "The Answer to the Ultimate Question of Life, The Universe, and Everything."
    return axpy(4, 10, 2)


def zen_hash():
    zen = importlib.resources.read_binary("cypack.data", "zen.txt")
    return hashlib.md5(zen).hexdigest()
