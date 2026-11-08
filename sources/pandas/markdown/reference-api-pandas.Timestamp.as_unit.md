[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.as_unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.as_unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.as_unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.as_unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.as_unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.as_unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.as_unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.as_unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.as_unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.as_unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.as_unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.as_unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.as\_unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas-timestamp-as-unit "Link to this heading")

=========================================================================================================================================================

Timestamp.as\_unit(_unit_, _round\_ok\=True_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "Link to this definition")

Convert the underlying int64 representation to the given unit.

This method changes the resolution of the Timestamp’s internal representation. When converting to a coarser resolution (e.g., nanoseconds to seconds), precision may be lost through rounding unless `round_ok` is set to False.

Parameters:

**unit**{“ns”, “us”, “ms”, “s”}

**round\_ok**bool, default True

If False and the conversion requires rounding, raise.

Returns:

Timestamp

See also

[`Timestamp.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas.Timestamp.asm8 "pandas.Timestamp.asm8")

Return numpy datetime64 format with same precision.

[`Timestamp.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas.Timestamp.to_pydatetime "pandas.Timestamp.to_pydatetime")

Convert Timestamp object to a native Python datetime object.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument into timedelta object, which can represent differences in times.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 00:00:00.01')
\>>> ts
Timestamp('2023-01-01 00:00:00.010000')
\>>> ts.unit
'us'
\>>> ts \= ts.as\_unit('s')
\>>> ts
Timestamp('2023-01-01 00:00:00')
\>>> ts.unit
's'

Copy to clipboard

On this page