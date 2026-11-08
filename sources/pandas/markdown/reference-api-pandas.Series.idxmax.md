[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.idxmax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.idxmax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.idxmax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.idxmax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.idxmax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.idxmax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.idxmax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.idxmax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.idxmax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.idxmax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.idxmax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.idxmax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.idxmax[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas-series-idxmax "Link to this heading")

============================================================================================================================================

Series.idxmax(_axis\=0_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2804-L2864)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "Link to this definition")

Return the row label of the maximum value.

If multiple values equal the maximum, the first row label with that value is returned.

Parameters:

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**skipna**bool, default True

Exclude NA/null values. If the entire Series is NA, or if `skipna=False` and there is an NA value, this method will raise a `ValueError`.

**\*args, \*\*kwargs**

Additional arguments and keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Index

Label of the maximum value.

Raises:

ValueError

If the Series is empty.

See also

[`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "(in NumPy v2.5)")

Return indices of the maximum values along the given axis.

[`DataFrame.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax "pandas.DataFrame.idxmax")

Return index of first occurrence of maximum over requested axis.

[`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")

Return index _label_ of the first occurrence of minimum of values.

Notes

This method is the Series version of `ndarray.argmax`. This method returns the label of the maximum, while `ndarray.argmax` returns the position. To get the position, use `series.values.argmax()`.

Examples

\>>> s \= pd.Series(data\=\[1, None, 4, 3, 4\], index\=\["A", "B", "C", "D", "E"\])
\>>> s
A    1.0
B    NaN
C    4.0
D    3.0
E    4.0
dtype: float64

Copy to clipboard

\>>> s.idxmax()
'C'

Copy to clipboard

On this page