[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.map[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html#pandas-categorical-map "Link to this heading")

==================================================================================================================================================

Categorical.map(_mapper_, _na\_action\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1696-L1825)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html#pandas.Categorical.map "Link to this definition")

Map categories using an input mapping or function.

Maps the categories to new categories. If the mapping correspondence is one-to-one the result is a [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 which has the same order property as the original, otherwise a [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 is returned. NaN values are unaffected.

If a dict or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is used any unmapped category is mapped to NaN. Note that if this happens an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 will be returned.

Parameters:

**mapper**function, dict, or Series

Mapping correspondence.

**na\_action**{None, ‘ignore’}, default None

If ‘ignore’, propagate NaN values, without passing them to the mapping correspondence.

Returns:

pandas.Categorical or pandas.Index

Mapped categorical.

See also

[`CategoricalIndex.map`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#pandas.CategoricalIndex.map "pandas.CategoricalIndex.map")

Apply a mapping correspondence on a [`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
.

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

\>>> cat \= pd.Categorical(\["a", "b", "c"\])
\>>> cat
\['a', 'b', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]
\>>> cat.map(lambda x: x.upper(), na\_action\=None)
\['A', 'B', 'C'\]
Categories (3, str): \['A', 'B', 'C'\]
\>>> cat.map({"a": "first", "b": "second", "c": "third"}, na\_action\=None)
\['first', 'second', 'third'\]
Categories (3, str): \['first', 'second', 'third'\]

Copy to clipboard

If the mapping is one-to-one the ordering of the categories is preserved:

\>>> cat \= pd.Categorical(\["a", "b", "c"\], ordered\=True)
\>>> cat
\['a', 'b', 'c'\]
Categories (3, str): \['a' < 'b' < 'c'\]
\>>> cat.map({"a": 3, "b": 2, "c": 1}, na\_action\=None)
\[3, 2, 1\]
Categories (3, int64): \[3 < 2 < 1\]

Copy to clipboard

If the mapping is not one-to-one an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 is returned:

\>>> cat.map({"a": "first", "b": "second", "c": "first"}, na\_action\=None)
Index(\['first', 'second', 'first'\], dtype='str')

Copy to clipboard

If a dict is used, all unmapped categories are mapped to NaN and the result is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
:

\>>> cat.map({"a": "first", "b": "second"}, na\_action\=None)
Index(\['first', 'second', nan\], dtype='str')

Copy to clipboard

The mapping function is applied to categories, not to each value. It is therefore only called once per unique category, and the result reused for all occurrences:

\>>> cat \= pd.Categorical(\["a", "a", "b"\])
\>>> calls \= \[\]
\>>> def f(x):
...     calls.append(x)
...     return x.upper()
\>>> result \= cat.map(f)
\>>> result
\['A', 'A', 'B'\]
Categories (2, str): \['A', 'B'\]
\>>> calls
\['a', 'b'\]

Copy to clipboard

On this page