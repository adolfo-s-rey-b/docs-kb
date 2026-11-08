[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.\_\_iter\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html#pandas-api-typing-dataframegroupby-iter "Link to this heading")

=================================================================================================================================================================================================================

DataFrameGroupBy.\_\_iter\_\_()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L646-L745)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html#pandas.api.typing.DataFrameGroupBy.__iter__ "Link to this definition")

Groupby iterator.

This method provides an iterator over the groups created by the `resample` or `groupby` operation on the object. The method yields tuples where the first element is the label (group key) corresponding to each group or resampled bin, and the second element is the subset of the data that falls within that group or bin.

Returns:

Iterator

Generator yielding a sequence of (name, subsetted object) for each group.

See also

`Series.groupby`

Group data by a specific key or column.

`DataFrame.groupby`

Group DataFrame using mapper or by columns.

`DataFrame.resample`

Resample a DataFrame.

`Series.resample`

Resample a Series.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3\], index\=lst)
\>>> ser
a    1
a    2
b    3
dtype: int64
\>>> for x, y in ser.groupby(level\=0):
...     print(f"{x}\\n{y}\\n")
a
a    1
a    2
dtype: int64
b
b    3
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(data, columns\=\["a", "b", "c"\])
\>>> df
   a  b  c
0  1  2  3
1  1  5  6
2  7  8  9
\>>> for x, y in df.groupby(by\=\["a"\]):
...     print(f"{x}\\n{y}\\n")
(1,)
   a  b  c
0  1  2  3
1  1  5  6
(7,)
   a  b  c
2  7  8  9

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    4
dtype: int64
\>>> for x, y in ser.resample("MS"):
...     print(f"{x}\\n{y}\\n")
2023-01-01 00:00:00
2023-01-01    1
2023-01-15    2
dtype: int64
2023-02-01 00:00:00
2023-02-01    3
2023-02-15    4
dtype: int64

Copy to clipboard

On this page