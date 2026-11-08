[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.to\_list[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html#pandas-index-to-list "Link to this heading")

=============================================================================================================================================

Index.to\_list()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L948-L983)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html#pandas.Index.to_list "Link to this definition")

Return a list of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Returns:

list

List containing the values as Python or pandas scalers.

See also

[`numpy.ndarray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "(in NumPy v2.5)")

Return the array as an a.ndim-levels deep nested list of Python scalars.

Examples

For Series

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.to\_list()
\[1, 2, 3\]

Copy to clipboard

For Index:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

\>>> idx.to\_list()
\[1, 2, 3\]

Copy to clipboard

On this page