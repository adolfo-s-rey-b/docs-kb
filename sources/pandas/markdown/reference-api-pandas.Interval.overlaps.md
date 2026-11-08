[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.overlaps.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.overlaps.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.overlaps.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.overlaps.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.overlaps.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.overlaps.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.overlaps.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.overlaps.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.overlaps.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.overlaps.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.overlaps.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.overlaps.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.overlaps[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas-interval-overlaps "Link to this heading")

========================================================================================================================================================

Interval.overlaps(_other_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas.Interval.overlaps "Link to this definition")

Check whether two Interval objects overlap.

Two intervals overlap if they share a common point, including closed endpoints. Intervals that only have an open endpoint in common do not overlap, and empty intervals contain no points at all, so they never overlap.

Parameters:

**other**Interval

Interval to check against for an overlap.

Returns:

bool

True if the two intervals overlap.

See also

`IntervalArray.overlaps`

The corresponding method for IntervalArray.

[`IntervalIndex.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")

The corresponding method for IntervalIndex.

Examples

\>>> i1 \= pd.Interval(0, 2)
\>>> i2 \= pd.Interval(1, 3)
\>>> i1.overlaps(i2)
True
\>>> i3 \= pd.Interval(4, 5)
\>>> i1.overlaps(i3)
False

Copy to clipboard

Intervals that share closed endpoints overlap:

\>>> i4 \= pd.Interval(0, 1, closed\='both')
\>>> i5 \= pd.Interval(1, 2, closed\='both')
\>>> i4.overlaps(i5)
True

Copy to clipboard

Intervals that only have an open endpoint in common do not overlap:

\>>> i6 \= pd.Interval(1, 2, closed\='neither')
\>>> i4.overlaps(i6)
False

Copy to clipboard

Empty intervals do not overlap with anything, including themselves:

\>>> i7 \= pd.Interval(1, 1, closed\='left')
\>>> i4.overlaps(i7)
False
\>>> i7.overlaps(i7)
False

Copy to clipboard

On this page