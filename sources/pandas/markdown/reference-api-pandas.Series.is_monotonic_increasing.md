[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.is\_monotonic\_increasing[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#pandas-series-is-monotonic-increasing "Link to this heading")

=================================================================================================================================================================================================

property Series.is\_monotonic\_increasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1289-L1319)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#pandas.Series.is_monotonic_increasing "Link to this definition")

Return True if values in the object are monotonically increasing.

This property checks whether each element is greater than or equal to the previous element. Equal consecutive values are considered monotonically increasing.

Returns:

bool

See also

[`Series.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas.Series.is_monotonic_decreasing "pandas.Series.is_monotonic_decreasing")

Return boolean if values in the object are monotonically decreasing.

Examples

\>>> s \= pd.Series(\[1, 2, 2\])
\>>> s.is\_monotonic\_increasing
True

Copy to clipboard

\>>> s \= pd.Series(\[3, 2, 1\])
\>>> s.is\_monotonic\_increasing
False

Copy to clipboard

On this page