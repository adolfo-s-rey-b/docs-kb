[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.le.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.le.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.le.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.le.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.le.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.le.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.le.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.le.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.le.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.le.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.le.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.le.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.le[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#pandas-series-le "Link to this heading")

================================================================================================================================

Series.le(_other_, _level\=None_, _fill\_value\=None_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L7685-L7751)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#pandas.Series.le "Link to this definition")

Return Less than or equal to of series and other, element-wise (binary operator le).

Equivalent to `series <= other`, but with support to substitute a fill\_value for missing data in either one of the inputs.

Parameters:

**other**object

When a Series is provided, will align on indexes. For all other types, will behave the same as `<=` but with possibly different results due to the other arguments.

**level**int or name

Broadcast across a level, matching Index values on the passed MultiIndex level.

**fill\_value**scalar or None, default None

Fill NA values, whether present in the original data or introduced by alignment, with this value before computation. Positions where both inputs are NA are left unfilled and behave as NA does for the operation.

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

Returns:

Series

The result of the operation.

See also

[`Series.ge`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ge.html#pandas.Series.ge "pandas.Series.ge")

Return elementwise Greater than or equal to of series and other.

[`Series.lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt "pandas.Series.lt")

Return elementwise Less than of series and other.

[`Series.gt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt "pandas.Series.gt")

Return elementwise Greater than of series and other.

[`Series.eq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html#pandas.Series.eq "pandas.Series.eq")

Return elementwise equal to of series and other.

Examples

\>>> a \= pd.Series(\[1, 1, 1, np.nan, 1\], index\=\['a', 'b', 'c', 'd', 'e'\])
\>>> a
a    1.0
b    1.0
c    1.0
d    NaN
e    1.0
dtype: float64
\>>> b \= pd.Series(\[0, 1, 2, np.nan, 1\], index\=\['a', 'b', 'c', 'd', 'f'\])
\>>> b
a    0.0
b    1.0
c    2.0
d    NaN
f    1.0
dtype: float64
\>>> a.le(b, fill\_value\=0)
a    False
b     True
c     True
d    False
e    False
f     True
dtype: bool

Copy to clipboard

On this page