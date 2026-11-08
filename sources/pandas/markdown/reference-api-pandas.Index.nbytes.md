[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.nbytes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.nbytes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.nbytes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.nbytes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.nbytes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.nbytes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.nbytes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.nbytes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.nbytes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.nbytes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.nbytes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.nbytes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.nbytes[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html#pandas-index-nbytes "Link to this heading")

=========================================================================================================================================

property Index.nbytes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L457-L491)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html#pandas.Index.nbytes "Link to this definition")

Return the number of bytes in the underlying data.

Includes only the memory used by the array values; overhead such as the index is not included. Useful for estimating memory usage.

See also

[`Series.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ndim.html#pandas.Series.ndim "pandas.Series.ndim")

Number of dimensions of the underlying data.

[`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size")

Return the number of elements in the underlying data.

Examples

For Series:

\>>> s \= pd.Series(\["Ant", "Bear", "Cow"\])
\>>> s
0     Ant
1    Bear
2     Cow
dtype: str
\>>> s.nbytes
34

Copy to clipboard

For Index:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.nbytes
24

Copy to clipboard

On this page