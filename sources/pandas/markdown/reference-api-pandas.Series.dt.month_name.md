[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.month\_name[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html#pandas-series-dt-month-name "Link to this heading")

==================================================================================================================================================================

Series.dt.month\_name(_locale\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimes.py#L1289-L1362)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html#pandas.Series.dt.month_name "Link to this definition")

Return the month names with specified locale.

This method returns the full name of the month (e.g., “January”, “February”) for each datetime value in the Series/Index. The names can be localized to different languages using the locale parameter.

Parameters:

**locale**str, optional

Locale determining the language in which to return the month name. Default is English locale (`'en_US.utf8'`). Use the command `locale -a` on your terminal on Unix systems to find your locale language code.

Returns:

Series or Index

Series or Index of month names.

See also

[`DatetimeIndex.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#pandas.DatetimeIndex.day_name "pandas.DatetimeIndex.day_name")

Return the day names with specified locale.

Examples

\>>> s \= pd.Series(pd.date\_range(start\="2018-01", freq\="ME", periods\=3))
\>>> s
0   2018-01-31
1   2018-02-28
2   2018-03-31
dtype: datetime64\[us\]
\>>> s.dt.month\_name()
0     January
1    February
2       March
dtype: str

Copy to clipboard

\>>> idx \= pd.date\_range(start\="2018-01", freq\="ME", periods\=3)
\>>> idx
DatetimeIndex(\['2018-01-31', '2018-02-28', '2018-03-31'\],
              dtype='datetime64\[us\]', freq='ME')
\>>> idx.month\_name()
Index(\['January', 'February', 'March'\], dtype='str')

Copy to clipboard

Using the `locale` parameter you can set a different locale language, for example: `idx.month_name(locale='pt_BR.utf8')` will return month names in Brazilian Portuguese language.

\>>> idx \= pd.date\_range(start\="2018-01", freq\="ME", periods\=3)
\>>> idx
DatetimeIndex(\['2018-01-31', '2018-02-28', '2018-03-31'\],
              dtype='datetime64\[us\]', freq='ME')
\>>> idx.month\_name(locale\="pt\_BR.utf8")
Index(\['Janeiro', 'Fevereiro', 'Março'\], dtype='str')

Copy to clipboard

On this page