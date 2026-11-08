[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.bfill[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html#pandas-series-bfill "Link to this heading")

=========================================================================================================================================

Series.bfill(_\*_, _axis\=None_, _inplace\=False_, _limit\=None_, _limit\_area\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L7575-L7683)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html#pandas.Series.bfill "Link to this definition")

Fill NA/NaN values by using the next valid observation to fill the gap.

This method fills missing values in a backward direction along the specified axis, propagating non-null values from later positions to earlier positions containing NaN.

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

[`DataFrame.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas.DataFrame.ffill "pandas.DataFrame.ffill")

Fill NA/NaN values by propagating the last valid observation to next valid.

Examples

For Series:

\>>> s \= pd.Series(\[1, None, None, 2\])
\>>> s.bfill()
0    1.0
1    2.0
2    2.0
3    2.0
dtype: float64
\>>> s.bfill(limit\=1)
0    1.0
1    NaN
2    2.0
3    2.0
dtype: float64

Copy to clipboard

With DataFrame:

\>>> df \= pd.DataFrame({"A": \[1, None, None, 4\], "B": \[None, 5, None, 7\]})
\>>> df
      A     B
0   1.0   NaN
1   NaN   5.0
2   NaN   NaN
3   4.0   7.0
\>>> df.bfill()
      A     B
0   1.0   5.0
1   4.0   5.0
2   4.0   7.0
3   4.0   7.0
\>>> df.bfill(limit\=1)
      A     B
0   1.0   5.0
1   NaN   5.0
2   4.0   7.0
3   4.0   7.0

Copy to clipboard

On this page