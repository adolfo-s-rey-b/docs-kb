[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.reshape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.reshape.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.reshape.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.reshape.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.reshape.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.reshape.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.reshape.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.reshape.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.reshape.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.reshape.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.reshape.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.reshape.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.reshape.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.reshape.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.reshape.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.reshape.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.reshape.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.reshape.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.reshape.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.reshape.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.reshape.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.reshape.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.reshape[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.reshape.html#numpy-ma-masked-array-reshape "Link to this heading")

============================================================================================================================================================================

method

ma.masked\_array.reshape(_\*s_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4752-L4817)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.reshape.html#numpy.ma.masked_array.reshape "Link to this definition")

Returns a reshaped masked array without changing its data.

Returns a masked array containing the same data, but with a new shape. The result is a view on the original array; if this is not possible, a ValueError is raised.

Parameters:

**shape**int or tuple of ints

The new shape should be compatible with the original shape. If an integer is supplied, then the result will be a 1-D array of that length.

**order**{‘C’, ‘F’}, optional

Determines whether the array data should be viewed as in C (row-major) or FORTRAN (column-major) order.

Returns:

**reshaped\_array**array

A new view on the array.

See also

[`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Equivalent function in the masked array module.

[`numpy.ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")

Equivalent method on ndarray object.

[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Equivalent function in the NumPy module.

Notes

By default, the reshaping operation will make a copy if a view with different strides is not possible. To ensure a view, pass `copy=False`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[1,2\],\[3,4\]\], mask\=\[1,0,0,1\])
\>>> x
masked\_array(
  data=\[\[--, 2\],\
        \[3, --\]\],
  mask=\[\[ True, False\],\
        \[False,  True\]\],
  fill\_value=999999)
\>>> x \= x.reshape((4,1))
\>>> x
masked\_array(
  data=\[\[--\],\
        \[2\],\
        \[3\],\
        \[--\]\],
  mask=\[\[ True\],\
        \[False\],\
        \[False\],\
        \[ True\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page