[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.std[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.std.html#pandas-api-typing-seriesgroupby-std "Link to this heading")

=========================================================================================================================================================================================

SeriesGroupBy.std(_ddof\=1_, _engine\=None_, _engine\_kwargs\=None_, _numeric\_only\=False_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L2186-L2305)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.std.html#pandas.api.typing.SeriesGroupBy.std "Link to this definition")

Compute standard deviation of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex.

Parameters:

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

**engine**str, default None

*   `'cython'` : Runs the operation through C-extensions from cython.
    
*   `'numba'` : Runs the operation through JIT compiled code from numba.
    
*   `None` : Defaults to `'cython'` or globally setting `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}`
    

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: numeric\_only now defaults to `False`.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

Added in version 3.0.0.

Returns:

Series or DataFrame

Standard deviation of values within each group.

See also

`Series.std`

Apply function std to a Series.

`DataFrame.std`

Apply function std to each row or column of a DataFrame.

Notes

To have the same behaviour as `numpy.std`, use `ddof=0` (instead of the default `ddof=1`) and `skipna=False`.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[7, 2, 8, 4, 3, 3\], index\=lst)
\>>> ser
a     7
a     2
a     8
b     4
b     3
b     3
dtype: int64
\>>> ser.groupby(level\=0).std()
a    3.21455
b    0.57735
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= {"a": \[1, 3, 5, 7, 7, 8, 3\], "b": \[1, 4, 8, 4, 4, 2, 1\]}
\>>> df \= pd.DataFrame(
...     data, index\=\["dog", "dog", "dog", "mouse", "mouse", "mouse", "mouse"\]
... )
\>>> df
         a  b
  dog    1  1
  dog    3  4
  dog    5  8
mouse    7  4
mouse    7  4
mouse    8  2
mouse    3  1
\>>> df.groupby(level\=0).std()
              a         b
dog    2.000000  3.511885
mouse  2.217356  1.500000

Copy to clipboard

On this page