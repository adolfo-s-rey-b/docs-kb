[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.from_fields.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.from_fields.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.from_fields.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.from_fields.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.from_fields.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.from_fields.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.from_fields.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.from_fields.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.from_fields.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.from_fields.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.from_fields.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.from_fields.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.from\_fields[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas-periodindex-from-fields "Link to this heading")

===========================================================================================================================================================================

classmethod PeriodIndex.from\_fields(_\*_, _year\=None_, _quarter\=None_, _month\=None_, _day\=None_, _hour\=None_, _minute\=None_, _second\=None_, _freq\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L782-L854)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas.PeriodIndex.from_fields "Link to this definition")

Construct a PeriodIndex from fields (year, month, day, etc.).

Each field (year, quarter, month, day, hour, minute, second) can be specified as a scalar or list-like. At least one field must be list-like; scalar fields are broadcast to its length. The frequency is inferred from the fields provided or can be given explicitly.

Parameters:

**year**int or list-like, default None

Year for the PeriodIndex.

**quarter**int or list-like, default None

Quarter for the PeriodIndex.

**month**int or list-like, default None

Month for the PeriodIndex.

**day**int or list-like, default None

Day for the PeriodIndex.

**hour**int or list-like, default None

Hour for the PeriodIndex.

**minute**int or list-like, default None

Minute for the PeriodIndex.

**second**int or list-like, default None

Second for the PeriodIndex.

**freq**str or period object, optional

One of pandas period strings or corresponding objects.

Returns:

PeriodIndex

See also

[`PeriodIndex.from_ordinals`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas.PeriodIndex.from_ordinals "pandas.PeriodIndex.from_ordinals")

Construct a PeriodIndex from ordinals.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeArray/Index.

Notes

A list-like field must be a `list`, `tuple`, `np.ndarray`, or `Series`. Other array-like inputs, such as a `range` or an `Index`, are not accepted.

Examples

\>>> idx \= pd.PeriodIndex.from\_fields(year\=\[2000, 2002\], quarter\=\[1, 3\])
\>>> idx
PeriodIndex(\['2000Q1', '2002Q3'\], dtype='period\[Q-DEC\]')

Copy to clipboard

On this page