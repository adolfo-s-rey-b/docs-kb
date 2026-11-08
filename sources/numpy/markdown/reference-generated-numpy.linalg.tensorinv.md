[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.tensorinv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.tensorinv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.tensorinv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.tensorinv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.tensorinv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.tensorinv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.tensorinv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.tensorinv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.tensorinv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.tensorinv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.tensorinv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.tensorinv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.tensorinv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.tensorinv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.tensorinv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.tensorinv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.tensorinv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.tensorinv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.tensorinv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.tensorinv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.tensorinv[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html#numpy-linalg-tensorinv "Link to this heading")

======================================================================================================================================================

linalg.tensorinv(_a_, _ind\=2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L472-L538)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html#numpy.linalg.tensorinv "Link to this definition")

Compute the ‘inverse’ of an N-dimensional array.

The result is an inverse for _a_ relative to the tensordot operation `tensordot(a, b, ind)`, i. e., up to floating-point accuracy, `tensordot(tensorinv(a), a, ind)` is the “identity” tensor for the tensordot operation.

Parameters:

**a**array\_like

Tensor to ‘invert’. Its shape must be ‘square’, i. e., `prod(a.shape[:ind]) == prod(a.shape[ind:])`.

**ind**int, optional

Number of first indices that are involved in the inverse sum. Must be a positive integer, default is 2.

Returns:

**b**ndarray

_a_’s tensordot inverse, shape `a.shape[ind:] + a.shape[:ind]`.

Raises:

LinAlgError

If _a_ is singular or not ‘square’ (in the above sense).

See also

[`numpy.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")
, [`tensorsolve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html#numpy.linalg.tensorsolve "numpy.linalg.tensorsolve")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.eye(4\*6).reshape((4, 6, 8, 3))
\>>> ainv \= np.linalg.tensorinv(a, ind\=2)
\>>> ainv.shape
(8, 3, 4, 6)
\>>> rng \= np.random.default\_rng()
\>>> b \= rng.normal(size\=(4, 6))
\>>> np.allclose(np.tensordot(ainv, b), np.linalg.tensorsolve(a, b))
True

Copy to clipboard

\>>> a \= np.eye(4\*6).reshape((24, 8, 3))
\>>> ainv \= np.linalg.tensorinv(a, ind\=1)
\>>> ainv.shape
(8, 3, 24)
\>>> rng \= np.random.default\_rng()
\>>> b \= rng.normal(size\=24)
\>>> np.allclose(np.tensordot(ainv, b, 1), np.linalg.tensorsolve(a, b))
True

Copy to clipboard

Go BackOpen In Tab

On this page