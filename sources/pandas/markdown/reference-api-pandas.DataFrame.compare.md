[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.compare.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.compare.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.compare.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.compare.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.compare.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.compare.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.compare.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.compare.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.compare.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.compare.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.compare.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.compare.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.compare[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#pandas-dataframe-compare "Link to this heading")

========================================================================================================================================================

DataFrame.compare(_other_, _align\_axis\=1_, _keep\_shape\=False_, _keep\_equal\=False_, _result\_names\=('self', 'other')_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L12973-L13131)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "Link to this definition")

Compare to another DataFrame and show the differences.

This method compares two DataFrames element-wise and returns a DataFrame highlighting the differences.

Parameters:

**other**DataFrame

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

DataFrame

DataFrame that shows the differences stacked side by side.

If align\_axis is 0 or ‘index’, the resulting row index will be a MultiIndex with ‘self’ and ‘other’ stacked alternately at the inner level.

If align\_axis is 1 or ‘columns’ (the default), the resulting columns will be a MultiIndex with ‘self’ and ‘other’ stacked alternately at the inner level.

Raises:

ValueError

When the two DataFrames don’t have identical labels or shape.

See also

[`Series.compare`](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#pandas.Series.compare "pandas.Series.compare")

Compare with another Series and show differences.

[`DataFrame.equals`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#pandas.DataFrame.equals "pandas.DataFrame.equals")

Test whether two objects contain the same elements.

Notes

Matching NaNs will not appear as a difference.

Can only compare identically-labeled (i.e. same shape, identical row and column labels) DataFrames

Examples

\>>> df \= pd.DataFrame(
...     {
...         "col1": \["a", "a", "b", "b", "a"\],
...         "col2": \[1.0, 2.0, 3.0, np.nan, 5.0\],
...         "col3": \[1.0, 2.0, 3.0, 4.0, 5.0\],
...     },
...     columns\=\["col1", "col2", "col3"\],
... )
\>>> df
  col1  col2  col3
0    a   1.0   1.0
1    a   2.0   2.0
2    b   3.0   3.0
3    b   NaN   4.0
4    a   5.0   5.0

Copy to clipboard

\>>> df2 \= df.copy()
\>>> df2.loc\[0, "col1"\] \= "c"
\>>> df2.loc\[2, "col3"\] \= 4.0
\>>> df2
  col1  col2  col3
0    c   1.0   1.0
1    a   2.0   2.0
2    b   3.0   4.0
3    b   NaN   4.0
4    a   5.0   5.0

Copy to clipboard

Align the differences on columns

\>>> df.compare(df2)
  col1       col3
  self other self other
0    a     c  NaN   NaN
2  NaN   NaN  3.0   4.0

Copy to clipboard

Assign result\_names

\>>> df.compare(df2, result\_names\=("left", "right"))
  col1       col3
  left right left right
0    a     c  NaN   NaN
2  NaN   NaN  3.0   4.0

Copy to clipboard

Stack the differences on rows

\>>> df.compare(df2, align\_axis\=0)
        col1  col3
0 self     a   NaN
  other    c   NaN
2 self   NaN   3.0
  other  NaN   4.0

Copy to clipboard

Keep the equal values

\>>> df.compare(df2, keep\_equal\=True)
  col1       col3
  self other self other
0    a     c  1.0   1.0
2    b     b  3.0   4.0

Copy to clipboard

Keep all original rows and columns

\>>> df.compare(df2, keep\_shape\=True)
  col1       col2       col3
  self other self other self other
0    a     c  NaN   NaN  NaN   NaN
1  NaN   NaN  NaN   NaN  NaN   NaN
2  NaN   NaN  NaN   NaN  3.0   4.0
3  NaN   NaN  NaN   NaN  NaN   NaN
4  NaN   NaN  NaN   NaN  NaN   NaN

Copy to clipboard

Keep all original rows and columns and also all original values

\>>> df.compare(df2, keep\_shape\=True, keep\_equal\=True)
  col1       col2       col3
  self other self other self other
0    a     c  1.0   1.0  1.0   1.0
1    a     a  2.0   2.0  2.0   2.0
2    b     b  3.0   3.0  3.0   4.0
3    b     b  NaN   NaN  4.0   4.0
4    a     a  5.0   5.0  5.0   5.0

Copy to clipboard

On this page