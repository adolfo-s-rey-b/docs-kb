[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.agg.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.agg.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.agg.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.agg.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.agg.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.agg.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.agg.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.agg.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.agg.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.agg.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.agg.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.agg.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.agg[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas-dataframe-agg "Link to this heading")

============================================================================================================================================

DataFrame.agg(_func\=None_, _axis\=0_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14898-L15017)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "Link to this definition")

Aggregate using one or more operations over the specified axis.

This method allows combining multiple aggregation functions at once, such as `sum`, `mean`, and `min`, and can apply them either per-column or per-row. It accepts functions as strings, callables, lists, or dictionaries mapping column labels to the desired aggregation(s).

Parameters:

**func**function, str, list or dict

Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply.

Accepted combinations are:

*   function
    
*   string function name
    
*   list of functions and/or function names, e.g. `[np.sum, 'mean']`
    
*   dict of axis labels -> functions, function names or list of such.
    

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

If 0 or ‘index’: apply function to each column. If 1 or ‘columns’: apply function to each row.

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

[`DataFrame.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")

Perform any type of operations.

[`DataFrame.transform`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")

Perform transformation type operations.

[`DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")

Perform operations over groups.

[`DataFrame.resample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample "pandas.DataFrame.resample")

Perform operations over resampled bins.

[`DataFrame.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "pandas.DataFrame.rolling")

Perform operations over rolling window.

[`DataFrame.expanding`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "pandas.DataFrame.expanding")

Perform operations over expanding window.

`core.window.ewm.ExponentialMovingWindow`

Perform operation over exponential weighted window.

Notes

The aggregation operations are always performed over an axis, either the index (default) or the column axis. This behavior is different from numpy aggregation functions (mean, median, prod, sum, std, var), where the default is to compute the aggregation of the flattened array, e.g., `numpy.mean(arr_2d)` as opposed to `numpy.mean(arr_2d, axis=0)`.

agg is an alias for aggregate. Use the alias.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

A passed user-defined-function will be passed a Series for evaluation.

If `func` defines an index relabeling, `axis` must be `0` or `index`.

Examples

\>>> df \= pd.DataFrame(
...     \[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], \[np.nan, np.nan, np.nan\]\],
...     columns\=\["A", "B", "C"\],
... )

Copy to clipboard

Aggregate these functions over the rows.

\>>> df.agg(\["sum", "min"\])
        A     B     C
sum  12.0  15.0  18.0
min   1.0   2.0   3.0

Copy to clipboard

Different aggregations per column.

\>>> df.agg({"A": \["sum", "min"\], "B": \["min", "max"\]})
        A    B
sum  12.0  NaN
min   1.0  2.0
max   NaN  8.0

Copy to clipboard

Aggregate different functions over the columns and rename the index of the resulting DataFrame.

\>>> df.agg(x\=("A", "max"), y\=("B", "min"), z\=("C", "mean"))
     A    B    C
x  7.0  NaN  NaN
y  NaN  2.0  NaN
z  NaN  NaN  6.0

Copy to clipboard

Aggregate over the columns.

\>>> df.agg("mean", axis\="columns")
0    2.0
1    5.0
2    8.0
3    NaN
dtype: float64

Copy to clipboard

On this page