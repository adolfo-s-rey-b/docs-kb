[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas-interval "Link to this heading")

=============================================================================================================================

class pandas.Interval[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/__init__.py)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "Link to this definition")

Immutable object implementing an Interval, a bounded slice-like interval.

An Interval represents a range of values between a left and right bound, with optional inclusion of the endpoints. It is used in [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
 and [`IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 for interval-based indexing and analysis.

Attributes

|     |     |
| --- | --- |
| [`left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "pandas.Interval.left") | Left bound for the interval. |
| [`right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "pandas.Interval.right") | Right bound for the interval. |
| [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed") | String describing the inclusive side the intervals. |

See also

[`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")

An Index of Interval objects that are all closed on the same side.

[`cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")

Convert continuous data into discrete bins (Categorical of Interval objects).

[`qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")

Convert continuous data into bins (Categorical of Interval objects) based on quantiles.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a period of time.

Notes

The parameters left and right must be from the same type, you must be able to compare them and they must satisfy `left <= right`.

A closed interval (in mathematics denoted by square brackets) contains its endpoints, i.e. the closed interval `[0, 5]` is characterized by the conditions `0 <= x <= 5`. This is what `closed='both'` stands for. An open interval (in mathematics denoted by parentheses) does not contain its endpoints, i.e. the open interval `(0, 5)` is characterized by the conditions `0 < x < 5`. This is what `closed='neither'` stands for. Intervals can also be half-open or half-closed, i.e. `[0, 5)` is described by `0 <= x < 5` (`closed='left'`) and `(0, 5]` is described by `0 < x <= 5` (`closed='right'`).

Examples

It is possible to build Intervals of different types, like numeric ones:

\>>> iv \= pd.Interval(left\=0, right\=5)
\>>> iv
Interval(0, 5, closed='right')

Copy to clipboard

You can check if an element belongs to it, or if it contains another interval:

\>>> 2.5 in iv
True
\>>> pd.Interval(left\=2, right\=5, closed\='both') in iv
True

Copy to clipboard

You can test the bounds (`closed='right'`, so `0 < x <= 5`):

\>>> 0 in iv
False
\>>> 5 in iv
True
\>>> 0.0001 in iv
True

Copy to clipboard

Calculate its length

\>>> iv.length
5

Copy to clipboard

You can operate with + and \* over an Interval and the operation is applied to each of its bounds, so the result depends on the type of the bound elements

\>>> shifted\_iv \= iv + 3
\>>> shifted\_iv
Interval(3, 8, closed='right')
\>>> extended\_iv \= iv \* 10.0
\>>> extended\_iv
Interval(0.0, 50.0, closed='right')

Copy to clipboard

To create a time interval you can use Timestamps as the bounds

\>>> year\_2017 \= pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),
...                         pd.Timestamp('2018-01-01 00:00:00'),
...                         closed\='left')
\>>> pd.Timestamp('2017-01-01 00:00') in year\_2017
True
\>>> year\_2017.length
Timedelta('365 days 00:00:00')

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed") | String describing the inclusive side the intervals. |
| [`closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "pandas.Interval.closed_left") | Check if the interval is closed on the left side. |
| [`closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "pandas.Interval.closed_right") | Check if the interval is closed on the right side. |
| [`is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas.Interval.is_empty "pandas.Interval.is_empty") | Indicates if an interval is empty, meaning it contains no points. |
| [`left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "pandas.Interval.left") | Left bound for the interval. |
| [`length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length") | Return the length of the Interval. |
| [`mid`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html#pandas.Interval.mid "pandas.Interval.mid") | Return the midpoint of the Interval. |
| [`open_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "pandas.Interval.open_left") | Check if the interval is open on the left side. |
| [`open_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "pandas.Interval.open_right") | Check if the interval is open on the right side. |
| [`right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "pandas.Interval.right") | Right bound for the interval. |

Methods

|     |     |
| --- | --- |
| [`overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas.Interval.overlaps "pandas.Interval.overlaps")<br>(other) | Check whether two Interval objects overlap. |

On this page