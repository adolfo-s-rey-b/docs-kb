[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.fillna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.fillna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.fillna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.fillna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.fillna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.fillna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.fillna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.fillna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.fillna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.fillna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.fillna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.fillna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.fillna[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#pandas-index-fillna "Link to this heading")

=========================================================================================================================================

Index.fillna(_value_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2859-L2921)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#pandas.Index.fillna "Link to this definition")

Fill NA/NaN values with the specified value.

Returns a new Index with all NA/NaN entries replaced by the given scalar value.

Parameters:

**value**scalar

Scalar value to use to fill holes (e.g. 0). This value cannot be a list-likes.

Returns:

Index

NA/NaN values replaced with value.

See also

[`DataFrame.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")

Fill NaN values of a DataFrame.

[`Series.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")

Fill NaN Values of a Series.

Examples

\>>> idx \= pd.Index(\[np.nan, np.nan, 3\])
\>>> idx.fillna(0)
Index(\[0.0, 0.0, 3.0\], dtype='float64')

Copy to clipboard

On this page