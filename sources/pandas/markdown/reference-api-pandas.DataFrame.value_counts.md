[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.value_counts.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.value_counts.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.value_counts.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.value_counts.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.value_counts.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.value_counts.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.value_counts.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.value_counts.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.value_counts.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.value_counts.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.value_counts.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.value_counts.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.value\_counts[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas-dataframe-value-counts "Link to this heading")

========================================================================================================================================================================

DataFrame.value\_counts(_subset\=None_, _normalize\=False_, _sort\=True_, _ascending\=False_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L9540-L9692)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "Link to this definition")

Return a Series containing the frequency of each distinct row in the DataFrame.

The resulting Series is indexed by the unique row combinations found in the DataFrame (or the specified subset of columns). By default the counts are sorted in descending order, and rows with `NaN` values in any column are excluded.

Parameters:

**subset**Hashable or a sequence of the previous, optional

Columns to use when counting unique combinations.

**normalize**bool, default False

Return proportions rather than frequencies.

**sort**bool, default True

Stable sort by frequencies when True. Preserve the order of the data when False.

Changed in version 3.0.0: Prior to 3.0.0, `sort=False` would sort by the columns values.

Changed in version 3.0.0: Prior to 3.0.0, the sort was unstable.

**ascending**bool, default False

Sort in ascending order.

**dropna**bool, default True

Do not include counts of rows that contain NA values.

Returns:

Series

Series containing the frequency of each distinct row in the DataFrame.

See also

[`Series.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")

Equivalent method on Series.

Notes

The returned Series will have a MultiIndex with one level per input column but an Index (non-multi) for a single label. By default, rows that contain any NA values are omitted from the result. By default, the resulting Series will be sorted by frequencies in descending order so that the first element is the most frequently-occurring row.

Examples

\>>> df \= pd.DataFrame(
...     {"num\_legs": \[2, 4, 4, 6\], "num\_wings": \[2, 0, 0, 0\]},
...     index\=\["falcon", "dog", "cat", "ant"\],
... )
\>>> df
        num\_legs  num\_wings
falcon         2          2
dog            4          0
cat            4          0
ant            6          0

Copy to clipboard

\>>> df.value\_counts()
num\_legs  num\_wings
4         0            2
2         2            1
6         0            1
Name: count, dtype: int64

Copy to clipboard

\>>> df.value\_counts(sort\=False)
num\_legs  num\_wings
2         2            1
4         0            2
6         0            1
Name: count, dtype: int64

Copy to clipboard

\>>> df.value\_counts(ascending\=True)
num\_legs  num\_wings
2         2            1
6         0            1
4         0            2
Name: count, dtype: int64

Copy to clipboard

\>>> df.value\_counts(normalize\=True)
num\_legs  num\_wings
4         0            0.50
2         2            0.25
6         0            0.25
Name: proportion, dtype: float64

Copy to clipboard

With dropna set to False we can also count rows with NA values.

\>>> df \= pd.DataFrame(
...     {
...         "first\_name": \["John", "Anne", "John", "Beth"\],
...         "middle\_name": \["Smith", pd.NA, pd.NA, "Louise"\],
...     }
... )
\>>> df
  first\_name middle\_name
0       John       Smith
1       Anne         NaN
2       John         NaN
3       Beth      Louise

Copy to clipboard

\>>> df.value\_counts()
first\_name  middle\_name
John        Smith          1
Beth        Louise         1
Name: count, dtype: int64

Copy to clipboard

\>>> df.value\_counts(dropna\=False)
first\_name  middle\_name
John        Smith          1
Anne        NaN            1
John        NaN            1
Beth        Louise         1
Name: count, dtype: int64

Copy to clipboard

\>>> df.value\_counts("first\_name")
first\_name
John    2
Anne    1
Beth    1
Name: count, dtype: int64

Copy to clipboard

On this page