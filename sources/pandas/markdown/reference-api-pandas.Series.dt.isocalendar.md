[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.isocalendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.isocalendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.isocalendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.isocalendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.isocalendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.isocalendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.isocalendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.isocalendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.isocalendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.isocalendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.isocalendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.isocalendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.isocalendar[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html#pandas-series-dt-isocalendar "Link to this heading")

====================================================================================================================================================================

Series.dt.isocalendar()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/accessors.py#L417-L449)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html#pandas.Series.dt.isocalendar "Link to this definition")

Calculate year, week, and day according to the ISO 8601 standard.

The ISO 8601 standard defines the first week of the year as the week containing the first Thursday. This method returns a DataFrame with columns for the ISO year, ISO week number, and ISO day of week.

Returns:

DataFrame

With columns year, week and day.

See also

[`Timestamp.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")

Function return a 3-tuple containing ISO year, week number, and weekday for the given Timestamp object.

[`datetime.date.isocalendar`](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "(in Python v3.15)")

Return a named tuple object with three components: year, week and weekday.

Examples

\>>> ser \= pd.to\_datetime(pd.Series(\["2010-01-01", pd.NaT\]))
\>>> ser.dt.isocalendar()
   year  week  day
0  2009    53     5
1  <NA>  <NA>  <NA>
\>>> ser.dt.isocalendar().week
0      53
1    <NA>
Name: week, dtype: UInt32

Copy to clipboard

On this page