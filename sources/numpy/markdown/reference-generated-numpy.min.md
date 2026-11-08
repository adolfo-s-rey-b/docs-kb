[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.min.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.min.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.min.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.min.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.min.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.min.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.min.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.min.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.min.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.min.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.min.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.min.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.min.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.min.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.min.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.min.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.min.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.min.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.min.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.min.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.min.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.min.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.min[#](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy-min "Link to this heading")

===============================================================================================================

numpy.min(_a_, _axis=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3187-L3300)
[#](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "Link to this definition")

Return the minimum of an array or minimum along an axis.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Axis or axes along which to operate. By default, flattened input is used.

If this is a tuple of ints, the minimum is selected over multiple axes, instead of a single axis or all the axes as before.

**out**ndarray, optional

Alternative output array in which to place the result. Must be of the same shape and buffer length as the expected output. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the `min` method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

The maximum value of an output element. Must be present to allow computation on empty slice. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

**where**array\_like of bool, optional

Elements to compare for the minimum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

Returns:

**min**ndarray or scalar

Minimum of _a_. If _axis_ is None, the result is a scalar value. If _axis_ is an int, the result is an array of dimension `a.ndim - 1`. If _axis_ is a tuple, the result is an array of dimension `a.ndim - len(axis)`.

See also

[`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")

The maximum value of an array along a given axis, propagating any NaNs.

[`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")

The minimum value of an array along a given axis, ignoring any NaNs.

[`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")

Element-wise minimum of two arrays, propagating any NaNs.

[`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")

Element-wise minimum of two arrays, ignoring any NaNs.

[`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")

Return the indices of the minimum values.

[`nanmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")
, [`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")
, [`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")

Notes

NaN values are propagated, that is if at least one item is NaN, the corresponding min value will be NaN as well. To ignore NaN values (MATLAB behavior), please use nanmin.

Don’t use [`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
 for element-wise comparison of 2 arrays; when `a.shape[0]` is 2, `minimum(a[0], a[1])` is faster than `min(a, axis=0)`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(4).reshape((2,2))
\>>> a
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> np.min(a)           \# Minimum of the flattened array
0
\>>> np.min(a, axis\=0)   \# Minima along the first axis
array(\[0, 1\])
\>>> np.min(a, axis\=1)   \# Minima along the second axis
array(\[0, 2\])
\>>> np.min(a, where\=\[False, True\], initial\=10, axis\=0)
array(\[10,  1\])

Copy to clipboard

\>>> b \= np.arange(5, dtype\=np.float64)
\>>> b\[2\] \= np.nan
\>>> np.min(b)
np.float64(nan)
\>>> np.min(b, where\=~np.isnan(b), initial\=10)
0.0
\>>> np.nanmin(b)
0.0

Copy to clipboard

\>>> np.min(\[\[\-50\], \[10\]\], axis\=-1, initial\=0)
array(\[-50,   0\])

Copy to clipboard

Notice that the initial value is used as one of the elements for which the minimum is determined, unlike for the default argument Python’s max function, which is only used for empty iterables.

Notice that this isn’t the same as Python’s `default` argument.

\>>> np.min(\[6\], initial\=5)
5
\>>> min(\[6\], default\=5)
6

Copy to clipboard

Go BackOpen In Tab

On this page