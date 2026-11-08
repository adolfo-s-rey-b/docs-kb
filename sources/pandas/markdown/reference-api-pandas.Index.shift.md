[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.shift.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.shift.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.shift.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.shift.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.shift.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.shift.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.shift.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.shift.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.shift.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.shift.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.shift.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.shift.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.shift[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#pandas-index-shift "Link to this heading")

======================================================================================================================================

Index.shift(_periods\=1_, _freq\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6264-L6323)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#pandas.Index.shift "Link to this definition")

Shift index by desired number of time frequency increments.

This method is for shifting the values of datetime-like indexes by a specified time increment a given number of times.

Parameters:

**periods**int, default 1

Number of periods (or increments) to shift by, can be positive or negative.

**freq**pandas.DateOffset, pandas.Timedelta or str, optional

Frequency increment to shift by. If None, the index is shifted by its own freq attribute. Offset aliases are valid strings, e.g., ‘D’, ‘W’, ‘M’ etc.

Returns:

pandas.Index

Shifted index.

See also

[`Series.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")

Shift values of Series.

Notes

This method is only implemented for datetime-like index classes, i.e., DatetimeIndex, PeriodIndex and TimedeltaIndex.

Examples

Put the first 5 month starts of 2011 into an index.

\>>> month\_starts \= pd.date\_range("1/1/2011", periods\=5, freq\="MS")
\>>> month\_starts
DatetimeIndex(\['2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01',\
               '2011-05-01'\],
              dtype='datetime64\[us\]', freq='MS')

Copy to clipboard

Shift the index by 10 days.

\>>> month\_starts.shift(10, freq\="D")
DatetimeIndex(\['2011-01-11', '2011-02-11', '2011-03-11', '2011-04-11',\
               '2011-05-11'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

The default value of freq is the freq attribute of the index, which is ‘MS’ (month start) in this example.

\>>> month\_starts.shift(10)
DatetimeIndex(\['2011-11-01', '2011-12-01', '2012-01-01', '2012-02-01',\
               '2012-03-01'\],
              dtype='datetime64\[us\]', freq='MS')

Copy to clipboard

On this page