[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.all.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.all.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.all[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.all.html#pandas-api-typing-dataframegroupby-all "Link to this heading")

==================================================================================================================================================================================================

DataFrameGroupBy.all(_skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L1811-L1873)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.all.html#pandas.api.typing.DataFrameGroupBy.all "Link to this definition")

Return True if all values in the group are truthful, else False.

This is equivalent to calling `bool` on each value in the group and returning `True` only if all are truthful.

Parameters:

**skipna**bool, default True

Flag to ignore nan values during truth testing.

Returns:

Series or DataFrame

DataFrame or Series of boolean values, where a value is True if all elements are True within its respective group, False otherwise.

See also

`Series.all`

Apply function all to a Series.

`DataFrame.all`

Apply function all to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 0\], index\=lst)
\>>> ser
a    1
a    2
b    0
dtype: int64
\>>> ser.groupby(level\=0).all()
a     True
b    False
dtype: bool

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 0, 3\], \[1, 5, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["ostrich", "penguin", "parrot"\]
... )
\>>> df
         a  b  c
ostrich  1  0  3
penguin  1  5  6
parrot   7  8  9
\>>> df.groupby(by\=\["a"\]).all()
       b      c
a
1  False   True
7   True   True

Copy to clipboard

On this page