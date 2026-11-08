[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.add_suffix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.add_suffix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.add_suffix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.add_suffix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.add_suffix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.add_suffix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.add_suffix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.add_suffix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.add_suffix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.add_suffix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.add_suffix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.add_suffix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.add\_suffix[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#pandas-series-add-suffix "Link to this heading")

=========================================================================================================================================================

Series.add\_suffix(_suffix_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L4897-L4966)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix "Link to this definition")

Suffix labels with string suffix.

For Series, the row labels are suffixed. For DataFrame, the column labels are suffixed.

Parameters:

**suffix**str

The string to add after each label.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Axis to add suffix on

Added in version 2.0.0.

Returns:

Series or DataFrame

New Series or DataFrame with updated labels.

See also

[`Series.add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_prefix.html#pandas.Series.add_prefix "pandas.Series.add_prefix")

Prefix row labels with string prefix.

[`DataFrame.add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#pandas.DataFrame.add_prefix "pandas.DataFrame.add_prefix")

Prefix column labels with string prefix.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s
0    1
1    2
2    3
3    4
dtype: int64

Copy to clipboard

\>>> s.add\_suffix("\_item")
0\_item    1
1\_item    2
2\_item    3
3\_item    4
dtype: int64

Copy to clipboard

\>>> df \= pd.DataFrame({"A": \[1, 2, 3, 4\], "B": \[3, 4, 5, 6\]})
\>>> df
   A  B
0  1  3
1  2  4
2  3  5
3  4  6

Copy to clipboard

\>>> df.add\_suffix("\_col")
     A\_col  B\_col
0       1       3
1       2       4
2       3       5
3       4       6

Copy to clipboard

On this page