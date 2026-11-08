[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dropna[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas-series-dropna "Link to this heading")

============================================================================================================================================

Series.dropna(_\*_, _axis\=0_, _inplace\=<no\_default>_, _how\=None_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L7041-L7142)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "Link to this definition")

Return a new Series with missing values removed.

See the [User Guide](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
 for more on which values are considered missing, and how to work with missing data.

Parameters:

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**inplace**bool, default False

If True, do operation inplace and return None.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**how**str, optional

Not in use. Kept for compatibility.

**ignore\_index**bool, default `False`

If `True`, the resulting axis will be labeled 0, 1, …, n - 1.

Added in version 2.0.0.

Returns:

Series or None

Series with NA entries dropped from it or None if `inplace=True`.

See also

[`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")

Indicate missing values.

[`Series.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")

Indicate existing (non-missing) values.

[`Series.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")

Replace missing values.

[`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")

Drop rows or columns which contain NA values.

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Drop missing indices.

Examples

\>>> ser \= pd.Series(\[1.0, 2.0, np.nan\])
\>>> ser
0    1.0
1    2.0
2    NaN
dtype: float64

Copy to clipboard

Drop NA values from a Series.

\>>> ser.dropna()
0    1.0
1    2.0
dtype: float64

Copy to clipboard

Empty strings are not considered NA values. `None` is considered an NA value.

\>>> ser \= pd.Series(\[np.nan, 2, pd.NaT, "", None, "I stay"\])
\>>> ser
0       NaN
1         2
2       NaT
3
4      None
5    I stay
dtype: object
\>>> ser.dropna()
1         2
3
5    I stay
dtype: object

Copy to clipboard

On this page