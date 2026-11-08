[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.day_name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.day_name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.day_name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.day_name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.day_name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.day_name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.day_name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.day_name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.day_name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.day_name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.day_name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.day_name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.day\_name[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#pandas-timestamp-day-name "Link to this heading")

============================================================================================================================================================

Timestamp.day\_name(_locale\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#pandas.Timestamp.day_name "Link to this definition")

Return the day name of the Timestamp with specified locale.

This method returns the full name of the day of the week (e.g., ‘Monday’, ‘Tuesday’) for the given Timestamp. The locale can be specified to return the name in a particular language.

Parameters:

**locale**str, default None (English locale)

Locale determining the language in which to return the day name.

Returns:

str

See also

[`Timestamp.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas.Timestamp.day_of_week "pandas.Timestamp.day_of_week")

Return day of the week.

[`Timestamp.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas.Timestamp.day_of_year "pandas.Timestamp.day_of_year")

Return day of the year.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts.day\_name()
'Saturday'

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.day\_name()
nan

Copy to clipboard

On this page