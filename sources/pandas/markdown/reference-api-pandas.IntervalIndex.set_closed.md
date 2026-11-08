[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.set_closed.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.set_closed.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.set_closed.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.set_closed.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.set_closed.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.set_closed.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.set_closed.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.set_closed.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.set_closed.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.set_closed.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.set_closed.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.set_closed.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.set\_closed[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#pandas-intervalindex-set-closed "Link to this heading")

==============================================================================================================================================================================

IntervalIndex.set\_closed(_closed_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L440-L473)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#pandas.IntervalIndex.set_closed "Link to this definition")

Return an identical IntervalIndex closed on the specified side.

This method creates a new IntervalIndex with the same bounds but with a different closure specification.

Parameters:

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}

Whether the intervals are closed on the left-side, right-side, both or neither.

Returns:

IntervalIndex

A new IntervalIndex with the specified side closures.

See also

[`IntervalIndex.closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#pandas.IntervalIndex.closed "pandas.IntervalIndex.closed")

Returns inclusive side of the IntervalIndex.

Examples

\>>> index \= pd.interval\_range(0, 3)
\>>> index
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\]\],
              dtype='interval\[int64, right\]')
\>>> index.set\_closed("both")
IntervalIndex(\[\[0, 1\], \[1, 2\], \[2, 3\]\],
              dtype='interval\[int64, both\]')

Copy to clipboard

On this page