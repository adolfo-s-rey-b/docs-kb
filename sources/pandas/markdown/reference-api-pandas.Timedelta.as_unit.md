[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.as_unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.as_unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.as_unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.as_unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.as_unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.as_unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.as_unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.as_unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.as_unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.as_unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.as_unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.as_unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.as\_unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas-timedelta-as-unit "Link to this heading")

=========================================================================================================================================================

Timedelta.as\_unit(_unit_, _round\_ok\=True_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas.Timedelta.as_unit "Link to this definition")

Convert the underlying int64 representation to the given unit.

Converts the Timedelta to a new resolution specified by `unit`. If the conversion would require rounding (loss of precision), this is allowed by default. Set `round_ok=False` to raise an error instead.

Parameters:

**unit**{“ns”, “us”, “ms”, “s”}

**round\_ok**bool, default True

If False and the conversion requires rounding, raise.

Returns:

Timedelta

See also

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration, the difference between two dates or times.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`Timedelta.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas.Timedelta.asm8 "pandas.Timedelta.asm8")

Return a numpy timedelta64 array scalar view.

Examples

\>>> td \= pd.Timedelta('1001ms')
\>>> td
Timedelta('0 days 00:00:01.001000')
\>>> td.as\_unit('s')
Timedelta('0 days 00:00:01')

Copy to clipboard

On this page