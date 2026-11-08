[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.asfreq.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.asfreq.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.asfreq.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.asfreq.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.asfreq.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.asfreq.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.asfreq.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.asfreq.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.asfreq.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.asfreq.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.asfreq.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.asfreq.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.asfreq[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#pandas-periodindex-asfreq "Link to this heading")

===========================================================================================================================================================

PeriodIndex.asfreq(_freq\=None_, _how\='E'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L174-L216)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#pandas.PeriodIndex.asfreq "Link to this definition")

Convert the PeriodIndex to the specified frequency freq.

Equivalent to applying [`pandas.Period.asfreq()`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")
 with the given arguments to each [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 in this PeriodIndex.

Parameters:

**freq**str

A frequency.

**how**{‘end’, ‘start’, ‘e’, ‘s’}, default ‘end’

Whether the elements should be aligned to the end or start of each period, e.g. January 31st vs. January 1st. Case-insensitive.

Returns:

PeriodIndex

The transformed PeriodIndex with the new frequency.

See also

`arrays.PeriodArray.asfreq`

Convert each Period in a PeriodArray to the given frequency.

[`Period.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")

Convert a [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 object to the given frequency.

Examples

\>>> pidx \= pd.period\_range("2010-01-01", "2015-01-01", freq\="Y")
\>>> pidx
PeriodIndex(\['2010', '2011', '2012', '2013', '2014', '2015'\],
dtype='period\[Y-DEC\]')

Copy to clipboard

\>>> pidx.asfreq("M")
PeriodIndex(\['2010-12', '2011-12', '2012-12', '2013-12', '2014-12',\
'2015-12'\], dtype='period\[M\]')

Copy to clipboard

\>>> pidx.asfreq("M", how\="S")
PeriodIndex(\['2010-01', '2011-01', '2012-01', '2013-01', '2014-01',\
'2015-01'\], dtype='period\[M\]')

Copy to clipboard

On this page