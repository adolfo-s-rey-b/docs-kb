[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.nlargest.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.nlargest.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.nlargest.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.nlargest.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.nlargest.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.nlargest.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.nlargest.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.nlargest.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.nlargest.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.nlargest.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.nlargest.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.nlargest.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.nlargest[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas-series-nlargest "Link to this heading")

==================================================================================================================================================

Series.nlargest(_n\=5_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4515-L4623)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest "Link to this definition")

Return the largest n elements.

This method is optimized for performance compared to sorting the entire Series when only a few of the top values are needed.

Parameters:

**n**int, default 5

Return this many descending sorted values.

**keep**{‘first’, ‘last’, ‘all’}, default ‘first’

When there are duplicate values that cannot all fit in a Series of n elements:

*   `first` : return the first n occurrences in order of appearance.
    
*   `last` : return the last n occurrences in reverse order of appearance.
    
*   `all` : keep all occurrences. This can result in a Series of size larger than n.
    

Returns:

Series

The n largest values in the Series, sorted in decreasing order.

See also

[`Series.nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest "pandas.Series.nsmallest")

Get the n smallest elements.

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Sort Series by values.

[`Series.head`](https://pandas.pydata.org/docs/reference/api/pandas.Series.head.html#pandas.Series.head "pandas.Series.head")

Return the first n rows.

Notes

Faster than `.sort_values(ascending=False).head(n)` for small n relative to the size of the `Series` object.

Examples

\>>> countries\_population \= {
...     "Italy": 59000000,
...     "France": 65000000,
...     "Malta": 434000,
...     "Maldives": 434000,
...     "Brunei": 434000,
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
Malta         434000
Maldives      434000
Brunei        434000
Iceland       337000
Nauru          11300
Tuvalu         11300
Anguilla       11300
Montserrat      5200
dtype: int64

Copy to clipboard

The n largest elements where `n=5` by default.

\>>> s.nlargest()
France      65000000
Italy       59000000
Malta         434000
Maldives      434000
Brunei        434000
dtype: int64

Copy to clipboard

The n largest elements where `n=3`. Default keep value is ‘first’ so Malta will be kept.

\>>> s.nlargest(3)
France    65000000
Italy     59000000
Malta       434000
dtype: int64

Copy to clipboard

The n largest elements where `n=3` and keeping the last duplicates. Brunei will be kept since it is the last with value 434000 based on the index order.

\>>> s.nlargest(3, keep\="last")
France      65000000
Italy       59000000
Brunei        434000
dtype: int64

Copy to clipboard

The n largest elements where `n=3` with all duplicates kept. Note that the returned Series has five elements due to the three duplicates.

\>>> s.nlargest(3, keep\="all")
France      65000000
Italy       59000000
Malta         434000
Maldives      434000
Brunei        434000
dtype: int64

Copy to clipboard

On this page