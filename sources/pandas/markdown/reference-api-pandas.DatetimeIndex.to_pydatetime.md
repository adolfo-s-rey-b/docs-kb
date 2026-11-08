[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.to_pydatetime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.to_pydatetime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.to\_pydatetime[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html#pandas-datetimeindex-to-pydatetime "Link to this heading")

=======================================================================================================================================================================================

DatetimeIndex.to\_pydatetime()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L938-L964)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html#pandas.DatetimeIndex.to_pydatetime "Link to this definition")

Return an ndarray of `datetime.datetime` objects.

This method converts each element in the DatetimeIndex to a native Python `datetime.datetime` object, including timezone information if present.

Returns:

numpy.ndarray

An ndarray of `datetime.datetime` objects.

See also

[`DatetimeIndex.to_julian_date`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html#pandas.DatetimeIndex.to_julian_date "pandas.DatetimeIndex.to_julian_date")

Converts Datetime Array to float64 ndarray of Julian Dates.

Examples

\>>> idx \= pd.date\_range("2018-02-27", periods\=3)
\>>> idx.to\_pydatetime()
array(\[datetime.datetime(2018, 2, 27, 0, 0),\
       datetime.datetime(2018, 2, 28, 0, 0),\
       datetime.datetime(2018, 3, 1, 0, 0)\], dtype=object)

Copy to clipboard

On this page