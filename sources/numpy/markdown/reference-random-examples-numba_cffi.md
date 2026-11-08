[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/numba_cffi.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/examples/numba_cffi.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/examples/numba_cffi.html)
[2.4](https://numpy.org/doc/2.4/reference/random/examples/numba_cffi.html)
[2.3](https://numpy.org/doc/2.3/reference/random/examples/numba_cffi.html)
[2.2](https://numpy.org/doc/2.2/reference/random/examples/numba_cffi.html)
[2.1](https://numpy.org/doc/2.1/reference/random/examples/numba_cffi.html)
[2.0](https://numpy.org/doc/2.0/reference/random/examples/numba_cffi.html)
[1.26](https://numpy.org/doc/1.26/reference/random/examples/numba_cffi.html)
[1.25](https://numpy.org/doc/1.25/reference/random/examples/numba_cffi.html)
[1.24](https://numpy.org/doc/1.24/reference/random/examples/numba_cffi.html)
[1.23](https://numpy.org/doc/1.23/reference/random/examples/numba_cffi.html)
[1.22](https://numpy.org/doc/1.22/reference/random/examples/numba_cffi.html)
[1.21](https://numpy.org/doc/1.21/reference/random/examples/numba_cffi.html)
[1.20](https://numpy.org/doc/1.20/reference/random/examples/numba_cffi.html)
[1.19](https://numpy.org/doc/1.19/reference/random/examples/numba_cffi.html)
[1.18](https://numpy.org/doc/1.18/reference/random/examples/numba_cffi.html)
[1.17](https://numpy.org/doc/1.17/reference/random/examples/numba_cffi.html)
[1.16](https://numpy.org/doc/1.16/reference/random/examples/numba_cffi.html)
[1.15](https://numpy.org/doc/1.15/reference/random/examples/numba_cffi.html)
[1.14](https://numpy.org/doc/1.14/reference/random/examples/numba_cffi.html)
[1.13](https://numpy.org/doc/1.13/reference/random/examples/numba_cffi.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Extending via Numba and CFFI[#](https://numpy.org/doc/stable/reference/random/examples/numba_cffi.html#extending-via-numba-and-cffi "Link to this heading")

============================================================================================================================================================

r"""
Building the required library in this example requires a source distribution
of NumPy or clone of the NumPy git repository since distributions.c is not
included in binary distributions.

On \*nix, execute in numpy/random/src/distributions

export ${PYTHON\_VERSION}=3.8 # Python version
export PYTHON\_INCLUDE=#path to Python's include folder, usually \\
    ${PYTHON\_HOME}/include/python${PYTHON\_VERSION}m
export NUMPY\_INCLUDE=#path to numpy's include folder, usually \\
    ${PYTHON\_HOME}/lib/python${PYTHON\_VERSION}/site-packages/numpy/\_core/include
gcc -shared -o libdistributions.so -fPIC distributions.c \\
    -I${NUMPY\_INCLUDE} -I${PYTHON\_INCLUDE}
mv libdistributions.so ../../\_examples/numba/

On Windows

rem PYTHON\_HOME and PYTHON\_VERSION are setup dependent, this is an example
set PYTHON\_HOME=c:\\Anaconda
set PYTHON\_VERSION=38
cl.exe /LD .\\distributions.c -DDLL\_EXPORT \\
    -I%PYTHON\_HOME%\\lib\\site-packages\\numpy\\\_core\\include \\
    -I%PYTHON\_HOME%\\include %PYTHON\_HOME%\\libs\\python%PYTHON\_VERSION%.lib
move distributions.dll ../../\_examples/numba/
"""
import os

import numba as nb
from cffi import FFI

import numpy as np
from numpy.random import PCG64

ffi \= FFI()
if os.path.exists('./distributions.dll'):
    lib \= ffi.dlopen('./distributions.dll')
elif os.path.exists('./libdistributions.so'):
    lib \= ffi.dlopen('./libdistributions.so')
else:
    raise RuntimeError('Required DLL/so file was not found.')

ffi.cdef("""
double random\_standard\_normal(void \*bitgen\_state);
""")
x \= PCG64()
xffi \= x.cffi
bit\_generator \= xffi.bit\_generator

random\_standard\_normal \= lib.random\_standard\_normal

def normals(n, bit\_generator):
    out \= np.empty(n)
    for i in range(n):
        out\[i\] \= random\_standard\_normal(bit\_generator)
    return out

normalsj \= nb.jit(normals, nopython\=True)

\# Numba requires a memory address for void \*
\# Can also get address from x.ctypes.bit\_generator.value
bit\_generator\_address \= int(ffi.cast('uintptr\_t', bit\_generator))

norm \= normalsj(1000, bit\_generator\_address)
print(norm\[:12\])

Copy to clipboard