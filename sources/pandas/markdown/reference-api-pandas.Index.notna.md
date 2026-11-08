[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.notna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.notna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.notna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.notna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.notna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.notna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.notna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.notna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.notna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.notna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.notna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.notna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.notna[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas-index-notna "Link to this heading")

======================================================================================================================================

final Index.notna()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2813-L2855)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas.Index.notna "Link to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to `True`. Characters such as empty strings `''` or `numpy.inf` are not considered NA values. NA values, such as None or `numpy.NaN`, get mapped to `False` values.

Returns:

numpy.ndarray\[bool\]

Boolean array to indicate which entries are not NA.

See also

`Index.notnull`

Alias of notna.

[`Index.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "pandas.Index.isna")

Inverse of notna.

[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")

Top-level notna.

Examples

Show which entries in an Index are not NA. The result is an array.

\>>> idx \= pd.Index(\[5.2, 6.0, np.nan\])
\>>> idx
Index(\[5.2, 6.0, nan\], dtype='float64')
\>>> idx.notna()
array(\[ True,  True, False\])

Copy to clipboard

Empty strings are not considered NA values. None is considered a NA value.

\>>> idx \= pd.Index(\["black", "", "red", None\])
\>>> idx
Index(\['black', '', 'red', nan\], dtype='str')
\>>> idx.notna()
array(\[ True,  True,  True, False\])

Copy to clipboard

On this page