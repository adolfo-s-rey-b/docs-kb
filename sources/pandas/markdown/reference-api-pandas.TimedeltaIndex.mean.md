[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.mean.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.mean.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.mean.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.mean.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.mean.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.mean.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.mean.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.mean.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.mean.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.mean.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.mean.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.mean.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html#pandas-timedeltaindex-mean "Link to this heading")

==============================================================================================================================================================

TimedeltaIndex.mean(_\*_, _skipna\=True_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimelike.py#L117-L165)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html#pandas.TimedeltaIndex.mean "Link to this definition")

Return the mean value of the Array.

This method computes the arithmetic mean of the datetime or timedelta values in the index, optionally skipping NaT values.

Parameters:

**skipna**bool, default True

Whether to ignore any NaT elements.

**axis**int, optional, default 0

Axis for the function to be applied on.

Returns:

scalar

Timestamp or Timedelta.

See also

[`numpy.ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "(in NumPy v2.5)")

Returns the average of array elements along a given axis.

[`Series.mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "pandas.Series.mean")

Return the mean value in a Series.

Notes

mean is only defined for Datetime and Timedelta dtypes, not for Period.

Examples

For [`pandas.DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
:

\>>> idx \= pd.date\_range("2001-01-01 00:00", periods\=3)
\>>> idx
DatetimeIndex(\['2001-01-01', '2001-01-02', '2001-01-03'\],
              dtype='datetime64\[us\]', freq='D')
\>>> idx.mean()
Timestamp('2001-01-02 00:00:00')

Copy to clipboard

For [`pandas.TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
:

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\="D")
\>>> tdelta\_idx
TimedeltaIndex(\['1 days', '2 days', '3 days'\],
                dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.mean()
Timedelta('2 days 00:00:00')

Copy to clipboard

On this page