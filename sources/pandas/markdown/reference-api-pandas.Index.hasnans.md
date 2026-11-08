[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.hasnans.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.hasnans.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.hasnans.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.hasnans.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.hasnans.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.hasnans.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.hasnans.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.hasnans.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.hasnans.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.hasnans.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.hasnans.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.hasnans.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.hasnans[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html#pandas-index-hasnans "Link to this heading")

============================================================================================================================================

Index.hasnans[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2722-L2753)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html#pandas.Index.hasnans "Link to this definition")

Return True if there are any NaNs.

Enables various performance speedups.

Returns:

bool

See also

[`Index.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "pandas.Index.isna")

Detect missing values.

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Return Index without NA/NaN values.

[`Index.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#pandas.Index.fillna "pandas.Index.fillna")

Fill NA/NaN values with the specified value.

Examples

\>>> s \= pd.Series(\[1, 2, 3\], index\=\["a", "b", None\])
\>>> s
a    1
b    2
None 3
dtype: int64
\>>> s.index.hasnans
True

Copy to clipboard

On this page