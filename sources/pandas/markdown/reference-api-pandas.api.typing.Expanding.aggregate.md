[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.aggregate.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.aggregate[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.aggregate.html#pandas-api-typing-expanding-aggregate "Link to this heading")

===============================================================================================================================================================================================

Expanding.aggregate(_func\=None_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L132-L213)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.aggregate.html#pandas.api.typing.Expanding.aggregate "Link to this definition")

Aggregate using one or more operations over the specified axis.

Accepts a function, string name, list, or dict of functions and applies them cumulatively over all data points seen so far.

Parameters:

**func**function, str, list or dict

Function to use for aggregating the data. If a function, must either work when passed a Series/Dataframe or when passed to Series/Dataframe.apply.

Accepted combinations are:

*   function
    
*   string function name
    
*   list of functions and/or function names, e.g. `[np.sum, 'mean']`
    
*   dict of axis labels -> functions, function names or list of such.
    

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

`DataFrame.aggregate`

Similar DataFrame method.

`Series.aggregate`

Similar Series method.

Notes

The aggregation operations are always performed over an axis, either the index (default) or the column axis. This behavior is different from numpy aggregation functions (mean, median, prod, sum, std, var), where the default is to compute the aggregation of the flattened array, e.g., `numpy.mean(arr_2d)` as opposed to `numpy.mean(arr_2d, axis=0)`.

agg is an alias for aggregate. Use the alias.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

A passed user-defined-function will be passed a Series for evaluation.

If `func` defines an index relabeling, `axis` must be `0` or `index`.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[4, 5, 6\], "C": \[7, 8, 9\]})
\>>> df
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

Copy to clipboard

\>>> df.expanding(2).sum()
     A     B     C
0  NaN   NaN   NaN
1  3.0   9.0  15.0
2  6.0  15.0  24.0

Copy to clipboard

\>>> df.expanding(2).agg({"A": "sum", "B": "min"})
     A    B
0  NaN  NaN
1  3.0  4.0
2  6.0  4.0

Copy to clipboard

On this page