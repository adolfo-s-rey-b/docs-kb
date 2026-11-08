[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.percentile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.percentile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.percentile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.percentile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.percentile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.percentile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.percentile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.percentile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.percentile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.percentile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.percentile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.percentile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.percentile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.percentile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.percentile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.percentile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.percentile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.percentile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.percentile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.percentile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.percentile[#](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy-percentile "Link to this heading")

====================================================================================================================================

numpy.percentile(_a_, _q_, _axis\=None_, _out\=None_, _overwrite\_input\=False_, _method\='linear'_, _keepdims\=False_, _\*_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L4064-L4259)
[#](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "Link to this definition")

Compute the q-th percentile of the data along the specified axis.

Returns the q-th percentile(s) of the array elements.

Parameters:

**a**array\_like of real numbers

Input array or object that can be converted to an array.

**q**array\_like of float

Percentage or sequence of percentages for the percentiles to compute. Values must be between 0 and 100 inclusive.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the percentiles are computed. The default is to compute the percentile(s) along a flattened version of the array.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output, but the type (of the output) will be cast if necessary.

**overwrite\_input**bool, optional

If True, then allow the input array _a_ to be modified by intermediate calculations, to save memory. In this case, the contents of the input _a_ after this function completes is undefined.

**method**str, optional

This parameter specifies the method to use for estimating the percentile. There are many different methods, some unique to NumPy. See the notes for explanation. The options sorted by their R type as summarized in the H&F paper [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#r08bde0ebf37b-1)
 are:

1.  ‘inverted\_cdf’
    
2.  ‘averaged\_inverted\_cdf’
    
3.  ‘closest\_observation’
    
4.  ‘interpolated\_inverted\_cdf’
    
5.  ‘hazen’
    
6.  ‘weibull’
    
7.  ‘linear’ (default)
    
8.  ‘median\_unbiased’
    
9.  ‘normal\_unbiased’
    

The first three methods are discontinuous. NumPy further defines the following discontinuous variations of the default ‘linear’ (7.) option:

*   ‘lower’
    
*   ‘higher’,
    
*   ‘midpoint’
    
*   ‘nearest’
    

Changed in version 1.22.0: This argument was previously called “interpolation” and only offered the “linear” default and last four options.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original array _a_.

**weights**array\_like, optional

An array of weights associated with the values in _a_. Each value in _a_ contributes to the percentile according to its associated weight. The weights array can either be 1-D (in which case its length must be the size of _a_ along the given axis) or of the same shape as _a_. If _weights=None_, then all data in _a_ are assumed to have a weight equal to one. Only _method=”inverted\_cdf”_ supports weights. See the notes for more details.

New in version 2.0.0.

Returns:

**percentile**scalar or ndarray

If _q_ is a single percentile and _axis=None_, then the result is a scalar. If multiple percentiles are given, first axis of the result corresponds to the percentiles. The other axes are the axes that remain after the reduction of _a_. If the input contains integers or floats smaller than `float64`, the output data-type is `float64`. Otherwise, the output data-type is the same as that of the input. If _out_ is specified, that array is returned instead.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

[`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")

equivalent to `percentile(..., 50)`

[`nanpercentile`](https://numpy.org/doc/stable/reference/generated/numpy.nanpercentile.html#numpy.nanpercentile "numpy.nanpercentile")

[`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")

equivalent to percentile, except q in the range \[0, 1\].

Notes

The behavior of [`numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
 with percentage _q_ is that of [`numpy.quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")
 with argument `q/100`. For more information, please see [`numpy.quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")
.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#id1)\
\]

R. J. Hyndman and Y. Fan, “Sample quantiles in statistical packages,” The American Statistician, 50(4), pp. 361-365, 1996

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[10, 7, 4\], \[3, 2, 1\]\])
\>>> a
array(\[\[10,  7,  4\],\
       \[ 3,  2,  1\]\])
\>>> np.percentile(a, 50)
3.5
\>>> np.percentile(a, 50, axis\=0)
array(\[6.5, 4.5, 2.5\])
\>>> np.percentile(a, 50, axis\=1)
array(\[7.,  2.\])
\>>> np.percentile(a, 50, axis\=1, keepdims\=True)
array(\[\[7.\],\
       \[2.\]\])

Copy to clipboard

\>>> m \= np.percentile(a, 50, axis\=0)
\>>> out \= np.zeros\_like(m)
\>>> np.percentile(a, 50, axis\=0, out\=out)
array(\[6.5, 4.5, 2.5\])
\>>> m
array(\[6.5, 4.5, 2.5\])

Copy to clipboard

\>>> b \= a.copy()
\>>> np.percentile(b, 50, axis\=1, overwrite\_input\=True)
array(\[7.,  2.\])
\>>> assert not np.all(a \== b)

Copy to clipboard

The different methods can be visualized graphically:

import matplotlib.pyplot as plt

a \= np.arange(4)
p \= np.linspace(0, 100, 6001)
ax \= plt.gca()
lines \= \[\
    ('linear', '-', 'C0'),\
    ('inverted\_cdf', ':', 'C1'),\
    \# Almost the same as \`inverted\_cdf\`:\
    ('averaged\_inverted\_cdf', '-.', 'C1'),\
    ('closest\_observation', ':', 'C2'),\
    ('interpolated\_inverted\_cdf', '--', 'C1'),\
    ('hazen', '--', 'C3'),\
    ('weibull', '-.', 'C4'),\
    ('median\_unbiased', '--', 'C5'),\
    ('normal\_unbiased', '-.', 'C6'),\
    \]
for method, style, color in lines:
    ax.plot(
        p, np.percentile(a, p, method\=method),
        label\=method, linestyle\=style, color\=color)
ax.set(
    title\='Percentiles for different methods and data: ' + str(a),
    xlabel\='Percentile',
    ylabel\='Estimated percentile value',
    yticks\=a)
ax.legend(bbox\_to\_anchor\=(1.03, 1))
plt.tight\_layout()
plt.show()

Copy to clipboard

![../../_images/numpy-percentile-1.png](https://numpy.org/doc/stable/_images/numpy-percentile-1.png)

Go BackOpen In Tab

On this page