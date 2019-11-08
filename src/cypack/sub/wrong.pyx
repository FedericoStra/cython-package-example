from ..utils cimport axpy
from .helper cimport one, three, four


cpdef the_answer():
    "The Answer to the Ultimate Question of Life, The Universe, and Everything."
    return axpy(three, four, one)
