[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.compare.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.compare.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.compare.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.compare.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.compare.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.compare.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.compare.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.compare.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.compare.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.compare.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.compare.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.compare.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.compare[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#pandas-series-compare "Link to this heading")

===============================================================================================================================================

Series.compare(_other_, _align\_axis\=1_, _keep\_shape\=False_, _keep\_equal\=False_, _result\_names\=('self', 'other')_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3596-L3700)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#pandas.Series.compare "Link to this definition")

Compare to another Series and show the differences.

This method aligns two Series and highlights only the values that differ between them. Equal values are shown as NaN by default.

Parameters:

**other**Series

Object to compare with.

**align\_axis**{0 or ‘index’, 1 or ‘columns’}, default 1

Determine which axis to align the comparison on.

*   0, or ‘index’ : Resulting differences are stacked vertically with rows drawn alternately from self and other.
    
*   1, or ‘columns’ : Resulting differences are aligned horizontally with columns drawn alternately from self and other.
    

**keep\_shape**bool, default False

If true, all rows and columns are kept. Otherwise, only the ones with different values are kept.

**keep\_equal**bool, default False

If true, the result keeps values that are equal. Otherwise, equal values are shown as NaNs.

**result\_names**tuple, default (‘self’, ‘other’)

Set the dataframes names in the comparison.

Returns:

Series or DataFrame

If axis is 0 or ‘index’ the result will be a Series. The resulting index will be a MultiIndex with ‘self’ and ‘other’ stacked alternately at the inner level.

If axis is 1 or ‘columns’ the result will be a DataFrame. It will have two columns namely ‘self’ and ‘other’.

See also

[`DataFrame.compare`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "pandas.DataFrame.compare")

Compare with another DataFrame and show differences.

Notes

Matching NaNs will not appear as a difference.

Examples

\>>> s1 \= pd.Series(\["a", "b", "c", "d", "e"\])
\>>> s2 \= pd.Series(\["a", "a", "c", "b", "e"\])

Copy to clipboard

Align the differences on columns

\>>> s1.compare(s2)
  self other
1    b     a
3    d     b

Copy to clipboard

Stack the differences on indices

\>>> s1.compare(s2, align\_axis\=0)
1  self     b
   other    a
3  self     d
   other    b
dtype: str

Copy to clipboard

Keep all original rows

\>>> s1.compare(s2, keep\_shape\=True)
  self other
0  NaN   NaN
1    b     a
2  NaN   NaN
3    d     b
4  NaN   NaN

Copy to clipboard

Keep all original rows and also all original values

\>>> s1.compare(s2, keep\_shape\=True, keep\_equal\=True)
  self other
0    a     a
1    b     a
2    c     c
3    d     b
4    e     e

Copy to clipboard

On this page