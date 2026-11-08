[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.resample[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html#pandas-api-typing-dataframegroupby-resample "Link to this heading")

=================================================================================================================================================================================================================

DataFrameGroupBy.resample(_rule_, _closed\=None_, _label\=None_, _convention\=None_, _on\=None_, _origin\='start\_day'_, _offset\=None_, _group\_keys\=False_, _\*_, _include\_groups\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3508-L3664)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html#pandas.api.typing.DataFrameGroupBy.resample "Link to this definition")

Provide resampling within each group of a groupby.

Given a grouper, the function resamples it according to a string “string” -> “frequency”.

See the [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 documentation for more details.

Parameters:

**rule**str or DateOffset

The offset string or object representing target grouper conversion.

**closed**{‘right’, ‘left’}, optional

Which side of bin interval is closed. See `Series.resample()`.

**label**{‘right’, ‘left’}, optional

Which bin edge label to label bucket with. See `Series.resample()`.

**convention**{‘start’, ‘end’, ‘s’, ‘e’}, optional

For `PeriodIndex` only. See `Series.resample()`.

**on**str, optional

For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.

**origin**Timestamp or str, default ‘start\_day’

The timestamp on which to adjust the grouping. See `Series.resample()` for accepted string values.

**offset**Timedelta or str, optional

An offset timedelta added to the origin.

**group\_keys**bool, default False

Whether to include the group keys in the result index when using `.apply()` on the resampled object.

**include\_groups**bool, default False

When True, will attempt to include the groupings in the operation in the case that they are columns of the DataFrame. If this raises a TypeError, the result will be computed with the groupings excluded. When False, the groupings will be excluded when applying `func`.

Added in version 2.2.0.

Changed in version 3.0: The default was changed to False, and True is no longer allowed.

**\*\*kwargs**

Additional keyword arguments forwarded to the underlying `Grouper`.

Returns:

DatetimeIndexResampler, PeriodIndexResampler or TimedeltaResampler

Resampler object for the type of the index.

See also

`Series.resample`

Resample a Series.

`DataFrame.resample`

Resample a DataFrame.

`Grouper`

Specify a frequency to resample with when grouping by a key.

`DatetimeIndex.resample`

Frequency conversion and resampling of time series.

Examples

\>>> idx \= pd.date\_range("1/1/2000", periods\=4, freq\="min")
\>>> df \= pd.DataFrame(data\=4 \* \[range(2)\], index\=idx, columns\=\["a", "b"\])
\>>> df.iloc\[2, 0\] \= 5
\>>> df
                    a  b
2000-01-01 00:00:00  0  1
2000-01-01 00:01:00  0  1
2000-01-01 00:02:00  5  1
2000-01-01 00:03:00  0  1

Copy to clipboard

Downsample the DataFrame into 3 minute bins and sum the values of the timestamps falling into a bin.

\>>> df.groupby("a").resample("3min").sum()
                         b
a
0   2000-01-01 00:00:00  2
    2000-01-01 00:03:00  1
5   2000-01-01 00:00:00  1

Copy to clipboard

Upsample the series into 30 second bins.

\>>> df.groupby("a").resample("30s").sum()
                    b
a
0   2000-01-01 00:00:00  1
    2000-01-01 00:00:30  0
    2000-01-01 00:01:00  1
    2000-01-01 00:01:30  0
    2000-01-01 00:02:00  0
    2000-01-01 00:02:30  0
    2000-01-01 00:03:00  1
5   2000-01-01 00:02:00  1

Copy to clipboard

Resample by month. Values are assigned to the month of the period.

\>>> df.groupby("a").resample("ME").sum()
            b
a
0   2000-01-31  3
5   2000-01-31  1

Copy to clipboard

Downsample the series into 3 minute bins as above, but close the right side of the bin interval.

\>>> (df.groupby("a").resample("3min", closed\="right").sum())
                         b
a
0   1999-12-31 23:57:00  1
    2000-01-01 00:00:00  2
5   2000-01-01 00:00:00  1

Copy to clipboard

Downsample the series into 3 minute bins and close the right side of the bin interval, but label each bin using the right edge instead of the left.

\>>> (df.groupby("a").resample("3min", closed\="right", label\="right").sum())
                         b
a
0   2000-01-01 00:00:00  1
    2000-01-01 00:03:00  2
5   2000-01-01 00:03:00  1

Copy to clipboard

On this page