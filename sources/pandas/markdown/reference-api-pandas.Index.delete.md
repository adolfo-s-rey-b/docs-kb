[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.delete[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas-index-delete "Link to this heading")

=========================================================================================================================================

Index.delete(_loc_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7452-L7495)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas.Index.delete "Link to this definition")

Make new Index with passed location(-s) deleted.

Returns a new Index with the entries at the given positional location(s) removed. The original Index is not modified.

Parameters:

**loc**int or list of int

Location of item(-s) which will be deleted. Use a list of locations to delete more than one value at the same time.

Returns:

Index

Will be same type as self, except for RangeIndex.

See also

[`numpy.delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "(in NumPy v2.5)")

Delete any rows and column from NumPy array (ndarray).

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.delete(1)
Index(\['a', 'c'\], dtype='str')

Copy to clipboard

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.delete(\[0, 2\])
Index(\['b'\], dtype='str')

Copy to clipboard

On this page