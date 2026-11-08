[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.round.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.round.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.round.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.round.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.round.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.round.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.round.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.round.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.round.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.round.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.round.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.round.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.round[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#pandas-series-round "Link to this heading")

=========================================================================================================================================

Series.round(_decimals\=0_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2866-L2927)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#pandas.Series.round "Link to this definition")

Round each value in a Series to the given number of decimals.

This method returns a new Series with each element rounded to the specified number of decimal places using the round-half-to-even strategy.

Parameters:

**decimals**int, default 0

Number of decimal places to round to. If decimals is negative, it specifies the number of positions to the left of the decimal point.

**\*args, \*\*kwargs**

Additional arguments and keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series

Rounded values of the Series.

See also

[`numpy.around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "(in NumPy v2.5)")

Round values of an np.array.

[`DataFrame.round`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas.DataFrame.round "pandas.DataFrame.round")

Round values of a DataFrame.

[`Series.dt.round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.round.html#pandas.Series.dt.round "pandas.Series.dt.round")

Round values of data to the specified freq.

Notes

For values exactly halfway between rounded decimal values, pandas rounds to the nearest even value (e.g. -0.5 and 0.5 round to 0.0, 1.5 and 2.5 round to 2.0, etc.).

Examples

\>>> s \= pd.Series(\[\-0.5, 0.1, 2.5, 1.3, 2.7\])
\>>> s.round()
0   -0.0
1    0.0
2    2.0
3    1.0
4    3.0
dtype: float64

Copy to clipboard

On this page