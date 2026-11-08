[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.tensorsolve.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.tensorsolve.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.tensorsolve.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.tensorsolve.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.tensorsolve.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.tensorsolve.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.tensorsolve.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.tensorsolve.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.tensorsolve.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.tensorsolve.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.tensorsolve.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.tensorsolve.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.tensorsolve.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.tensorsolve.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.tensorsolve.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.tensorsolve.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.tensorsolve.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.tensorsolve.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.tensorsolve.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.tensorsolve.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.tensorsolve[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html#numpy-linalg-tensorsolve "Link to this heading")

============================================================================================================================================================

linalg.tensorsolve(_a_, _b_, _axes\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L293-L367)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html#numpy.linalg.tensorsolve "Link to this definition")

Solve the tensor equation `a x = b` for x.

It is assumed that all indices of _x_ are summed over in the product, together with the rightmost indices of _a_, as is done in, for example, `tensordot(a, x, axes=x.ndim)`.

Parameters:

**a**array\_like

Coefficient tensor, of shape `b.shape + Q`. _Q_, a tuple, equals the shape of that sub-tensor of _a_ consisting of the appropriate number of its rightmost indices, and must be such that `prod(Q) == prod(b.shape)` (in which sense _a_ is said to be ‘square’).

**b**array\_like

Right-hand tensor, which can be of any shape.

**axes**tuple of ints, optional

Axes in _a_ to reorder to the right, before inversion. If None (default), no reordering is done.

Returns:

**x**ndarray, shape Q

Raises:

LinAlgError

If _a_ is singular or not ‘square’ (in the above sense).

See also

[`numpy.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")
, [`tensorinv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html#numpy.linalg.tensorinv "numpy.linalg.tensorinv")
, [`numpy.einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.eye(2\*3\*4).reshape((2\*3, 4, 2, 3, 4))
\>>> rng \= np.random.default\_rng()
\>>> b \= rng.normal(size\=(2\*3, 4))
\>>> x \= np.linalg.tensorsolve(a, b)
\>>> x.shape
(2, 3, 4)
\>>> np.allclose(np.tensordot(a, x, axes\=3), b)
True

Copy to clipboard

Go BackOpen In Tab

On this page