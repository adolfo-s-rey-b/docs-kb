[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.IndexingError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.IndexingError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.IndexingError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.IndexingError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.IndexingError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.IndexingError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.IndexingError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.IndexingError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.IndexingError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.IndexingError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.IndexingError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.IndexingError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.IndexingError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.IndexingError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.IndexingError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.IndexingError.html#pandas-errors-indexingerror "Link to this heading")

=================================================================================================================================================================

exception pandas.errors.IndexingError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L778-L806)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.IndexingError.html#pandas.errors.IndexingError "Link to this definition")

Exception is raised when trying to index and there is a mismatch in dimensions.

Raised by properties like [`pandas.DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")
 when an indexer is out of bounds or [`pandas.DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")
 when its index is unalignable to the frame index.

See also

`DataFrame.iloc`

Purely integer-location based indexing for selection by position.

`DataFrame.loc`

Access a group of rows and columns by label(s) or a boolean array.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 1, 1\]})
\>>> df.loc\[..., ..., "A"\]
... \# IndexingError: indexer may only contain one '...' entry
\>>> df \= pd.DataFrame({"A": \[1, 1, 1\]})
\>>> df.loc\[1, ..., ...\]
... \# IndexingError: Too many indexers
\>>> df\[pd.Series(\[True\], dtype\=bool)\]
... \# IndexingError: Unalignable boolean Series provided as indexer...
\>>> s \= pd.Series(range(2), index\=pd.MultiIndex.from\_product(\[\["a", "b"\], \["c"\]\]))
\>>> s.loc\["a", "c", "d"\]
... \# IndexingError: Too many indexers

Copy to clipboard

On this page