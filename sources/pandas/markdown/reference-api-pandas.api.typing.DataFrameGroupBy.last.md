[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.last.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.last.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.last[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.last.html#pandas-api-typing-dataframegroupby-last "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.last(_numeric\_only\=False_, _min\_count\=\-1_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3287-L3355)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.last.html#pandas.api.typing.DataFrameGroupBy.last "Link to this definition")

Compute the last entry of each column within each group.

NA values are skipped by default, so the result is the last non-NA value per column — which may differ from the last row of the group. Pass `skipna=False` to keep NAs.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data.

**min\_count**int, default -1

The required number of valid values to perform the operation. If fewer than `min_count` valid values are present the result will be NA.

**skipna**bool, default True

Exclude NA values. If an entire group is NA, the result will be NA.

Added in version 2.2.1.

Returns:

Series or DataFrame

Last values within each group.

See also

`DataFrame.groupby`

Apply a function groupby to each row or column of a DataFrame.

`api.typing.DataFrameGroupBy.first`

Compute the first entry of each column within each group.

`api.typing.DataFrameGroupBy.nth`

Take the nth row from each group.

Examples

\>>> df \= pd.DataFrame(dict(A\=\[1, 1, 3\], B\=\[5, None, 6\], C\=\[1, 2, 3\]))
\>>> df.groupby("A").last()
     B  C
A
1  5.0  2
3  6.0  3

Copy to clipboard

On this page