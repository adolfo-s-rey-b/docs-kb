[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.insert.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.insert.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.insert.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.insert.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.insert.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.insert.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.insert.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.insert.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.insert.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.insert.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.insert.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.insert.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.insert[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas-index-insert "Link to this heading")

=========================================================================================================================================

Index.insert(_loc_, _item_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7497-L7574)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas.Index.insert "Link to this definition")

Make new Index inserting new item at location.

Follows Python numpy.insert semantics for negative values.

Parameters:

**loc**int

The integer location where the new item will be inserted.

**item**object

The new item to be inserted into the Index.

Returns:

Index

Returns a new Index object resulting from inserting the specified item at the specified location within the original Index.

See also

[`Index.append`](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas.Index.append "pandas.Index.append")

Append a collection of Indexes together.

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.insert(1, "x")
Index(\['a', 'x', 'b', 'c'\], dtype='str')

Copy to clipboard

On this page