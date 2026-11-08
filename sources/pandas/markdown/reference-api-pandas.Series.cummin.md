[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cummin[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#pandas-series-cummin "Link to this heading")

============================================================================================================================================

Series.cummin(_axis\=0_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L10107-L10169)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#pandas.Series.cummin "Link to this definition")

Return cumulative minimum over a Series.

Returns a Series of the same size containing the cumulative minimum.

Parameters:

**axis**{0 or ‘index’}, default 0

This parameter is unused and defaults to 0.

**skipna**bool, default True

If the entire series is NA, the result will be NA.

**\*args, \*\*kwargs**

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series

Return cumulative minimum of the Series.

See also

`core.window.expanding.Expanding.min`

Similar functionality but ignores `NaN` values.

[`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")

Return the minimum value of the Series.

[`Series.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax "pandas.Series.cummax")

Return cumulative maximum.

[`Series.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumsum.html#pandas.Series.cumsum "pandas.Series.cumsum")

Return cumulative sum.

[`Series.cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod "pandas.Series.cumprod")

Return cumulative product.

Examples

\>>> s \= pd.Series(\[2, np.nan, 5, \-1, 0\])
\>>> s
0    2.0
1    NaN
2    5.0
3   -1.0
4    0.0
dtype: float64

Copy to clipboard

By default, NA values are ignored.

\>>> s.cummin()
0    2.0
1    NaN
2    2.0
3   -1.0
4   -1.0
dtype: float64

Copy to clipboard

To include NA values in the operation, use `skipna=False`

\>>> s.cummin(skipna\=False)
0    2.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

Copy to clipboard

On this page