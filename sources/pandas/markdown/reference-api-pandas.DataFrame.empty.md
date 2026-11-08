[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.empty[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#pandas-dataframe-empty "Link to this heading")

==================================================================================================================================================

property DataFrame.empty[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1906-L1964)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#pandas.DataFrame.empty "Link to this definition")

Indicator whether Series/DataFrame is empty.

True if Series/DataFrame is entirely empty (no items), meaning any of the axes are of length 0.

Returns:

bool

If Series/DataFrame is empty, return True, if not return False.

See also

[`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")

Return series without null values.

[`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")

Return DataFrame with labels on given axis omitted where (all or any) data are missing.

Notes

If Series/DataFrame contains only NaNs, it is still not considered empty. See the example below.

Examples

An example of an actual empty DataFrame. Notice the index is empty:

\>>> df\_empty \= pd.DataFrame({"A": \[\]})
\>>> df\_empty
Empty DataFrame
Columns: \[A\]
Index: \[\]
\>>> df\_empty.empty
True

Copy to clipboard

If we only have NaNs in our DataFrame, it is not considered empty! We will need to drop the NaNs to make the DataFrame empty:

\>>> df \= pd.DataFrame({"A": \[np.nan\]})
\>>> df
    A
0 NaN
\>>> df.empty
False
\>>> df.dropna().empty
True

Copy to clipboard

\>>> ser\_empty \= pd.Series({"A": \[\]})
\>>> ser\_empty
A    \[\]
dtype: object
\>>> ser\_empty.empty
False
\>>> ser\_empty \= pd.Series()
\>>> ser\_empty.empty
True

Copy to clipboard

On this page