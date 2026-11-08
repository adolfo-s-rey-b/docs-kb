[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.describe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.describe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.describe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.describe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.describe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.describe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.describe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.describe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.describe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.describe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.describe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.describe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.describe[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas-dataframe-describe "Link to this heading")

===========================================================================================================================================================

DataFrame.describe(_percentiles\=None_, _include\=None_, _exclude\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16356-L16483)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "Link to this definition")

Generate descriptive statistics.

Summarize the central tendency, dispersion, and shape of each analyzed column’s distribution, excluding `NaN` values. By default only numeric columns are analyzed; pass `include` to also analyze non-numeric columns (or `exclude` to omit columns by dtype).

Parameters:

**percentiles**list-like of numbers, optional

The percentiles to include in the output. All should fall between 0 and 1. The default, `None`, returns the 25th, 50th, and 75th percentiles.

**include**‘all’, list-like of dtypes or None (default), optional

Which column dtypes to include. Options:

*   `'all'` : Include all columns, including non-numeric ones.
    
*   list-like of dtypes : Limit the result to columns of the given dtypes, in the style of [`DataFrame.select_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")
     (e.g. `include=[np.number]` or `include=["category"]`).
    
*   `None` (default) : Include only numeric columns, falling back to object and categorical columns if there are no numeric columns.
    

**exclude**list-like of dtypes or None (default), optional

Column dtypes to omit from the result, in the style of [`DataFrame.select_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")
. `None` (default) excludes nothing.

Returns:

DataFrame

Summary statistics of the DataFrame’s columns.

See also

[`Series.describe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html#pandas.Series.describe "pandas.Series.describe")

Generate descriptive statistics of a Series.

[`DataFrame.count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")

Count of non-NA observations per column.

[`DataFrame.max`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max "pandas.DataFrame.max")

Maximum of the values in each column.

[`DataFrame.min`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min "pandas.DataFrame.min")

Minimum of the values in each column.

[`DataFrame.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean "pandas.DataFrame.mean")

Mean of the values.

[`DataFrame.std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")

Standard deviation of the observations.

[`DataFrame.select_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")

Subset of a DataFrame including/excluding columns based on their dtype.

Notes

For numeric columns, the result’s index includes `count`, `mean`, `std`, `min`, `max`, and the requested percentiles. By default the lower percentile is `25` and the upper is `75`; the `50` percentile is the same as the median.

For object columns, the result’s index includes `count`, `unique`, `top`, and `freq`. The `top` is the most common value and `freq` is its count. If multiple values tie for the highest count, `top` is chosen arbitrarily from among them.

With `include='all'`, the result’s index is the union of the per-dtype indices, with `NaN` for statistics that do not apply to a given column’s dtype.

Examples

By default, only numeric columns are analyzed.

\>>> df \= pd.DataFrame(
...     {
...         "categorical": pd.Categorical(\["d", "e", "f"\]),
...         "numeric": \[1, 2, 3\],
...         "object": \["a", "b", "c"\],
...     }
... )
\>>> df.describe()
       numeric
count      3.0
mean       2.0
std        1.0
min        1.0
25%        1.5
50%        2.0
75%        2.5
max        3.0

Copy to clipboard

All columns regardless of dtype.

\>>> df.describe(include\="all")
       categorical  numeric object
count            3      3.0      3
unique           3      NaN      3
top              d      NaN      a
freq             1      NaN      1
mean           NaN      2.0    NaN
std            NaN      1.0    NaN
min            NaN      1.0    NaN
25%            NaN      1.5    NaN
50%            NaN      2.0    NaN
75%            NaN      2.5    NaN
max            NaN      3.0    NaN

Copy to clipboard

Restrict the result to a specific dtype.

\>>> df.describe(include\=\["category"\])
       categorical
count            3
unique           3
top              d
freq             1

Copy to clipboard

Exclude a specific dtype.

\>>> df.describe(exclude\=\[np.number\])
       categorical object
count            3      3
unique           3      3
top              d      a
freq             1      1

Copy to clipboard

On this page