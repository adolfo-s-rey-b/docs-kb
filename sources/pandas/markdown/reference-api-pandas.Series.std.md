[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.std[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas-series-std "Link to this heading")

===================================================================================================================================

Series.std(_\*_, _axis\=None_, _skipna\=True_, _ddof\=1_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9928-L9995)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "Link to this definition")

Return sample standard deviation.

Normalized by N-1 by default. This can be changed using the ddof argument.

Parameters:

**axis**{index (0)}

This parameter is unused and defaults to 0.

**skipna**bool, default True

Exclude NA/null values. If Series is NA, the result will be NA.

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

**numeric\_only**bool, default False

Not implemented for Series.

**\*\*kwargs**

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

scalar

Standard deviation over all values in the Series.

See also

[`numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")

Compute the standard deviation along the specified axis.

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Return unbiased variance over requested axis.

[`Series.sem`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sem.html#pandas.Series.sem "pandas.Series.sem")

Return unbiased standard error of the mean over requested axis.

[`Series.mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "pandas.Series.mean")

Return the mean of the values over the requested axis.

[`Series.median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")

Return the median of the values over the requested axis.

[`Series.mode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "pandas.Series.mode")

Return the mode(s) of the Series.

Notes

To have the same behaviour as `numpy.std`, use `ddof=0` (instead of the default `ddof=1`) and `skipna=False`.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.std()
1.0

Copy to clipboard

Alternatively, `ddof=0` can be set to normalize by $N$ instead of $N-1$:

\>>> s.std(ddof\=0)
0.816496580927726

Copy to clipboard

On this page