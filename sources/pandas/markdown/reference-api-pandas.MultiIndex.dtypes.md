[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.dtypes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.dtypes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.dtypes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.dtypes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.dtypes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.dtypes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.dtypes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.dtypes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.dtypes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.dtypes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.dtypes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.dtypes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.dtypes[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html#pandas-multiindex-dtypes "Link to this heading")

========================================================================================================================================================

MultiIndex.dtypes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L810-L844)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html#pandas.MultiIndex.dtypes "Link to this definition")

Return the dtypes as a Series for the underlying MultiIndex.

Each element in the returned Series corresponds to the dtype of one level of the MultiIndex, indexed by the level names.

See also

[`Index.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype")

Return the dtype object of the underlying data.

[`Series.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes "pandas.Series.dtypes")

Return the data type of the underlying Series.

Examples

\>>> idx \= pd.MultiIndex.from\_product(
...     \[(0, 1, 2), ("green", "purple")\], names\=\["number", "color"\]
... )
\>>> idx
MultiIndex(\[(0,  'green'),\
            (0, 'purple'),\
            (1,  'green'),\
            (1, 'purple'),\
            (2,  'green'),\
            (2, 'purple')\],
           names=\['number', 'color'\])
\>>> idx.dtypes
number     int64
color     object
dtype: object

Copy to clipboard

On this page