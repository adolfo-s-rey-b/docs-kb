[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.idxmin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.idxmin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.idxmin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.idxmin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.idxmin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.idxmin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.idxmin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.idxmin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.idxmin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.idxmin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.idxmin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.idxmin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.idxmin[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas-series-idxmin "Link to this heading")

============================================================================================================================================

Series.idxmin(_axis\=0_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2743-L2802)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "Link to this definition")

Return the row label of the minimum value.

If multiple values equal the minimum, the first row label with that value is returned.

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

Label of the minimum value.

Raises:

ValueError

If the Series is empty.

See also

[`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "(in NumPy v2.5)")

Return indices of the minimum values along the given axis.

[`DataFrame.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin "pandas.DataFrame.idxmin")

Return index of first occurrence of minimum over requested axis.

[`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")

Return index _label_ of the first occurrence of maximum of values.

Notes

This method is the Series version of `ndarray.argmin`. This method returns the label of the minimum, while `ndarray.argmin` returns the position. To get the position, use `series.values.argmin()`.

Examples

\>>> s \= pd.Series(data\=\[1, None, 4, 1\], index\=\["A", "B", "C", "D"\])
\>>> s
A    1.0
B    NaN
C    4.0
D    1.0
dtype: float64

Copy to clipboard

\>>> s.idxmin()
'A'

Copy to clipboard

On this page