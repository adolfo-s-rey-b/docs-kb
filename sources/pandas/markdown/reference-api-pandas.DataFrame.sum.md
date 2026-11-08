[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sum.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sum.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sum.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sum.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sum.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sum.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sum.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sum.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sum.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sum.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sum.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sum.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sum[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas-dataframe-sum "Link to this heading")

============================================================================================================================================

DataFrame.sum(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _min\_count\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L17755-L17855)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "Link to this definition")

Return the sum of the values over the requested axis.

This is equivalent to the method `numpy.sum`.

Parameters:

**axis**{index (0), columns (1)}, default 0

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

Series or scalar

Sum over requested axis.

See also

[`Series.sum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "pandas.Series.sum")

Return the sum over Series values.

[`DataFrame.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean "pandas.DataFrame.mean")

Return the mean of the values over the requested axis.

[`DataFrame.median`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html#pandas.DataFrame.median "pandas.DataFrame.median")

Return the median of the values over the requested axis.

[`DataFrame.mode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas.DataFrame.mode "pandas.DataFrame.mode")

Get the mode(s) of each element along the requested axis.

[`DataFrame.std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")

Return the standard deviation of the values over the requested axis.

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