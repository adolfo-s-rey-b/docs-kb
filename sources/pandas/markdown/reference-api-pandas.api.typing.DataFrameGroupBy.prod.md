[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.prod[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html#pandas-api-typing-dataframegroupby-prod "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.prod(_numeric\_only\=False_, _min\_count\=0_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L2866-L2952)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html#pandas.api.typing.DataFrameGroupBy.prod "Link to this definition")

Compute prod of group values.

This method computes the product of all values within each group, returning a result for each group.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None`.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

Added in version 3.0.0.

Returns:

Series or DataFrame

Computed prod of values within each group.

See also

`Series.prod`

Return the product of the values over the requested axis.

`DataFrame.prod`

Return the product of the values over the requested axis.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3, 4\], index\=lst)
\>>> ser
a    1
a    2
b    3
b    4
dtype: int64
\>>> ser.groupby(level\=0).prod()
a    2
b   12
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 8, 2\], \[1, 2, 5\], \[2, 5, 8\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data,
...     columns\=\["a", "b", "c"\],
...     index\=\["tiger", "leopard", "cheetah", "lion"\],
... )
\>>> df
          a  b  c
  tiger   1  8  2
leopard   1  2  5
cheetah   2  5  8
   lion   2  6  9
\>>> df.groupby("a").prod()
     b    c
a
1   16   10
2   30   72

Copy to clipboard

On this page