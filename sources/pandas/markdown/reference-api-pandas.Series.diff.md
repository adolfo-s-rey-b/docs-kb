[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.diff.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.diff.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.diff.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.diff.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.diff.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.diff.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.diff.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.diff.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.diff.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.diff.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.diff.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.diff.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.diff[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas-series-diff "Link to this heading")

======================================================================================================================================

Series.diff(_periods\=1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3268-L3354)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas.Series.diff "Link to this definition")

First discrete difference of Series elements.

Calculates the difference of a Series element compared with another element in the Series (default is element in previous row).

Parameters:

**periods**int, default 1

Periods to shift for calculating difference, accepts negative values.

Returns:

Series

First differences of the Series.

See also

[`Series.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change "pandas.Series.pct_change")

Percent change over given number of periods.

[`Series.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")

Shift index by desired number of periods with an optional time freq.

[`DataFrame.diff`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas.DataFrame.diff "pandas.DataFrame.diff")

First discrete difference of object.

Notes

Equivalent to `self - self.shift(periods)`, except that boolean dtypes use `operator.xor()` rather than `operator.sub()`; the result dtype follows from that operation.

In particular, because the leading `periods` positions are filled with a missing value, NumPy integer dtypes are cast to floating and NumPy `bool` to `object`.

Examples

Difference with previous row

\>>> s \= pd.Series(\[1, 1, 2, 3, 5, 8\])
\>>> s.diff()
0    NaN
1    0.0
2    1.0
3    1.0
4    2.0
5    3.0
dtype: float64

Copy to clipboard

Difference with 3rd previous row

\>>> s.diff(periods\=3)
0    NaN
1    NaN
2    NaN
3    2.0
4    4.0
5    6.0
dtype: float64

Copy to clipboard

Difference with following row

\>>> s.diff(periods\=-1)
0    0.0
1   -1.0
2   -1.0
3   -2.0
4   -3.0
5    NaN
dtype: float64

Copy to clipboard

Overflow in input dtype

\>>> s \= pd.Series(\[1, 0\], dtype\=np.uint8)
\>>> s.diff()
0      NaN
1    255.0
dtype: float64

Copy to clipboard

On this page