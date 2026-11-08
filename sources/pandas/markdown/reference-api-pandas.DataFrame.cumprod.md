[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.cumprod[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html#pandas-dataframe-cumprod "Link to this heading")

========================================================================================================================================================

DataFrame.cumprod(_axis\=0_, _skipna\=True_, _numeric\_only\=False_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19142-L19246)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html#pandas.DataFrame.cumprod "Link to this definition")

Return cumulative product over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative product.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The index or the name of the axis. 0 is equivalent to None or ‘index’. For Series this parameter is unused and defaults to 0.

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*args, \*\*kwargs**

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or DataFrame

Return cumulative product of Series or DataFrame.

See also

[`DataFrame.prod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.prod.html#pandas.DataFrame.prod "pandas.DataFrame.prod")

Return the product over DataFrame axis.

[`DataFrame.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummax.html#pandas.DataFrame.cummax "pandas.DataFrame.cummax")

Return cumulative maximum over DataFrame axis.

[`DataFrame.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummin.html#pandas.DataFrame.cummin "pandas.DataFrame.cummin")

Return cumulative minimum over DataFrame axis.

[`DataFrame.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html#pandas.DataFrame.cumsum "pandas.DataFrame.cumsum")

Return cumulative sum over DataFrame axis.

Examples

**Series**

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

\>>> s.cumprod()
0     2.0
1     NaN
2    10.0
3   -10.0
4    -0.0
dtype: float64

Copy to clipboard

To include NA values in the operation, use `skipna=False`

\>>> s.cumprod(skipna\=False)
0    2.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

Copy to clipboard

**DataFrame**

\>>> df \= pd.DataFrame(
...     \[\[2.0, 1.0\], \[3.0, np.nan\], \[1.0, 0.0\]\], columns\=list("AB")
... )
\>>> df
     A    B
0  2.0  1.0
1  3.0  NaN
2  1.0  0.0

Copy to clipboard

By default, iterates over rows and finds the product in each column. This is equivalent to `axis=None` or `axis='index'`.

\>>> df.cumprod()
     A    B
0  2.0  1.0
1  6.0  NaN
2  6.0  0.0

Copy to clipboard

To iterate over columns and find the product in each row, use `axis=1`

\>>> df.cumprod(axis\=1)
     A    B
0  2.0  2.0
1  3.0  NaN
2  1.0  0.0

Copy to clipboard

On this page