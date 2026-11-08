[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.apply.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.apply.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.apply.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.apply.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.apply.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.apply.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.apply.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.apply.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.apply.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.apply.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.apply.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.apply.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.apply[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html#pandas-api-typing-resampler-apply "Link to this heading")

===================================================================================================================================================================================

Resampler.apply(_func\=None_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L345-L452)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html#pandas.api.typing.Resampler.apply "Link to this definition")

Aggregate using one or more operations over the specified axis.

This method applies aggregation functions to resampled groups, enabling summary statistics to be computed for each time period.

Parameters:

**func**function, str, list or dict

Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply.

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

`DataFrame.groupby.aggregate`

Aggregate using callable, string, dict, or list of string/callables.

`DataFrame.resample.transform`

Transforms the Series on each group based on the given function.

`DataFrame.aggregate`

Aggregate using one or more operations over the specified axis.

Notes

The aggregation operations are always performed over an axis, either the index (default) or the column axis. This behavior is different from numpy aggregation functions (mean, median, prod, sum, std, var), where the default is to compute the aggregation of the flattened array, e.g., `numpy.mean(arr_2d)` as opposed to `numpy.mean(arr_2d, axis=0)`.

agg is an alias for aggregate. Use the alias.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

A passed user-defined-function will be passed a Series for evaluation.

If `func` defines an index relabeling, `axis` must be `0` or `index`.

Examples

\>>> s \= pd.Series(
...     \[1, 2, 3, 4, 5\], index\=pd.date\_range("20130101", periods\=5, freq\="s")
... )
\>>> s
2013-01-01 00:00:00    1
2013-01-01 00:00:01    2
2013-01-01 00:00:02    3
2013-01-01 00:00:03    4
2013-01-01 00:00:04    5
Freq: s, dtype: int64

Copy to clipboard

\>>> r \= s.resample("2s")

Copy to clipboard

\>>> r.agg("sum")
2013-01-01 00:00:00    3
2013-01-01 00:00:02    7
2013-01-01 00:00:04    5
Freq: 2s, dtype: int64

Copy to clipboard

\>>> r.agg(\["sum", "mean", "max"\])
                    sum  mean  max
2013-01-01 00:00:00    3   1.5    2
2013-01-01 00:00:02    7   3.5    4
2013-01-01 00:00:04    5   5.0    5

Copy to clipboard

\>>> r.agg({"result": lambda x: x.mean() / x.std(), "total": "sum"})
                    result  total
2013-01-01 00:00:00  2.121320      3
2013-01-01 00:00:02  4.949747      7
2013-01-01 00:00:04       NaN      5

Copy to clipboard

\>>> r.agg(average\="mean", total\="sum")
                        average  total
2013-01-01 00:00:00      1.5      3
2013-01-01 00:00:02      3.5      7
2013-01-01 00:00:04      5.0      5

Copy to clipboard

On this page