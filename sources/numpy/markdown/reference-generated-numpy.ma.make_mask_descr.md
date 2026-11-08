[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.make_mask_descr.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.make_mask_descr.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.make_mask_descr.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.make_mask_descr.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.make_mask_descr.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.make_mask_descr.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.make_mask_descr.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.make_mask_descr.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.make_mask_descr.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.make_mask_descr.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.make_mask_descr.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.make_mask_descr.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.make_mask_descr.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.make_mask_descr.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.make_mask_descr.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.make_mask_descr.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.make_mask_descr.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.make_mask_descr.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.make_mask_descr.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.make_mask_descr.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.make\_mask\_descr[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html#numpy-ma-make-mask-descr "Link to this heading")

==============================================================================================================================================================

ma.make\_mask\_descr(_ndtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1377-L1408)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html#numpy.ma.make_mask_descr "Link to this definition")

Construct a dtype description list from a given dtype.

Returns a new dtype object, with the type of all fields in _ndtype_ to a boolean type. Field names are not altered.

Parameters:

**ndtype**dtype

The dtype to convert.

Returns:

**result**dtype

A dtype that looks like _ndtype_, the type of all fields is boolean.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> dtype \= np.dtype({'names':\['foo', 'bar'\],
...                   'formats':\[np.float32, np.int64\]})
\>>> dtype
dtype(\[('foo', '<f4'), ('bar', '<i8')\])
\>>> ma.make\_mask\_descr(dtype)
dtype(\[('foo', '|b1'), ('bar', '|b1')\])
\>>> ma.make\_mask\_descr(np.float32)
dtype('bool')

Copy to clipboard

Go BackOpen In Tab

On this page