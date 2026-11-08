[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.mean.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.mean.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.mean.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.mean.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.mean.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.mean.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.mean.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.mean.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.mean.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.mean.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.mean.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.mean.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.mean.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.mean.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.mean.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.mean.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.mean.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.mean.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.mean.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.mean.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.mean[#](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy-mean "Link to this heading")

==================================================================================================================

numpy.mean(_a_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_, _\*_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3737-L3863)
[#](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "Link to this definition")

Compute the arithmetic mean along the specified axis.

Returns the average of the array elements. The average is taken over the flattened array by default, otherwise over the specified axis. [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 intermediate and return values are used for integer inputs.

Parameters:

**a**array\_like

Array containing numbers whose mean is desired. If _a_ is not an array, a conversion is attempted.

**axis**None or int or tuple of ints, optional

Axis or axes along which the means are computed. The default is to compute the mean of the flattened array.

If this is a tuple of ints, a mean is performed over multiple axes, instead of a single axis or all the axes as before.

**dtype**data-type, optional

Type to use in computing the mean. For integer inputs, the default is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
; for floating point inputs, it is the same as the input dtype.

**out**ndarray, optional

Alternate output array in which to place the result. The default is `None`; if provided, it must have the same shape as the expected output, but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**where**array\_like of bool, optional

Elements to include in the mean. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.20.0.

Returns:

**m**ndarray, see dtype parameter above

If _out=None_, returns a new array containing the mean values, otherwise a reference to the output array is returned.

See also

[`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")

Weighted average

[`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
, [`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
, [`nanmean`](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy.nanmean "numpy.nanmean")
, [`nanstd`](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html#numpy.nanstd "numpy.nanstd")
, [`nanvar`](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy.nanvar "numpy.nanvar")

Notes

The arithmetic mean is the sum of the elements along the axis divided by the number of elements.

Note that for floating-point input, the mean is computed using the same precision the input has. Depending on the input data, this can cause the results to be inaccurate, especially for [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 (see example below). Specifying a higher-precision accumulator using the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 keyword can alleviate this issue.

By default, [`float16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float16 "numpy.float16")
 results are computed using [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 intermediates for extra precision.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.mean(a)
2.5
\>>> np.mean(a, axis\=0)
array(\[2., 3.\])
\>>> np.mean(a, axis\=1)
array(\[1.5, 3.5\])

Copy to clipboard

In single precision, [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 can be inaccurate:

\>>> a \= np.zeros((2, 512\*512), dtype\=np.float32)
\>>> a\[0, :\] \= 1.0
\>>> a\[1, :\] \= 0.1
\>>> np.mean(a)
np.float32(0.54999924)

Copy to clipboard

Computing the mean in float64 is more accurate:

\>>> np.mean(a, dtype\=np.float64)
0.55000000074505806 # may vary

Copy to clipboard

Computing the mean in timedelta64 is available:

\>>> b \= np.array(\[1, 3\], dtype\="timedelta64\[D\]")
\>>> np.mean(b)
np.timedelta64(2,'D')

Copy to clipboard

Specifying a where argument:

\>>> a \= np.array(\[\[5, 9, 13\], \[14, 10, 12\], \[11, 15, 19\]\])
\>>> np.mean(a)
12.0
\>>> np.mean(a, where\=\[\[True\], \[False\], \[False\]\])
9.0

Copy to clipboard

Go BackOpen In Tab

On this page