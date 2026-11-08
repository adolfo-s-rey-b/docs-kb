[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.is_overlapping.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.is_overlapping.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.is_overlapping.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.is_overlapping.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.is_overlapping.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.is_overlapping.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.is_overlapping.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.is\_overlapping[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#pandas-intervalindex-is-overlapping "Link to this heading")

==========================================================================================================================================================================================

property IntervalIndex.is\_overlapping[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L922-L980)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#pandas.IntervalIndex.is_overlapping "Link to this definition")

Return True if the IntervalIndex has overlapping intervals, else False.

Two intervals overlap if they share a common point, including closed endpoints. Intervals that only have an open endpoint in common do not overlap, and empty intervals contain no points at all, so they never overlap.

Returns:

bool

Boolean indicating if the IntervalIndex has overlapping intervals.

See also

[`Interval.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas.Interval.overlaps "pandas.Interval.overlaps")

Check whether two Interval objects overlap.

[`IntervalIndex.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")

Check an IntervalIndex elementwise for overlaps.

Examples

\>>> index \= pd.IntervalIndex.from\_tuples(\[(0, 2), (1, 3), (4, 5)\])
\>>> index
IntervalIndex(\[(0, 2\], (1, 3\], (4, 5\]\],
      dtype='interval\[int64, right\]')
\>>> index.is\_overlapping
True

Copy to clipboard

Intervals that share closed endpoints overlap:

\>>> index \= pd.interval\_range(0, 3, closed\="both")
\>>> index
IntervalIndex(\[\[0, 1\], \[1, 2\], \[2, 3\]\],
      dtype='interval\[int64, both\]')
\>>> index.is\_overlapping
True

Copy to clipboard

Intervals that only have an open endpoint in common do not overlap:

\>>> index \= pd.interval\_range(0, 3, closed\="left")
\>>> index
IntervalIndex(\[\[0, 1), \[1, 2), \[2, 3)\],\
      dtype='interval\[int64, left\]')\
\>>> index.is\_overlapping\
False\
\
Copy to clipboard\
\
Empty intervals never overlap, even when nested inside another interval:\
\
\>>> index \= pd.IntervalIndex.from\_tuples(\[(0, 3), (1, 1)\], closed\="left")\
\>>> index\
IntervalIndex(\[\[0, 3), \[1, 1)\],\
      dtype='interval\[int64, left\]')\
\>>> index.is\_overlapping\
False\
\
Copy to clipboard\
\
On this page