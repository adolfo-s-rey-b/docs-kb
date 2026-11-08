[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.month_name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.month_name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.month_name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.month_name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.month_name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.month_name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.month_name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.month_name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.month_name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.month_name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.month_name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.month_name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.month\_name[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#pandas-timestamp-month-name "Link to this heading")

==================================================================================================================================================================

Timestamp.month\_name(_locale\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#pandas.Timestamp.month_name "Link to this definition")

Return the month name of the Timestamp with specified locale.

This method returns the full name of the month corresponding to the Timestamp, such as ‘January’, ‘February’, etc. The month name can be returned in a specified locale if provided; otherwise, it defaults to the English locale.

Parameters:

**locale**str, default None (English locale)

Locale determining the language in which to return the month name.

Returns:

str

The full month name as a string.

See also

[`Timestamp.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#pandas.Timestamp.day_name "pandas.Timestamp.day_name")

Returns the name of the day of the week.

[`Timestamp.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")

Returns a formatted string of the Timestamp.

[`datetime.datetime.strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.15)")

Returns a string representing the date and time.

Examples

Get the month name in English (default):

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts.month\_name()
'March'

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.month\_name()
nan

Copy to clipboard

On this page