[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.agg.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.agg.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.agg[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.agg.html#pandas-api-typing-seriesgroupby-agg "Link to this heading")

=========================================================================================================================================================================================

SeriesGroupBy.agg(_func\=None_, _\*args_, _engine\=None_, _engine\_kwargs\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L324-L508)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.agg.html#pandas.api.typing.SeriesGroupBy.agg "Link to this definition")

Aggregate using one or more operations.

The `aggregate` method enables flexible and efficient aggregation of grouped data using a variety of functions, including built-in, user-defined, and optimized JIT-compiled functions.

Parameters:

**func**function, str, list or None

Function to use for aggregating the data. If a function, must either work when passed a Series or when passed to Series.apply.

Accepted combinations are:

*   function
    
*   string function name
    
*   list of functions and/or function names, e.g. `[np.sum, 'mean']`
    
*   None, in which case `**kwargs` are used with Named Aggregation. Here the output has one column for each element in `**kwargs`. The name of the column is keyword, whereas the value determines the aggregation used to compute the values in the column.
    
    Can also accept a Numba JIT function with `engine='numba'` specified. Only passing a single function is supported with this engine.
    
    If the `'numba'` engine is chosen, the function must be a user defined function with `values` and `index` as the first and second arguments respectively in the function signature. Each group’s index will be passed to the user defined function and optionally available for use.
    

**\*args**

Positional arguments to pass to func.

**engine**str, default None

*   `'cython'` : Runs the function through C-extensions from cython.
    
*   `'numba'` : Runs the function through JIT compiled code from numba.
    
*   `None`Defaults to `'cython'` or globally setting
    
    `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}` and will be applied to the function
    

**\*\*kwargs**

*   If `func` is None, `**kwargs` are used to define the output names and aggregations via Named Aggregation. See `func` entry.
    
*   Otherwise, keyword arguments to be passed into func.
    

Returns:

Series

Aggregated Series based on the grouping and the applied aggregation functions.

See also

[`SeriesGroupBy.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.apply.html#pandas.api.typing.SeriesGroupBy.apply "pandas.api.typing.SeriesGroupBy.apply")

Apply function func group-wise and combine the results together.

[`SeriesGroupBy.transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#pandas.api.typing.SeriesGroupBy.transform "pandas.api.typing.SeriesGroupBy.transform")

Transforms the Series on each group based on the given function.

`Series.aggregate`

Aggregate using one or more operations.

Notes

See [Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-aggregate)
 in the User Guide for more details and examples.

When using `engine='numba'`, there will be no “fall back” behavior internally. The group data and group index will be passed as numpy arrays to the JITed user defined function, and no alternative execution attempts will be tried.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

The resulting dtype will reflect the return value of the passed `func`, see the examples below.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])

Copy to clipboard

\>>> s
0    1
1    2
2    3
3    4
dtype: int64

Copy to clipboard

\>>> s.groupby(\[1, 1, 2, 2\]).min()
1    1
2    3
dtype: int64

Copy to clipboard

\>>> s.groupby(\[1, 1, 2, 2\]).agg("min")
1    1
2    3
dtype: int64

Copy to clipboard

\>>> s.groupby(\[1, 1, 2, 2\]).agg(\["min", "max"\])
   min  max
1    1    2
2    3    4

Copy to clipboard

The output column names can be controlled by passing the desired column names and aggregations as keyword arguments.

\>>> s.groupby(\[1, 1, 2, 2\]).agg(
...     minimum\="min",
...     maximum\="max",
... )
   minimum  maximum
1        1        2
2        3        4

Copy to clipboard

The resulting dtype will reflect the return value of the aggregating function.

\>>> s.groupby(\[1, 1, 2, 2\]).agg(lambda x: x.astype(float).min())
1    1.0
2    3.0
dtype: float64

Copy to clipboard

On this page