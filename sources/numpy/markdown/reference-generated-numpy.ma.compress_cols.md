[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_cols.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.compress_cols.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_cols.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.compress_cols.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.compress_cols.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.compress_cols.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.compress_cols.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.compress_cols.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.compress_cols.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.compress_cols.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.compress_cols.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.compress_cols.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.compress_cols.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.compress_cols.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.compress_cols.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.compress_cols.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.compress_cols.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.compress_cols.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.compress_cols.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.compress_cols.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.compress_cols.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.compress_cols.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.compress\_cols[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_cols.html#numpy-ma-compress-cols "Link to this heading")

=======================================================================================================================================================

ma.compress\_cols(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L994-L1032)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_cols.html#numpy.ma.compress_cols "Link to this definition")

Suppress whole columns of a 2-D array that contain masked values.

This is equivalent to `np.ma.compress_rowcols(a, 1)`, see [`compress_rowcols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_rowcols.html#numpy.ma.compress_rowcols "numpy.ma.compress_rowcols")
 for details.

Parameters:

**x**array\_like, MaskedArray

The array to operate on. If not a MaskedArray instance (or if no array elements are masked), _x_ is interpreted as a MaskedArray with _mask_ set to [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
. Must be a 2D array.

Returns:

**compressed\_array**ndarray

The compressed array.

See also

[`compress_rowcols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_rowcols.html#numpy.ma.compress_rowcols "numpy.ma.compress_rowcols")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(np.arange(9).reshape(3, 3), mask\=\[\[1, 0, 0\],\
...                                                   \[1, 0, 0\],\
...                                                   \[0, 0, 0\]\])
\>>> np.ma.compress\_cols(a)
array(\[\[1, 2\],\
       \[4, 5\],\
       \[7, 8\]\])

Copy to clipboard

Go BackOpen In Tab

On this page