[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.day_name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.day_name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.day_name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.day_name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.day_name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.day_name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.day_name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.day_name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.day_name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.day_name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.day_name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.day_name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.day\_name[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#pandas-datetimeindex-day-name "Link to this heading")

========================================================================================================================================================================

DatetimeIndex.day\_name(_locale\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1113-L1155)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#pandas.DatetimeIndex.day_name "Link to this definition")

Return the day names with specified locale.

This method returns the full name of the day of the week (e.g., “Monday”, “Tuesday”) for each datetime value in the Series/Index. The names can be localized to different languages using the locale parameter.

Parameters:

**locale**str, optional

Locale determining the language in which to return the day name. Default is English locale (`'en_US.utf8'`). Use the command `locale -a` on your terminal on Unix systems to find your locale language code.

Returns:

Index

Index of day names.

See also

[`DatetimeIndex.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month_name.html#pandas.DatetimeIndex.month_name "pandas.DatetimeIndex.month_name")

Return the month names with specified locale.

Examples

\>>> idx \= pd.date\_range(start\="2018-01-01", freq\="D", periods\=3)
\>>> idx
DatetimeIndex(\['2018-01-01', '2018-01-02', '2018-01-03'\],
              dtype='datetime64\[us\]', freq='D')
\>>> idx.day\_name()
Index(\['Monday', 'Tuesday', 'Wednesday'\], dtype='str')

Copy to clipboard

Using the `locale` parameter you can set a different locale language, for example: `idx.day_name(locale='pt_BR.utf8')` will return day names in Brazilian Portuguese language.

\>>> idx.day\_name(locale\="pt\_BR.utf8")
Index(\['Segunda', 'Terça', 'Quarta'\], dtype='str')

Copy to clipboard

On this page