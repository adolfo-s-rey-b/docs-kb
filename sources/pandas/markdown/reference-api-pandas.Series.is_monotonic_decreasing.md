[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.is_monotonic_decreasing.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.is_monotonic_decreasing.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.is_monotonic_decreasing.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.is_monotonic_decreasing.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.is_monotonic_decreasing.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.is_monotonic_decreasing.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.is_monotonic_decreasing.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.is\_monotonic\_decreasing[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas-series-is-monotonic-decreasing "Link to this heading")

=================================================================================================================================================================================================

property Series.is\_monotonic\_decreasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1321-L1351)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas.Series.is_monotonic_decreasing "Link to this definition")

Return True if values in the object are monotonically decreasing.

This property checks whether each element is less than or equal to the previous element. Equal consecutive values are considered monotonically decreasing.

Returns:

bool

See also

[`Series.is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#pandas.Series.is_monotonic_increasing "pandas.Series.is_monotonic_increasing")

Return boolean if values in the object are monotonically increasing.

Examples

\>>> s \= pd.Series(\[3, 2, 2, 1\])
\>>> s.is\_monotonic\_decreasing
True

Copy to clipboard

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.is\_monotonic\_decreasing
False

Copy to clipboard

On this page