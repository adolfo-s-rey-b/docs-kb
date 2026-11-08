[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.corr.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.corr.html#pandas-api-typing-seriesgroupby-corr "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.corr(_other_, _method\='pearson'_, _min\_periods\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1795-L1836)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.corr.html#pandas.api.typing.SeriesGroupBy.corr "Link to this definition")

Compute correlation between each group and another Series.

This method computes the pairwise correlation between each group’s values and the corresponding values in `other`, using the specified correlation method.

Parameters:

**other**Series

Series to compute correlation with.

**method**{‘pearson’, ‘kendall’, ‘spearman’}, default ‘pearson’

Method of correlation to use.

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

Returns:

Series

Correlation value for each group.

See also

`Series.corr`

Equivalent method on `Series`.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\], index\=\[0, 0, 1, 1\])
\>>> g \= s.groupby(\[0, 0, 1, 1\])
\>>> g.corr()

Copy to clipboard

On this page