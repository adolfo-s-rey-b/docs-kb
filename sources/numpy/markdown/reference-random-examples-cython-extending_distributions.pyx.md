[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/cython/extending_distributions.pyx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/examples/cython/extending_distributions.pyx.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/examples/cython/extending_distributions.pyx.html)
[2.4](https://numpy.org/doc/2.4/reference/random/examples/cython/extending_distributions.pyx.html)
[2.3](https://numpy.org/doc/2.3/reference/random/examples/cython/extending_distributions.pyx.html)
[2.2](https://numpy.org/doc/2.2/reference/random/examples/cython/extending_distributions.pyx.html)
[2.1](https://numpy.org/doc/2.1/reference/random/examples/cython/extending_distributions.pyx.html)
[2.0](https://numpy.org/doc/2.0/reference/random/examples/cython/extending_distributions.pyx.html)
[1.26](https://numpy.org/doc/1.26/reference/random/examples/cython/extending_distributions.pyx.html)
[1.25](https://numpy.org/doc/1.25/reference/random/examples/cython/extending_distributions.pyx.html)
[1.24](https://numpy.org/doc/1.24/reference/random/examples/cython/extending_distributions.pyx.html)
[1.23](https://numpy.org/doc/1.23/reference/random/examples/cython/extending_distributions.pyx.html)
[1.22](https://numpy.org/doc/1.22/reference/random/examples/cython/extending_distributions.pyx.html)
[1.21](https://numpy.org/doc/1.21/reference/random/examples/cython/extending_distributions.pyx.html)
[1.20](https://numpy.org/doc/1.20/reference/random/examples/cython/extending_distributions.pyx.html)
[1.19](https://numpy.org/doc/1.19/reference/random/examples/cython/extending_distributions.pyx.html)
[1.18](https://numpy.org/doc/1.18/reference/random/examples/cython/extending_distributions.pyx.html)
[1.17](https://numpy.org/doc/1.17/reference/random/examples/cython/extending_distributions.pyx.html)
[1.16](https://numpy.org/doc/1.16/reference/random/examples/cython/extending_distributions.pyx.html)
[1.15](https://numpy.org/doc/1.15/reference/random/examples/cython/extending_distributions.pyx.html)
[1.14](https://numpy.org/doc/1.14/reference/random/examples/cython/extending_distributions.pyx.html)
[1.13](https://numpy.org/doc/1.13/reference/random/examples/cython/extending_distributions.pyx.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

extending\_distributions.pyx[#](https://numpy.org/doc/stable/reference/random/examples/cython/extending_distributions.pyx.html#extending-distributions-pyx "Link to this heading")

===================================================================================================================================================================================

#cython: language\_level=3
"""
This file shows how the to use a BitGenerator to create a distribution.
"""
import numpy as np
cimport numpy as np
cimport cython
from cpython.pycapsule cimport PyCapsule\_IsValid, PyCapsule\_GetPointer
from libc.stdint cimport uint16\_t, uint64\_t
from numpy.random cimport bitgen\_t
from numpy.random import PCG64
from numpy.random.c\_distributions cimport (
      random\_standard\_uniform\_fill, random\_standard\_uniform\_fill\_f)

np.import\_array()

@cython.boundscheck(False)
@cython.wraparound(False)
def uniforms(Py\_ssize\_t n):
    """
    Create an array of \`n\` uniformly distributed doubles.
    A 'real' distribution would want to process the values into
    some non-uniform distribution
    """
    cdef Py\_ssize\_t i
    cdef bitgen\_t \*rng
    cdef const char \*capsule\_name \= "BitGenerator"
    cdef double\[::1\] random\_values

    x \= PCG64()
    capsule \= x.capsule
    \# Optional check that the capsule if from a BitGenerator
    if not PyCapsule\_IsValid(capsule, capsule\_name):
        raise ValueError("Invalid pointer to anon\_func\_state")
    \# Cast the pointer
    rng \= <bitgen\_t \*> PyCapsule\_GetPointer(capsule, capsule\_name)
    random\_values \= np.empty(n, dtype\='float64')
    with x.lock, nogil:
        for i in range(n):
            \# Call the function
            random\_values\[i\] \= rng.next\_double(rng.state)
    randoms \= np.asarray(random\_values)

    return randoms

\# cython example 2
@cython.boundscheck(False)
@cython.wraparound(False)
def uint10\_uniforms(Py\_ssize\_t n):
    """Uniform 10 bit integers stored as 16-bit unsigned integers"""
    cdef Py\_ssize\_t i
    cdef bitgen\_t \*rng
    cdef const char \*capsule\_name \= "BitGenerator"
    cdef uint16\_t\[::1\] random\_values
    cdef int bits\_remaining
    cdef int width \= 10
    cdef uint64\_t buff, mask \= 0x3FF

    x \= PCG64()
    capsule \= x.capsule
    if not PyCapsule\_IsValid(capsule, capsule\_name):
        raise ValueError("Invalid pointer to anon\_func\_state")
    rng \= <bitgen\_t \*> PyCapsule\_GetPointer(capsule, capsule\_name)
    random\_values \= np.empty(n, dtype\='uint16')
    \# Best practice is to release GIL and acquire the lock
    bits\_remaining \= 0
    with x.lock, nogil:
        for i in range(n):
            if bits\_remaining < width:
                buff \= rng.next\_uint64(rng.state)
            random\_values\[i\] \= buff & mask
            buff \>>= width

    randoms \= np.asarray(random\_values)
    return randoms

\# cython example 3
def uniforms\_ex(bit\_generator, Py\_ssize\_t n, dtype\=np.float64):
    """
    Create an array of \`n\` uniformly distributed doubles via a "fill" function.

    A 'real' distribution would want to process the values into
    some non-uniform distribution

    Parameters
    ----------
    bit\_generator: BitGenerator instance
    n: int
        Output vector length
    dtype: {str, dtype}, optional
        Desired dtype, either 'd' (or 'float64') or 'f' (or 'float32'). The
        default dtype value is 'd'
    """
    cdef bitgen\_t \*rng
    cdef const char \*capsule\_name \= "BitGenerator"
    cdef np.ndarray randoms

    capsule \= bit\_generator.capsule
    \# Optional check that the capsule if from a BitGenerator
    if not PyCapsule\_IsValid(capsule, capsule\_name):
        raise ValueError("Invalid pointer to anon\_func\_state")
    \# Cast the pointer
    rng \= <bitgen\_t \*> PyCapsule\_GetPointer(capsule, capsule\_name)

    \_dtype \= np.dtype(dtype)
    randoms \= np.empty(n, dtype\=\_dtype)
    if \_dtype \== np.float32:
        with bit\_generator.lock:
            random\_standard\_uniform\_fill\_f(rng, n, <float\*>np.PyArray\_DATA(randoms))
    elif \_dtype \== np.float64:
        with bit\_generator.lock:
            random\_standard\_uniform\_fill(rng, n, <double\*>np.PyArray\_DATA(randoms))
    else:
        raise TypeError('Unsupported dtype %r for random' % \_dtype)
    return randoms

Copy to clipboard