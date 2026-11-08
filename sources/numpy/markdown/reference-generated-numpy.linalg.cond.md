[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.cond.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.cond.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.cond.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.cond.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.cond.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.cond.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.cond.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.cond.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.cond.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.cond.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.cond.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.cond.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.cond.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.cond.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.cond.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.cond.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.cond.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.cond.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.cond.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.cond.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.cond[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#numpy-linalg-cond "Link to this heading")

=======================================================================================================================================

linalg.cond(_x_, _p\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1913-L2027)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond "Link to this definition")

Compute the condition number of a matrix.

This function is capable of returning the condition number using one of seven different norms, depending on the value of _p_ (see Parameters below).

Parameters:

**x**(…, M, N) array\_like

The matrix whose condition number is sought.

**p**{None, 1, -1, 2, -2, inf, -inf, ‘fro’}, optional

Order of the norm used in the condition number computation:

| p   | norm for matrices |
| --- | --- |
| None | 2-norm, computed directly using the `SVD` |
| ‘fro’ | Frobenius norm |
| inf | max(sum(abs(x), axis=1)) |
| \-inf | min(sum(abs(x), axis=1)) |
| 1   | max(sum(abs(x), axis=0)) |
| \-1 | min(sum(abs(x), axis=0)) |
| 2   | 2-norm (largest sing. value) |
| \-2 | smallest singular value |

inf means the [`numpy.inf`](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")
 object, and the Frobenius norm is the root-of-sum-of-squares norm.

Returns:

**c**{float, inf}

The condition number of the matrix. May be infinite.

See also

[`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")

Notes

The condition number of _x_ is defined as the norm of _x_ times the norm of the inverse of _x_ [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#r611900c44d60-1)
; the norm can be the usual L2-norm (root-of-sum-of-squares) or one of a number of other matrix norms.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#id1)\
\]

G. Strang, _Linear Algebra and Its Applications_, Orlando, FL, Academic Press, Inc., 1980, pg. 285.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy import linalg as LA
\>>> a \= np.array(\[\[1, 0, \-1\], \[0, 1, 0\], \[1, 0, 1\]\])
\>>> a
array(\[\[ 1,  0, -1\],\
       \[ 0,  1,  0\],\
       \[ 1,  0,  1\]\])
\>>> LA.cond(a)
1.4142135623730951
\>>> LA.cond(a, 'fro')
3.1622776601683795
\>>> LA.cond(a, np.inf)
2.0
\>>> LA.cond(a, \-np.inf)
1.0
\>>> LA.cond(a, 1)
2.0
\>>> LA.cond(a, \-1)
1.0
\>>> LA.cond(a, 2)
1.4142135623730951
\>>> LA.cond(a, \-2)
0.70710678118654746 # may vary
\>>> (min(LA.svd(a, compute\_uv\=False)) \*
... min(LA.svd(LA.inv(a), compute\_uv\=False)))
0.70710678118654746 # may vary

Copy to clipboard

Go BackOpen In Tab

On this page