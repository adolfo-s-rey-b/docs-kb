[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.diff.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.diff.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.diff.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.diff.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.diff.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.diff.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.diff.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.diff.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.diff.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.diff.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.diff.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.diff.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.diff[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas-dataframe-diff "Link to this heading")

===============================================================================================================================================

DataFrame.diff(_periods\=1_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14745-L14869)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas.DataFrame.diff "Link to this definition")

First discrete difference of element.

Calculates the difference of a DataFrame element compared with another element in the DataFrame (default is element in previous row).

Parameters:

**periods**int, default 1

Periods to shift for calculating difference, accepts negative values.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Take difference over rows (0) or columns (1).

Returns:

DataFrame

First differences of the Series.

See also

[`DataFrame.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#pandas.DataFrame.pct_change "pandas.DataFrame.pct_change")

Percent change over given number of periods.

[`DataFrame.shift`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift "pandas.DataFrame.shift")

Shift index by desired number of periods with an optional time freq.

[`Series.diff`](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas.Series.diff "pandas.Series.diff")

First discrete difference of object.

Notes

Equivalent to `self - self.shift(periods)`, except that boolean dtypes use `operator.xor()` rather than `operator.sub()`; the result dtype follows from that operation.

In particular, because the leading `periods` positions are filled with a missing value, NumPy integer dtypes are cast to floating and NumPy `bool` to `object`.

Examples

Difference with previous row

\>>> df \= pd.DataFrame(
...     {
...         "a": \[1, 2, 3, 4, 5, 6\],
...         "b": \[1, 1, 2, 3, 5, 8\],
...         "c": \[1, 4, 9, 16, 25, 36\],
...     }
... )
\>>> df
   a  b   c
0  1  1   1
1  2  1   4
2  3  2   9
3  4  3  16
4  5  5  25
5  6  8  36
\>>> df.diff()
     a    b     c
0  NaN  NaN   NaN
1  1.0  0.0   3.0
2  1.0  1.0   5.0
3  1.0  1.0   7.0
4  1.0  2.0   9.0
5  1.0  3.0  11.0

Copy to clipboard

Difference with previous column

\>>> df.diff(axis\=1)
    a  b   c
0 NaN  0   0
1 NaN -1   3
2 NaN -1   7
3 NaN -1  13
4 NaN  0  20
5 NaN  2  28

Copy to clipboard

Difference with 3rd previous row

\>>> df.diff(periods\=3)
     a    b     c
0  NaN  NaN   NaN
1  NaN  NaN   NaN
2  NaN  NaN   NaN
3  3.0  2.0  15.0
4  3.0  4.0  21.0
5  3.0  6.0  27.0

Copy to clipboard

Difference with following row

\>>> df.diff(periods\=-1)
     a    b     c
0 -1.0  0.0  -3.0
1 -1.0 -1.0  -5.0
2 -1.0 -1.0  -7.0
3 -1.0 -2.0  -9.0
4 -1.0 -3.0 -11.0
5  NaN  NaN   NaN

Copy to clipboard

Overflow in input dtype

\>>> df \= pd.DataFrame({"a": \[1, 0\]}, dtype\=np.uint8)
\>>> df.diff()
       a
0    NaN
1  255.0

Copy to clipboard

On this page