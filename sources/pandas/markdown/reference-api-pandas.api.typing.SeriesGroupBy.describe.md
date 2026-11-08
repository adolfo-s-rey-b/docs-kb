[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.describe.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.describe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.describe.html#pandas-api-typing-seriesgroupby-describe "Link to this heading")

========================================================================================================================================================================================================

SeriesGroupBy.describe(_percentiles\=None_, _include\=None_, _exclude\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L962-L1015)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.describe.html#pandas.api.typing.SeriesGroupBy.describe "Link to this definition")

Generate descriptive statistics for each group.

Within each group, summarize the central tendency, dispersion, and shape of the Series’s distribution, excluding `NaN` values. The per-group statistics depend on the Series’s dtype; see Notes.

Parameters:

**percentiles**list-like of numbers, optional

The percentiles to include in the output. All should fall between 0 and 1. The default, `None`, returns the 25th, 50th, and 75th percentiles.

**include**None

Has no effect on a Series groupby. Deprecated and will be removed in a future version.

**exclude**None

Has no effect on a Series groupby. Deprecated and will be removed in a future version.

Returns:

DataFrame

One row per group; columns are the per-group statistics.

See also

`Series.describe`

Generate descriptive statistics of a Series.

[`DataFrameGroupBy.describe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.describe.html#pandas.api.typing.DataFrameGroupBy.describe "pandas.api.typing.DataFrameGroupBy.describe")

Generate descriptive statistics for each group of a DataFrame.

Notes

For numeric Series, the per-group columns are `count`, `mean`, `std`, `min`, `max`, and the requested percentiles. By default the lower percentile is `25` and the upper is `75`; the `50` percentile is the same as the median.

For object Series (e.g. strings), the per-group columns are `count`, `unique`, `top`, and `freq`. The `top` is the most common value within the group and `freq` is its count.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s.groupby(\[1, 1, 2, 2\]).describe()
   count  mean       std  min   25%  50%   75%  max
1    2.0   1.5  0.707107  1.0  1.25  1.5  1.75  2.0
2    2.0   3.5  0.707107  3.0  3.25  3.5  3.75  4.0

Copy to clipboard

On this page