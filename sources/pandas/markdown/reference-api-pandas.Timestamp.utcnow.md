[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.utcnow.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.utcnow.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.utcnow.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.utcnow.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.utcnow.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.utcnow.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.utcnow.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.utcnow.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.utcnow.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.utcnow.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.utcnow.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.utcnow.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.utcnow[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas-timestamp-utcnow "Link to this heading")

=====================================================================================================================================================

classmethod Timestamp.utcnow()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas.Timestamp.utcnow "Link to this definition")

Return a new Timestamp representing UTC day and time.

Deprecated since version 3.0.0: `Timestamp.utcnow` is deprecated and will be removed in a future version. Use `Timestamp.now('UTC')` instead.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Constructs an arbitrary datetime.

[`Timestamp.now`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas.Timestamp.now "pandas.Timestamp.now")

Return the current local date and time, which can be timezone-aware.

[`Timestamp.today`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas.Timestamp.today "pandas.Timestamp.today")

Return the current local date and time with timezone information set to None.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`Timestamp.utctimetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#pandas.Timestamp.utctimetuple "pandas.Timestamp.utctimetuple")

Return UTC time tuple, compatible with time.localtime().

Examples

\>>> pd.Timestamp.utcnow()
Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')

Copy to clipboard

On this page