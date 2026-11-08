[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.agg[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas-series-agg "Link to this heading")

===================================================================================================================================

Series.agg(_func\=None_, _axis\=0_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5206-L5296)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "Link to this definition")

Aggregate using one or more operations over the specified axis.

This method applies one or more aggregation functions to the Series and returns a scalar, Series, or DataFrame depending on the function(s) provided.

Parameters:

**func**function, str, list or dict

Function to use for aggregating the data. If a function, must either work when passed a Series or when passed to Series.apply.

Accepted combinations are:

*   function
    
*   string function name
    
*   list of functions and/or function names, e.g. `[np.sum, 'mean']`
    
*   dict of axis labels -> functions, function names or list of such.
    

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns:

scalar, Series or DataFrame

The return can be:

*   scalar : when Series.agg is called with single function
    
*   Series : when DataFrame.agg is called with a single function
    
*   DataFrame : when DataFrame.agg is called with several functions
    

See also

[`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")

Invoke function on a Series.

[`Series.transform`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")

Transform function producing a Series with like indexes.

Notes

The aggregation operations are always performed over an axis, either the index (default) or the column axis. This behavior is different from numpy aggregation functions (mean, median, prod, sum, std, var), where the default is to compute the aggregation of the flattened array, e.g., `numpy.mean(arr_2d)` as opposed to `numpy.mean(arr_2d, axis=0)`.

agg is an alias for aggregate. Use the alias.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

A passed user-defined-function will be passed a Series for evaluation.

If `func` defines an index relabeling, `axis` must be `0` or `index`.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s
0    1
1    2
2    3
3    4
dtype: int64

Copy to clipboard

\>>> s.agg("min")
1

Copy to clipboard

\>>> s.agg(\["min", "max"\])
min   1
max   4
dtype: int64

Copy to clipboard

On this page