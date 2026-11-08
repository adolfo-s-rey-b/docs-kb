[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.inv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.inv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.inv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.inv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.inv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.inv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.inv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.inv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.inv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.inv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.inv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.inv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.inv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.inv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.inv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.inv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.inv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.inv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.inv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.inv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.inv[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#numpy-linalg-inv "Link to this heading")

====================================================================================================================================

linalg.inv(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L547-L660)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv "Link to this definition")

Compute the inverse of a matrix.

Given a square matrix _a_, return the matrix _ainv_ satisfying `a @ ainv = ainv @ a = eye(a.shape[0])`.

Parameters:

**a**(…, M, M) array\_like

Matrix to be inverted.

Returns:

**ainv**(…, M, M) ndarray or matrix

Inverse of the matrix _a_.

Raises:

LinAlgError

If _a_ is not square or inversion fails.

See also

[`scipy.linalg.inv`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "(in SciPy v1.18.0)")

Similar function in SciPy.

[`numpy.linalg.cond`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond "numpy.linalg.cond")

Compute the condition number of a matrix.

[`numpy.linalg.svd`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd "numpy.linalg.svd")

Compute the singular value decomposition of a matrix.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

If _a_ is detected to be singular, a [`LinAlgError`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy.linalg.LinAlgError "numpy.linalg.LinAlgError")
 is raised. If _a_ is ill-conditioned, a [`LinAlgError`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy.linalg.LinAlgError "numpy.linalg.LinAlgError")
 may or may not be raised, and results may be inaccurate due to floating-point errors.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#id2)\
\]

Wikipedia, “Condition number”, [https://en.wikipedia.org/wiki/Condition\_number](https://en.wikipedia.org/wiki/Condition_number)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.linalg import inv
\>>> a \= np.array(\[\[1., 2.\], \[3., 4.\]\])
\>>> ainv \= inv(a)
\>>> np.allclose(a @ ainv, np.eye(2))
True
\>>> np.allclose(ainv @ a, np.eye(2))
True

Copy to clipboard

If a is a matrix object, then the return value is a matrix as well:

\>>> ainv \= inv(np.matrix(a))
\>>> ainv
matrix(\[\[-2. ,  1. \],\
        \[ 1.5, -0.5\]\])

Copy to clipboard

Inverses of several matrices can be computed at once:

\>>> a \= np.array(\[\[\[1., 2.\], \[3., 4.\]\], \[\[1, 3\], \[3, 5\]\]\])
\>>> inv(a)
array(\[\[\[-2.  ,  1.  \],\
        \[ 1.5 , -0.5 \]\],\
       \[\[-1.25,  0.75\],\
        \[ 0.75, -0.25\]\]\])

Copy to clipboard

If a matrix is close to singular, the computed inverse may not satisfy `a @ ainv = ainv @ a = eye(a.shape[0])` even if a [`LinAlgError`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy.linalg.LinAlgError "numpy.linalg.LinAlgError")
 is not raised:

\>>> a \= np.array(\[\[2,4,6\],\[2,0,2\],\[6,8,14\]\])
\>>> inv(a)  \# No errors raised
array(\[\[-1.12589991e+15, -5.62949953e+14,  5.62949953e+14\],\
   \[-1.12589991e+15, -5.62949953e+14,  5.62949953e+14\],\
   \[ 1.12589991e+15,  5.62949953e+14, -5.62949953e+14\]\])
\>>> a @ inv(a)
array(\[\[ 0.   , -0.5  ,  0.   \],  # may vary\
       \[-0.5  ,  0.625,  0.25 \],\
       \[ 0.   ,  0.   ,  1.   \]\])

Copy to clipboard

To detect ill-conditioned matrices, you can use [`numpy.linalg.cond`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond "numpy.linalg.cond")
 to compute its _condition number_ [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#r02f022d4b0fe-1)
. The larger the condition number, the more ill-conditioned the matrix is. As a rule of thumb, if the condition number `cond(a) = 10**k`, then you may lose up to `k` digits of accuracy on top of what would be lost to the numerical method due to loss of precision from arithmetic methods.

\>>> from numpy.linalg import cond
\>>> cond(a)
np.float64(8.659885634118668e+17)  # may vary

Copy to clipboard

It is also possible to detect ill-conditioning by inspecting the matrix’s singular values directly. The ratio between the largest and the smallest singular value is the condition number:

\>>> from numpy.linalg import svd
\>>> sigma \= svd(a, compute\_uv\=False)  \# Do not compute singular vectors
\>>> sigma.max()/sigma.min()
8.659885634118668e+17  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page