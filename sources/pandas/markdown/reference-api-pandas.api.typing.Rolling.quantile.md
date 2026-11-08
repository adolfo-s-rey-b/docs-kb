[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.quantile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.quantile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.quantile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.quantile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.quantile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.quantile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.quantile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.quantile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.quantile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.quantile.html#pandas-api-typing-rolling-quantile "Link to this heading")

======================================================================================================================================================================================

Rolling.quantile(_q_, _interpolation\='linear'_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3152-L3217)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.quantile.html#pandas.api.typing.Rolling.quantile "Link to this definition")

Calculate the rolling quantile.

Return the `q`\-th quantile of the values in each rolling window. The `interpolation` parameter controls how quantiles falling between two data points are handled.

Parameters:

**q**float

Quantile to compute. 0 <= quantile <= 1.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

This optional parameter specifies the interpolation method to use, when the desired quantile lies between two data points i and j:

> *   linear: i + (j - i) \* fraction, where fraction is the fractional part of the index surrounded by i and j.
>     
> *   lower: i.
>     
> *   higher: j.
>     
> *   nearest: i or j whichever is nearest.
>     
> *   midpoint: (i + j) / 2.
>     

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.quantile`

Aggregating quantile for Series.

`DataFrame.quantile`

Aggregating quantile for DataFrame.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s.rolling(2).quantile(0.4, interpolation\="lower")
0    NaN
1    1.0
2    2.0
3    3.0
dtype: float64

Copy to clipboard

\>>> s.rolling(2).quantile(0.4, interpolation\="midpoint")
0    NaN
1    1.5
2    2.5
3    3.5
dtype: float64

Copy to clipboard

On this page