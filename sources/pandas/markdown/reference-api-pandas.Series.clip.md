[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.clip.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.clip.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.clip.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.clip.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.clip.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.clip.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.clip.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.clip.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.clip.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.clip.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.clip.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.clip.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.clip[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas-series-clip "Link to this heading")

======================================================================================================================================

Series.clip(_lower\=None_, _upper\=None_, _\*_, _axis\=None_, _inplace\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L8942-L9119)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas.Series.clip "Link to this definition")

Trim values at input threshold(s).

Assigns values outside boundary to boundary values. Thresholds can be singular values or array like, and in the latter case the clipping is performed element-wise in the specified axis.

Parameters:

**lower**float or array-like, default None

Minimum threshold value. All values below this threshold will be set to it. A missing threshold (e.g NA) will not clip the value.

**upper**float or array-like, default None

Maximum threshold value. All values above this threshold will be set to it. A missing threshold (e.g NA) will not clip the value.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Align object with lower and upper along the given axis. For Series this parameter is unused and defaults to None.

**inplace**bool, default False

Whether to perform the operation in place on the data.

**\*\*kwargs**

For compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or DataFrame

Same type as calling object with the values outside the clip boundaries replaced.

See also

[`Series.clip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas.Series.clip "pandas.Series.clip")

Trim values at input threshold in series.

[`DataFrame.clip`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html#pandas.DataFrame.clip "pandas.DataFrame.clip")

Trim values at input threshold in DataFrame.

[`numpy.clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "(in NumPy v2.5)")

Clip (limit) the values in an array.

Examples

\>>> data \= {"col\_0": \[9, \-3, 0, \-1, 5\], "col\_1": \[\-2, \-7, 6, 8, \-5\]}
\>>> df \= pd.DataFrame(data)
\>>> df
   col\_0  col\_1
0      9     -2
1     -3     -7
2      0      6
3     -1      8
4      5     -5

Copy to clipboard

Clips per column using lower and upper thresholds:

\>>> df.clip(\-4, 6)
   col\_0  col\_1
0      6     -2
1     -3     -4
2      0      6
3     -1      6
4      5     -4

Copy to clipboard

Clips using specific lower and upper thresholds per column:

\>>> df.clip(\[\-2, \-1\], \[4, 5\])
    col\_0  col\_1
0      4     -1
1     -2     -1
2      0      5
3     -1      5
4      4     -1

Copy to clipboard

Clips using specific lower and upper thresholds per column element:

\>>> t \= pd.Series(\[2, \-4, \-1, 6, 3\])
\>>> t
0    2
1   -4
2   -1
3    6
4    3
dtype: int64

Copy to clipboard

\>>> df.clip(t, t + 4, axis\=0)
   col\_0  col\_1
0      6      2
1     -3     -4
2      0      3
3      6      8
4      5      3

Copy to clipboard

Clips using specific lower threshold per column element, with missing values:

\>>> t \= pd.Series(\[2, \-4, np.nan, 6, 3\])
\>>> t
0    2.0
1   -4.0
2    NaN
3    6.0
4    3.0
dtype: float64

Copy to clipboard

\>>> df.clip(t, axis\=0)
col\_0  col\_1
0      9.0    2.0
1     -3.0   -4.0
2      0.0    6.0
3      6.0    8.0
4      5.0    3.0

Copy to clipboard

On this page