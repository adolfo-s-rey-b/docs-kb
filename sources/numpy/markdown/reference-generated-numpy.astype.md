[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.astype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.astype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.astype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.astype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.astype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.astype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.astype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.astype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.astype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.astype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.astype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.astype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.astype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.astype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.astype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.astype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.astype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.astype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.astype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.astype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.astype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.astype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.astype[#](https://numpy.org/doc/stable/reference/generated/numpy.astype.html#numpy-astype "Link to this heading")

========================================================================================================================

numpy.astype(_x_, _dtype_, _/_, _\*_, _copy\=True_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2613-L2676)
[#](https://numpy.org/doc/stable/reference/generated/numpy.astype.html#numpy.astype "Link to this definition")

Copies an array to a specified data type.

This function is an Array API compatible alternative to [`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
.

Parameters:

**x**ndarray

Input NumPy array to cast. `array_likes` are explicitly not supported here.

**dtype**dtype

Data type of the result.

**copy**bool, optional

Specifies whether to copy an array when the specified dtype matches the data type of the input array `x`. If `True`, a newly allocated array must always be returned. If `False` and the specified dtype matches the data type of the input array, the input array must be returned; otherwise, a newly allocated array must be returned. Defaults to `True`.

**device**str, optional

The device on which to place the returned array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.1.0.

Returns:

**out**ndarray

An array having the specified data type.

See also

[`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.array(\[1, 2, 3\]); arr
array(\[1, 2, 3\])
\>>> np.astype(arr, np.float64)
array(\[1., 2., 3.\])

Copy to clipboard

Non-copy case:

\>>> arr \= np.array(\[1, 2, 3\])
\>>> arr\_noncpy \= np.astype(arr, arr.dtype, copy\=False)
\>>> np.shares\_memory(arr, arr\_noncpy)
True

Copy to clipboard

Go BackOpen In Tab

On this page