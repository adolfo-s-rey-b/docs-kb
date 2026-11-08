[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.rdivmod.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.rdivmod.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.rdivmod.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.rdivmod.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.rdivmod.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.rdivmod.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.rdivmod.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.rdivmod.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.rdivmod.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.rdivmod.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.rdivmod.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.rdivmod.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.rdivmod[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html#pandas-series-rdivmod "Link to this heading")

===============================================================================================================================================

Series.rdivmod(_other_, _level\=None_, _fill\_value\=None_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L8944-L9013)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html#pandas.Series.rdivmod "Link to this definition")

Return Integer division and modulo of series and other, element-wise (binary operator rdivmod).

Equivalent to `other divmod series`, but with support to substitute a fill\_value for missing data in either one of the inputs.

Parameters:

**other**object

When a Series is provided, will align on indexes. For all other types, will behave the same as `//` and `%` but with possibly different results due to the other arguments.

**level**int or name

Broadcast across a level, matching Index values on the passed MultiIndex level.

**fill\_value**scalar or None, default None

Fill NA values, whether present in the original data or introduced by alignment, with this value before computation. Positions where both inputs are NA are left unfilled and behave as NA does for the operation.

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

Returns:

2-Tuple of Series

The result of the operation.

See also

[`Series.divmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.divmod.html#pandas.Series.divmod "pandas.Series.divmod")

Element-wise Integer division and modulo, see [Python documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
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
\>>> a.rdivmod(b, fill\_value\=0)
(a    1.0
 b    0.0
 c    0.0
 d    inf
 e    NaN
 dtype: float64,
 a    0.0
 b    0.0
 c    0.0
 d    NaN
 e    NaN
 dtype: float64)

Copy to clipboard

On this page