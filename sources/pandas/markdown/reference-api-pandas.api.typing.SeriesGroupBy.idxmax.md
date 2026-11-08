[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.idxmax[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html#pandas-api-typing-seriesgroupby-idxmax "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.idxmax(_skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1734-L1793)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html#pandas.api.typing.SeriesGroupBy.idxmax "Link to this definition")

Return the row label of the maximum value.

If multiple values equal the maximum, the first row label with that value is returned.

Parameters:

**skipna**bool, default True

Exclude NA values.

Returns:

Series

Indexes of maxima in each group.

Raises:

ValueError

When there are no valid values for a group. Then can happen if:

> *   There is an unobserved group and `observed=False`.
>     
> *   All values for a group are NA.
>     
> *   Some values for a group are NA and `skipna=False`.
>     

Changed in version 3.0.0: Previously if all values for a group are NA or some values for a group are NA and `skipna=False`, this method would return NA. Now it raises instead.

See also

[`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "(in NumPy v2.5)")

Return indices of the maximum values along the given axis.

`DataFrame.idxmax`

Return index of first occurrence of maximum over requested axis.

`Series.idxmin`

Return index _label_ of the first occurrence of minimum of values.

Examples

\>>> ser \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    4
dtype: int64

Copy to clipboard

\>>> ser.groupby(\["a", "a", "b", "b"\]).idxmax()
a   2023-01-15
b   2023-02-15
dtype: datetime64\[us\]

Copy to clipboard

On this page