[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.cumprod[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html#pandas-api-typing-dataframegroupby-cumprod "Link to this heading")

==============================================================================================================================================================================================================

DataFrameGroupBy.cumprod(_numeric\_only\=False_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4783-L4872)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html#pandas.api.typing.DataFrameGroupBy.cumprod "Link to this definition")

Cumulative product for each group.

Returns a Series or DataFrame of the same size with the cumulative product computed within each group.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**\*args**tuple

Positional arguments to be passed to func.

Deprecated since version 3.1.0: Passing `*args` to GroupBy.cumprod is deprecated and will be removed in a future version of pandas.

**\*\*kwargs**dict

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to GroupBy.cumprod is deprecated and will be removed in a future version of pandas.

Returns:

Series or DataFrame

Cumulative product for each group. Same object type as the caller.

See also

`Series.cumprod`

Apply function cumprod to a Series.

`DataFrame.cumprod`

Apply function cumprod to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[6, 2, 0\], index\=lst)
\>>> ser
a    6
a    2
b    0
dtype: int64
\>>> ser.groupby(level\=0).cumprod()
a    6
a   12
b    0
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 8, 2\], \[1, 2, 5\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["cow", "horse", "bull"\]
... )
\>>> df
        a   b   c
cow     1   8   2
horse   1   2   5
bull    2   6   9
\>>> df.groupby("a").groups
{1: \['cow', 'horse'\], 2: \['bull'\]}
\>>> df.groupby("a").cumprod()
        b   c
cow     8   2
horse  16  10
bull    6   9

Copy to clipboard

On this page