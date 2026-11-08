[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.std.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.std.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.std.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.std.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.std.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.std.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.std.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.std.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.std.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.std.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.std.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.std.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.std.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.std.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.std.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.std.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.std.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.std.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.std.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.std.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.std.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.std[#](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy-std "Link to this heading")

===============================================================================================================

numpy.std(_a_, _axis=None_, _dtype=None_, _out=None_, _ddof=0_, _keepdims=<no value>_, _\*_, _where=<no value>_, _mean=<no value>_, _correction=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3871-L4067)
[#](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "Link to this definition")

Compute the standard deviation along the specified axis.

Returns the standard deviation, a measure of the spread of a distribution, of the array elements. The standard deviation is computed for the flattened array by default, otherwise over the specified axis.

Parameters:

**a**array\_like

Calculate the standard deviation of these values.

**axis**None or int or tuple of ints, optional

Axis or axes along which the standard deviation is computed. The default is to compute the standard deviation of the flattened array. If this is a tuple of ints, a standard deviation is performed over multiple axes, instead of a single axis or all the axes as before.

**dtype**dtype, optional

Type to use in computing the standard deviation. For arrays of integer type the default is float64, for arrays of float types it is the same as the array type.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape as the expected output but the type (of the calculated values) will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**ddof**{int, float}, optional

Means Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements. By default _ddof_ is zero. See Notes for details about use of _ddof_.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**where**array\_like of bool, optional

Elements to include in the standard deviation. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.20.0.

**mean**array\_like, optional

Provide the mean to prevent its recalculation. The mean should have a shape as if it was calculated with `keepdims=True`. The axis for the calculation of the mean should be the same as used in the call to this std function.

New in version 2.0.0.

**correction**{int, float}, optional

Array API compatible name for the `ddof` parameter. Only one of them can be provided at the same time.

New in version 2.0.0.

Returns:

**standard\_deviation**ndarray, see dtype parameter above.

If _out_ is None, return a new array containing the standard deviation, otherwise return a reference to the output array.

See also

[`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
, [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
, [`nanmean`](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy.nanmean "numpy.nanmean")
, [`nanstd`](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html#numpy.nanstd "numpy.nanstd")
, [`nanvar`](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy.nanvar "numpy.nanvar")

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Notes

There are several common variants of the array standard deviation calculation. Assuming the input _a_ is a one-dimensional NumPy array and `mean` is either provided as an argument or computed as `a.mean()`, NumPy computes the standard deviation of an array as:

N \= len(a)
d2 \= abs(a \- mean)\*\*2  \# abs is for complex \`a\`
var \= d2.sum() / (N \- ddof)  \# note use of \`ddof\`
std \= var\*\*0.5

Copy to clipboard

Different values of the argument _ddof_ are useful in different contexts. NumPy’s default `ddof=0` corresponds with the expression:

\\\[\\sqrt{\\frac{\\sum\_i{|a\_i - \\bar{a}|^2 }}{N}}\\\]

which is sometimes called the “population standard deviation” in the field of statistics because it applies the definition of standard deviation to _a_ as if _a_ were a complete population of possible observations.

Many other libraries define the standard deviation of an array differently, e.g.:

\\\[\\sqrt{\\frac{\\sum\_i{|a\_i - \\bar{a}|^2 }}{N - 1}}\\\]

In statistics, the resulting quantity is sometimes called the “sample standard deviation” because if _a_ is a random sample from a larger population, this calculation provides the square root of an unbiased estimate of the variance of the population. The use of \\(N-1\\) in the denominator is often called “Bessel’s correction” because it corrects for bias (toward lower values) in the variance estimate introduced when the sample mean of _a_ is used in place of the true mean of the population. The resulting estimate of the standard deviation is still biased, but less than it would have been without the correction. For this quantity, use `ddof=1`.

Note that, for complex numbers, [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
 takes the absolute value before squaring, so that the result is always real and nonnegative.

For floating-point input, the standard deviation is computed using the same precision the input has. Depending on the input data, this can cause the results to be inaccurate, especially for float32 (see example below). Specifying a higher-accuracy accumulator using the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 keyword can alleviate this issue.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.std(a)
1.1180339887498949 # may vary
\>>> np.std(a, axis\=0)
array(\[1.,  1.\])
\>>> np.std(a, axis\=1)
array(\[0.5,  0.5\])

Copy to clipboard

In single precision, std() can be inaccurate:

\>>> a \= np.zeros((2, 512\*512), dtype\=np.float32)
\>>> a\[0, :\] \= 1.0
\>>> a\[1, :\] \= 0.1
\>>> np.std(a)
np.float32(0.45000005)

Copy to clipboard

Computing the standard deviation in float64 is more accurate:

\>>> np.std(a, dtype\=np.float64)
0.44999999925494177 # may vary

Copy to clipboard

Specifying a where argument:

\>>> a \= np.array(\[\[14, 8, 11, 10\], \[7, 9, 10, 11\], \[10, 15, 5, 10\]\])
\>>> np.std(a)
2.614064523559687 # may vary
\>>> np.std(a, where\=\[\[True\], \[True\], \[False\]\])
2.0

Copy to clipboard

Using the mean keyword to save computation time:

\>>> import numpy as np
\>>> from timeit import timeit
\>>> a \= np.array(\[\[14, 8, 11, 10\], \[7, 9, 10, 11\], \[10, 15, 5, 10\]\])
\>>> mean \= np.mean(a, axis\=1, keepdims\=True)
\>>>
\>>> g \= globals()
\>>> n \= 10000
\>>> t1 \= timeit("std = np.std(a, axis=1, mean=mean)", globals\=g, number\=n)
\>>> t2 \= timeit("std = np.std(a, axis=1)", globals\=g, number\=n)
\>>> print(f'Percentage execution time saved {100\*(t2\-t1)/t2:.0f}%')

Percentage execution time saved 30%

Copy to clipboard

Go BackOpen In Tab

On this page