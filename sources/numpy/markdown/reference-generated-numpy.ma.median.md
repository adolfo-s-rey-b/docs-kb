[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.median.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.median[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.median.html#numpy-ma-median "Link to this heading")

=================================================================================================================================

ma.median(_a_, _axis\=None_, _out\=None_, _overwrite\_input\=False_, _keepdims\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L678-L753)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.median.html#numpy.ma.median "Link to this definition")

Compute the median along the specified axis.

Returns the median of the array elements.

Parameters:

**a**array\_like

Input array or object that can be converted to an array.

**axis**int, optional

Axis along which the medians are computed. The default (None) is to compute the median along a flattened version of the array.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type will be cast if necessary.

**overwrite\_input**bool, optional

If True, then allow use of memory of input array (a) for calculations. The input array will be modified by the call to median. This will save memory when you do not need to preserve the contents of the input array. Treat the input as undefined, but it will probably be fully or partially sorted. Default is False. Note that, if _overwrite\_input_ is True, and the input is not already an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, an error will be raised.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

Returns:

**median**ndarray

A new array holding the result is returned unless out is specified, in which case a reference to out is returned. Return data-type is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 for integers and floats smaller than [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, or the input data-type, otherwise.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

Notes

Given a vector `V` with `N` non masked values, the median of `V` is the middle value of a sorted copy of `V` (`Vs`) - i.e. `Vs[(N-1)/2]`, when `N` is odd, or `{Vs[N/2 - 1] + Vs[N/2]}/2` when `N` is even.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.arange(8), mask\=\[0\]\*4 + \[1\]\*4)
\>>> np.ma.median(x)
1.5

Copy to clipboard

\>>> x \= np.ma.array(np.arange(10).reshape(2, 5), mask\=\[0\]\*6 + \[1\]\*4)
\>>> np.ma.median(x)
2.5
\>>> np.ma.median(x, axis\=-1, overwrite\_input\=True)
masked\_array(data=\[2.0, 5.0\],
             mask=\[False, False\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page