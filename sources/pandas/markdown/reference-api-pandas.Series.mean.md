[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.mean.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.mean.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.mean.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.mean.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.mean.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.mean.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.mean.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.mean.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.mean.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.mean.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.mean.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.mean.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas-series-mean "Link to this heading")

======================================================================================================================================

Series.mean(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9637-L9693)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "Link to this definition")

Return the mean of the values over the requested axis.

This method computes the arithmetic mean of the Series values, optionally skipping missing values.

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

Mean of the values for the requested axis.

See also

[`numpy.median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "(in NumPy v2.5)")

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

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.mean()
2.0

Copy to clipboard

On this page