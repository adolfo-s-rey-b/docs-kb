[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.fromisoformat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.fromisoformat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.fromisoformat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.fromisoformat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.fromisoformat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.fromisoformat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.fromisoformat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.fromisoformat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.fromisoformat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.fromisoformat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.fromisoformat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.fromisoformat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.fromisoformat[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html#pandas-timestamp-fromisoformat "Link to this heading")

==========================================================================================================================================================================

classmethod Timestamp.fromisoformat(_date\_string_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html#pandas.Timestamp.fromisoformat "Link to this definition")

Construct a Timestamp from a string in ISO 8601 format.

This classmethod wraps [`datetime.datetime.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat "(in Python v3.15)")
, returning a [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 instead of a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
.

Parameters:

**date\_string**str

A date-time string in one of the ISO 8601 formats supported by [`datetime.datetime.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat "(in Python v3.15)")
.

Returns:

Timestamp

A Timestamp corresponding to the parsed date-time string.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to `datetime`.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`datetime.datetime.fromisoformat`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat "(in Python v3.15)")

The standard library counterpart.

Examples

\>>> pd.Timestamp.fromisoformat("2023-01-15")
Timestamp('2023-01-15 00:00:00')

Copy to clipboard

\>>> pd.Timestamp.fromisoformat("2023-01-15T10:30:00")
Timestamp('2023-01-15 10:30:00')

Copy to clipboard

On this page