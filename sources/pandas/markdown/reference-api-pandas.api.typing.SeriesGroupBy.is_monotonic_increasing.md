[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.is\_monotonic\_increasing[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html#pandas-api-typing-seriesgroupby-is-monotonic-increasing "Link to this heading")

=======================================================================================================================================================================================================================================================

property SeriesGroupBy.is\_monotonic\_increasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1877-L1902)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html#pandas.api.typing.SeriesGroupBy.is_monotonic_increasing "Link to this definition")

Return whether each group’s values are monotonically increasing.

A group is considered monotonically increasing if each successive element is greater than or equal to the previous one.

Returns:

Series

See also

[`SeriesGroupBy.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing.html#pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing "pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing")

Return whether each group’s values are monotonically decreasing.

Examples

\>>> s \= pd.Series(\[2, 1, 3, 4\], index\=\["Falcon", "Falcon", "Parrot", "Parrot"\])
\>>> s.groupby(level\=0).is\_monotonic\_increasing
Falcon    False
Parrot     True
dtype: bool

Copy to clipboard

On this page