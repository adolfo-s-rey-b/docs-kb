[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.is_empty.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.is_empty.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.is_empty.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.is_empty.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.is_empty.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.is_empty.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.is_empty.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.is_empty.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.is_empty.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.is_empty.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.is_empty.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.is_empty.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.is\_empty[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html#pandas-intervalindex-is-empty "Link to this heading")

========================================================================================================================================================================

property IntervalIndex.is\_empty[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L401-L438)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html#pandas.IntervalIndex.is_empty "Link to this definition")

Indicates if an interval is empty, meaning it contains no points.

An interval is considered empty if its left and right endpoints are equal, and it is not closed on both sides. Returns a boolean ndarray positionally indicating the emptiness of each interval.

Returns:

numpy.ndarray\[bool\]

A boolean ndarray positionally indicating if an Interval is empty.

See also

[`Interval.is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas.Interval.is_empty "pandas.Interval.is_empty")

Indicates if a scalar Interval is empty.

[`IntervalIndex.length`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "pandas.IntervalIndex.length")

Return the length of each interval.

Examples

\>>> ivs \= \[\
...     pd.Interval(0, 0, closed\="neither"),\
...     pd.Interval(1, 2, closed\="neither"),\
... \]
\>>> pd.IntervalIndex(ivs).is\_empty
array(\[ True, False\])

Copy to clipboard

Missing values are not considered empty:

\>>> ivs \= \[pd.Interval(0, 0, closed\="neither"), np.nan\]
\>>> pd.IntervalIndex(ivs).is\_empty
array(\[ True, False\])

Copy to clipboard

On this page