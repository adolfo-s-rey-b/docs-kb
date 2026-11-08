[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.idxmin[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmin.html#pandas-api-typing-seriesgroupby-idxmin "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.idxmin(_skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1673-L1732)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmin.html#pandas.api.typing.SeriesGroupBy.idxmin "Link to this definition")

Return the row label of the minimum value.

If multiple values equal the minimum, the first row label with that value is returned.

Parameters:

**skipna**bool, default True

Exclude NA values.

Returns:

Series

Indexes of minima in each group.

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

[`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "(in NumPy v2.5)")

Return indices of the minimum values along the given axis.

`DataFrame.idxmin`

Return index of first occurrence of minimum over requested axis.

`Series.idxmax`

Return index _label_ of the first occurrence of maximum of values.

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

\>>> ser.groupby(\["a", "a", "b", "b"\]).idxmin()
a   2023-01-01
b   2023-02-01
dtype: datetime64\[us\]

Copy to clipboard

On this page