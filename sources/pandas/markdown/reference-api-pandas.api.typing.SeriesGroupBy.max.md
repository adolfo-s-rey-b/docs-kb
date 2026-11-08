[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.max.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.max.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.max.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.max[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.max.html#pandas-api-typing-seriesgroupby-max "Link to this heading")

=========================================================================================================================================================================================

SeriesGroupBy.max(_numeric\_only\=False_, _min\_count\=\-1_, _skipna\=True_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3078-L3198)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.max.html#pandas.api.typing.SeriesGroupBy.max "Link to this definition")

Compute max of group values.

Returns the maximum value for each group. Missing values are excluded by default but this behavior can be controlled with the `skipna` parameter.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None`.

**min\_count**int, default -1

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

**skipna**bool, default True

Exclude NA/null values. If the entire group is NA and `skipna` is `True`, the result will be NA.

Changed in version 3.0.0.

**engine**str, default None None

*   `'cython'` : Runs rolling apply through C-extensions from cython.
    
*   `'numba'`Runs rolling apply through JIT compiled code from numba.
    
    Only available when `raw` is set to `True`.
    
*   `None`Defaults to `'cython'` or globally setting
    
    `compute.use_numba`
    

**engine\_kwargs**dict, default None None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil`
    
    and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}` and will be applied to both the `func` and the `apply` groupby aggregation.
    

Returns:

Series or DataFrame

Computed max of values within each group.

See also

`Series.max`

Return the maximum of the values over the requested axis.

`DataFrame.max`

Return the maximum of the values over the requested axis.

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
\>>> ser.groupby(level\=0).max()
a    2
b    4
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
\>>> df.groupby("a").max()
    b  c
a
1   8  5
2   6  9

Copy to clipboard

On this page