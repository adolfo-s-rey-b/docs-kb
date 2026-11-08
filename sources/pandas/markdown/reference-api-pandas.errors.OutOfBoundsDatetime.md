[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsDatetime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.OutOfBoundsDatetime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.OutOfBoundsDatetime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.OutOfBoundsDatetime[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsDatetime.html#pandas-errors-outofboundsdatetime "Link to this heading")

===================================================================================================================================================================================

exception pandas.errors.OutOfBoundsDatetime[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsDatetime.html#pandas.errors.OutOfBoundsDatetime "Link to this definition")

Raised when the datetime is outside the range that can be represented.

This error occurs when attempting to convert or parse a datetime value that exceeds the bounds supported by pandas’ internal datetime representation.

See also

`to_datetime`

Convert argument to datetime.

`Timestamp`

Pandas replacement for python `datetime.datetime` object.

Examples

\>>> pd.to\_datetime("08335394550")
Traceback (most recent call last):
OutOfBoundsDatetime: Parsing "08335394550" to datetime overflows,
at position 0

Copy to clipboard

On this page