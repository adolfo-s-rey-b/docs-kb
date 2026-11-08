[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.idxmax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.idxmax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.idxmax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.idxmax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.idxmax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.idxmax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.idxmax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.idxmax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.idxmax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.idxmax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.idxmax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.idxmax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.idxmax[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas-dataframe-idxmax "Link to this heading")

=====================================================================================================================================================

DataFrame.idxmax(_axis\=0_, _skipna\=True_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19388-L19485)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax "Link to this definition")

Return index of first occurrence of maximum over requested axis.

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

Indexes of maxima along the specified axis.

Raises:

ValueError

*   If the row/column is empty
    

See also

[`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")

Return index of the maximum element.

Notes

This method is the DataFrame version of `ndarray.argmax`.

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

By default, it returns the index for the maximum value in each column.

\>>> df.idxmax()
consumption      Wheat Products
co2\_emissions              Beef
dtype: str

Copy to clipboard

To return the index for the maximum value in each row, use `axis="columns"`.

\>>> df.idxmax(axis\="columns")
Pork              co2\_emissions
Wheat Products     consumption
Beef              co2\_emissions
dtype: str

Copy to clipboard

On this page