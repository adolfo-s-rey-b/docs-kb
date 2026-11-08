[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.asfreq.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.asfreq.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.asfreq.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.asfreq.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.asfreq.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.asfreq.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.asfreq.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.asfreq.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.asfreq.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.asfreq.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.asfreq.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.asfreq.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.asfreq[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#pandas-series-asfreq "Link to this heading")

============================================================================================================================================

Series.asfreq(_freq_, _method\=None_, _how\=None_, _normalize\=False_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L9121-L9244)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#pandas.Series.asfreq "Link to this definition")

Convert time series to specified frequency.

Returns the original data conformed to a new index with the specified frequency.

If the index of this Series/DataFrame is a [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")
, the new index is the result of transforming the original index with [`PeriodIndex.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#pandas.PeriodIndex.asfreq "pandas.PeriodIndex.asfreq")
 (so the original index will map one-to-one to the new index).

Otherwise, the new index will be equivalent to `pd.date_range(start, end, freq=freq)` where `start` and `end` are, respectively, the min and max entries in the original index (see [`pandas.date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
). The values corresponding to any timesteps in the new index which were not present in the original index will be null (`NaN`), unless a method for filling such unknowns is provided (see the `method` parameter below).

The [`resample()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")
 method is more appropriate if an operation on each group of timesteps (such as an aggregate) is necessary to represent the data at the new frequency.

Parameters:

**freq**DateOffset or str

Frequency DateOffset or string.

**method**{‘backfill’/’bfill’, ‘pad’/’ffill’}, default None

Method to use for filling holes in reindexed Series (note this does not fill NaNs that already were present):

*   ‘pad’ / ‘ffill’: propagate last valid observation forward to next valid based on the order of the index
    
*   ‘backfill’ / ‘bfill’: use NEXT valid observation to fill.
    

**how**{‘end’, ‘start’, ‘e’, ‘s’}, default ‘end’

For PeriodIndex only (see PeriodIndex.asfreq).

**normalize**bool, default False

Whether to reset output index to midnight.

**fill\_value**scalar, optional

Value to use for missing values, applied during upsampling (note this does not fill NaNs that already were present).

Returns:

Series/DataFrame

Series/DataFrame object reindexed to the specified frequency.

See also

[`reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")

Conform DataFrame to new index with optional filling logic.

Notes

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

Start by creating a series with 4 one minute timestamps.

\>>> index \= pd.date\_range("1/1/2000", periods\=4, freq\="min")
\>>> series \= pd.Series(\[0.0, None, 2.0, 3.0\], index\=index)
\>>> df \= pd.DataFrame({"s": series})
\>>> df
                       s
2000-01-01 00:00:00    0.0
2000-01-01 00:01:00    NaN
2000-01-01 00:02:00    2.0
2000-01-01 00:03:00    3.0

Copy to clipboard

Upsample the series into 30 second bins.

\>>> df.asfreq(freq\="30s")
                       s
2000-01-01 00:00:00    0.0
2000-01-01 00:00:30    NaN
2000-01-01 00:01:00    NaN
2000-01-01 00:01:30    NaN
2000-01-01 00:02:00    2.0
2000-01-01 00:02:30    NaN
2000-01-01 00:03:00    3.0

Copy to clipboard

Upsample again, providing a `fill value`.

\>>> df.asfreq(freq\="30s", fill\_value\=9.0)
                       s
2000-01-01 00:00:00    0.0
2000-01-01 00:00:30    9.0
2000-01-01 00:01:00    NaN
2000-01-01 00:01:30    9.0
2000-01-01 00:02:00    2.0
2000-01-01 00:02:30    9.0
2000-01-01 00:03:00    3.0

Copy to clipboard

Upsample again, providing a `method`.

\>>> df.asfreq(freq\="30s", method\="bfill")
                       s
2000-01-01 00:00:00    0.0
2000-01-01 00:00:30    NaN
2000-01-01 00:01:00    NaN
2000-01-01 00:01:30    2.0
2000-01-01 00:02:00    2.0
2000-01-01 00:02:30    3.0
2000-01-01 00:03:00    3.0

Copy to clipboard

On this page