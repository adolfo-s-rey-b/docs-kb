[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeTZDtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeTZDtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeTZDtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeTZDtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeTZDtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeTZDtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeTZDtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeTZDtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeTZDtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeTZDtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeTZDtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeTZDtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeTZDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas-datetimetzdtype "Link to this heading")

==================================================================================================================================================

class pandas.DatetimeTZDtype(_unit\='ns'_, _tz\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L722-L997)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "Link to this definition")

An ExtensionDtype for timezone-aware datetime data.

**This is not an actual numpy dtype**, but a duck type.

Parameters:

**unit**str, default “ns”

The precision of the datetime data. Valid options are `"s"`, `"ms"`, `"us"`, `"ns"`.

**tz**str, int, or datetime.tzinfo

The timezone.

Attributes

|     |     |
| --- | --- |
| [`unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html#pandas.DatetimeTZDtype.unit "pandas.DatetimeTZDtype.unit") | The precision of the datetime data. |
| [`tz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.tz.html#pandas.DatetimeTZDtype.tz "pandas.DatetimeTZDtype.tz") | The timezone. |

Raises:

ZoneInfoNotFoundError

When the requested timezone cannot be found.

See also

[`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")

Numpy data type for datetime.

[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")

Python datetime object.

Examples

\>>> from zoneinfo import ZoneInfo
\>>> pd.DatetimeTZDtype(tz\=ZoneInfo("UTC"))
datetime64\[ns, UTC\]

Copy to clipboard

\>>> pd.DatetimeTZDtype(tz\=ZoneInfo("Europe/Paris"))
datetime64\[ns, Europe/Paris\]

Copy to clipboard

On this page