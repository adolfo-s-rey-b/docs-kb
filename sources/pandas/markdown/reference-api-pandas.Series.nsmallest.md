[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.nsmallest.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.nsmallest.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.nsmallest.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.nsmallest.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.nsmallest.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.nsmallest.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.nsmallest.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.nsmallest.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.nsmallest.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.nsmallest.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.nsmallest.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.nsmallest.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.nsmallest[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas-series-nsmallest "Link to this heading")

=====================================================================================================================================================

Series.nsmallest(_n\=5_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4625-L4732)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest "Link to this definition")

Return the smallest n elements.

This method is optimized for performance compared to sorting the entire Series when only a few of the bottom values are needed.

Parameters:

**n**int, default 5

Return this many ascending sorted values.

**keep**{‘first’, ‘last’, ‘all’}, default ‘first’

When there are duplicate values that cannot all fit in a Series of n elements:

*   `first` : return the first n occurrences in order of appearance.
    
*   `last` : return the last n occurrences in reverse order of appearance.
    
*   `all` : keep all occurrences. This can result in a Series of size larger than n.
    

Returns:

Series

The n smallest values in the Series, sorted in increasing order.

See also

[`Series.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest "pandas.Series.nlargest")

Get the n largest elements.

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Sort Series by values.

[`Series.head`](https://pandas.pydata.org/docs/reference/api/pandas.Series.head.html#pandas.Series.head "pandas.Series.head")

Return the first n rows.

Notes

Faster than `.sort_values().head(n)` for small n relative to the size of the `Series` object.

Examples

\>>> countries\_population \= {
...     "Italy": 59000000,
...     "France": 65000000,
...     "Brunei": 434000,
...     "Malta": 434000,
...     "Maldives": 434000,
...     "Iceland": 337000,
...     "Nauru": 11300,
...     "Tuvalu": 11300,
...     "Anguilla": 11300,
...     "Montserrat": 5200,
... }
\>>> s \= pd.Series(countries\_population)
\>>> s
Italy       59000000
France      65000000
Brunei        434000
Malta         434000
Maldives      434000
Iceland       337000
Nauru          11300
Tuvalu         11300
Anguilla       11300
Montserrat      5200
dtype: int64

Copy to clipboard

The n smallest elements where `n=5` by default.

\>>> s.nsmallest()
Montserrat    5200
Nauru        11300
Tuvalu       11300
Anguilla     11300
Iceland     337000
dtype: int64

Copy to clipboard

The n smallest elements where `n=3`. Default keep value is ‘first’ so Nauru and Tuvalu will be kept.

\>>> s.nsmallest(3)
Montserrat   5200
Nauru       11300
Tuvalu      11300
dtype: int64

Copy to clipboard

The n smallest elements where `n=3` and keeping the last duplicates. Anguilla and Tuvalu will be kept since they are the last with value 11300 based on the index order.

\>>> s.nsmallest(3, keep\="last")
Montserrat   5200
Anguilla    11300
Tuvalu      11300
dtype: int64

Copy to clipboard

The n smallest elements where `n=3` with all duplicates kept. Note that the returned Series has four elements due to the three duplicates.

\>>> s.nsmallest(3, keep\="all")
Montserrat   5200
Nauru       11300
Tuvalu      11300
Anguilla    11300
dtype: int64

Copy to clipboard

On this page