from .utils cimport axpy

import pkg_resources
import hashlib

cpdef the_answer():
    "The Answer to the Ultimate Question of Life, The Universe, and Everything."
    return axpy(4, 10, 2)


def zen_hash():
    zen = pkg_resources.resource_string("cypack", "data/zen.txt")
    return hashlib.md5(zen).hexdigest()
