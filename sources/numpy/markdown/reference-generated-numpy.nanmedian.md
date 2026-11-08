[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nanmedian.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nanmedian.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nanmedian.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nanmedian.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nanmedian.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nanmedian.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nanmedian.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nanmedian.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nanmedian.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nanmedian.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nanmedian.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nanmedian.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nanmedian.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nanmedian.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nanmedian.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nanmedian.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nanmedian.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nanmedian.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nanmedian.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nanmedian.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nanmedian[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html#numpy-nanmedian "Link to this heading")

=================================================================================================================================

numpy.nanmedian(_a_, _axis=None_, _out=None_, _overwrite\_input=False_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L1125-L1217)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html#numpy.nanmedian "Link to this definition")

Compute the median along the specified axis, while ignoring NaNs.

Returns the median of the array elements.

Parameters:

**a**array\_like

Input array or object that can be converted to an array.

**axis**{int, sequence of int, None}, optional

Axis or axes along which the medians are computed. The default is to compute the median along a flattened version of the array. A sequence of axes is supported since version 1.9.0.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output, but the type (of the output) will be cast if necessary.

**overwrite\_input**bool, optional

If True, then allow use of memory of input array _a_ for calculations. The input array will be modified by the call to [`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")
. This will save memory when you do not need to preserve the contents of the input array. Treat the input as undefined, but it will probably be fully or partially sorted. Default is False. If _overwrite\_input_ is `True` and _a_ is not already an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, an error will be raised.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_.

If this is anything but the default value it will be passed through (in the special case of an empty array) to the [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 function of the underlying array. If the array is a sub-class and [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 does not have the kwarg _keepdims_ this will raise a RuntimeError.

Returns:

**median**ndarray

A new array holding the result. If the input contains integers or floats smaller than `float64`, then the output data-type is `np.float64`. Otherwise, the data-type of the output is the same as that of the input. If _out_ is specified, that array is returned instead.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
, [`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")
, [`percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")

Notes

Given a vector `V` of length `N`, the median of `V` is the middle value of a sorted copy of `V`, `V_sorted` - i.e., `V_sorted[(N-1)/2]`, when `N` is odd and the average of the two middle values of `V_sorted` when `N` is even.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[10.0, 7, 4\], \[3, 2, 1\]\])
\>>> a\[0, 1\] \= np.nan
\>>> a
array(\[\[10., nan,  4.\],\
       \[ 3.,  2.,  1.\]\])
\>>> np.median(a)
np.float64(nan)
\>>> np.nanmedian(a)
3.0
\>>> np.nanmedian(a, axis\=0)
array(\[6.5, 2. , 2.5\])
\>>> np.median(a, axis\=1)
array(\[nan,  2.\])
\>>> b \= a.copy()
\>>> np.nanmedian(b, axis\=1, overwrite\_input\=True)
array(\[7.,  2.\])
\>>> assert not np.all(a\==b)
\>>> b \= a.copy()
\>>> np.nanmedian(b, axis\=None, overwrite\_input\=True)
3.0
\>>> assert not np.all(a\==b)

Copy to clipboard

Go BackOpen In Tab

On this page