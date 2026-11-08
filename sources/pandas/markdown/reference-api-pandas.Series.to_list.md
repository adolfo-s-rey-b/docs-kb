[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_list.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_list.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_list.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_list.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_list.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_list.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_list.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_list.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_list.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_list.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_list.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_list.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_list[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas-series-to-list "Link to this heading")

================================================================================================================================================

Series.to\_list()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L948-L983)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list "Link to this definition")

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