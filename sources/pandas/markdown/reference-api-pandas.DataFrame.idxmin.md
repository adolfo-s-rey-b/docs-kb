[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.idxmin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.idxmin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.idxmin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.idxmin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.idxmin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.idxmin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.idxmin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.idxmin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.idxmin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.idxmin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.idxmin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.idxmin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.idxmin[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas-dataframe-idxmin "Link to this heading")

=====================================================================================================================================================

DataFrame.idxmin(_axis\=0_, _skipna\=True_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19289-L19386)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin "Link to this definition")

Return index of first occurrence of minimum over requested axis.

NA/null values are excluded.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to use. 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.

**skipna**bool, default True

Exclude NA/null values. If the entire DataFrame is NA, or if `skipna=False` and there is an NA value, this method will raise a `ValueError`.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Returns:

Series

Indexes of minima along the specified axis.

Raises:

ValueError

*   If the row/column is empty
    

See also

[`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")

Return index of the minimum element.

Notes

This method is the DataFrame version of `ndarray.argmin`.

Examples

Consider a dataset containing food consumption in Argentina.

\>>> df \= pd.DataFrame(
...     {
...         "consumption": \[10.51, 103.11, 55.48\],
...         "co2\_emissions": \[37.2, 19.66, 1712\],
...     },
...     index\=\["Pork", "Wheat Products", "Beef"\],
... )

Copy to clipboard

\>>> df
                consumption  co2\_emissions
Pork                  10.51         37.20
Wheat Products       103.11         19.66
Beef                  55.48       1712.00

Copy to clipboard

By default, it returns the index for the minimum value in each column.

\>>> df.idxmin()
consumption                Pork
co2\_emissions    Wheat Products
dtype: str

Copy to clipboard

To return the index for the minimum value in each row, use `axis="columns"`.

\>>> df.idxmin(axis\="columns")
Pork                consumption
Wheat Products    co2\_emissions
Beef                consumption
dtype: str

Copy to clipboard

On this page