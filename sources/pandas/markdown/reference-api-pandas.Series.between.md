[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.between.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.between.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.between.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.between.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.between.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.between.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.between.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.between.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.between.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.between.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.between.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.between.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.between[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#pandas-series-between "Link to this heading")

===============================================================================================================================================

Series.between(_left_, _right_, _inclusive\='both'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6617-L6706)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#pandas.Series.between "Link to this definition")

Return boolean Series equivalent to left <= series <= right.

This function returns a boolean vector containing True wherever the corresponding Series element is between the boundary values left and right. NA values are treated as False.

Parameters:

**left**scalar or list-like

Left boundary.

**right**scalar or list-like

Right boundary.

**inclusive**{“both”, “neither”, “left”, “right”}

Include boundaries. Whether to set each bound as closed or open.

Returns:

Series

Series representing whether each element is between left and right (inclusive).

See also

[`Series.gt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt "pandas.Series.gt")

Greater than of series and other.

[`Series.lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt "pandas.Series.lt")

Less than of series and other.

Notes

This function is equivalent to `(left <= ser) & (ser <= right)`

Examples

\>>> s \= pd.Series(\[2, 0, 4, 8, np.nan\])

Copy to clipboard

Boundary values are included by default:

\>>> s.between(1, 4)
0     True
1    False
2     True
3    False
4    False
dtype: bool

Copy to clipboard

With inclusive set to `"neither"` boundary values are excluded:

\>>> s.between(1, 4, inclusive\="neither")
0     True
1    False
2    False
3    False
4    False
dtype: bool

Copy to clipboard

left and right can be any scalar value:

\>>> s \= pd.Series(\["Alice", "Bob", "Carol", "Eve"\])
\>>> s.between("Anna", "Daniel")
0    False
1     True
2     True
3    False
dtype: bool

Copy to clipboard

On this page