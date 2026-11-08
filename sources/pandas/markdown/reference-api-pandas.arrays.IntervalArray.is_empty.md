[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_empty.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.is_empty.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.is_empty.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.is\_empty[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_empty.html#pandas-arrays-intervalarray-is-empty "Link to this heading")

=============================================================================================================================================================================================

IntervalArray.is\_empty[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_empty.html#pandas.arrays.IntervalArray.is_empty "Link to this definition")

Indicates if an interval is empty, meaning it contains no points.

An interval is considered empty if its left and right endpoints are equal, and it is not closed on both sides. This means that the interval does not include any real points. In the case of an [`pandas.arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 or `IntervalIndex`, the property returns a boolean array indicating the emptiness of each interval.

Returns:

bool or ndarray

A boolean indicating if a scalar `Interval` is empty, or a boolean `ndarray` positionally indicating if an `Interval` in an `IntervalArray` or `IntervalIndex` is empty.

See also

`Interval.length`

Return the length of the Interval.

Examples

An `Interval` that contains points is not empty:

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

An `IntervalArray` or `IntervalIndex` returns a boolean `ndarray` positionally indicating if an `Interval` is empty:

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