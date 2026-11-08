[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_nd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.compress_nd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_nd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.compress_nd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.compress_nd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.compress_nd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.compress_nd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.compress_nd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.compress_nd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.compress_nd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.compress_nd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.compress_nd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.compress_nd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.compress_nd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.compress_nd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.compress_nd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.compress_nd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.compress_nd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.compress_nd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.compress_nd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.compress_nd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.compress_nd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.compress\_nd[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_nd.html#numpy-ma-compress-nd "Link to this heading")

=================================================================================================================================================

ma.compress\_nd(_x_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L841-L896)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_nd.html#numpy.ma.compress_nd "Link to this definition")

Suppress slices from multiple dimensions which contain masked values.

Parameters:

**x**array\_like, MaskedArray

The array to operate on. If not a MaskedArray instance (or if no array elements are masked), _x_ is interpreted as a MaskedArray with _mask_ set to [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
.

**axis**tuple of ints or int, optional

Which dimensions to suppress slices from can be configured with this parameter. - If axis is a tuple of ints, those are the axes to suppress slices from. - If axis is an int, then that is the only axis to suppress slices from. - If axis is None, all axis are selected.

Returns:

**compress\_array**ndarray

The compressed array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= \[\[1, 2\], \[3, 4\]\]
\>>> mask \= \[\[0, 1\], \[0, 0\]\]
\>>> x \= np.ma.array(arr, mask\=mask)
\>>> np.ma.compress\_nd(x, axis\=0)
array(\[\[3, 4\]\])
\>>> np.ma.compress\_nd(x, axis\=1)
array(\[\[1\],\
       \[3\]\])
\>>> np.ma.compress\_nd(x)
array(\[\[3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page