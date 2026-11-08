[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.dropna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.dropna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.dropna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.dropna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.dropna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.dropna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.dropna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.dropna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.dropna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.dropna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.dropna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.dropna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.dropna[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas-dataframe-dropna "Link to this heading")

=====================================================================================================================================================

DataFrame.dropna(_\*_, _axis\=0_, _how\=<no\_default>_, _thresh\=<no\_default>_, _subset\=None_, _inplace\=<no\_default>_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L8583-L8760)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "Link to this definition")

Remove missing values.

See the [User Guide](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
 for more on which values are considered missing, and how to work with missing data.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Determine if rows or columns which contain missing values are removed.

*   0, or ‘index’ : Drop rows which contain missing values.
    
*   1, or ‘columns’ : Drop columns which contain missing values.
    

Only a single axis is allowed.

**how**{‘any’, ‘all’}, default ‘any’

Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.

*   ‘any’ : If any NA values are present, drop that row or column.
    
*   ‘all’ : If all values are NA, drop that row or column.
    

**thresh**int, optional

Require that many non-NA values. Cannot be combined with how.

**subset**column label or iterable of labels, optional

Labels along other axis to consider, e.g. if you are dropping rows these would be a list of columns to include.

**inplace**bool, default False

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**ignore\_index**bool, default `False`

If `True`, the resulting axis will be labeled 0, 1, …, n - 1.

Added in version 2.0.0.

Returns:

DataFrame or None

DataFrame with NA entries dropped from it or None if `inplace=True`.

See also

[`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")

Indicate missing values.

[`DataFrame.notna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")

Indicate existing (non-missing) values.

[`DataFrame.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")

Replace missing values.

[`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")

Drop missing values.

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Drop missing indices.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "name": \["Alfred", "Batman", "Catwoman"\],
...         "toy": \[np.nan, "Batmobile", "Bullwhip"\],
...         "born": \[pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT\],
...     }
... )
\>>> df
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT

Copy to clipboard

Drop the rows where at least one element is missing.

\>>> df.dropna()
     name        toy       born
1  Batman  Batmobile 1940-04-25

Copy to clipboard

Drop the columns where at least one element is missing.

\>>> df.dropna(axis\="columns")
       name
0    Alfred
1    Batman
2  Catwoman

Copy to clipboard

Drop the rows where all elements are missing.

\>>> df.dropna(how\="all")
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT

Copy to clipboard

Keep only the rows with at least 2 non-NA values.

\>>> df.dropna(thresh\=2)
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT

Copy to clipboard

Define in which columns to look for missing values.

\>>> df.dropna(subset\=\["name", "toy"\])
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT

Copy to clipboard

On this page