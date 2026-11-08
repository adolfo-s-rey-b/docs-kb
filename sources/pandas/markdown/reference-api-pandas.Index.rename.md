[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.rename[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas-index-rename "Link to this heading")

=========================================================================================================================================

Index.rename(_name_, _\*_, _inplace\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2159-L2210)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "Link to this definition")

Alter Index or MultiIndex name.

Able to set new names without level. Defaults to returning new index. Length of names must match number of levels in MultiIndex.

Parameters:

**name**Hashable or a sequence of the previous

Name(s) to set.

**inplace**bool, default False

Modifies the object directly, instead of creating a new Index or MultiIndex.

Returns:

Index or None

The same type as the caller or None if `inplace=True`.

See also

[`Index.set_names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")

Able to set new names partially and by level.

Examples

\>>> idx \= pd.Index(\["A", "C", "A", "B"\], name\="score")
\>>> idx.rename("grade")
Index(\['A', 'C', 'A', 'B'\], dtype='str', name='grade')

Copy to clipboard

\>>> idx \= pd.MultiIndex.from\_product(
...     \[\["python", "cobra"\], \[2018, 2019\]\], names\=\["kind", "year"\]
... )
\>>> idx
MultiIndex(\[('python', 2018),\
            ('python', 2019),\
            ( 'cobra', 2018),\
            ( 'cobra', 2019)\],
           names=\['kind', 'year'\])
\>>> idx.rename(\["species", "year"\])
MultiIndex(\[('python', 2018),\
            ('python', 2019),\
            ( 'cobra', 2018),\
            ( 'cobra', 2019)\],
           names=\['species', 'year'\])
\>>> idx.rename("species")
Traceback (most recent call last):
TypeError: Must pass list-like as \`names\`.

Copy to clipboard

On this page