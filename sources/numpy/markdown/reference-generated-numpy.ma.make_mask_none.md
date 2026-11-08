[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_none.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.make_mask_none.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_none.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.make_mask_none.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.make_mask_none.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.make_mask_none.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.make_mask_none.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.make_mask_none.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.make_mask_none.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.make_mask_none.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.make_mask_none.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.make_mask_none.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.make_mask_none.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.make_mask_none.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.make_mask_none.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.make_mask_none.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.make_mask_none.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.make_mask_none.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.make_mask_none.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.make_mask_none.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.make_mask_none.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.make_mask_none.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.make\_mask\_none[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_none.html#numpy-ma-make-mask-none "Link to this heading")

===========================================================================================================================================================

ma.make\_mask\_none(_newshape_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1698-L1746)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_none.html#numpy.ma.make_mask_none "Link to this definition")

Return a boolean mask of the given shape, filled with False.

This function returns a boolean ndarray with all entries False, that can be used in common mask manipulations. If a complex dtype is specified, the type of each field is converted to a boolean type.

Parameters:

**newshape**tuple

A tuple indicating the shape of the mask.

**dtype**{None, dtype}, optional

If None, use a MaskType instance. Otherwise, use a new datatype with the same fields as [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, converted to boolean types.

Returns:

**result**ndarray

An ndarray of appropriate shape and dtype, filled with False.

See also

[`make_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html#numpy.ma.make_mask "numpy.ma.make_mask")

Create a boolean mask from an array.

[`make_mask_descr`](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html#numpy.ma.make_mask_descr "numpy.ma.make_mask_descr")

Construct a dtype description list from a given dtype.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> ma.make\_mask\_none((3,))
array(\[False, False, False\])

Copy to clipboard

Defining a more complex dtype.

\>>> dtype \= np.dtype({'names':\['foo', 'bar'\],
...                   'formats':\[np.float32, np.int64\]})
\>>> dtype
dtype(\[('foo', '<f4'), ('bar', '<i8')\])
\>>> ma.make\_mask\_none((3,), dtype\=dtype)
array(\[(False, False), (False, False), (False, False)\],
      dtype=\[('foo', '|b1'), ('bar', '|b1')\])

Copy to clipboard

Go BackOpen In Tab

On this page