[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.droplevel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.droplevel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.droplevel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.droplevel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.droplevel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.droplevel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.droplevel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.droplevel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.droplevel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.droplevel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.droplevel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.droplevel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.droplevel[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html#pandas-series-droplevel "Link to this heading")

=====================================================================================================================================================

Series.droplevel(_level_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L771-L842)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html#pandas.Series.droplevel "Link to this definition")

Return Series/DataFrame with requested index / column level(s) removed.

This method is useful for simplifying a MultiIndex by removing one or more levels.

Parameters:

**level**int, str, or list-like

If a string is given, must be the name of a level If list-like, elements must be names or positional indexes of levels.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Axis along which the level(s) is removed:

*   0 or ‘index’: remove level(s) in column.
    
*   1 or ‘columns’: remove level(s) in row.
    

For Series this parameter is unused and defaults to 0.

Returns:

Series/DataFrame

Series/DataFrame with requested index / column level(s) removed.

See also

[`DataFrame.replace`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")

Replace values given in to\_replace with value.

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Return reshaped DataFrame organized by given index / column values.

Examples

\>>> df \= (
...     pd.DataFrame(\[\[1, 2, 3, 4\], \[5, 6, 7, 8\], \[9, 10, 11, 12\]\])
...     .set\_index(\[0, 1\])
...     .rename\_axis(\["a", "b"\])
... )

Copy to clipboard

\>>> df.columns \= pd.MultiIndex.from\_tuples(
...     \[("c", "e"), ("d", "f")\], names\=\["level\_1", "level\_2"\]
... )

Copy to clipboard

\>>> df
level\_1   c   d
level\_2   e   f
a b
1 2      3   4
5 6      7   8
9 10    11  12

Copy to clipboard

\>>> df.droplevel("a")
level\_1   c   d
level\_2   e   f
b
2        3   4
6        7   8
10      11  12

Copy to clipboard

\>>> df.droplevel("level\_2", axis\=1)
level\_1   c   d
a b
1 2      3   4
5 6      7   8
9 10    11  12

Copy to clipboard

On this page