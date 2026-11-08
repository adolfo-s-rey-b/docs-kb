[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.quantile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.quantile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.quantile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.quantile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.quantile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.quantile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.quantile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.quantile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.quantile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.quantile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.quantile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.quantile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html#pandas-dataframe-quantile "Link to this heading")

===========================================================================================================================================================

DataFrame.quantile(_q\=0.5_, _axis\=0_, _numeric\_only\=False_, _interpolation\='linear'_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19624-L19804)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html#pandas.DataFrame.quantile "Link to this definition")

Return values at the given quantile over requested axis.

This method computes the value below which a given proportion of observations fall. By default, it computes quantiles column-wise, but row-wise computation is also supported via `axis=1`.

Parameters:

**q**float or array-like, default 0.5 (50% quantile)

Value between 0 <= q <= 1, the quantile(s) to compute.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Equals 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

This optional parameter specifies the interpolation method to use, when the desired quantile lies between two data points i and j:

*   linear: i + (j - i) \* fraction, where fraction is the fractional part of the index surrounded by i and j.
    
*   lower: i.
    
*   higher: j.
    
*   nearest: i or j whichever is nearest.
    
*   midpoint: (i + j) / 2.
    

**method**{‘single’, ‘table’}, default ‘single’

Whether to compute quantiles per-column (‘single’) or over all columns (‘table’). When ‘table’, the only allowed interpolation methods are ‘nearest’, ‘lower’, and ‘higher’.

Returns:

Series or DataFrame

If `q` is an array, a DataFrame will be returned where the

index is `q`, the columns are the columns of self, and the values are the quantiles.

If `q` is a float, a Series will be returned where the

index is the columns of self and the values are the quantiles.

See also

`core.window.rolling.Rolling.quantile`

Rolling quantile.

[`numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "(in NumPy v2.5)")

Numpy function to compute the percentile.

Examples

\>>> df \= pd.DataFrame(
...     np.array(\[\[1, 1\], \[2, 10\], \[3, 100\], \[4, 100\]\]), columns\=\["a", "b"\]
... )
\>>> df.quantile(0.1)
a    1.3
b    3.7
Name: 0.1, dtype: float64
\>>> df.quantile(\[0.1, 0.5\])
       a     b
0.1  1.3   3.7
0.5  2.5  55.0

Copy to clipboard

Specifying method=’table’ will compute the quantile over all columns.

\>>> df.quantile(0.1, method\="table", interpolation\="nearest")
a    1
b    1
Name: 0.1, dtype: int64
\>>> df.quantile(\[0.1, 0.5\], method\="table", interpolation\="nearest")
     a    b
0.1  1    1
0.5  3  100

Copy to clipboard

Specifying numeric\_only=False will compute the quantiles for all columns.

\>>> df \= pd.DataFrame(
...     {
...         "A": \[1, 2\],
...         "B": \[pd.Timestamp("2010"), pd.Timestamp("2011")\],
...         "C": \[pd.Timedelta("1 days"), pd.Timedelta("2 days")\],
...     }
... )
\>>> df.quantile(0.5, numeric\_only\=False)
A                    1.5
B    2010-07-02 12:00:00
C        1 days 12:00:00
Name: 0.5, dtype: object

Copy to clipboard

On this page