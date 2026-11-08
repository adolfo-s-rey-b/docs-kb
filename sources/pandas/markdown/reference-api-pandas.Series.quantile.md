[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.quantile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.quantile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.quantile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.quantile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.quantile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.quantile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.quantile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.quantile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.quantile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.quantile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.quantile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.quantile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#pandas-series-quantile "Link to this heading")

==================================================================================================================================================

Series.quantile(_q\=0.5_, _interpolation\='linear'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2948-L3014)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#pandas.Series.quantile "Link to this definition")

Return value at the given quantile.

This method computes the value below which a given fraction of the data falls. When multiple quantiles are requested, a Series indexed by the quantile values is returned.

Parameters:

**q**float or array-like, default 0.5 (50% quantile)

The quantile(s) to compute, which can lie in range: 0 <= q <= 1.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

This optional parameter specifies the interpolation method to use, when the desired quantile lies between two data points i and j:

> *   linear: i + (j - i) \* (x-i)/(j-i), where (x-i)/(j-i) is the fractional part of the index surrounded by i > j.
>     
> *   lower: i.
>     
> *   higher: j.
>     
> *   nearest: i or j whichever is nearest.
>     
> *   midpoint: (i + j) / 2.
>     

Returns:

float or Series

If `q` is an array, a Series will be returned where the index is `q` and the values are the quantiles, otherwise a float will be returned.

See also

`core.window.Rolling.quantile`

Calculate the rolling quantile.

[`numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "(in NumPy v2.5)")

Returns the q-th percentile(s) of the array elements.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s.quantile(0.5)
2.5
\>>> s.quantile(\[0.25, 0.5, 0.75\])
0.25    1.75
0.50    2.50
0.75    3.25
dtype: float64

Copy to clipboard

On this page