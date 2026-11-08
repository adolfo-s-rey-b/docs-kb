[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.multi_dot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.multi_dot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.multi_dot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.multi_dot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.multi_dot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.multi_dot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.multi_dot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.multi_dot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.multi_dot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.multi_dot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.multi_dot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.multi_dot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.multi_dot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.multi_dot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.multi_dot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.multi_dot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.multi_dot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.multi_dot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.multi_dot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.multi_dot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.multi\_dot[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy-linalg-multi-dot "Link to this heading")

=======================================================================================================================================================

linalg.multi\_dot(_arrays_, _\*_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2864-L2981)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "Link to this definition")

Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order.

[`multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")
 chains [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
 and uses optimal parenthesization of the matrices [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#r451bed364cc6-1)
 [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#r451bed364cc6-2)
. Depending on the shapes of the matrices, this can speed up the multiplication a lot.

If the first argument is 1-D it is treated as a row vector. If the last argument is 1-D it is treated as a column vector. The other arguments must be 2-D.

Think of [`multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")
 as:

def multi\_dot(arrays): return functools.reduce(np.dot, arrays)

Copy to clipboard

Parameters:

**arrays**sequence of array\_like

If the first argument is 1-D it is treated as row vector. If the last argument is 1-D it is treated as column vector. The other arguments must be 2-D.

**out**ndarray, optional

Output argument. This must have the exact kind that would be returned if it was not used. In particular, it must have the right type, must be C-contiguous, and its dtype must be the dtype that would be returned for _dot(a, b)_. This is a performance feature. Therefore, if these conditions are not met, an exception is raised, instead of attempting to be flexible.

Returns:

**output**ndarray

Returns the dot product of the supplied arrays.

See also

[`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")

dot multiplication with two arguments.

Notes

The cost for a matrix multiplication can be calculated with the following function:

def cost(A, B):
    return A.shape\[0\] \* A.shape\[1\] \* B.shape\[1\]

Copy to clipboard

Assume we have three matrices \\(A\_{10 \\times 100}, B\_{100 \\times 5}, C\_{5 \\times 50}\\).

The costs for the two different parenthesizations are as follows:

cost((AB)C) \= 10\*100\*5 + 10\*5\*50   \= 5000 + 2500   \= 7500
cost(A(BC)) \= 10\*100\*50 + 100\*5\*50 \= 50000 + 25000 \= 75000

Copy to clipboard

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#id1)\
\]

Cormen, “Introduction to Algorithms”, Chapter 15.2, p. 370-378

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#id2)\
\]

[https://en.wikipedia.org/wiki/Matrix\_chain\_multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)

Examples

Try it in your browser!

[`multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")
 allows you to write:

\>>> import numpy as np
\>>> from numpy.linalg import multi\_dot
\>>> \# Prepare some data
\>>> A \= np.random.random((10000, 100))
\>>> B \= np.random.random((100, 1000))
\>>> C \= np.random.random((1000, 5))
\>>> D \= np.random.random((5, 333))
\>>> \# the actual dot multiplication
\>>> \_ \= multi\_dot(\[A, B, C, D\])

Copy to clipboard

instead of:

\>>> \_ \= np.dot(np.dot(np.dot(A, B), C), D)
\>>> \# or
\>>> \_ \= A.dot(B).dot(C).dot(D)

Copy to clipboard

Go BackOpen In Tab

On this page