[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.infer\_freq[#](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html#pandas-infer-freq "Link to this heading")

====================================================================================================================================

pandas.infer\_freq(_index_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/frequencies.py#L175-L225)
[#](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html#pandas.infer_freq "Link to this definition")

Infer the most likely frequency given the input index.

Deprecated since version 3.1.0: A future version of pandas will return a `BaseOffset` instead of a string. Use `pd.set_option('future.infer_freq_returns_offset', True)` to opt in to the future behavior.

This method attempts to deduce the most probable frequency (e.g., ‘D’ for daily, ‘H’ for hourly) from a sequence of datetime-like objects. It is particularly useful when the frequency of a time series is not explicitly set or known but can be inferred from its values.

Parameters:

**index**DatetimeIndex, TimedeltaIndex, Series or array-like

If passed a Series will use the values of the series (NOT THE INDEX).

Returns:

str or None

None if no discernible frequency.

Raises:

TypeError

If the index is not datetime-like.

ValueError

If there are fewer than three values.

See also

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")

Return a fixed frequency TimedeltaIndex with day as the default.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Return a fixed frequency PeriodIndex.

[`DatetimeIndex.freq`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#pandas.DatetimeIndex.freq "pandas.DatetimeIndex.freq")

Return the frequency object if it is set, otherwise None.

Examples

\>>> idx \= pd.date\_range(start\="2020/12/01", end\="2020/12/30", periods\=30)
\>>> pd.infer\_freq(idx)
'D'

Copy to clipboard

On this page