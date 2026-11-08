[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.shape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.char.chararray.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.shape.html#numpy-char-chararray-shape "Link to this heading")

==================================================================================================================================================================

attribute

char.chararray.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.shape.html#numpy.char.chararray.shape "Link to this definition")

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