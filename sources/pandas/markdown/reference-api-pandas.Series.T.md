[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.T.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.T.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.T.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.T.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.T.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.T.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.T.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.T.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.T.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.T.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.T.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.T.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.T[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html#pandas-series-t "Link to this heading")

=============================================================================================================================

property Series.T[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L302-L312)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html#pandas.Series.T "Link to this definition")

Return the transpose, which is by definition self.

For 1D objects (Series, Index) transposition has no effect; the object is returned unchanged. Provided for API compatibility with DataFrame and NumPy.

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

Immutable sequence used for indexing and alignment.

Examples

For Series:

\>>> s \= pd.Series(\['Ant', 'Bear', 'Cow'\])
\>>> s
0     Ant
1    Bear
2     Cow
dtype: str
\>>> s.T
0     Ant
1    Bear
2     Cow
dtype: str

Copy to clipboard

For Index:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.T
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

On this page