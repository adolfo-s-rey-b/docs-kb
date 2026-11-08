[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.make_mask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.make_mask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.make_mask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.make_mask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.make_mask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.make_mask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.make_mask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.make_mask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.make_mask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.make_mask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.make_mask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.make_mask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.make_mask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.make_mask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.make_mask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.make_mask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.make_mask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.make_mask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.make_mask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.make_mask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.make\_mask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html#numpy-ma-make-mask "Link to this heading")

===========================================================================================================================================

ma.make\_mask(_m_, _copy=False_, _shrink=True_, _dtype=<class 'numpy.bool'>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1607-L1695)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html#numpy.ma.make_mask "Link to this definition")

Create a boolean mask from an array.

Return _m_ as a boolean mask, creating a copy if necessary or requested. The function can accept any sequence that is convertible to integers, or `nomask`. Does not require that contents must be 0s and 1s, values of 0 are interpreted as False, everything else as True.

Parameters:

**m**array\_like

Potential mask.

**copy**bool, optional

Whether to return a copy of _m_ (True) or _m_ itself (False).

**shrink**bool, optional

Whether to shrink _m_ to `nomask` if all its values are False.

**dtype**dtype, optional

Data-type of the output mask. By default, the output mask has a dtype of MaskType (bool). If the dtype is flexible, each field has a boolean dtype. This is ignored when _m_ is `nomask`, in which case `nomask` is always returned.

Returns:

**result**ndarray

A boolean mask derived from _m_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> m \= \[True, False, True, True\]
\>>> ma.make\_mask(m)
array(\[ True, False,  True,  True\])
\>>> m \= \[1, 0, 1, 1\]
\>>> ma.make\_mask(m)
array(\[ True, False,  True,  True\])
\>>> m \= \[1, 0, 2, \-3\]
\>>> ma.make\_mask(m)
array(\[ True, False,  True,  True\])

Copy to clipboard

Effect of the _shrink_ parameter.

\>>> m \= np.zeros(4)
\>>> m
array(\[0., 0., 0., 0.\])
\>>> ma.make\_mask(m)
False
\>>> ma.make\_mask(m, shrink\=False)
array(\[False, False, False, False\])

Copy to clipboard

Using a flexible [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

\>>> m \= \[1, 0, 1, 1\]
\>>> n \= \[0, 1, 0, 0\]
\>>> arr \= \[\]
\>>> for man, mouse in zip(m, n):
...     arr.append((man, mouse))
\>>> arr
\[(1, 0), (0, 1), (1, 0), (1, 0)\]
\>>> dtype \= np.dtype({'names':\['man', 'mouse'\],
...                   'formats':\[np.int64, np.int64\]})
\>>> arr \= np.array(arr, dtype\=dtype)
\>>> arr
array(\[(1, 0), (0, 1), (1, 0), (1, 0)\],
      dtype=\[('man', '<i8'), ('mouse', '<i8')\])
\>>> ma.make\_mask(arr, dtype\=dtype)
array(\[(True, False), (False, True), (True, False), (True, False)\],
      dtype=\[('man', '|b1'), ('mouse', '|b1')\])

Copy to clipboard

Go BackOpen In Tab

On this page