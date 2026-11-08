[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.is_monotonic_increasing.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.is_monotonic_increasing.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.is_monotonic_increasing.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.is_monotonic_increasing.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.is_monotonic_increasing.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.is_monotonic_increasing.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.is_monotonic_increasing.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.is\_monotonic\_increasing[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas-index-is-monotonic-increasing "Link to this heading")

==============================================================================================================================================================================================

property Index.is\_monotonic\_increasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2457-L2490)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas.Index.is_monotonic_increasing "Link to this definition")

Return a boolean if the values are equal or increasing.

A monotonically increasing index has values that are equal to or greater than the preceding value. This is useful for checking if an index is sorted in non-decreasing order.

Returns:

bool

See also

[`Index.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas.Index.is_monotonic_decreasing "pandas.Index.is_monotonic_decreasing")

Check if the values are equal or decreasing.

Examples

\>>> pd.Index(\[1, 2, 3\]).is\_monotonic\_increasing
True
\>>> pd.Index(\[1, 2, 2\]).is\_monotonic\_increasing
True
\>>> pd.Index(\[1, 3, 2\]).is\_monotonic\_increasing
False

Copy to clipboard

On this page