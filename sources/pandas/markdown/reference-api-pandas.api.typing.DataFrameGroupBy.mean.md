[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html#pandas-api-typing-dataframegroupby-mean "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.mean(_numeric\_only\=False_, _skipna\=True_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L1981-L2085)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html#pandas.api.typing.DataFrameGroupBy.mean "Link to this definition")

Compute mean of groups, excluding missing values.

Returns the arithmetic mean for each group. Missing values are ignored unless the entire group is NA, in which case the result for that group is NA.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None` and defaults to `False`.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

**engine**str, default None

*   `'cython'` : Runs the operation through C-extensions from cython.
    
*   `'numba'` : Runs the operation through JIT compiled code from numba.
    
*   `None` : Defaults to `'cython'` or globally setting `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}`
    

Returns:

pandas.Series or pandas.DataFrame

Mean of values within each group. Same object type as the caller.

See also

`Series.mean`

Apply function mean to a Series.

`DataFrame.mean`

Apply function mean to each row or column of a DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[1, 1, 2, 1, 2\], "B": \[np.nan, 2, 3, 4, 5\], "C": \[1, 2, 1, 1, 2\]},
...     columns\=\["A", "B", "C"\],
... )

Copy to clipboard

Groupby one column and return the mean of the remaining columns in each group.

\>>> df.groupby("A").mean()
     B         C
A
1  3.0  1.333333
2  4.0  1.500000

Copy to clipboard

Groupby two columns and return the mean of the remaining column.

\>>> df.groupby(\["A", "B"\]).mean()
         C
A B
1 2.0  2.0
  4.0  1.0
2 3.0  1.0
  5.0  2.0

Copy to clipboard

Groupby one column and return the mean of only particular column in the group.

\>>> df.groupby("A")\["B"\].mean()
A
1    3.0
2    4.0
Name: B, dtype: float64

Copy to clipboard

On this page