[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.update[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html#pandas-dataframe-update "Link to this heading")

=====================================================================================================================================================

DataFrame.update(_other_, _join\='left'_, _overwrite\=True_, _filter\_func\=None_, _errors\='ignore'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L13394-L13559)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html#pandas.DataFrame.update "Link to this definition")

Modify in place using non-NA values from another DataFrame.

Aligns on indices. There is no return value.

Parameters:

**other**DataFrame, or object coercible into a DataFrame

Should have at least one matching index/column label with the original DataFrame. If a Series is passed, its name attribute must be set, and that will be used as the column name to align with the original DataFrame.

**join**{‘left’}, default ‘left’

Only left join is implemented, keeping the index and columns of the original object.

**overwrite**bool, default True

How to handle non-NA values for overlapping keys:

*   True: overwrite original DataFrame’s values with values from other.
    
*   False: only update values that are NA in the original DataFrame.
    

**filter\_func**callable(1d-array) -> bool 1d-array, optional

Can choose to replace values other than NA. Return True for values that should be updated.

**errors**{‘raise’, ‘ignore’}, default ‘ignore’

If ‘raise’, will raise a ValueError if the DataFrame and other both contain non-NA data in the same place.

Returns:

None

This method directly changes calling object.

Raises:

ValueError

*   When errors=’raise’ and there’s overlapping non-NA data.
    
*   When errors is not either ‘ignore’ or ‘raise’
    

NotImplementedError

*   If join != ‘left’
    

See also

[`dict.update`](https://docs.python.org/3/builtins/stdtypes.html#dict.update "(in Python v3.15)")

Similar method for dictionaries.

[`DataFrame.merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")

For column(s)-on-column(s) operations.

Notes

1.  Duplicate indices on other are not supported and raises ValueError.
    

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[400, 500, 600\]})
\>>> new\_df \= pd.DataFrame({"B": \[4, 5, 6\], "C": \[7, 8, 9\]})
\>>> df.update(new\_df)
\>>> df
   A  B
0  1  4
1  2  5
2  3  6

Copy to clipboard

The DataFrame’s length does not increase as a result of the update, only values at matching index/column labels are updated.

\>>> df \= pd.DataFrame({"A": \["a", "b", "c"\], "B": \["x", "y", "z"\]})
\>>> new\_df \= pd.DataFrame({"B": \["d", "e", "f", "g", "h", "i"\]})
\>>> df.update(new\_df)
\>>> df
   A  B
0  a  d
1  b  e
2  c  f

Copy to clipboard

\>>> df \= pd.DataFrame({"A": \["a", "b", "c"\], "B": \["x", "y", "z"\]})
\>>> new\_df \= pd.DataFrame({"B": \["d", "f"\]}, index\=\[0, 2\])
\>>> df.update(new\_df)
\>>> df
   A  B
0  a  d
1  b  y
2  c  f

Copy to clipboard

For Series, its name attribute must be set.

\>>> df \= pd.DataFrame({"A": \["a", "b", "c"\], "B": \["x", "y", "z"\]})
\>>> new\_column \= pd.Series(\["d", "e", "f"\], name\="B")
\>>> df.update(new\_column)
\>>> df
   A  B
0  a  d
1  b  e
2  c  f

Copy to clipboard

If other contains NaNs the corresponding values are not updated in the original dataframe.

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[400.0, 500.0, 600.0\]})
\>>> new\_df \= pd.DataFrame({"B": \[4, np.nan, 6\]})
\>>> df.update(new\_df)
\>>> df
   A      B
0  1    4.0
1  2  500.0
2  3    6.0

Copy to clipboard

On this page