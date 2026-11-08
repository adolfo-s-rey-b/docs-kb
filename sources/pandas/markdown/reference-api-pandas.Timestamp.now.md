[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.now.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.now.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.now.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.now.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.now.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.now.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.now.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.now.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.now.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.now.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.now.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.now.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.now[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas-timestamp-now "Link to this heading")

============================================================================================================================================

classmethod Timestamp.now(_tz\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas.Timestamp.now "Link to this definition")

Return new Timestamp object representing current time local to tz.

This method returns a new Timestamp object that represents the current time. If a timezone is provided, either through a timezone object or an IANA standard timezone identifier, the current time will be localized to that timezone. Otherwise, it returns the current local time.

Parameters:

**tz**str or timezone object, default None

Timezone to localize to.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`Timestamp.utcnow`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas.Timestamp.utcnow "pandas.Timestamp.utcnow")

Return a new Timestamp representing UTC day and time.

[`Timestamp.today`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas.Timestamp.today "pandas.Timestamp.today")

Return the current time in the local timezone.

Examples

\>>> pd.Timestamp.now()
Timestamp('2020-11-16 22:06:16.378782')

Copy to clipboard

If you want a specific timezone, in this case ‘Brazil/East’:

\>>> pd.Timestamp.now('Brazil/East')
Timestamp('2025-11-11 22:17:59.609943-03:00)

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.now()
NaT

Copy to clipboard

On this page