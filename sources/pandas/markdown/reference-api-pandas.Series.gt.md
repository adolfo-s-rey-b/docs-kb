[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.gt[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas-series-gt "Link to this heading")

================================================================================================================================

Series.gt(_other_, _level\=None_, _fill\_value\=None_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L7889-L7954)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt "Link to this definition")

Return Greater than of series and other, element-wise (binary operator gt).

Equivalent to `series > other`, but with support to substitute a fill\_value for missing data in either one of the inputs.

Parameters:

**other**object

When a Series is provided, will align on indexes. For all other types, will behave the same as `>` but with possibly different results due to the other arguments.

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

[`Series.lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt "pandas.Series.lt")

Reverse of the Greater than operator, see [Python documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
 for more details.

Examples

\>>> a \= pd.Series(\[1, 1, 1, np.nan, 1\], index\=\["a", "b", "c", "d", "e"\])
\>>> a
a    1.0
b    1.0
c    1.0
d    NaN
e    1.0
dtype: float64
\>>> b \= pd.Series(\[0, 1, 2, np.nan, 1\], index\=\["a", "b", "c", "d", "f"\])
\>>> b
a    0.0
b    1.0
c    2.0
d    NaN
f    1.0
dtype: float64
\>>> a.gt(b, fill\_value\=0)
a     True
b    False
c    False
d    False
e     True
f    False
dtype: bool

Copy to clipboard

On this page