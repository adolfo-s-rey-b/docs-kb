[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.today.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.today.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.today.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.today.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.today.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.today.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.today.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.today.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.today.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.today.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.today.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.today.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.today[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas-timestamp-today "Link to this heading")

==================================================================================================================================================

classmethod Timestamp.today(_tz\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas.Timestamp.today "Link to this definition")

Return the current time in the local timezone.

This differs from datetime.today() in that it can be localized to a passed timezone.

Parameters:

**tz**str or timezone object, default None

Timezone to localize to.

See also

[`datetime.datetime.today`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "(in Python v3.15)")

Returns the current local date.

[`Timestamp.now`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas.Timestamp.now "pandas.Timestamp.now")

Returns current time with optional timezone.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

A class representing a specific timestamp.

Examples

\>>> pd.Timestamp.today()
Timestamp('2020-11-16 22:37:39.969883')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.today()
NaT

Copy to clipboard

On this page