[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.any.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.any.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.any[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.any.html#pandas-api-typing-dataframegroupby-any "Link to this heading")

==================================================================================================================================================================================================

DataFrameGroupBy.any(_skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L1748-L1809)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.any.html#pandas.api.typing.DataFrameGroupBy.any "Link to this definition")

Return True if any value in the group is truthful, else False.

This is equivalent to calling `bool` on each value in the group and returning `True` if at least one is truthful.

Parameters:

**skipna**bool, default True

Flag to ignore nan values during truth testing.

Returns:

Series or DataFrame

DataFrame or Series of boolean values, where a value is True if any element is True within its respective group, False otherwise.

See also

`Series.any`

Apply function any to a Series.

`DataFrame.any`

Apply function any to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 0\], index\=lst)
\>>> ser
a    1
a    2
b    0
dtype: int64
\>>> ser.groupby(level\=0).any()
a     True
b    False
dtype: bool

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 0, 3\], \[1, 0, 6\], \[7, 1, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["ostrich", "penguin", "parrot"\]
... )
\>>> df
         a  b  c
ostrich  1  0  3
penguin  1  0  6
parrot   7  1  9
\>>> df.groupby(by\=\["a"\]).any()
       b      c
a
1  False   True
7   True   True

Copy to clipboard

On this page