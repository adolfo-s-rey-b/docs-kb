[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.interval\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas-interval-range "Link to this heading")

================================================================================================================================================

pandas.interval\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _name\=None_, _closed\='right'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L1681-L1869)
[#](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "Link to this definition")

Return a fixed frequency IntervalIndex.

This function generates a sequence of evenly spaced intervals over a specified range, supporting numeric, datetime-like, and timedelta endpoints.

Parameters:

**start**numeric or datetime-like, default None

Left bound for generating intervals.

**end**numeric or datetime-like, default None

Right bound for generating intervals.

**periods**int, default None

Number of periods to generate.

**freq**numeric, str, Timedelta, datetime.timedelta, or DateOffset, default None

The length of each interval. Must be consistent with the type of start and end, e.g. 2 for numeric, or ‘5H’ for datetime-like. Default is 1 for numeric and ‘D’ for datetime-like.

**name**str, default None

Name of the resulting IntervalIndex.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

Returns:

IntervalIndex

Object with a fixed frequency.

See also

[`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")

An Index of intervals that are all closed on the same side.

Notes

Of the four parameters `start`, `end`, `periods`, and `freq`, exactly three must be specified. If `freq` is omitted, the resulting `IntervalIndex` will have `periods` linearly spaced elements between `start` and `end`, inclusively.

To learn more about datetime-like frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

Numeric `start` and `end` is supported.

\>>> pd.interval\_range(start\=0, end\=5)
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\], (3, 4\], (4, 5\]\],
              dtype='interval\[int64, right\]')

Copy to clipboard

Additionally, datetime-like input is also supported.

\>>> pd.interval\_range(
...     start\=pd.Timestamp("2017-01-01"), end\=pd.Timestamp("2017-01-04")
... )
IntervalIndex(\[(2017-01-01 00:00:00, 2017-01-02 00:00:00\],
               (2017-01-02 00:00:00, 2017-01-03 00:00:00\],
               (2017-01-03 00:00:00, 2017-01-04 00:00:00\]\],
              dtype='interval\[datetime64\[us\], right\]')

Copy to clipboard

The `freq` parameter specifies the frequency between the left and right. endpoints of the individual intervals within the `IntervalIndex`. For numeric `start` and `end`, the frequency must also be numeric.

\>>> pd.interval\_range(start\=0, periods\=4, freq\=1.5)
IntervalIndex(\[(0.0, 1.5\], (1.5, 3.0\], (3.0, 4.5\], (4.5, 6.0\]\],
              dtype='interval\[float64, right\]')

Copy to clipboard

Similarly, for datetime-like `start` and `end`, the frequency must be convertible to a DateOffset.

\>>> pd.interval\_range(start\=pd.Timestamp("2017-01-01"), periods\=3, freq\="MS")
IntervalIndex(\[(2017-01-01 00:00:00, 2017-02-01 00:00:00\],
               (2017-02-01 00:00:00, 2017-03-01 00:00:00\],
               (2017-03-01 00:00:00, 2017-04-01 00:00:00\]\],
              dtype='interval\[datetime64\[us\], right\]')

Copy to clipboard

Specify `start`, `end`, and `periods`; the frequency is generated automatically (linearly spaced).

\>>> pd.interval\_range(start\=0, end\=6, periods\=4)
IntervalIndex(\[(0.0, 1.5\], (1.5, 3.0\], (3.0, 4.5\], (4.5, 6.0\]\],
          dtype='interval\[float64, right\]')

Copy to clipboard

The `closed` parameter specifies which endpoints of the individual intervals within the `IntervalIndex` are closed.

\>>> pd.interval\_range(end\=5, periods\=4, closed\="both")
IntervalIndex(\[\[1, 2\], \[2, 3\], \[3, 4\], \[4, 5\]\],
              dtype='interval\[int64, both\]')

Copy to clipboard

On this page