[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.isoweekday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.isoweekday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.isoweekday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.isoweekday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.isoweekday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.isoweekday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.isoweekday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.isoweekday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.isoweekday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.isoweekday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.isoweekday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.isoweekday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.isoweekday[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#pandas-timestamp-isoweekday "Link to this heading")

=================================================================================================================================================================

Timestamp.isoweekday()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#pandas.Timestamp.isoweekday "Link to this definition")

Return the day of the week represented by the date.

Monday == 1 … Sunday == 7.

See also

[`Timestamp.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")

Return the day of the week with Monday=0, Sunday=6.

[`Timestamp.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")

Return a tuple containing ISO year, week number and weekday.

[`datetime.date.isoweekday`](https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday "(in Python v3.15)")

Equivalent method in datetime module.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.isoweekday()
7

Copy to clipboard

On this page