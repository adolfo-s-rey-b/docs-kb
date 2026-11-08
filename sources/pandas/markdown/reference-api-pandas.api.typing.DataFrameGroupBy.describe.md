[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.describe.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.describe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.describe.html#pandas-api-typing-dataframegroupby-describe "Link to this heading")

=================================================================================================================================================================================================================

DataFrameGroupBy.describe(_percentiles\=None_, _include\=None_, _exclude\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3301-L3376)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.describe.html#pandas.api.typing.DataFrameGroupBy.describe "Link to this definition")

Generate descriptive statistics for each group.

Within each group, summarize the central tendency, dispersion, and shape of each analyzed column’s distribution, excluding `NaN` values. By default only numeric columns are analyzed; pass `include` to also analyze non-numeric columns (or `exclude` to omit columns by dtype).

Parameters:

**percentiles**list-like of numbers, optional

The percentiles to include in the output. All should fall between 0 and 1. The default, `None`, returns the 25th, 50th, and 75th percentiles.

**include**‘all’, list-like of dtypes or None (default), optional

Which column dtypes to include. Options:

*   `'all'` : Include all columns, including non-numeric ones.
    
*   list-like of dtypes : Limit the result to columns of the given dtypes, in the style of `DataFrame.select_dtypes()` (e.g. `include=[np.number]` or `include=["category"]`).
    
*   `None` (default) : Include only numeric columns, falling back to object and categorical columns if there are no numeric columns.
    

**exclude**list-like of dtypes or None (default), optional

Column dtypes to omit from the result, in the style of `DataFrame.select_dtypes()`. `None` (default) excludes nothing.

Returns:

DataFrame

One row per group. The columns form a MultiIndex whose outer level is the analyzed column and whose inner level is the statistic name.

See also

`DataFrame.describe`

Generate descriptive statistics of a DataFrame.

[`SeriesGroupBy.describe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.describe.html#pandas.api.typing.SeriesGroupBy.describe "pandas.api.typing.SeriesGroupBy.describe")

Generate descriptive statistics for each group of a Series.

`DataFrame.select_dtypes`

Subset of a DataFrame including/excluding columns based on their dtype.

Notes

For numeric columns, the per-group statistics are `count`, `mean`, `std`, `min`, `max`, and the requested percentiles. By default the lower percentile is `25` and the upper is `75`; the `50` percentile is the same as the median.

For object columns, the per-group statistics are `count`, `unique`, `top`, and `freq`. The `top` is the most common value within the group and `freq` is its count.

Examples

\>>> df \= pd.DataFrame({"group": \["a", "a", "b", "b"\], "value": \[1, 2, 3, 4\]})
\>>> df.groupby("group").describe()
      value
      count mean       std  min   25%  50%   75%  max
group
a       2.0  1.5  0.707107  1.0  1.25  1.5  1.75  2.0
b       2.0  3.5  0.707107  3.0  3.25  3.5  3.75  4.0

Copy to clipboard

On this page