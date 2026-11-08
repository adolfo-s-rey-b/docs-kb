[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.ffill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.ffill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.ffill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.ffill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.ffill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.ffill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.ffill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.ffill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.ffill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.ffill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.ffill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.ffill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.ffill[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas-dataframe-ffill "Link to this heading")

==================================================================================================================================================

DataFrame.ffill(_\*_, _axis\=None_, _inplace\=False_, _limit\=None_, _limit\_area\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L7473-L7573)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas.DataFrame.ffill "Link to this definition")

Fill NA/NaN values by propagating the last valid observation to next valid.

This method fills missing values using forward fill, where the last valid observation is propagated forward to fill the gaps.

Parameters:

**axis**{0 or ‘index’} for Series, {0 or ‘index’, 1 or ‘columns’} for DataFrame

Axis along which to fill missing values. For Series this parameter is unused and defaults to 0.

**inplace**bool, default False

If True, fill in-place. Note: this will modify any other views on this object (e.g., a no-copy slice for a column in a DataFrame).

**limit**int, default None

Maximum number of consecutive NaN values to fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. Must be greater than 0 if not None.

**limit\_area**{None, ‘inside’, ‘outside’}, default None

Restrict which NaNs are filled based on their position relative to the valid values.

*   `None`: No fill restriction.
    
*   ‘inside’: Only fill NaNs surrounded by valid values (interpolate).
    
*   ‘outside’: Only fill NaNs outside valid values (extrapolate).
    

Added in version 2.2.0.

Returns:

Series/DataFrame

Object with missing values filled.

See also

[`DataFrame.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html#pandas.DataFrame.bfill "pandas.DataFrame.bfill")

Fill NA/NaN values by using the next valid observation to fill the gap.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         \[np.nan, 2, np.nan, 0\],\
...         \[3, 4, np.nan, 1\],\
...         \[np.nan, np.nan, np.nan, np.nan\],\
...         \[np.nan, 3, np.nan, 4\],\
...     \],
...     columns\=list("ABCD"),
... )
\>>> df
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  NaN  NaN NaN  NaN
3  NaN  3.0 NaN  4.0

Copy to clipboard

\>>> df.ffill()
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  3.0  4.0 NaN  1.0
3  3.0  3.0 NaN  4.0

Copy to clipboard

\>>> ser \= pd.Series(\[1, np.nan, 2, 3\])
\>>> ser.ffill()
0   1.0
1   1.0
2   2.0
3   3.0
dtype: float64

Copy to clipboard

On this page