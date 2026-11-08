[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nanargmin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nanargmin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nanargmin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nanargmin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nanargmin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nanargmin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nanargmin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nanargmin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nanargmin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nanargmin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nanargmin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nanargmin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nanargmin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nanargmin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nanargmin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nanargmin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nanargmin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nanargmin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nanargmin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nanargmin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nanargmin[#](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html#numpy-nanargmin "Link to this heading")

=================================================================================================================================

numpy.nanargmin(_a_, _axis=None_, _out=None_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L510-L564)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html#numpy.nanargmin "Link to this definition")

Return the indices of the minimum values in the specified axis ignoring NaNs. For all-NaN slices `ValueError` is raised. Warning: the results cannot be trusted if a slice contains only NaNs and Infs.

Parameters:

**a**array\_like

Input data.

**axis**int, optional

Axis along which to operate. By default flattened input is used.

**out**array, optional

If provided, the result will be inserted into this array. It should be of the appropriate shape and dtype.

New in version 1.22.0.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

New in version 1.22.0.

Returns:

**index\_array**ndarray

An array of indices or a single index value.

See also

[`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")
, [`nanargmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanargmax.html#numpy.nanargmax "numpy.nanargmax")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[np.nan, 4\], \[2, 3\]\])
\>>> np.argmin(a)
0
\>>> np.nanargmin(a)
2
\>>> np.nanargmin(a, axis\=0)
array(\[1, 1\])
\>>> np.nanargmin(a, axis\=1)
array(\[1, 0\])

Copy to clipboard

Go BackOpen In Tab

On this page