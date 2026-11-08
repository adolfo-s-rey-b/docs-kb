[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.plot.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.plot[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.plot.html#pandas-api-typing-seriesgroupby-plot "Link to this heading")

============================================================================================================================================================================================

property SeriesGroupBy.plot[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1511-L1535)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.plot.html#pandas.api.typing.SeriesGroupBy.plot "Link to this definition")

Make plots of groups from a Series.

Uses the backend specified by the option `plotting.backend`. By default, matplotlib is used.

Returns:

GroupByPlot

A plotting object that can be used to create plots for each group.

See also

`Series.plot`

Make plots of Series.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4, 5\], index\=\["a", "a", "b", "b", "c"\])
\>>> g \= ser.groupby(level\=0)
\>>> g.plot()

Copy to clipboard

On this page