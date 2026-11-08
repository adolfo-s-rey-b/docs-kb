[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.nth[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html#pandas-api-typing-dataframegroupby-nth "Link to this heading")

==================================================================================================================================================================================================

property DataFrameGroupBy.nth[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4272-L4343)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html#pandas.api.typing.DataFrameGroupBy.nth "Link to this definition")

Take the nth row from each group if n is an int, otherwise a subset of rows.

Deprecated since version 3.1.0: Index notation (`g.nth[n]`) is deprecated in favor of calling `g.nth(n)` and will be removed in a future version of pandas.

If dropna, will take the nth non-null row, dropna is either ‘all’ or ‘any’; this is equivalent to calling dropna(how=dropna) before the groupby.

Returns:

Series or DataFrame

N-th value within each group.

See also

`Series.nth`

Apply function nth to a Series.

`DataFrame.nth`

Apply function nth to each row or column of a DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[1, 1, 2, 1, 2\], "B": \[np.nan, 2, 3, 4, 5\]}, columns\=\["A", "B"\]
... )
\>>> g \= df.groupby("A")
\>>> g.nth(0)
   A   B
0  1 NaN
2  2 3.0
\>>> g.nth(1)
   A   B
1  1 2.0
4  2 5.0
\>>> g.nth(\-1)
   A   B
3  1 4.0
4  2 5.0
\>>> g.nth(\[0, 1\])
   A   B
0  1 NaN
1  1 2.0
2  2 3.0
4  2 5.0
\>>> g.nth(slice(None, \-1))
   A   B
0  1 NaN
1  1 2.0
2  2 3.0

Copy to clipboard

Specifying dropna allows ignoring `NaN` values

\>>> g.nth(0, dropna\="any")
   A   B
1  1 2.0
2  2 3.0

Copy to clipboard

When the specified `n` is larger than any of the groups, an empty DataFrame is returned

\>>> g.nth(3, dropna\="any")
Empty DataFrame
Columns: \[A, B\]
Index: \[\]

Copy to clipboard

On this page