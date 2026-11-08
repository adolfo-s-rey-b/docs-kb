[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.combine.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.combine.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.combine.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.combine.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.combine.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.combine.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.combine.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.combine.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.combine.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.combine.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.combine.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.combine.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.combine[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html#pandas-timestamp-combine "Link to this heading")

========================================================================================================================================================

classmethod Timestamp.combine(_date_, _time_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html#pandas.Timestamp.combine "Link to this definition")

Combine a date and time into a single Timestamp object.

This method takes a date object and a time object and combines them into a single Timestamp that has the same date and time fields.

Parameters:

**date**datetime.date

The date part of the Timestamp.

**time**datetime.time

The time part of the Timestamp.

Returns:

Timestamp

A new Timestamp object representing the combined date and time.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Converts various types of data to datetime.

Examples

\>>> from datetime import date, time
\>>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))
Timestamp('2020-03-14 15:30:15')

Copy to clipboard

On this page