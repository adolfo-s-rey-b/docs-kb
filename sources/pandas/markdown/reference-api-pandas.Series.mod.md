[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.mod.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.mod.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.mod.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.mod.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.mod.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.mod.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.mod.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.mod.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.mod.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.mod.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.mod.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.mod.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.mod[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#pandas-series-mod "Link to this heading")

===================================================================================================================================

Series.mod(_other_, _level\=None_, _fill\_value\=None_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L8616-L8676)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#pandas.Series.mod "Link to this definition")

Return Modulo of series and other, element-wise (binary operator mod).

Equivalent to `series % other`, but with support to substitute a fill\_value for missing data in either one of the inputs.

Parameters:

**other**Series or scalar value

Series with which to compute modulo.

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

[`Series.rmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rmod.html#pandas.Series.rmod "pandas.Series.rmod")

Reverse of the Modulo operator, see [Python documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
 for more details.

Examples

\>>> a \= pd.Series(\[1, 1, 1, np.nan\], index\=\["a", "b", "c", "d"\])
\>>> a
a    1.0
b    1.0
c    1.0
d    NaN
dtype: float64
\>>> b \= pd.Series(\[1, np.nan, 1, np.nan\], index\=\["a", "b", "d", "e"\])
\>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
\>>> a.mod(b, fill\_value\=0)
a    0.0
b    NaN
c    NaN
d    0.0
e    NaN
dtype: float64

Copy to clipboard

On this page