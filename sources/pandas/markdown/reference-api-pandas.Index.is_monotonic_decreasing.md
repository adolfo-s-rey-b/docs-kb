[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.is\_monotonic\_decreasing[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas-index-is-monotonic-decreasing "Link to this heading")

==============================================================================================================================================================================================

property Index.is\_monotonic\_decreasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2492-L2525)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas.Index.is_monotonic_decreasing "Link to this definition")

Return a boolean if the values are equal or decreasing.

A monotonically decreasing index has values that are equal to or less than the preceding value. This is useful for checking if an index is sorted in non-increasing order.

Returns:

bool

See also

[`Index.is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas.Index.is_monotonic_increasing "pandas.Index.is_monotonic_increasing")

Check if the values are equal or increasing.

Examples

\>>> pd.Index(\[3, 2, 1\]).is\_monotonic\_decreasing
True
\>>> pd.Index(\[3, 2, 2\]).is\_monotonic\_decreasing
True
\>>> pd.Index(\[3, 1, 2\]).is\_monotonic\_decreasing
False

Copy to clipboard

On this page