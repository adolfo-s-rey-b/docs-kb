[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compress.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.compress.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.compress.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.compress.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.compress[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compress.html#numpy-ma-maskedarray-compress "Link to this heading")

===========================================================================================================================================================================

method

ma.MaskedArray.compress(_condition_, _axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3974-L4045)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compress.html#numpy.ma.MaskedArray.compress "Link to this definition")

Return _a_ where condition is `True`.

If condition is a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, missing values are considered as `False`.

Parameters:

**condition**var

Boolean 1-d array selecting which entries to return. If len(condition) is less than the size of a along the axis, then output is truncated to length of condition array.

**axis**{None, int}, optional

Axis along which the operation must be performed.

**out**{None, ndarray}, optional

Alternative output array in which to place the result. It must have the same shape as the expected output but the type will be cast if necessary.

Returns:

**result**MaskedArray

A [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 object.

Notes

Please note the difference with [`compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")
 ! The output of [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")
 has a mask, the output of [`compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")
 does not.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[1,2,3\],\[4,5,6\],\[7,8,9\]\], mask\=\[0\] + \[1,0\]\*4)
\>>> x
masked\_array(
  data=\[\[1, --, 3\],\
        \[--, 5, --\],\
        \[7, --, 9\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)
\>>> x.compress(\[1, 0, 1\])
masked\_array(data=\[1, 3\],
             mask=\[False, False\],
       fill\_value=999999)

Copy to clipboard

\>>> x.compress(\[1, 0, 1\], axis\=1)
masked\_array(
  data=\[\[1, 3\],\
        \[--, --\],\
        \[7, 9\]\],
  mask=\[\[False, False\],\
        \[ True,  True\],\
        \[False, False\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page