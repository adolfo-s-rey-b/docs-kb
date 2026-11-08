[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.plot.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.plot[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.plot.html#pandas-api-typing-dataframegroupby-plot "Link to this heading")

=====================================================================================================================================================================================================

property DataFrameGroupBy.plot[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3800-L3826)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.plot.html#pandas.api.typing.DataFrameGroupBy.plot "Link to this definition")

Make plots of groups from a DataFrame.

Uses the backend specified by the option `plotting.backend`. By default, matplotlib is used.

Returns:

GroupByPlot

A plotting object that can be used to create plots for each group.

See also

`DataFrame.plot`

Make plots of DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[1, 2, 3, 4\], "B": \[5, 6, 7, 8\]}, index\=\["a", "a", "b", "b"\]
... )
\>>> g \= df.groupby(level\=0)
\>>> g.plot()

Copy to clipboard

On this page