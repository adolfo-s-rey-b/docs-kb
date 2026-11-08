[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html#pandas-tseries-offsets-baseoffset "Link to this heading")

===================================================================================================================================================================================

class pandas.tseries.offsets.BaseOffset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html#pandas.tseries.offsets.BaseOffset "Link to this definition")

Base class for all pandas date offsets.

Every offset in `pandas.tseries.offsets` is a subclass of `BaseOffset`, so `isinstance(obj, BaseOffset)` is the way to check whether an object is a pandas offset. `BaseOffset` is not meant to be instantiated directly.

Attributes

|     |     |
| --- | --- |
| [`n`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.n.html#pandas.tseries.offsets.BaseOffset.n "pandas.tseries.offsets.BaseOffset.n") | Return the count of the number of periods. |
| [`normalize`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.normalize.html#pandas.tseries.offsets.BaseOffset.normalize "pandas.tseries.offsets.BaseOffset.normalize") | Return boolean whether the frequency can align with midnight. |

See also

`tseries.offsets.DateOffset`

Offset backed by a `dateutil.relativedelta`.

`tseries.frequencies.to_offset`

Convert a string or timedelta to an offset.

Examples

\>>> pd.offsets.Hour(5).n
5
\>>> pd.offsets.Hour(5).normalize
False

Copy to clipboard

\>>> isinstance(pd.offsets.BDay(), pd.offsets.BaseOffset)
True

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| `base` | Returns a copy of the calling offset object with n=1 and all other attributes equal. |
| [`freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html#pandas.tseries.offsets.BaseOffset.freqstr "pandas.tseries.offsets.BaseOffset.freqstr") | Return a string representing the frequency. |
| [`kwds`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.kwds.html#pandas.tseries.offsets.BaseOffset.kwds "pandas.tseries.offsets.BaseOffset.kwds") | Return a dict of extra parameters for the offset. |
| [`n`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.n.html#pandas.tseries.offsets.BaseOffset.n "pandas.tseries.offsets.BaseOffset.n") | Return the count of the number of periods. |
| [`name`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html#pandas.tseries.offsets.BaseOffset.name "pandas.tseries.offsets.BaseOffset.name") | (DEPRECATED) Return a string representing the base frequency. |
| [`nanos`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.nanos.html#pandas.tseries.offsets.BaseOffset.nanos "pandas.tseries.offsets.BaseOffset.nanos") | Return an integer of the total number of nanoseconds. |
| [`normalize`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.normalize.html#pandas.tseries.offsets.BaseOffset.normalize "pandas.tseries.offsets.BaseOffset.normalize") | Return boolean whether the frequency can align with midnight. |
| [`rule_code`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html#pandas.tseries.offsets.BaseOffset.rule_code "pandas.tseries.offsets.BaseOffset.rule_code") | Return a string representing the base frequency. |

Methods

|     |     |
| --- | --- |
| [`copy`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html#pandas.tseries.offsets.BaseOffset.copy "pandas.tseries.offsets.BaseOffset.copy")<br>() | Return a copy of the frequency. |
| [`is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_month_end.html#pandas.tseries.offsets.BaseOffset.is_month_end "pandas.tseries.offsets.BaseOffset.is_month_end")<br>(ts) | Return boolean whether a timestamp occurs on the month end. |
| [`is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_month_start.html#pandas.tseries.offsets.BaseOffset.is_month_start "pandas.tseries.offsets.BaseOffset.is_month_start")<br>(ts) | Return boolean whether a timestamp occurs on the month start. |
| [`is_on_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#pandas.tseries.offsets.BaseOffset.is_on_offset "pandas.tseries.offsets.BaseOffset.is_on_offset")<br>(dt) | Return boolean whether a timestamp intersects with this frequency. |
| [`is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_end.html#pandas.tseries.offsets.BaseOffset.is_quarter_end "pandas.tseries.offsets.BaseOffset.is_quarter_end")<br>(ts) | Return boolean whether a timestamp occurs on the quarter end. |
| [`is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html#pandas.tseries.offsets.BaseOffset.is_quarter_start "pandas.tseries.offsets.BaseOffset.is_quarter_start")<br>(ts) | Return boolean whether a timestamp occurs on the quarter start. |
| [`is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html#pandas.tseries.offsets.BaseOffset.is_year_end "pandas.tseries.offsets.BaseOffset.is_year_end")<br>(ts) | Return boolean whether a timestamp occurs on the year end. |
| [`is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_start.html#pandas.tseries.offsets.BaseOffset.is_year_start "pandas.tseries.offsets.BaseOffset.is_year_start")<br>(ts) | Return boolean whether a timestamp occurs on the year start. |
| [`rollback`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollback.html#pandas.tseries.offsets.BaseOffset.rollback "pandas.tseries.offsets.BaseOffset.rollback")<br>(dt) | Roll provided date backward to next offset only if not on offset. |
| [`rollforward`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollforward.html#pandas.tseries.offsets.BaseOffset.rollforward "pandas.tseries.offsets.BaseOffset.rollforward")<br>(dt) | Roll provided date forward to next offset only if not on offset. |

On this page