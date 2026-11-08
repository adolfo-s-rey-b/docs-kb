[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.to_julian_date.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.to_julian_date.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.to\_julian\_date[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html#pandas-datetimeindex-to-julian-date "Link to this heading")

===========================================================================================================================================================================================

DatetimeIndex.to\_julian\_date()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1805-L1829)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html#pandas.DatetimeIndex.to_julian_date "Link to this definition")

Convert Timestamp to a Julian Date.

This method returns the number of days as a float since noon January 1, 4713 BC.

[https://en.wikipedia.org/wiki/Julian\_day](https://en.wikipedia.org/wiki/Julian_day)

Returns:

ndarray or Index

Float values that represent each date in Julian Calendar.

See also

[`Timestamp.to_julian_date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#pandas.Timestamp.to_julian_date "pandas.Timestamp.to_julian_date")

Equivalent method on `Timestamp` objects.

Examples

\>>> idx \= pd.DatetimeIndex(\["2028-08-12 00:54", "2028-08-12 02:06"\])
\>>> idx.to\_julian\_date()
Index(\[2461995.5375, 2461995.5875\], dtype='float64')

Copy to clipboard

On this page