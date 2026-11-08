[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nanvar.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nanvar.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nanvar.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nanvar.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nanvar.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nanvar.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nanvar.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nanvar.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nanvar.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nanvar.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nanvar.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nanvar.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nanvar.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nanvar.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nanvar.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nanvar.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nanvar.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nanvar.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nanvar.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nanvar.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nanvar[#](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy-nanvar "Link to this heading")

========================================================================================================================

numpy.nanvar(_a_, _axis=None_, _dtype=None_, _out=None_, _ddof=0_, _keepdims=<no value>_, _\*_, _where=<no value>_, _mean=<no value>_, _correction=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L1693-L1874)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy.nanvar "Link to this definition")

Compute the variance along the specified axis, while ignoring NaNs.

Returns the variance of the array elements, a measure of the spread of a distribution. The variance is computed for the flattened array by default, otherwise over the specified axis.

For all-NaN slices or slices with zero degrees of freedom, NaN is returned and a _RuntimeWarning_ is raised.

Parameters:

**a**array\_like

Array containing numbers whose variance is desired. If _a_ is not an array, a conversion is attempted.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the variance is computed. The default is to compute the variance of the flattened array.

**dtype**data-type, optional

Type to use in computing the variance. For arrays of integer type the default is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
; for arrays of float types it is the same as the array type.

**out**ndarray, optional

Alternate output array in which to place the result. It must have the same shape as the expected output, but the type is cast if necessary.

**ddof**{int, float}, optional

“Delta Degrees of Freedom”: the divisor used in the calculation is `N - ddof`, where `N` represents the number of non-NaN elements. By default _ddof_ is zero.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_.

**where**array\_like of bool, optional

Elements to include in the variance. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

**mean**array\_like, optional

Provide the mean to prevent its recalculation. The mean should have a shape as if it was calculated with `keepdims=True`. The axis for the calculation of the mean should be the same as used in the call to this var function.

New in version 2.0.0.

**correction**{int, float}, optional

Array API compatible name for the `ddof` parameter. Only one of them can be provided at the same time.

New in version 2.0.0.

Returns:

**variance**ndarray, see dtype parameter above

If _out_ is None, return a new array containing the variance, otherwise return a reference to the output array. If ddof is >= the number of non-NaN elements in a slice or the slice contains only NaNs, then the result for that slice is NaN.

See also

[`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")

Standard deviation

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

Average

[`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")

Variance while not ignoring NaNs

[`nanstd`](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html#numpy.nanstd "numpy.nanstd")
, [`nanmean`](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy.nanmean "numpy.nanmean")

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Notes

The variance is the average of the squared deviations from the mean, i.e., `var = mean(abs(x - x.mean())**2)`.

The mean is normally calculated as `x.sum() / N`, where `N = len(x)`. If, however, _ddof_ is specified, the divisor `N - ddof` is used instead. In standard statistical practice, `ddof=1` provides an unbiased estimator of the variance of a hypothetical infinite population. `ddof=0` provides a maximum likelihood estimate of the variance for normally distributed variables.

Note that for complex numbers, the absolute value is taken before squaring, so that the result is always real and nonnegative.

For floating-point input, the variance is computed using the same precision the input has. Depending on the input data, this can cause the results to be inaccurate, especially for [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 (see example below). Specifying a higher-accuracy accumulator using the `dtype` keyword can alleviate this issue.

For this function to work on sub-classes of ndarray, they must define [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 with the kwarg _keepdims_

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, np.nan\], \[3, 4\]\])
\>>> np.nanvar(a)
1.5555555555555554
\>>> np.nanvar(a, axis\=0)
array(\[1.,  0.\])
\>>> np.nanvar(a, axis\=1)
array(\[0.,  0.25\])  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page