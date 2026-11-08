[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.mode.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.mode.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.mode.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.mode.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.mode.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.mode.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.mode.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.mode.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.mode.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.mode.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.mode.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.mode.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.mode[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas-series-mode "Link to this heading")

======================================================================================================================================

Series.mode(_dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2382-L2450)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "Link to this definition")

Return the mode(s) of the Series.

The mode is the value that appears most often. There can be multiple modes.

Always returns Series even if only one value is returned.

Parameters:

**dropna**bool, default True

Don’t consider counts of NaN/NaT.

Returns:

Series

Modes of the Series in sorted order.

See also

`numpy.mode`

Equivalent numpy function for computing median.

[`Series.sum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "pandas.Series.sum")

Sum of the values.

[`Series.median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")

Median of the values.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Standard deviation of the values.

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Variance of the values.

[`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")

Minimum value.

[`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")

Maximum value.

Examples

\>>> s \= pd.Series(\[2, 4, 2, 2, 4, None\])
\>>> s.mode()
0    2.0
dtype: float64

Copy to clipboard

More than one mode:

\>>> s \= pd.Series(\[2, 4, 8, 2, 4, None\])
\>>> s.mode()
0    2.0
1    4.0
dtype: float64

Copy to clipboard

With and without considering null value:

\>>> s \= pd.Series(\[2, 4, None, None, 4, None\])
\>>> s.mode(dropna\=False)
0   NaN
dtype: float64
\>>> s \= pd.Series(\[2, 4, None, None, 4, None\])
\>>> s.mode()
0    4.0
dtype: float64

Copy to clipboard

On this page