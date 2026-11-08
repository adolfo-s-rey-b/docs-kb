[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.kurtosis[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html#pandas-series-kurtosis "Link to this heading")

==================================================================================================================================================

Series.kurtosis(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L10043-L10102)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html#pandas.Series.kurtosis "Link to this definition")

Return unbiased kurtosis over requested axis.

Kurtosis obtained using Fisher’s definition of kurtosis (kurtosis of normal == 0.0). Normalized by N-1.

Parameters:

**axis**{index (0)}

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

For DataFrames, specifying `axis=None` will apply the aggregation across both axes.

Added in version 2.0.0.

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*\*kwargs**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

scalar

Unbiased kurtosis.

See also

[`Series.skew`](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#pandas.Series.skew "pandas.Series.skew")

Return unbiased skew over requested axis.

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Return unbiased variance over requested axis.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Return unbiased standard deviation over requested axis.

Examples

\>>> s \= pd.Series(\[1, 2, 2, 3\], index\=\["cat", "dog", "dog", "mouse"\])
\>>> s
cat    1
dog    2
dog    2
mouse  3
dtype: int64
\>>> round(s.kurt(), 6)
1.5

Copy to clipboard

On this page