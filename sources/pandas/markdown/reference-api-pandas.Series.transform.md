[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.transform.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.transform.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.transform.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.transform.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.transform.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.transform.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.transform.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.transform.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.transform.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.transform.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.transform.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.transform.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.transform[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas-series-transform "Link to this heading")

=====================================================================================================================================================

Series.transform(_func_, _axis\=0_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5300-L5449)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "Link to this definition")

Call `func` on self producing a Series with the same axis shape as self.

Unlike `agg`, which can return a scalar or a smaller result, `transform` must return a result that is the same size as the input. This makes it suitable for element-wise operations.

Parameters:

**func**function, str, list-like or dict-like

Function to use for transforming the data. If a function, must either work when passed a Series or when passed to Series.apply. If func is both list-like and dict-like, dict-like behavior takes precedence.

Accepted combinations are:

*   function
    
*   string function name
    
*   list-like of functions and/or function names, e.g. `[np.exp, 'sqrt']`
    
*   dict-like of axis labels -> functions, function names or list-like of such
    

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns:

Series

A Series that must have the same length as self.

Raises:

**ValueError**If the returned Series has a different length than self.

See also

[`Series.agg`](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "pandas.Series.agg")

Only perform aggregating type operations.

[`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")

Invoke function on a Series.

Notes

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

Examples

\>>> df \= pd.DataFrame({"A": range(3), "B": range(1, 4)})
\>>> df
A  B
0  0  1
1  1  2
2  2  3
\>>> df.transform(lambda x: x + 1)
A  B
0  1  2
1  2  3
2  3  4

Copy to clipboard

Even though the resulting Series must have the same length as the input Series, it is possible to provide several input functions:

\>>> s \= pd.Series(range(3))
\>>> s
0    0
1    1
2    2
dtype: int64
\>>> s.transform(\[np.sqrt, np.exp\])
    sqrt        exp
0  0.000000   1.000000
1  1.000000   2.718282
2  1.414214   7.389056

Copy to clipboard

You can call transform on a GroupBy object:

\>>> df \= pd.DataFrame(
...     {
...         "Date": \[\
...             "2015-05-08",\
...             "2015-05-07",\
...             "2015-05-06",\
...             "2015-05-05",\
...             "2015-05-08",\
...             "2015-05-07",\
...             "2015-05-06",\
...             "2015-05-05",\
...         \],
...         "Data": \[5, 8, 6, 1, 50, 100, 60, 120\],
...     }
... )
\>>> df
        Date  Data
0  2015-05-08     5
1  2015-05-07     8
2  2015-05-06     6
3  2015-05-05     1
4  2015-05-08    50
5  2015-05-07   100
6  2015-05-06    60
7  2015-05-05   120
\>>> df.groupby("Date")\["Data"\].transform("sum")
0     55
1    108
2     66
3    121
4     55
5    108
6     66
7    121
Name: Data, dtype: int64

Copy to clipboard

\>>> df \= pd.DataFrame(
...     {
...         "c": \[1, 1, 1, 2, 2, 2, 2\],
...         "type": \["m", "n", "o", "m", "m", "n", "n"\],
...     }
... )
\>>> df
c type
0  1    m
1  1    n
2  1    o
3  2    m
4  2    m
5  2    n
6  2    n
\>>> df\["size"\] \= df.groupby("c")\["type"\].transform(len)
\>>> df
c type size
0  1    m    3
1  1    n    3
2  1    o    3
3  2    m    4
4  2    m    4
5  2    n    4
6  2    n    4

Copy to clipboard

On this page