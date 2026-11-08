[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.is\_empty[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas-interval-is-empty "Link to this heading")

=========================================================================================================================================================

Interval.is\_empty[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas.Interval.is_empty "Link to this definition")

Indicates if an interval is empty, meaning it contains no points.

An interval is considered empty if its left and right endpoints are equal, and it is not closed on both sides. This means that the interval does not include any real points. In the case of an [`pandas.arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 or [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
, the property returns a boolean array indicating the emptiness of each interval.

Returns:

bool or ndarray

A boolean indicating if a scalar [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 is empty, or a boolean `ndarray` positionally indicating if an `Interval` in an [`IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 or [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
 is empty.

See also

[`Interval.length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length")

Return the length of the Interval.

Examples

An [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 that contains points is not empty:

\>>> pd.Interval(0, 1, closed\='right').is\_empty
False

Copy to clipboard

An `Interval` that does not contain any points is empty:

\>>> pd.Interval(0, 0, closed\='right').is\_empty
True
\>>> pd.Interval(0, 0, closed\='left').is\_empty
True
\>>> pd.Interval(0, 0, closed\='neither').is\_empty
True

Copy to clipboard

An `Interval` that contains a single point is not empty:

\>>> pd.Interval(0, 0, closed\='both').is\_empty
False

Copy to clipboard

An [`IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 or [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
 returns a boolean `ndarray` positionally indicating if an `Interval` is empty:

\>>> ivs \= \[pd.Interval(0, 0, closed\='neither'),\
...        pd.Interval(1, 2, closed\='neither')\]
\>>> pd.arrays.IntervalArray(ivs).is\_empty
array(\[ True, False\])

Copy to clipboard

Missing values are not considered empty:

\>>> ivs \= \[pd.Interval(0, 0, closed\='neither'), np.nan\]
\>>> pd.IntervalIndex(ivs).is\_empty
array(\[ True, False\])

Copy to clipboard

On this page