[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.squeeze.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.squeeze[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.squeeze.html#numpy-ma-squeeze "Link to this heading")

====================================================================================================================================

ma.squeeze(_a_, _axis\=None_, _\*_, _fill\_value\=None_, _hardmask\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.squeeze.html#numpy.ma.squeeze "Link to this definition")

Remove axes of length one from _a_.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Selects a subset of the entries of length one in the shape. If an axis is selected with shape entry greater than one, an error is raised.

Returns:

**squeezed**MaskedArray

The input array, but with all or a subset of the dimensions of length 1 removed. This is always _a_ itself or a view into _a_. Note that if all axes are squeezed, the result is a 0d array and not a scalar.

Raises:

ValueError

If _axis_ is not None, and an axis being squeezed is not of length 1

See also

[`expand_dims`](https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html#numpy.expand_dims "numpy.expand_dims")

The inverse operation, adding entries of length one

[`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Insert, remove, and combine dimensions, and resize existing ones

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[\[0\], \[1\], \[2\]\]\])
\>>> x.shape
(1, 3, 1)
\>>> np.squeeze(x).shape
(3,)
\>>> np.squeeze(x, axis\=0).shape
(3, 1)
\>>> np.squeeze(x, axis\=1).shape
Traceback (most recent call last):
...
ValueError: cannot select an axis to squeeze out which has size
not equal to one
\>>> np.squeeze(x, axis\=2).shape
(1, 3)
\>>> x \= np.array(\[\[1234\]\])
\>>> x.shape
(1, 1)
\>>> np.squeeze(x)
array(1234)  # 0d array
\>>> np.squeeze(x).shape
()
\>>> np.squeeze(x)\[()\]
1234

Copy to clipboard

Go BackOpen In Tab

On this page