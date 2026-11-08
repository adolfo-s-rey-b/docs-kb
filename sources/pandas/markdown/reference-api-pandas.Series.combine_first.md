[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.combine_first.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.combine_first.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.combine_first.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.combine_first.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.combine_first.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.combine_first.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.combine_first.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.combine_first.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.combine_first.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.combine_first.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.combine_first.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.combine_first.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.combine\_first[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#pandas-series-combine-first "Link to this heading")

==================================================================================================================================================================

Series.combine\_first(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3841-L3916)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#pandas.Series.combine_first "Link to this definition")

Update null elements with value in the same location in ‘other’.

Combine two Series objects by filling null values in one Series with non-null values from the other Series. Result index will be the union of the two indexes.

Parameters:

**other**Series

The value(s) to be used for filling null values.

Returns:

Series

The result of combining the provided Series with the other object.

See also

[`Series.combine`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas.Series.combine "pandas.Series.combine")

Perform element-wise operation on two Series using a given function.

Examples

\>>> s1 \= pd.Series(\[1, np.nan\])
\>>> s2 \= pd.Series(\[3, 4, 5\])
\>>> s1.combine\_first(s2)
0    1.0
1    4.0
2    5.0
dtype: float64

Copy to clipboard

Null values still persist if the location of that null value does not exist in other

\>>> s1 \= pd.Series({"falcon": np.nan, "eagle": 160.0})
\>>> s2 \= pd.Series({"eagle": 200.0, "duck": 30.0})
\>>> s1.combine\_first(s2)
duck       30.0
eagle     160.0
falcon      NaN
dtype: float64

Copy to clipboard

On this page