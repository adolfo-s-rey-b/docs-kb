[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.truncate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.truncate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.truncate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.truncate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.truncate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.truncate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.truncate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.truncate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.truncate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.truncate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.truncate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.truncate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.truncate[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#pandas-series-truncate "Link to this heading")

==================================================================================================================================================

Series.truncate(_before\=None_, _after\=None_, _axis\=None_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L11103-L11283)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#pandas.Series.truncate "Link to this definition")

Truncate a Series or DataFrame before and after some index value.

This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.

Parameters:

**before**date, str, int

Truncate all rows before this index value.

**after**date, str, int

Truncate all rows after this index value.

**axis**{0 or ‘index’, 1 or ‘columns’}, optional

Axis to truncate. Truncates the index (rows) by default. For Series this parameter is unused and defaults to 0.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

type of caller

The truncated Series or DataFrame.

See also

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Select a subset of a DataFrame by label.

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Select a subset of a DataFrame by position.

Notes

If the index being truncated contains only datetime values, before and after may be specified as strings instead of Timestamps.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "A": \["a", "b", "c", "d", "e"\],
...         "B": \["f", "g", "h", "i", "j"\],
...         "C": \["k", "l", "m", "n", "o"\],
...     },
...     index\=\[1, 2, 3, 4, 5\],
... )
\>>> df
   A  B  C
1  a  f  k
2  b  g  l
3  c  h  m
4  d  i  n
5  e  j  o

Copy to clipboard

\>>> df.truncate(before\=2, after\=4)
   A  B  C
2  b  g  l
3  c  h  m
4  d  i  n

Copy to clipboard

The columns of a DataFrame can be truncated.

\>>> df.truncate(before\="A", after\="B", axis\="columns")
   A  B
1  a  f
2  b  g
3  c  h
4  d  i
5  e  j

Copy to clipboard

For Series, only rows can be truncated.

\>>> df\["A"\].truncate(before\=2, after\=4)
2    b
3    c
4    d
Name: A, dtype: str

Copy to clipboard

The index values in `truncate` can be datetimes or string dates.

\>>> dates \= pd.date\_range("2016-01-01", "2016-02-01", freq\="s")
\>>> df \= pd.DataFrame(index\=dates, data\={"A": 1})
\>>> df.tail()
                     A
2016-01-31 23:59:56  1
2016-01-31 23:59:57  1
2016-01-31 23:59:58  1
2016-01-31 23:59:59  1
2016-02-01 00:00:00  1

Copy to clipboard

\>>> df.truncate(
...     before\=pd.Timestamp("2016-01-05"), after\=pd.Timestamp("2016-01-10")
... ).tail()
                     A
2016-01-09 23:59:56  1
2016-01-09 23:59:57  1
2016-01-09 23:59:58  1
2016-01-09 23:59:59  1
2016-01-10 00:00:00  1

Copy to clipboard

Because the index is a DatetimeIndex containing only dates, we can specify before and after as strings. They will be coerced to Timestamps before truncation.

\>>> df.truncate("2016-01-05", "2016-01-10").tail()
                     A
2016-01-09 23:59:56  1
2016-01-09 23:59:57  1
2016-01-09 23:59:58  1
2016-01-09 23:59:59  1
2016-01-10 00:00:00  1

Copy to clipboard

Note that `truncate` assumes a 0 value for any unspecified time component (midnight). This differs from partial string slicing, which returns any partially matching dates.

\>>> df.loc\["2016-01-05":"2016-01-10", :\].tail()
                     A
2016-01-10 23:59:55  1
2016-01-10 23:59:56  1
2016-01-10 23:59:57  1
2016-01-10 23:59:58  1
2016-01-10 23:59:59  1

Copy to clipboard

On this page