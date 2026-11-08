[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sum.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sum.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sum.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sum.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sum.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sum.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sum.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sum.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sum.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sum.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sum.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sum.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sum[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas-series-sum "Link to this heading")

===================================================================================================================================

Series.sum(_\*_, _axis\=None_, _skipna\=True_, _numeric\_only\=False_, _min\_count\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9449-L9549)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "Link to this definition")

Return the sum of the values over the requested axis.

This is equivalent to the method `numpy.sum`.

Parameters:

**axis**{index (0)}

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

Warning

The behavior of DataFrame.sum with `axis=None` is deprecated, in a future version this will reduce over both axes and return a scalar To retain the old behavior, pass axis=0 (or do not pass axis).

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

Sum of the values for the requested axis.

See also

[`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "(in NumPy v2.5)")

Equivalent numpy function for computing sum.

[`Series.mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "pandas.Series.mean")

Mean of the values.

[`Series.median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")

Median of the values.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Standard deviation of the values.

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Variance of the values.

[`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")

Minimum value.

[`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")

Maximum value.

Examples

\>>> idx \= pd.MultiIndex.from\_arrays(
...     \[\["warm", "warm", "cold", "cold"\], \["dog", "falcon", "fish", "spider"\]\],
...     names\=\["blooded", "animal"\],
... )
\>>> s \= pd.Series(\[4, 2, 0, 8\], name\="legs", index\=idx)
\>>> s
blooded  animal
warm     dog       4
         falcon    2
cold     fish      0
         spider    8
Name: legs, dtype: int64

Copy to clipboard

\>>> s.sum()
14

Copy to clipboard

By default, the sum of an empty or all-NA Series is `0`.

\>>> pd.Series(\[\], dtype\="float64").sum()  \# min\_count=0 is the default
0.0

Copy to clipboard

This can be controlled with the `min_count` parameter. For example, if you’d like the sum of an empty series to be NaN, pass `min_count=1`.

\>>> pd.Series(\[\], dtype\="float64").sum(min\_count\=1)
nan

Copy to clipboard

Thanks to the `skipna` parameter, `min_count` handles all-NA and empty series identically.

\>>> pd.Series(\[np.nan\]).sum()
0.0

Copy to clipboard

\>>> pd.Series(\[np.nan\]).sum(min\_count\=1)
nan

Copy to clipboard

On this page