[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/numba.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/examples/numba.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/examples/numba.html)
[2.4](https://numpy.org/doc/2.4/reference/random/examples/numba.html)
[2.3](https://numpy.org/doc/2.3/reference/random/examples/numba.html)
[2.2](https://numpy.org/doc/2.2/reference/random/examples/numba.html)
[2.1](https://numpy.org/doc/2.1/reference/random/examples/numba.html)
[2.0](https://numpy.org/doc/2.0/reference/random/examples/numba.html)
[1.26](https://numpy.org/doc/1.26/reference/random/examples/numba.html)
[1.25](https://numpy.org/doc/1.25/reference/random/examples/numba.html)
[1.24](https://numpy.org/doc/1.24/reference/random/examples/numba.html)
[1.23](https://numpy.org/doc/1.23/reference/random/examples/numba.html)
[1.22](https://numpy.org/doc/1.22/reference/random/examples/numba.html)
[1.21](https://numpy.org/doc/1.21/reference/random/examples/numba.html)
[1.20](https://numpy.org/doc/1.20/reference/random/examples/numba.html)
[1.19](https://numpy.org/doc/1.19/reference/random/examples/numba.html)
[1.18](https://numpy.org/doc/1.18/reference/random/examples/numba.html)
[1.17](https://numpy.org/doc/1.17/reference/random/examples/numba.html)
[1.16](https://numpy.org/doc/1.16/reference/random/examples/numba.html)
[1.15](https://numpy.org/doc/1.15/reference/random/examples/numba.html)
[1.14](https://numpy.org/doc/1.14/reference/random/examples/numba.html)
[1.13](https://numpy.org/doc/1.13/reference/random/examples/numba.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Extending via Numba[#](https://numpy.org/doc/stable/reference/random/examples/numba.html#extending-via-numba "Link to this heading")

=====================================================================================================================================

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

\# example 2

next\_u32 \= bit\_gen.ctypes.next\_uint32
ctypes\_state \= bit\_gen.ctypes.state

@nb.jit(nopython\=True)
def bounded\_uint(lb, ub, state):
    mask \= delta \= ub \- lb
    mask |= mask \>> 1
    mask |= mask \>> 2
    mask |= mask \>> 4
    mask |= mask \>> 8
    mask |= mask \>> 16

    val \= next\_u32(state) & mask
    while val \> delta:
        val \= next\_u32(state) & mask

    return lb + val

print(bounded\_uint(323, 2394691, ctypes\_state.value))

@nb.jit(nopython\=True)
def bounded\_uints(lb, ub, n, state):
    out \= np.empty(n, dtype\=np.uint32)
    for i in range(n):
        out\[i\] \= bounded\_uint(lb, ub, state)

bounded\_uints(323, 2394691, 10000000, ctypes\_state.value)

Copy to clipboard