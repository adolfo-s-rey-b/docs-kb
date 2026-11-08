[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.empty.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.empty.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.empty.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.empty.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.empty.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.empty.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.empty.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.empty.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.empty.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.empty.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.empty.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.empty.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.empty[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html#pandas-index-empty "Link to this heading")

======================================================================================================================================

property Index.empty[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L754-L796)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html#pandas.Index.empty "Link to this definition")

Indicator whether Index is empty.

An Index is considered empty if it has no elements. This property can be useful for quickly checking the state of an Index, especially in data processing and analysis workflows where handling of empty datasets might be required.

Returns:

bool

If Index is empty, return True, if not return False.

See also

[`Index.size`](https://pandas.pydata.org/docs/reference/api/pandas.Index.size.html#pandas.Index.size "pandas.Index.size")

Return the number of elements in the underlying data.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.empty
False

Copy to clipboard

\>>> idx\_empty \= pd.Index(\[\])
\>>> idx\_empty
Index(\[\], dtype='object')
\>>> idx\_empty.empty
True

Copy to clipboard

If we only have NaNs in our DataFrame, it is not considered empty!

\>>> idx \= pd.Index(\[np.nan, np.nan\])
\>>> idx
Index(\[nan, nan\], dtype='float64')
\>>> idx.empty
False

Copy to clipboard

On this page