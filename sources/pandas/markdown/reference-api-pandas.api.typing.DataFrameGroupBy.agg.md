[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.agg.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.agg[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.agg.html#pandas-api-typing-dataframegroupby-agg "Link to this heading")

==================================================================================================================================================================================================

DataFrameGroupBy.agg(_func\=None_, _\*args_, _engine\=None_, _engine\_kwargs\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L2076-L2312)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.agg.html#pandas.api.typing.DataFrameGroupBy.agg "Link to this definition")

Aggregate using one or more operations.

The `aggregate` function allows the application of one or more aggregation operations on groups of data within a DataFrameGroupBy object. It supports various aggregation methods, including user-defined functions and predefined functions such as ‘sum’, ‘mean’, etc.

Parameters:

**func**function, str, list, dict or None

Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply.

Accepted combinations are:

*   function
    
*   string function name
    
*   list of functions and/or function names, e.g. `[np.sum, 'mean']`
    
*   dict of index labels -> functions, function names or list of such.
    
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

DataFrame

Aggregated DataFrame based on the grouping and the applied aggregation functions.

See also

`DataFrame.groupby.apply`

Apply function func group-wise and combine the results together.

`DataFrame.groupby.transform`

Transforms the Series on each group based on the given function.

`DataFrame.aggregate`

Aggregate using one or more operations.

Notes

See [Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-aggregate)
 in the User Guide for more details and examples.

When using `engine='numba'`, there will be no “fall back” behavior internally. The group data and group index will be passed as numpy arrays to the JITed user defined function, and no alternative execution attempts will be tried.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

The resulting dtype will reflect the return value of the passed `func`, see the examples below.

Examples

\>>> data \= {
...     "A": \[1, 1, 2, 2\],
...     "B": \[1, 2, 3, 4\],
...     "C": \[0.362838, 0.227877, 1.267767, \-0.562860\],
... }
\>>> df \= pd.DataFrame(data)
\>>> df
   A  B         C
0  1  1  0.362838
1  1  2  0.227877
2  2  3  1.267767
3  2  4 -0.562860

Copy to clipboard

The aggregation is for each column.

\>>> df.groupby("A").agg("min")
   B         C
A
1  1  0.227877
2  3 -0.562860

Copy to clipboard

Multiple aggregations

\>>> df.groupby("A").agg(\["min", "max"\])
    B             C
  min max       min       max
A
1   1   2  0.227877  0.362838
2   3   4 -0.562860  1.267767

Copy to clipboard

Select a column for aggregation

\>>> df.groupby("A").B.agg(\["min", "max"\])
   min  max
A
1    1    2
2    3    4

Copy to clipboard

User-defined function for aggregation

\>>> df.groupby("A").agg(lambda x: sum(x) + 2)
    B          C
A
1       5       2.590715
2       9       2.704907

Copy to clipboard

Different aggregations per column

\>>> df.groupby("A").agg({"B": \["min", "max"\], "C": "sum"})
    B             C
  min max       sum
A
1   1   2  0.590715
2   3   4  0.704907

Copy to clipboard

To control the output names with different aggregations per column, pandas supports “named aggregation”

\>>> df.groupby("A").agg(
...     b\_min\=pd.NamedAgg(column\="B", aggfunc\="min"),
...     c\_sum\=pd.NamedAgg(column\="C", aggfunc\="sum"),
... )
   b\_min     c\_sum
A
1      1  0.590715
2      3  0.704907

Copy to clipboard

*   The keywords are the _output_ column names
    
*   The values are tuples whose first element is the column to select and the second element is the aggregation to apply to that column. Pandas provides the `pandas.NamedAgg` namedtuple with the fields `['column', 'aggfunc']` to make it clearer what the arguments are. As usual, the aggregation can be a callable or a string alias.
    

See [Named aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-aggregate-named)
 for more.

The resulting dtype will reflect the return value of the aggregating function.

\>>> df.groupby("A")\[\["B"\]\].agg(lambda x: x.astype(float).min())
      B
A
1   1.0
2   3.0

Copy to clipboard

On this page