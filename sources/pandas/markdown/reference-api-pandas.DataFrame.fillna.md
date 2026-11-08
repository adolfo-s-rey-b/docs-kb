[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.fillna[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas-dataframe-fillna "Link to this heading")

=====================================================================================================================================================

DataFrame.fillna(_value_, _\*_, _axis\=None_, _inplace\=False_, _limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L7229-L7471)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "Link to this definition")

Fill NA/NaN values with value.

This method replaces missing values with a specified value.

Parameters:

**value**scalar, dict, Series, or DataFrame

Value to use to fill holes (e.g. 0), alternately a dict/Series/DataFrame of values specifying which value to use for each index (for a Series) or column (for a DataFrame). Values not in the dict/Series/DataFrame will not be filled. This value cannot be a list.

**axis**{0 or ‘index’} for Series, {0 or ‘index’, 1 or ‘columns’} for DataFrame

Axis along which to fill missing values. For Series this parameter is unused and defaults to 0.

**inplace**bool, default False

If True, fill in-place. Note: this will modify any other views on this object (e.g., a no-copy slice for a column in a DataFrame).

**limit**int, default None

This is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None.

Returns:

Series/DataFrame

Object with missing values filled.

See also

[`ffill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas.DataFrame.ffill "pandas.DataFrame.ffill")

Fill values by propagating the last valid observation to next valid.

[`bfill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html#pandas.DataFrame.bfill "pandas.DataFrame.bfill")

Fill values by using the next valid observation to fill the gap.

[`interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "pandas.DataFrame.interpolate")

Fill NaN values using interpolation.

[`reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")

Conform object to new index.

[`asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html#pandas.DataFrame.asfreq "pandas.DataFrame.asfreq")

Convert TimeSeries to specified frequency.

Notes

For non-object dtype, `value=None` will use the NA value of the dtype. See more details in the [Filling missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data-fillna)
 section.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         \[np.nan, 2, np.nan, 0\],\
...         \[3, 4, np.nan, 1\],\
...         \[np.nan, np.nan, np.nan, np.nan\],\
...         \[np.nan, 3, np.nan, 4\],\
...     \],
...     columns\=list("ABCD"),
... )
\>>> df
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  NaN  NaN NaN  NaN
3  NaN  3.0 NaN  4.0

Copy to clipboard

Replace all NaN elements with 0s.

\>>> df.fillna(0)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  0.0
3  0.0  3.0  0.0  4.0

Copy to clipboard

Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively.

\>>> values \= {"A": 0, "B": 1, "C": 2, "D": 3}
\>>> df.fillna(value\=values)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  2.0  1.0
2  0.0  1.0  2.0  3.0
3  0.0  3.0  2.0  4.0

Copy to clipboard

Only replace the first NaN element.

\>>> df.fillna(value\=values, limit\=1)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  NaN  1.0
2  NaN  1.0  NaN  3.0
3  NaN  3.0  NaN  4.0

Copy to clipboard

When filling using a DataFrame, replacement happens along the same column names and same indices

\>>> df2 \= pd.DataFrame(np.zeros((4, 4)), columns\=list("ABCE"))
\>>> df.fillna(df2)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  NaN
3  0.0  3.0  0.0  4.0

Copy to clipboard

Note that column D is not affected since it is not present in df2.

On this page