[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/cython/extending.pyx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

extending.pyx[#](https://numpy.org/doc/stable/reference/random/examples/cython/extending.pyx.html#extending-pyx "Link to this heading")

========================================================================================================================================

#cython: language\_level=3

from libc.stdint cimport uint32\_t
from cpython.pycapsule cimport PyCapsule\_IsValid, PyCapsule\_GetPointer

import numpy as np
cimport numpy as np
cimport cython

from numpy.random cimport bitgen\_t
from numpy.random import PCG64

np.import\_array()

@cython.boundscheck(False)
@cython.wraparound(False)
def uniform\_mean(Py\_ssize\_t n):
    cdef Py\_ssize\_t i
    cdef bitgen\_t \*rng
    cdef const char \*capsule\_name \= "BitGenerator"
    cdef double\[::1\] random\_values
    cdef np.ndarray randoms

    x \= PCG64()
    capsule \= x.capsule
    if not PyCapsule\_IsValid(capsule, capsule\_name):
        raise ValueError("Invalid pointer to anon\_func\_state")
    rng \= <bitgen\_t \*> PyCapsule\_GetPointer(capsule, capsule\_name)
    random\_values \= np.empty(n)
    \# Best practice is to acquire the lock whenever generating random values.
    \# This prevents other threads from modifying the state. Acquiring the lock
    \# is only necessary if the GIL is also released, as in this example.
    with x.lock, nogil:
        for i in range(n):
            random\_values\[i\] \= rng.next\_double(rng.state)
    randoms \= np.asarray(random\_values)
    return randoms.mean()

\# This function is declared nogil so it can be used without the GIL below
cdef uint32\_t bounded\_uint(uint32\_t lb, uint32\_t ub, bitgen\_t \*rng) nogil:
    cdef uint32\_t mask, delta, val
    mask \= delta \= ub \- lb
    mask |= mask \>> 1
    mask |= mask \>> 2
    mask |= mask \>> 4
    mask |= mask \>> 8
    mask |= mask \>> 16

    val \= rng.next\_uint32(rng.state) & mask
    while val \> delta:
        val \= rng.next\_uint32(rng.state) & mask

    return lb + val

@cython.boundscheck(False)
@cython.wraparound(False)
def bounded\_uints(uint32\_t lb, uint32\_t ub, Py\_ssize\_t n):
    cdef Py\_ssize\_t i
    cdef bitgen\_t \*rng
    cdef uint32\_t\[::1\] out
    cdef const char \*capsule\_name \= "BitGenerator"

    x \= PCG64()
    out \= np.empty(n, dtype\=np.uint32)
    capsule \= x.capsule

    if not PyCapsule\_IsValid(capsule, capsule\_name):
        raise ValueError("Invalid pointer to anon\_func\_state")
    rng \= <bitgen\_t \*>PyCapsule\_GetPointer(capsule, capsule\_name)

    with x.lock, nogil:
        for i in range(n):
            out\[i\] \= bounded\_uint(lb, ub, rng)
    return np.asarray(out)

Copy to clipboard