[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.shift[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html#pandas-api-typing-dataframegroupby-shift "Link to this heading")

========================================================================================================================================================================================================

DataFrameGroupBy.shift(_periods\=1_, _freq\=None_, _fill\_value\=<no\_default>_, _suffix\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5146-L5288)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html#pandas.api.typing.DataFrameGroupBy.shift "Link to this definition")

Shift each group by periods observations.

If freq is passed, the index will be increased using the periods and the freq.

Parameters:

**periods**int | Sequence\[int\], default 1

Number of periods to shift. If a list of values, shift each group by each period.

**freq**str, optional

Frequency string.

**fill\_value**optional

The scalar value to use for newly introduced missing values.

Changed in version 2.1.0: Will raise a `ValueError` if `freq` is provided too.

**suffix**str, optional

A string to add to each shifted column if there are multiple periods. Ignored otherwise.

Returns:

Series or DataFrame

Object shifted within each group.

See also

`Index.shift`

Shift values of Index.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3, 4\], index\=lst)
\>>> ser
a    1
a    2
b    3
b    4
dtype: int64
\>>> ser.groupby(level\=0).shift(1)
a    NaN
a    1.0
b    NaN
b    3.0
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[2, 5, 8\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data,
...     columns\=\["a", "b", "c"\],
...     index\=\["tuna", "salmon", "catfish", "goldfish"\],
... )
\>>> df
           a  b  c
    tuna   1  2  3
  salmon   1  5  6
 catfish   2  5  8
goldfish   2  6  9
\>>> df.groupby("a").shift(1)
              b    c
    tuna    NaN  NaN
  salmon    2.0  3.0
 catfish    NaN  NaN
goldfish    5.0  8.0

Copy to clipboard

On this page