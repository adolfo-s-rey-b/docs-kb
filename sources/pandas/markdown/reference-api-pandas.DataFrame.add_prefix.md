[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.add_prefix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.add_prefix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.add_prefix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.add_prefix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.add_prefix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.add_prefix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.add_prefix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.add_prefix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.add_prefix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.add_prefix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.add_prefix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.add_prefix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.add\_prefix[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#pandas-dataframe-add-prefix "Link to this heading")

==================================================================================================================================================================

DataFrame.add\_prefix(_prefix_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L4825-L4895)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#pandas.DataFrame.add_prefix "Link to this definition")

Prefix labels with string prefix.

For Series, the row labels are prefixed. For DataFrame, the column labels are prefixed.

Parameters:

**prefix**str

The string to add before each label.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Axis to add prefix on

Added in version 2.0.0.

Returns:

Series or DataFrame

New Series or DataFrame with updated labels.

See also

[`Series.add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix "pandas.Series.add_suffix")

Suffix row labels with string suffix.

[`DataFrame.add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_suffix.html#pandas.DataFrame.add_suffix "pandas.DataFrame.add_suffix")

Suffix column labels with string suffix.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s
0    1
1    2
2    3
3    4
dtype: int64

Copy to clipboard

\>>> s.add\_prefix("item\_")
item\_0    1
item\_1    2
item\_2    3
item\_3    4
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

\>>> df.add\_prefix("col\_")
     col\_A  col\_B
0       1       3
1       2       4
2       3       5
3       4       6

Copy to clipboard

On this page