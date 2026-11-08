[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.from_ordinals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.from_ordinals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.from_ordinals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.from_ordinals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.from_ordinals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.from_ordinals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.from_ordinals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.from\_ordinals[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas-periodindex-from-ordinals "Link to this heading")

=================================================================================================================================================================================

classmethod PeriodIndex.from\_ordinals(_ordinals_, _\*_, _freq_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L856-L892)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas.PeriodIndex.from_ordinals "Link to this definition")

Construct a PeriodIndex from ordinals.

Ordinals are integer offsets from the proleptic Gregorian epoch, interpreted according to the given frequency.

Parameters:

**ordinals**array-like of int

The period offsets from the proleptic Gregorian epoch.

**freq**str or period object

One of pandas period strings or corresponding objects.

**name**str, default None

Name of the resulting PeriodIndex.

Returns:

PeriodIndex

See also

[`PeriodIndex.from_fields`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas.PeriodIndex.from_fields "pandas.PeriodIndex.from_fields")

Construct a PeriodIndex from fields (year, month, day, etc.).

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeArray/Index.

Examples

\>>> idx \= pd.PeriodIndex.from\_ordinals(\[\-1, 0, 1\], freq\="Q")
\>>> idx
PeriodIndex(\['1969Q4', '1970Q1', '1970Q2'\], dtype='period\[Q-DEC\]')

Copy to clipboard

On this page