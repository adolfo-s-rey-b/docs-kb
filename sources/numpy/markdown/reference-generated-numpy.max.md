[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.max.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.max.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.max.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.max.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.max.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.max.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.max.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.max.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.max.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.max.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.max.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.max.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.max.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.max.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.max.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.max.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.max.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.max.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.max.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.max.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.max.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.max.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.max[#](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy-max "Link to this heading")

===============================================================================================================

numpy.max(_a_, _axis=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3049-L3162)
[#](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "Link to this definition")

Return the maximum of an array or maximum along an axis.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Axis or axes along which to operate. By default, flattened input is used. If this is a tuple of ints, the maximum is selected over multiple axes, instead of a single axis or all the axes as before.

**out**ndarray, optional

Alternative output array in which to place the result. Must be of the same shape and buffer length as the expected output. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the `max` method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

The minimum value of an output element. Must be present to allow computation on empty slice. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

**where**array\_like of bool, optional

Elements to compare for the maximum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

Returns:

**max**ndarray or scalar

Maximum of _a_. If _axis_ is None, the result is a scalar value. If _axis_ is an int, the result is an array of dimension `a.ndim - 1`. If _axis_ is a tuple, the result is an array of dimension `a.ndim - len(axis)`.

See also

[`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")

The minimum value of an array along a given axis, propagating any NaNs.

[`nanmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")

The maximum value of an array along a given axis, ignoring any NaNs.

[`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")

Element-wise maximum of two arrays, propagating any NaNs.

[`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")

Element-wise maximum of two arrays, ignoring any NaNs.

[`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")

Return the indices of the maximum values.

[`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")
, [`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")
, [`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")

Notes

NaN values are propagated, that is if at least one item is NaN, the corresponding max value will be NaN as well. To ignore NaN values (MATLAB behavior), please use nanmax.

Don’t use [`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
 for element-wise comparison of 2 arrays; when `a.shape[0]` is 2, `maximum(a[0], a[1])` is faster than `max(a, axis=0)`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(4).reshape((2,2))
\>>> a
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> np.max(a)           \# Maximum of the flattened array
3
\>>> np.max(a, axis\=0)   \# Maxima along the first axis
array(\[2, 3\])
\>>> np.max(a, axis\=1)   \# Maxima along the second axis
array(\[1, 3\])
\>>> np.max(a, where\=\[False, True\], initial\=-1, axis\=0)
array(\[-1,  3\])
\>>> b \= np.arange(5, dtype\=np.float64)
\>>> b\[2\] \= np.nan
\>>> np.max(b)
np.float64(nan)
\>>> np.max(b, where\=~np.isnan(b), initial\=-1)
4.0
\>>> np.nanmax(b)
4.0

Copy to clipboard

You can use an initial value to compute the maximum of an empty slice, or to initialize it to a different value:

\>>> np.max(\[\[\-50\], \[10\]\], axis\=-1, initial\=0)
array(\[ 0, 10\])

Copy to clipboard

Notice that the initial value is used as one of the elements for which the maximum is determined, unlike for the default argument Python’s max function, which is only used for empty iterables.

\>>> np.max(\[5\], initial\=6)
6
\>>> max(\[5\], default\=6)
5

Copy to clipboard

Go BackOpen In Tab

On this page