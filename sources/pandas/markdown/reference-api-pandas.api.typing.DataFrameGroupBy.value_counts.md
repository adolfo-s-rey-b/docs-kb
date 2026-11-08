[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.value\_counts[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html#pandas-api-typing-dataframegroupby-value-counts "Link to this heading")

==============================================================================================================================================================================================================================

DataFrameGroupBy.value\_counts(_subset\=None_, _normalize\=False_, _sort\=True_, _ascending\=False_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3378-L3498)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html#pandas.api.typing.DataFrameGroupBy.value_counts "Link to this definition")

Return a Series or DataFrame containing counts of unique rows.

The resulting object will be in descending order so that the first element in each group is the most frequently-occurring row.

Parameters:

**subset**list-like, optional

Columns to use when counting unique combinations.

**normalize**bool, default False

Return proportions rather than frequencies.

**sort**bool, default True

Stable sort by frequencies when True. When False, non-grouping columns will appear in the order they occur in within groups.

Changed in version 3.0.0: In prior versions, `sort=False` would sort the non-grouping columns by label.

**ascending**bool, default False

Sort in ascending order.

**dropna**bool, default True

Don’t include counts of rows that contain NA values.

Returns:

Series or DataFrame

Series if the groupby `as_index` is True, otherwise DataFrame.

See also

`Series.value_counts`

Equivalent method on Series.

`DataFrame.value_counts`

Equivalent method on DataFrame.

[`SeriesGroupBy.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.value_counts.html#pandas.api.typing.SeriesGroupBy.value_counts "pandas.api.typing.SeriesGroupBy.value_counts")

Equivalent method on SeriesGroupBy.

Notes

*   If the groupby `as_index` is True then the returned Series will have a MultiIndex with one level per input column.
    
*   If the groupby `as_index` is False then the returned DataFrame will have an additional column with the value\_counts. The column is labelled ‘count’ or ‘proportion’, depending on the `normalize` parameter.
    

By default, rows that contain any NA values are omitted from the result.

By default, the result will be in descending order so that the first element of each group is the most frequently-occurring row.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "gender": \["male", "male", "female", "male", "female", "male"\],
...         "education": \["low", "medium", "high", "low", "high", "low"\],
...         "country": \["US", "FR", "US", "FR", "FR", "FR"\],
...     }
... )

Copy to clipboard

\>>> df
        gender  education   country
0       male    low         US
1       male    medium      FR
2       female  high        US
3       male    low         FR
4       female  high        FR
5       male    low         FR

Copy to clipboard

\>>> df.groupby("gender").value\_counts()
gender  education  country
female  high       US         1
                   FR         1
male    low        FR         2
                   US         1
        medium     FR         1
Name: count, dtype: int64

Copy to clipboard

\>>> df.groupby("gender").value\_counts(ascending\=True)
gender  education  country
female  high       US         1
                   FR         1
male    low        US         1
        medium     FR         1
        low        FR         2
Name: count, dtype: int64

Copy to clipboard

\>>> df.groupby("gender").value\_counts(normalize\=True)
gender  education  country
female  high       US         0.50
                   FR         0.50
male    low        FR         0.50
                   US         0.25
        medium     FR         0.25
Name: proportion, dtype: float64

Copy to clipboard

\>>> df.groupby("gender", as\_index\=False).value\_counts()
   gender education country  count
0  female      high      US      1
1  female      high      FR      1
2    male       low      FR      2
3    male       low      US      1
4    male    medium      FR      1

Copy to clipboard

\>>> df.groupby("gender", as\_index\=False).value\_counts(normalize\=True)
   gender education country  proportion
0  female      high      US        0.50
1  female      high      FR        0.50
2    male       low      FR        0.50
3    male       low      US        0.25
4    male    medium      FR        0.25

Copy to clipboard

On this page