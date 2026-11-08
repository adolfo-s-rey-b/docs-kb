[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.map[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#pandas-categoricalindex-map "Link to this heading")

=================================================================================================================================================================

CategoricalIndex.map(_mapper_, _na\_action\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L1035-L1110)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#pandas.CategoricalIndex.map "Link to this definition")

Map values using input an input mapping or function.

Maps the values (their categories, not the codes) of the index to new categories. If the mapping correspondence is one-to-one the result is a [`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
 which has the same order property as the original, otherwise an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 is returned.

If a dict or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is used any unmapped category is mapped to NaN. Note that if this happens an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 will be returned.

Parameters:

**mapper**function, dict, or Series

Mapping correspondence.

**na\_action**{None, ‘ignore’}, default ‘ignore’

If ‘ignore’, propagate NaN values, without passing them to the mapping correspondence.

Returns:

pandas.CategoricalIndex or pandas.Index

Mapped index.

See also

[`Index.map`](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#pandas.Index.map "pandas.Index.map")

Apply a mapping correspondence on an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
.

[`Series.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")

Apply a mapping correspondence on a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

[`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")

Apply more complex functions on a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

Examples

\>>> idx \= pd.CategoricalIndex(\["a", "b", "c"\])
\>>> idx
CategoricalIndex(\['a', 'b', 'c'\], categories=\['a', 'b', 'c'\],
                  ordered=False, dtype='category')
\>>> idx.map(lambda x: x.upper())
CategoricalIndex(\['A', 'B', 'C'\], categories=\['A', 'B', 'C'\],
                 ordered=False, dtype='category')
\>>> idx.map({"a": "first", "b": "second", "c": "third"})
CategoricalIndex(\['first', 'second', 'third'\], categories=\['first',\
                 'second', 'third'\], ordered=False, dtype='category')

Copy to clipboard

If the mapping is one-to-one the ordering of the categories is preserved:

\>>> idx \= pd.CategoricalIndex(\["a", "b", "c"\], ordered\=True)
\>>> idx
CategoricalIndex(\['a', 'b', 'c'\], categories=\['a', 'b', 'c'\],
                 ordered=True, dtype='category')
\>>> idx.map({"a": 3, "b": 2, "c": 1})
CategoricalIndex(\[3, 2, 1\], categories=\[3, 2, 1\], ordered=True,
                 dtype='category')

Copy to clipboard

If the mapping is not one-to-one an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 is returned:

\>>> idx.map({"a": "first", "b": "second", "c": "first"})
Index(\['first', 'second', 'first'\], dtype='str')

Copy to clipboard

If a dict is used, all unmapped categories are mapped to NaN and the result is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
:

\>>> idx.map({"a": "first", "b": "second"})
Index(\['first', 'second', nan\], dtype='str')

Copy to clipboard

On this page