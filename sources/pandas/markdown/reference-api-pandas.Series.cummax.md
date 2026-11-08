[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cummax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cummax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cummax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cummax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cummax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cummax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cummax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cummax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cummax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cummax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cummax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cummax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cummax[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas-series-cummax "Link to this heading")

============================================================================================================================================

Series.cummax(_axis\=0_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L10171-L10233)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax "Link to this definition")

Return cumulative maximum over a Series.

Returns a Series of the same size containing the cumulative maximum.

Parameters:

**axis**{0 or ‘index’}, default 0

This parameter is unused and defaults to 0.

**skipna**bool, default True

Exclude NA/null values. If the series is NA, the result is NA.

**\*args, \*\*kwargs**

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series

Return cumulative maximum of Series.

See also

`core.window.expanding.Expanding.max`

Similar functionality but ignores `NaN` values.

[`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")

Return the maximum over a Series.

[`Series.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#pandas.Series.cummin "pandas.Series.cummin")

Return cumulative minimum.

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

\>>> s.cummax()
0    2.0
1    NaN
2    5.0
3    5.0
4    5.0
dtype: float64

Copy to clipboard

To include NA values in the operation, use `skipna=False`

\>>> s.cummax(skipna\=False)
0    2.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

Copy to clipboard

On this page