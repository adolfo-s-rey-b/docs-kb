[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.dtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.dtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.dtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.dtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.dtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.dtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.dtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.dtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.dtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.dtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.dtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.dtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.dtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.dtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.dtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.dtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.dtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.dtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.dtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.dtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.char.chararray.dtype[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html#numpy-char-chararray-dtype "Link to this heading")

==================================================================================================================================================================

attribute

char.chararray.dtype[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html#numpy.char.chararray.dtype "Link to this definition")

Data-type of the array’s elements.

Warning

Setting `arr.dtype` is discouraged and may be deprecated in the future. Setting will replace the `dtype` without modifying the memory (see also [`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")
 and [`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
).

Parameters:

**None**

Returns:

**d**numpy dtype object

See also

[`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")

Cast the values contained in the array to a new data-type.

[`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")

Create a view of the same data but a different data-type.

[`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(4).reshape((2, 2))
\>>> x
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> x.dtype
dtype('int64')   # may vary (OS, bitness)
\>>> isinstance(x.dtype, np.dtype)
True

Copy to clipboard

Go BackOpen In Tab

On this page