[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.first_valid_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.first_valid_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.first_valid_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.first_valid_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.first_valid_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.first_valid_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.first_valid_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.first_valid_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.first_valid_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.first_valid_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.first_valid_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.first_valid_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.first\_valid\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html#pandas-dataframe-first-valid-index "Link to this heading")

========================================================================================================================================================================================

DataFrame.first\_valid\_index()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L12836-L12921)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html#pandas.DataFrame.first_valid_index "Link to this definition")

Return index for first non-missing value or None, if no value is found.

See the [User Guide](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
 for more information on which values are considered missing.

Returns:

type of index

Index of first non-missing value.

See also

[`DataFrame.last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.last_valid_index.html#pandas.DataFrame.last_valid_index "pandas.DataFrame.last_valid_index")

Return index for last non-NA value or None, if no non-NA value is found.

[`Series.last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.last_valid_index.html#pandas.Series.last_valid_index "pandas.Series.last_valid_index")

Return index for last non-NA value or None, if no non-NA value is found.

[`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")

Detect missing values.

Examples

For Series:

\>>> s \= pd.Series(\[None, 3, 4\])
\>>> s.first\_valid\_index()
1
\>>> s.last\_valid\_index()
2

Copy to clipboard

\>>> s \= pd.Series(\[None, None\])
\>>> print(s.first\_valid\_index())
None
\>>> print(s.last\_valid\_index())
None

Copy to clipboard

If all elements in Series are NA/null, returns None.

\>>> s \= pd.Series()
\>>> print(s.first\_valid\_index())
None
\>>> print(s.last\_valid\_index())
None

Copy to clipboard

If Series is empty, returns None.

For DataFrame:

\>>> df \= pd.DataFrame({"A": \[None, None, 2\], "B": \[None, 3, 4\]})
\>>> df
     A      B
0  NaN    NaN
1  NaN    3.0
2  2.0    4.0
\>>> df.first\_valid\_index()
1
\>>> df.last\_valid\_index()
2

Copy to clipboard

\>>> df \= pd.DataFrame({"A": \[None, None, None\], "B": \[None, None, None\]})
\>>> df
     A      B
0  None   None
1  None   None
2  None   None
\>>> print(df.first\_valid\_index())
None
\>>> print(df.last\_valid\_index())
None

Copy to clipboard

If all elements in DataFrame are NA/null, returns None.

\>>> df \= pd.DataFrame()
\>>> df
Empty DataFrame
Columns: \[\]
Index: \[\]
\>>> print(df.first\_valid\_index())
None
\>>> print(df.last\_valid\_index())
None

Copy to clipboard

If DataFrame is empty, returns None.

On this page