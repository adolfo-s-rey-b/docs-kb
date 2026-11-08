[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.map[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#pandas-index-map "Link to this heading")

================================================================================================================================

Index.map(_mapper_, _na\_action\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6846-L6923)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#pandas.Index.map "Link to this definition")

Map values using an input mapping or function.

Applies a function, dict, or Series to each element of the Index, returning a new Index (or MultiIndex if tuples are returned).

Parameters:

**mapper**function, dict, or Series

Mapping correspondence.

**na\_action**{None, ‘ignore’}

If ‘ignore’, propagate NA values, without passing them to the mapping correspondence.

Returns:

Union\[Index, MultiIndex\]

The output of the mapping function applied to the index. If the function returns a tuple with more than one element a MultiIndex will be returned.

See also

[`Index.where`](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#pandas.Index.where "pandas.Index.where")

Replace values where the condition is False.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.map({1: "a", 2: "b", 3: "c"})
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

Using map with a function:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.map("I am a {}".format)
Index(\['I am a 1', 'I am a 2', 'I am a 3'\], dtype='str')

Copy to clipboard

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.map(lambda x: x.upper())
Index(\['A', 'B', 'C'\], dtype='str')

Copy to clipboard

On this page