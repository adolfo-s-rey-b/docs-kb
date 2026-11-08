[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/cffi.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/examples/cffi.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/examples/cffi.html)
[2.4](https://numpy.org/doc/2.4/reference/random/examples/cffi.html)
[2.3](https://numpy.org/doc/2.3/reference/random/examples/cffi.html)
[2.2](https://numpy.org/doc/2.2/reference/random/examples/cffi.html)
[2.1](https://numpy.org/doc/2.1/reference/random/examples/cffi.html)
[2.0](https://numpy.org/doc/2.0/reference/random/examples/cffi.html)
[1.26](https://numpy.org/doc/1.26/reference/random/examples/cffi.html)
[1.25](https://numpy.org/doc/1.25/reference/random/examples/cffi.html)
[1.24](https://numpy.org/doc/1.24/reference/random/examples/cffi.html)
[1.23](https://numpy.org/doc/1.23/reference/random/examples/cffi.html)
[1.22](https://numpy.org/doc/1.22/reference/random/examples/cffi.html)
[1.21](https://numpy.org/doc/1.21/reference/random/examples/cffi.html)
[1.20](https://numpy.org/doc/1.20/reference/random/examples/cffi.html)
[1.19](https://numpy.org/doc/1.19/reference/random/examples/cffi.html)
[1.18](https://numpy.org/doc/1.18/reference/random/examples/cffi.html)
[1.17](https://numpy.org/doc/1.17/reference/random/examples/cffi.html)
[1.16](https://numpy.org/doc/1.16/reference/random/examples/cffi.html)
[1.15](https://numpy.org/doc/1.15/reference/random/examples/cffi.html)
[1.14](https://numpy.org/doc/1.14/reference/random/examples/cffi.html)
[1.13](https://numpy.org/doc/1.13/reference/random/examples/cffi.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Extending via CFFI[#](https://numpy.org/doc/stable/reference/random/examples/cffi.html#extending-via-cffi "Link to this heading")

==================================================================================================================================

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