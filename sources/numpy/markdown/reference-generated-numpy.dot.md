[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dot[#](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy-dot "Link to this heading")

===============================================================================================================

numpy.dot(_a_, _b_, _out\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "Link to this definition")

Dot product of two arrays. Specifically,

*   If both _a_ and _b_ are 1-D arrays, it is inner product of vectors (without complex conjugation).
    
*   If both _a_ and _b_ are 2-D arrays, it is matrix multiplication, but using [`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
     or `a @ b` is preferred.
    
*   If either _a_ or _b_ is 0-D (scalar), it is equivalent to [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html#numpy.multiply "numpy.multiply")
     and using `numpy.multiply(a, b)` or `a * b` is preferred.
    
*   If _a_ is an N-D array and _b_ is a 1-D array, it is a sum product over the last axis of _a_ and _b_.
    
*   If _a_ is an N-D array and _b_ is an M-D array (where `M>=2`), it is a sum product over the last axis of _a_ and the second-to-last axis of _b_:
    
    dot(a, b)\[i,j,k,m\] \= sum(a\[i,j,:\] \* b\[k,:,m\])
    
    Copy to clipboard
    

It uses an optimized BLAS library when possible (see [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
).

Parameters:

**a**array\_like

First argument.

**b**array\_like

Second argument.

**out**ndarray, optional

Output argument. This must have the exact kind that would be returned if it was not used. In particular, it must have the right type, must be C-contiguous, and its dtype must be the dtype that would be returned for _dot(a,b)_. This is a performance feature. Therefore, if these conditions are not met, an exception is raised, instead of attempting to be flexible.

Returns:

**output**ndarray

Returns the dot product of _a_ and _b_. If _a_ and _b_ are both scalars or both 1-D arrays then a scalar is returned; otherwise an array is returned. If _out_ is given, then it is returned.

Raises:

ValueError

If the last dimension of _a_ is not the same size as the second-to-last dimension of _b_.

See also

[`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")

Complex-conjugating dot product.

[`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Vector dot product of two arrays.

[`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")

Sum products over arbitrary axes.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

[`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")

‘@’ operator as method with out parameter.

[`linalg.multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")

Chained dot product.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.dot(3, 4)
12

Copy to clipboard

Neither argument is complex-conjugated:

\>>> np.dot(\[2j, 3j\], \[2j, 3j\])
(-13+0j)

Copy to clipboard

For 2-D arrays it is the matrix product:

\>>> a \= \[\[1, 0\], \[0, 1\]\]
\>>> b \= \[\[4, 1\], \[2, 2\]\]
\>>> np.dot(a, b)
array(\[\[4, 1\],\
       \[2, 2\]\])

Copy to clipboard

\>>> a \= np.arange(3\*4\*5\*6).reshape((3,4,5,6))
\>>> b \= np.arange(3\*4\*5\*6)\[::\-1\].reshape((5,4,6,3))
\>>> np.dot(a, b)\[2,3,2,1,2,2\]
499128
\>>> sum(a\[2,3,2,:\] \* b\[1,2,:,2\])
499128

Copy to clipboard

Go BackOpen In Tab

On this page