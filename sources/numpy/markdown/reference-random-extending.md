[Skip to main content](https://numpy.org/doc/stable/reference/random/extending.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/extending.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/extending.html)
[2.4](https://numpy.org/doc/2.4/reference/random/extending.html)
[2.3](https://numpy.org/doc/2.3/reference/random/extending.html)
[2.2](https://numpy.org/doc/2.2/reference/random/extending.html)
[2.1](https://numpy.org/doc/2.1/reference/random/extending.html)
[2.0](https://numpy.org/doc/2.0/reference/random/extending.html)
[1.26](https://numpy.org/doc/1.26/reference/random/extending.html)
[1.25](https://numpy.org/doc/1.25/reference/random/extending.html)
[1.24](https://numpy.org/doc/1.24/reference/random/extending.html)
[1.23](https://numpy.org/doc/1.23/reference/random/extending.html)
[1.22](https://numpy.org/doc/1.22/reference/random/extending.html)
[1.21](https://numpy.org/doc/1.21/reference/random/extending.html)
[1.20](https://numpy.org/doc/1.20/reference/random/extending.html)
[1.19](https://numpy.org/doc/1.19/reference/random/extending.html)
[1.18](https://numpy.org/doc/1.18/reference/random/extending.html)
[1.17](https://numpy.org/doc/1.17/reference/random/extending.html)
[1.16](https://numpy.org/doc/1.16/reference/random/extending.html)
[1.15](https://numpy.org/doc/1.15/reference/random/extending.html)
[1.14](https://numpy.org/doc/1.14/reference/random/extending.html)
[1.13](https://numpy.org/doc/1.13/reference/random/extending.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Extending[#](https://numpy.org/doc/stable/reference/random/extending.html#extending "Link to this heading")

============================================================================================================

The [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s have been designed to be extendable using standard tools for high-performance Python – numba and Cython. The [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 object can also be used with user-provided [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s as long as these export a small set of required functions.

Numba[#](https://numpy.org/doc/stable/reference/random/extending.html#numba "Link to this heading")

----------------------------------------------------------------------------------------------------

Numba can be used with either [CTypes](https://docs.python.org/3/library/ctypes.html)
 or [CFFI](https://cffi.readthedocs.io/en/stable/overview.html)
. The current iteration of the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s all export a small set of functions through both interfaces.

This example shows how Numba can be used to produce Gaussian samples using a pure Python implementation which is then compiled. The random numbers are provided by `ctypes.next_double`.

from timeit import timeit

import numba as nb

import numpy as np
from numpy.random import PCG64

bit\_gen \= PCG64()
next\_d \= bit\_gen.cffi.next\_double
state\_addr \= bit\_gen.cffi.state\_address

def normals(n, state):
    out \= np.empty(n)
    for i in range((n + 1) // 2):
        x1 \= 2.0 \* next\_d(state) \- 1.0
        x2 \= 2.0 \* next\_d(state) \- 1.0
        r2 \= x1 \* x1 + x2 \* x2
        while r2 \>= 1.0 or r2 \== 0.0:
            x1 \= 2.0 \* next\_d(state) \- 1.0
            x2 \= 2.0 \* next\_d(state) \- 1.0
            r2 \= x1 \* x1 + x2 \* x2
        f \= np.sqrt(\-2.0 \* np.log(r2) / r2)
        out\[2 \* i\] \= f \* x1
        if 2 \* i + 1 < n:
            out\[2 \* i + 1\] \= f \* x2
    return out

\# Compile using Numba
normalsj \= nb.jit(normals, nopython\=True)
\# Must use state address not state with numba
n \= 10000

def numbacall():
    return normalsj(n, state\_addr)

rg \= np.random.Generator(PCG64())

def numpycall():
    return rg.normal(size\=n)

\# Check that the functions work
r1 \= numbacall()
r2 \= numpycall()
assert r1.shape \== (n,)
assert r1.shape \== r2.shape

t1 \= timeit(numbacall, number\=1000)
print(f'{t1:.2f} secs for {n} PCG64 (Numba/PCG64) gaussian randoms')
t2 \= timeit(numpycall, number\=1000)
print(f'{t2:.2f} secs for {n} PCG64 (NumPy/PCG64) gaussian randoms')

Copy to clipboard

Both CTypes and CFFI allow the more complicated distributions to be used directly in Numba after compiling the file distributions.c into a `DLL` or `so`. An example showing the use of a more complicated distribution is in the [Examples](https://numpy.org/doc/stable/reference/random/extending.html#examples)
 section below.

Cython[#](https://numpy.org/doc/stable/reference/random/extending.html#cython "Link to this heading")

------------------------------------------------------------------------------------------------------

Cython can be used to unpack the `PyCapsule` provided by a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
. This example uses [`PCG64`](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64")
 and the example from above. The usual caveats for writing high-performance code using Cython – removing bounds checks and wrap around, providing array alignment information – still apply.

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

Copy to clipboard

The [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 can also be directly accessed using the members of the `bitgen_t` struct.

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

Copy to clipboard

Cython can be used to directly access the functions in `numpy/random/c_distributions.pxd`. This requires linking with the `npyrandom` library located in `numpy/random/lib`.

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

See [Extending numpy.random via Cython](https://numpy.org/doc/stable/reference/random/examples/cython/index.html#extending-cython-example)
 for the complete listings of these examples and a minimal `setup.py` to build the c-extension modules.

CFFI[#](https://numpy.org/doc/stable/reference/random/extending.html#id2 "Link to this heading")

-------------------------------------------------------------------------------------------------

CFFI can be used to directly access the functions in `include/numpy/random/distributions.h`. Some “massaging” of the header file is required:

"""
Use cffi to access any of the underlying C functions from distributions.h
"""
import os

import cffi

import numpy as np

from .parse import parse\_distributions\_h

ffi \= cffi.FFI()

inc\_dir \= os.path.join(np.get\_include(), 'numpy')

\# Basic numpy types
ffi.cdef('''
    typedef intptr\_t npy\_intp;
    typedef unsigned char npy\_bool;

''')

parse\_distributions\_h(ffi, inc\_dir)

Copy to clipboard

Once the header is parsed by `ffi.cdef`, the functions can be accessed directly from the `_generator` shared object, using the [`BitGenerator.cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.cffi.html#numpy.random.BitGenerator.cffi "numpy.random.BitGenerator.cffi")
 interface.

lib \= ffi.dlopen(np.random.\_generator.\_\_file\_\_)

\# Compare the distributions.h random\_standard\_normal\_fill to
\# Generator.standard\_random
bit\_gen \= np.random.PCG64()
rng \= np.random.Generator(bit\_gen)
state \= bit\_gen.state

interface \= rng.bit\_generator.cffi
n \= 100
vals\_cffi \= ffi.new(f'double\[{n}\]')
lib.random\_standard\_normal\_fill(interface.bit\_generator, n, vals\_cffi)

\# reset the state
bit\_gen.state \= state

vals \= rng.standard\_normal(n)

for i in range(n):
    assert vals\[i\] \== vals\_cffi\[i\]

Copy to clipboard

New BitGenerators[#](https://numpy.org/doc/stable/reference/random/extending.html#new-bitgenerators "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 can be used with user-provided [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s. The simplest way to write a new [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 is to examine the pyx file of one of the existing [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s. The key structure that must be provided is the `capsule` which contains a `PyCapsule` to a struct pointer of type `bitgen_t`,

typedef struct bitgen {
  void \*state;
  uint64\_t (\*next\_uint64)(void \*st);
  uint32\_t (\*next\_uint32)(void \*st);
  double (\*next\_double)(void \*st);
  uint64\_t (\*next\_raw)(void \*st);
} bitgen\_t;

Copy to clipboard

which provides 5 pointers. The first is an opaque pointer to the data structure used by the [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
s. The next three are function pointers which return the next 64- and 32-bit unsigned integers, the next random double and the next raw value. This final function is used for testing and so can be set to the next 64-bit unsigned integer function if not needed. Functions inside [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 use this structure as in

bitgen\_state\->next\_uint64(bitgen\_state\->state)

Copy to clipboard

Examples[#](https://numpy.org/doc/stable/reference/random/extending.html#examples "Link to this heading")

----------------------------------------------------------------------------------------------------------

*   [Numba](https://numpy.org/doc/stable/reference/random/examples/numba.html)
    
*   [CFFI + Numba](https://numpy.org/doc/stable/reference/random/examples/numba_cffi.html)
    
*   [Cython](https://numpy.org/doc/stable/reference/random/examples/cython/index.html)
    *   [meson.build](https://numpy.org/doc/stable/reference/random/examples/cython/meson.build.html)
        
    *   [extending.pyx](https://numpy.org/doc/stable/reference/random/examples/cython/extending.pyx.html)
        
    *   [extending\_distributions.pyx](https://numpy.org/doc/stable/reference/random/examples/cython/extending_distributions.pyx.html)
        
*   [CFFI](https://numpy.org/doc/stable/reference/random/examples/cffi.html)
    

On this page