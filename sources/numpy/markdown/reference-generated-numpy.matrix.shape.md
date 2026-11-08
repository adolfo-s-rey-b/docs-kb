[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.shape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.shape.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.shape.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.shape.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.shape.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.shape.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.shape.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.shape.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.shape.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.shape.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.shape.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.shape.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.shape.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.shape.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.shape.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.shape.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.shape.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.shape.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.shape.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.shape.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.shape.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.shape.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.matrix.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.shape.html#numpy-matrix-shape "Link to this heading")

==========================================================================================================================================

attribute

matrix.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.shape.html#numpy.matrix.shape "Link to this definition")

Tuple of array dimensions.

The shape property is usually used to get the current shape of an array, but may also be used to reshape the array in-place by assigning a tuple of array dimensions to it. As with [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
, one of the new shape dimensions can be -1, in which case its value is inferred from the size of the array and the remaining dimensions. Reshaping an array in-place will fail if a copy is required.

Warning

Setting `arr.shape` is deprecated and may be removed in the future. Using [`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")
 is the preferred approach.

See also

[`numpy.shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Equivalent getter function.

[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Function similar to setting `shape`.

[`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")

Method similar to setting `shape`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3, 4\])
\>>> x.shape
(4,)
\>>> y \= np.zeros((2, 3, 4))
\>>> y.shape
(2, 3, 4)

Copy to clipboard

Go BackOpen In Tab

On this page