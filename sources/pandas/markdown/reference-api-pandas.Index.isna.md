[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.isna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.isna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.isna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.isna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.isna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.isna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.isna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.isna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.isna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.isna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.isna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.isna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.isna[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas-index-isna "Link to this heading")

===================================================================================================================================

final Index.isna()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2755-L2809)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "Link to this definition")

Detect missing values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as `None`, `numpy.NaN` or `pd.NaT`, get mapped to `True` values. Everything else get mapped to `False` values. Characters such as empty strings ‘’ or `numpy.inf` are not considered NA values.

Returns:

numpy.ndarray\[bool\]

A boolean array of whether my values are NA.

See also

[`Index.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas.Index.notna "pandas.Index.notna")

Boolean inverse of isna.

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Omit entries with missing values.

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Top-level isna.

[`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")

Detect missing values in Series object.

Examples

Show which entries in a pandas.Index are NA. The result is an array.

\>>> idx \= pd.Index(\[5.2, 6.0, np.nan\])
\>>> idx
Index(\[5.2, 6.0, nan\], dtype='float64')
\>>> idx.isna()
array(\[False, False,  True\])

Copy to clipboard

Empty strings are not considered NA values. None is considered an NA value.

\>>> idx \= pd.Index(\["black", "", "red", None\])
\>>> idx
Index(\['black', '', 'red', nan\], dtype='str')
\>>> idx.isna()
array(\[False, False, False,  True\])

Copy to clipboard

For datetimes, NaT (Not a Time) is considered as an NA value.

\>>> idx \= pd.DatetimeIndex(
...     \[pd.Timestamp("1940-04-25"), pd.Timestamp(""), None, pd.NaT\]
... )
\>>> idx
DatetimeIndex(\['1940-04-25', 'NaT', 'NaT', 'NaT'\],
              dtype='datetime64\[us\]', freq=None)
\>>> idx.isna()
array(\[False,  True,  True,  True\])

Copy to clipboard

On this page