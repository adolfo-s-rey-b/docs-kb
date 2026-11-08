[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.set\_names[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas-index-set-names "Link to this heading")

===================================================================================================================================================

Index.set\_names(_names_, _\*_, _level\=None_, _inplace\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2042-L2147)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "Link to this definition")

Set Index or MultiIndex name.

Able to set new names partially and by level.

Parameters:

**names**Hashable or a sequence of the previous or dict-like for MultiIndex

Name(s) to set.

**level**int, Hashable or a sequence of the previous, optional

If the index is a MultiIndex and names is not dict-like, level(s) to set (None for all levels). Otherwise level must be None.

**inplace**bool, default False

Modifies the object directly, instead of creating a new Index or MultiIndex.

Returns:

Index or None

The same type as the caller or None if `inplace=True`.

See also

[`Index.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")

Able to set new names without level.

Examples

\>>> idx \= pd.Index(\[1, 2, 3, 4\])
\>>> idx
Index(\[1, 2, 3, 4\], dtype='int64')
\>>> idx.set\_names("quarter")
Index(\[1, 2, 3, 4\], dtype='int64', name='quarter')

Copy to clipboard

\>>> idx \= pd.MultiIndex.from\_product(\[\["python", "cobra"\], \[2018, 2019\]\])
\>>> idx
MultiIndex(\[('python', 2018),\
            ('python', 2019),\
            ( 'cobra', 2018),\
            ( 'cobra', 2019)\],
           )
\>>> idx \= idx.set\_names(\["kind", "year"\])
\>>> idx.set\_names("species", level\=0)
MultiIndex(\[('python', 2018),\
            ('python', 2019),\
            ( 'cobra', 2018),\
            ( 'cobra', 2019)\],
           names=\['species', 'year'\])

Copy to clipboard

When renaming levels with a dict, levels can not be passed.

\>>> idx.set\_names({"kind": "snake"})
MultiIndex(\[('python', 2018),\
            ('python', 2019),\
            ( 'cobra', 2018),\
            ( 'cobra', 2019)\],
           names=\['snake', 'year'\])

Copy to clipboard

On this page