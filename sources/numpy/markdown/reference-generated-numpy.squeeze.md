[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.squeeze.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.squeeze.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.squeeze.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.squeeze.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.squeeze.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.squeeze.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.squeeze.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.squeeze.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.squeeze.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.squeeze.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.squeeze.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.squeeze.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.squeeze.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.squeeze.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.squeeze.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.squeeze.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.squeeze.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.squeeze.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.squeeze.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.squeeze.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.squeeze[#](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy-squeeze "Link to this heading")

===========================================================================================================================

numpy.squeeze(_a_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1634-L1701)
[#](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "Link to this definition")

Remove axes of length one from _a_.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Selects a subset of the entries of length one in the shape. If an axis is selected with shape entry greater than one, an error is raised.

Returns:

**squeezed**ndarray

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