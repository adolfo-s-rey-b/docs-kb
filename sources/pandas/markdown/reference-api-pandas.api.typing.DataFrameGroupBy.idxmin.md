[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.idxmin[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html#pandas-api-typing-dataframegroupby-idxmin "Link to this heading")

===========================================================================================================================================================================================================

DataFrameGroupBy.idxmin(_skipna\=True_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3224-L3297)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html#pandas.api.typing.DataFrameGroupBy.idxmin "Link to this definition")

Return index of first occurrence of minimum in each group.

For each group and each column, identifies the row label where the minimum value first occurs. NA values are excluded by default.

Parameters:

**skipna**bool, default True

Exclude NA values.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Returns:

DataFrame

Indexes of minima in each column according to the group.

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

`Series.idxmin`

Return index of the minimum element.

`DataFrame.idxmin`

Indexes of minima along the specified axis.

Notes

This method is the DataFrame version of `ndarray.argmin`.

Examples

Consider a dataset containing food consumption in Argentina.

\>>> df \= pd.DataFrame(
...     {
...         "consumption": \[10.51, 103.11, 55.48\],
...         "co2\_emissions": \[37.2, 19.66, 1712\],
...         "food\_type": \["meat", "plant", "meat"\],
...     },
...     index\=\["Pork", "Wheat Products", "Beef"\],
... )

Copy to clipboard

\>>> df
                consumption  co2\_emissions food\_type
Pork                  10.51         37.20       meat
Wheat Products       103.11         19.66      plant
Beef                  55.48       1712.00       meat

Copy to clipboard

By default, it returns the index for the minimum value in each column according to the group.

\>>> df.groupby("food\_type").idxmin()
              consumption   co2\_emissions
food\_type
meat                 Pork            Pork
plant      Wheat Products  Wheat Products

Copy to clipboard

On this page