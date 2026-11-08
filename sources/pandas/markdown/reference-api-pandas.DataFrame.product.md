[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.product[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html#pandas-dataframe-product "Link to this heading")

========================================================================================================================================================

DataFrame.product(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _min\_count\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L17857-L17948)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html#pandas.DataFrame.product "Link to this definition")

Return the product of the values over the requested axis.

This multiplies all values in each column (or row when `axis=1`) together, skipping missing values by default. An empty or all-NA column returns `1` unless `min_count` is specified.

Parameters:

**axis**{index (0), columns (1)}, default 0

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

Series or scalar

The product of the values over the requested axis.

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

Copy to clipboard

\>>> pd.Series(\[np.nan\]).prod(min\_count\=1)
nan

Copy to clipboard

On this page