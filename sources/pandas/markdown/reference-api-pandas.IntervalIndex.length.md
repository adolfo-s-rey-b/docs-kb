[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.length.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.length.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.length.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.length.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.length.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.length.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.length.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.length.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.length.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.length.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.length.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.length.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.length[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas-intervalindex-length "Link to this heading")

=================================================================================================================================================================

property IntervalIndex.length[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L1530-L1560)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "Link to this definition")

Calculate the length of each interval in the IntervalIndex.

This method returns a new Index containing the lengths of each interval in the IntervalIndex. The length of an interval is defined as the difference between its end and its start.

Returns:

Index

An Index containing the lengths of each interval.

See also

[`Interval.length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length")

Return the length of the Interval.

Examples

\>>> intervals \= pd.IntervalIndex.from\_arrays(
...     \[1, 2, 3\], \[4, 5, 6\], closed\="right"
... )
\>>> intervals.length
Index(\[3, 3, 3\], dtype='int64')

Copy to clipboard

\>>> intervals \= pd.IntervalIndex.from\_tuples(\[(1, 5), (6, 10), (11, 15)\])
\>>> intervals.length
Index(\[4, 4, 4\], dtype='int64')

Copy to clipboard

On this page