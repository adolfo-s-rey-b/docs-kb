[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.expanding[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas-dataframe-expanding "Link to this heading")

==============================================================================================================================================================

DataFrame.expanding(_min\_periods\=1_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L12453-L12524)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "Link to this definition")

Provide expanding window calculations.

An expanding window yields the value of an aggregation statistic with all the data available up to that point in time.

Parameters:

**min\_periods**int, default 1

Minimum number of observations in window required to have a value; otherwise, result is `np.nan`.

**method**str {‘single’, ‘table’}, default ‘single’

Execute the rolling operation per single column or row (`'single'`) or over the entire object (`'table'`).

This argument is only implemented when specifying `engine='numba'` in the method call.

Returns:

pandas.api.typing.Expanding

An instance of Expanding for further expanding window calculations, e.g. using the `sum` method.

See also

[`rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "pandas.DataFrame.rolling")

Provides rolling window calculations.

[`ewm`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html#pandas.DataFrame.ewm "pandas.DataFrame.ewm")

Provides exponential weighted functions.

Notes

See [Windowing Operations](https://pandas.pydata.org/docs/user_guide/window.html#window-expanding)
 for further usage details and examples.

Examples

\>>> df \= pd.DataFrame({"B": \[0, 1, 2, np.nan, 4\]})
\>>> df
     B
0  0.0
1  1.0
2  2.0
3  NaN
4  4.0

Copy to clipboard

**min\_periods**

Expanding sum with 1 vs 3 observations needed to calculate a value.

\>>> df.expanding(1).sum()
     B
0  0.0
1  1.0
2  3.0
3  3.0
4  7.0
\>>> df.expanding(3).sum()
     B
0  NaN
1  NaN
2  3.0
3  3.0
4  7.0

Copy to clipboard

On this page