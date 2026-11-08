[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nanmean.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nanmean.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nanmean.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nanmean.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nanmean.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nanmean.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nanmean.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nanmean.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nanmean.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nanmean.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nanmean.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nanmean.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nanmean.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nanmean.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nanmean.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nanmean.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nanmean.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nanmean.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nanmean.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nanmean.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nanmean[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy-nanmean "Link to this heading")

===========================================================================================================================

numpy.nanmean(_a_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_, _\*_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L952-L1054)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy.nanmean "Link to this definition")

Compute the arithmetic mean along the specified axis, ignoring NaNs.

Returns the average of the array elements. The average is taken over the flattened array by default, otherwise over the specified axis. [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 intermediate and return values are used for integer inputs.

For all-NaN slices, NaN is returned and a _RuntimeWarning_ is raised.

Parameters:

**a**array\_like

Array containing numbers whose mean is desired. If _a_ is not an array, a conversion is attempted.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the means are computed. The default is to compute the mean of the flattened array.

**dtype**data-type, optional

Type to use in computing the mean. For integer inputs, the default is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
; for inexact inputs, it is the same as the input dtype.

**out**ndarray, optional

Alternate output array in which to place the result. The default is `None`; if provided, it must have the same shape as the expected output, but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_.

If the value is anything but the default, then _keepdims_ will be passed through to the [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 or [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 methods of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. If the sub-classes methods does not implement _keepdims_ any exceptions will be raised.

**where**array\_like of bool, optional

Elements to include in the mean. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

Returns:

**m**ndarray, see dtype parameter above

If _out=None_, returns a new array containing the mean values, otherwise a reference to the output array is returned. Nan is returned for slices that contain only NaNs.

See also

[`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")

Weighted average

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

Arithmetic mean taken while not ignoring NaNs

[`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
, [`nanvar`](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy.nanvar "numpy.nanvar")

Notes

The arithmetic mean is the sum of the non-NaN elements along the axis divided by the number of non-NaN elements.

Note that for floating-point input, the mean is computed using the same precision the input has. Depending on the input data, this can cause the results to be inaccurate, especially for [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
. Specifying a higher-precision accumulator using the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 keyword can alleviate this issue.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, np.nan\], \[3, 4\]\])
\>>> np.nanmean(a)
2.6666666666666665
\>>> np.nanmean(a, axis\=0)
array(\[2.,  4.\])
\>>> np.nanmean(a, axis\=1)
array(\[1.,  3.5\]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page