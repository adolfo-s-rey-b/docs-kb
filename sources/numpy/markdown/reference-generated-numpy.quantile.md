[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.quantile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.quantile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.quantile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.quantile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.quantile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.quantile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.quantile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.quantile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.quantile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.quantile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.quantile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.quantile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.quantile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.quantile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.quantile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.quantile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.quantile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.quantile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.quantile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.quantile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.quantile[#](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy-quantile "Link to this heading")

==============================================================================================================================

numpy.quantile(_a_, _q_, _axis\=None_, _out\=None_, _overwrite\_input\=False_, _method\='linear'_, _keepdims\=False_, _\*_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L4267-L4509)
[#](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "Link to this definition")

Compute the q-th quantile of the data along the specified axis.

Parameters:

**a**array\_like of real numbers

Input array or object that can be converted to an array.

**q**array\_like of float

Probability or sequence of probabilities of the quantiles to compute. Values must be between 0 and 1 inclusive.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the quantiles are computed. The default is to compute the quantile(s) along a flattened version of the array.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output, but the type (of the output) will be cast if necessary.

**overwrite\_input**bool, optional

If True, then allow the input array _a_ to be modified by intermediate calculations, to save memory. In this case, the contents of the input _a_ after this function completes is undefined.

**method**str, optional

This parameter specifies the method to use for estimating the quantile. There are many different methods, some unique to NumPy. The recommended options, numbered as they appear in [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#re01cd3f3acfe-1)
, are:

1.  ‘inverted\_cdf’
    
2.  ‘averaged\_inverted\_cdf’
    
3.  ‘closest\_observation’
    
4.  ‘interpolated\_inverted\_cdf’
    
5.  ‘hazen’
    
6.  ‘weibull’
    
7.  ‘linear’ (default)
    
8.  ‘median\_unbiased’
    
9.  ‘normal\_unbiased’
    

The first three methods are discontinuous. For backward compatibility with previous versions of NumPy, the following discontinuous variations of the default ‘linear’ (7.) option are available:

*   ‘lower’
    
*   ‘higher’,
    
*   ‘midpoint’
    
*   ‘nearest’
    

See Notes for details.

Changed in version 1.22.0: This argument was previously called “interpolation” and only offered the “linear” default and last four options.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original array _a_.

**weights**array\_like, optional

An array of weights associated with the values in _a_. Each value in _a_ contributes to the quantile according to its associated weight. The weights array can either be 1-D (in which case its length must be the size of _a_ along the given axis) or of the same shape as _a_. If _weights=None_, then all data in _a_ are assumed to have a weight equal to one. Only _method=”inverted\_cdf”_ supports weights. See the notes for more details.

New in version 2.0.0.

Returns:

**quantile**scalar or ndarray

If _q_ is a single probability and _axis=None_, then the result is a scalar. If multiple probability levels are given, first axis of the result corresponds to the quantiles. The other axes are the axes that remain after the reduction of _a_. If the input contains integers or floats smaller than `float64`, the output data-type is `float64`. Otherwise, the output data-type is the same as that of the input. If _out_ is specified, that array is returned instead.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

[`percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")

equivalent to quantile, but with q in the range \[0, 100\].

[`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")

equivalent to `quantile(..., 0.5)`

[`nanquantile`](https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html#numpy.nanquantile "numpy.nanquantile")

Notes

Given a sample _a_ from an underlying distribution, [`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")
 provides a nonparametric estimate of the inverse cumulative distribution function.

By default, this is done by interpolating between adjacent elements in `y`, a sorted copy of _a_:

(1\-g)\*y\[j\] + g\*y\[j+1\]

Copy to clipboard

where the index `j` and coefficient `g` are the integral and fractional components of `q * (n-1)`, and `n` is the number of elements in the sample.

This is a special case of Equation 1 of H&F [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#re01cd3f3acfe-1)
. More generally,

*   `j = (q*n + m - 1) // 1`, and
    
*   `g = (q*n + m - 1) % 1`,
    

where `m` may be defined according to several different conventions. The preferred convention may be selected using the `method` parameter:

| `method` | number in H&F | `m` |
| --- | --- | --- |
| `interpolated_inverted_cdf` | 4   | `0` |
| `hazen` | 5   | `1/2` |
| `weibull` | 6   | `q` |
| `linear` (default) | 7   | `1 - q` |
| `median_unbiased` | 8   | `q/3 + 1/3` |
| `normal_unbiased` | 9   | `q/4 + 3/8` |

Note that indices `j` and `j + 1` are clipped to the range `0` to `n - 1` when the results of the formula would be outside the allowed range of non-negative indices. The `- 1` in the formulas for `j` and `g` accounts for Python’s 0-based indexing.

The table above includes only the estimators from H&F that are continuous functions of probability _q_ (estimators 4-9). NumPy also provides the three discontinuous estimators from H&F (estimators 1-3), where `j` is defined as above, `m` is defined as follows, and `g` is a function of the real-valued `index = q*n + m - 1` and `j`.

1.  `inverted_cdf`: `m = 0` and `g = int(index - j > 0)`
    
2.  `averaged_inverted_cdf`: `m = 0` and `g = (1 + int(index - j > 0)) / 2`
    
3.  `closest_observation`: `m = -1/2` and `g = 1 - int((index == j) & (j%2 == 1))`
    

For backward compatibility with previous versions of NumPy, [`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")
 provides four additional discontinuous estimators. Like `method='linear'`, all have `m = 1 - q` so that `j = q*(n-1) // 1`, but `g` is defined as follows.

*   `lower`: `g = 0`
    
*   `midpoint`: `g = 0.5`
    
*   `higher`: `g = 1`
    
*   `nearest`: `g = (q*(n-1) % 1) > 0.5`
    

**Weighted quantiles:** More formally, the quantile at probability level \\(q\\) of a cumulative distribution function \\(F(y)=P(Y \\leq y)\\) with probability measure \\(P\\) is defined as any number \\(x\\) that fulfills the _coverage conditions_

\\\[P(Y < x) \\leq q \\quad\\text{and}\\quad P(Y \\leq x) \\geq q\\\]

with random variable \\(Y\\sim P\\). Sample quantiles, the result of [`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")
, provide nonparametric estimation of the underlying population counterparts, represented by the unknown \\(F\\), given a data vector _a_ of length `n`.

Some of the estimators above arise when one considers \\(F\\) as the empirical distribution function of the data, i.e. \\(F(y) = \\frac{1}{n} \\sum\_i 1\_{a\_i \\leq y}\\). Then, different methods correspond to different choices of \\(x\\) that fulfill the above coverage conditions. Methods that follow this approach are `inverted_cdf` and `averaged_inverted_cdf`.

For weighted quantiles, the coverage conditions still hold. The empirical cumulative distribution is simply replaced by its weighted version, i.e. \\(P(Y \\leq t) = \\frac{1}{\\sum\_i w\_i} \\sum\_i w\_i 1\_{x\_i \\leq t}\\). Only `method="inverted_cdf"` supports weights.

References

\[1\] ([1](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#id1)
,[2](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#id2)
)

R. J. Hyndman and Y. Fan, “Sample quantiles in statistical packages,” The American Statistician, 50(4), pp. 361-365, 1996

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[10, 7, 4\], \[3, 2, 1\]\])
\>>> a
array(\[\[10,  7,  4\],\
       \[ 3,  2,  1\]\])
\>>> np.quantile(a, 0.5)
3.5
\>>> np.quantile(a, 0.5, axis\=0)
array(\[6.5, 4.5, 2.5\])
\>>> np.quantile(a, 0.5, axis\=1)
array(\[7.,  2.\])
\>>> np.quantile(a, 0.5, axis\=1, keepdims\=True)
array(\[\[7.\],\
       \[2.\]\])
\>>> m \= np.quantile(a, 0.5, axis\=0)
\>>> out \= np.zeros\_like(m)
\>>> np.quantile(a, 0.5, axis\=0, out\=out)
array(\[6.5, 4.5, 2.5\])
\>>> m
array(\[6.5, 4.5, 2.5\])
\>>> b \= a.copy()
\>>> np.quantile(b, 0.5, axis\=1, overwrite\_input\=True)
array(\[7.,  2.\])
\>>> assert not np.all(a \== b)

Copy to clipboard

See also [`numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
 for a visualization of most methods.

Go BackOpen In Tab

On this page