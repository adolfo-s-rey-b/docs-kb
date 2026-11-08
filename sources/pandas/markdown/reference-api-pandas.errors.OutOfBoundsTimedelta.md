[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsTimedelta.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.OutOfBoundsTimedelta.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.OutOfBoundsTimedelta.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.OutOfBoundsTimedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsTimedelta.html#pandas-errors-outofboundstimedelta "Link to this heading")

======================================================================================================================================================================================

exception pandas.errors.OutOfBoundsTimedelta[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.OutOfBoundsTimedelta.html#pandas.errors.OutOfBoundsTimedelta "Link to this definition")

Raised when encountering a timedelta value that cannot be represented.

Representation should be within a timedelta64\[ns\].

See also

`date_range`

Return a fixed frequency DatetimeIndex.

Examples

\>>> pd.date\_range(start\="1/1/1700", freq\="B", periods\=100000, unit\="ns")
Traceback (most recent call last):
OutOfBoundsTimedelta: Cannot cast 139999 days 00:00:00
to unit='ns' without overflow.

Copy to clipboard

On this page