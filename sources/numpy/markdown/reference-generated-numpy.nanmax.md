[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nanmax.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nanmax.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nanmax.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nanmax.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nanmax.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nanmax.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nanmax.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nanmax.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nanmax.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nanmax.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nanmax.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nanmax.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nanmax.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nanmax.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nanmax.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nanmax.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nanmax.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nanmax.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nanmax.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nanmax.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nanmax[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy-nanmax "Link to this heading")

========================================================================================================================

numpy.nanmax(_a_, _axis=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L382-L503)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "Link to this definition")

Return the maximum of an array or maximum along an axis, ignoring any NaNs. When all-NaN slices are encountered a `RuntimeWarning` is raised and NaN is returned for that slice.

Parameters:

**a**array\_like

Array containing numbers whose maximum is desired. If _a_ is not an array, a conversion is attempted.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the maximum is computed. The default is to compute the maximum of the flattened array.

**out**ndarray, optional

Alternate output array in which to place the result. The default is `None`; if provided, it must have the same shape as the expected output, but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_. If the value is anything but the default, then _keepdims_ will be passed through to the [`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. If the sub-classes methods does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

The minimum value of an output element. Must be present to allow computation on empty slice. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

**where**array\_like of bool, optional

Elements to compare for the maximum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

Returns:

**nanmax**ndarray

An array with the same shape as _a_, with the specified axis removed. If _a_ is a 0-d array, or if axis is None, an ndarray scalar is returned. The same dtype as _a_ is returned.

See also

[`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")

The minimum value of an array along a given axis, ignoring any NaNs.

[`amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")

The maximum value of an array along a given axis, propagating any NaNs.

[`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")

Element-wise maximum of two arrays, ignoring any NaNs.

[`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")

Element-wise maximum of two arrays, propagating any NaNs.

[`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Shows which elements are Not a Number (NaN).

[`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")

Shows which elements are neither NaN nor infinity.

[`amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")
, [`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")
, [`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity. Positive infinity is treated as a very large number and negative infinity is treated as a very small (i.e. negative) number.

If the input has a integer type the function is equivalent to np.max.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, np.nan\]\])
\>>> np.nanmax(a)
3.0
\>>> np.nanmax(a, axis\=0)
array(\[3.,  2.\])
\>>> np.nanmax(a, axis\=1)
array(\[2.,  3.\])

Copy to clipboard

When positive infinity and negative infinity are present:

\>>> np.nanmax(\[1, 2, np.nan, \-np.inf\])
2.0
\>>> np.nanmax(\[1, 2, np.nan, np.inf\])
inf

Copy to clipboard

Go BackOpen In Tab

On this page