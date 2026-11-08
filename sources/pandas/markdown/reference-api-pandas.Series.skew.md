[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.skew.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.skew.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.skew.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.skew.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.skew.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.skew.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.skew.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.skew.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.skew.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.skew.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.skew.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.skew.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#pandas-series-skew "Link to this heading")

======================================================================================================================================

Series.skew(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9997-L10041)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#pandas.Series.skew "Link to this definition")

Return unbiased skew over requested axis.

Normalized by N-1.

Parameters:

**axis**{index (0)}

This parameter is unused and defaults to 0.

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Unused.

**\*\*kwargs**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

scalar

Unbiased skew of the Series.

See also

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Return unbiased variance over requested axis.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Return unbiased standard deviation over requested axis.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.skew()
0.0

Copy to clipboard

On this page