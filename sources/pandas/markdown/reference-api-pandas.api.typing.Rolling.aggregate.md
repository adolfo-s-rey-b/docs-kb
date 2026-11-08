[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.aggregate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.aggregate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.aggregate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.aggregate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.aggregate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.aggregate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.aggregate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.aggregate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.aggregate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.aggregate[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.aggregate.html#pandas-api-typing-rolling-aggregate "Link to this heading")

=========================================================================================================================================================================================

Rolling.aggregate(_func\=None_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2040-L2122)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.aggregate.html#pandas.api.typing.Rolling.aggregate "Link to this definition")

Aggregate using one or more operations over the specified axis.

This method allows combining multiple aggregation functions (e.g. `'sum'`, `'mean'`) in a single call, returning a result for each function applied to each rolling window.

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

`Series.rolling`

Calling object with Series data.

`DataFrame.rolling`

Calling object with DataFrame data.

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

\>>> df.rolling(2).sum()
    A     B     C
0  NaN   NaN   NaN
1  3.0   9.0  15.0
2  5.0  11.0  17.0

Copy to clipboard

\>>> df.rolling(2).agg({"A": "sum", "B": "min"})
    A    B
0  NaN  NaN
1  3.0  4.0
2  5.0  5.0

Copy to clipboard

On this page