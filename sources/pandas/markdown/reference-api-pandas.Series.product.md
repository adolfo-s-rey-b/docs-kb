[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.product.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.product.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.product.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.product.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.product.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.product.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.product.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.product.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.product.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.product.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.product.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.product.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.product[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html#pandas-series-product "Link to this heading")

===============================================================================================================================================

Series.product(_\*_, _axis\=None_, _skipna\=True_, _numeric\_only\=False_, _min\_count\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9551-L9635)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html#pandas.Series.product "Link to this definition")

Return the product of the values over the requested axis.

By default, missing values are skipped. To include them in the calculation, set `skipna` parameter to False.

Parameters:

**axis**{index (0)}

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

Warning

The behavior of DataFrame.prod with `axis=None` is deprecated, in a future version this will reduce over both axes and return a scalar To retain the old behavior, pass axis=0 (or do not pass axis).

Added in version 2.0.0.

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

**\*\*kwargs**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

scalar

Value containing the calculation referenced in the description.

See also

[`Series.sum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "pandas.Series.sum")

Return the sum.

[`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")

Return the minimum.

[`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")

Return the maximum.

[`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")

Return the index of the minimum.

[`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")

Return the index of the maximum.

[`DataFrame.sum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "pandas.DataFrame.sum")

Return the sum over the requested axis.

[`DataFrame.min`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min "pandas.DataFrame.min")

Return the minimum over the requested axis.

[`DataFrame.max`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max "pandas.DataFrame.max")

Return the maximum over the requested axis.

[`DataFrame.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin "pandas.DataFrame.idxmin")

Return the index of the minimum over the requested axis.

[`DataFrame.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax "pandas.DataFrame.idxmax")

Return the index of the maximum over the requested axis.

Examples

By default, the product of an empty or all-NA Series is `1`

\>>> pd.Series(\[\], dtype\="float64").prod()
1.0

Copy to clipboard

This can be controlled with the `min_count` parameter

\>>> pd.Series(\[\], dtype\="float64").prod(min\_count\=1)
nan

Copy to clipboard

Thanks to the `skipna` parameter, `min_count` handles all-NA and empty series identically.

\>>> pd.Series(\[np.nan\]).prod()
1.0
\>>> pd.Series(\[np.nan\]).prod(min\_count\=1)
nan

Copy to clipboard

On this page