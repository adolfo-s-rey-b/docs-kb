[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.melt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.melt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.melt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.melt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.melt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.melt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.melt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.melt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.melt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.melt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.melt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.melt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.melt[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas-dataframe-melt "Link to this heading")

===============================================================================================================================================

DataFrame.melt(_id\_vars\=None_, _value\_vars\=None_, _var\_name\=None_, _value\_name\='value'_, _col\_level\=None_, _ignore\_index\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14602-L14740)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas.DataFrame.melt "Link to this definition")

Unpivot DataFrame from wide to long format, optionally leaving identifiers set.

This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id\_vars), while all other columns, considered measured variables (value\_vars), are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.

Parameters:

**id\_vars**scalar, tuple, list, or ndarray, optional

Column(s) to use as identifier variables.

**value\_vars**scalar, tuple, list, or ndarray, optional

Column(s) to unpivot. If not specified, uses all columns that are not set as id\_vars.

**var\_name**scalar, default None

Name to use for the ‘variable’ column. If None it uses `frame.columns.name` or ‘variable’.

**value\_name**scalar, default ‘value’

Name to use for the ‘value’ column, can’t be an existing column label.

**col\_level**scalar, optional

If columns are a MultiIndex then use this level to melt.

**ignore\_index**bool, default True

If True, original index is ignored. If False, original index is retained. Index labels will be repeated as necessary.

Returns:

DataFrame

Unpivoted DataFrame.

See also

[`melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")

Identical method.

[`pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html#pandas.pivot_table "pandas.pivot_table")

Create a spreadsheet-style pivot table as a DataFrame.

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Return reshaped DataFrame organized by given index / column values.

[`DataFrame.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "pandas.DataFrame.explode")

Explode a DataFrame from list-like columns to long format.

Notes

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-melt)
 for more examples.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "A": {0: "a", 1: "b", 2: "c"},
...         "B": {0: 1, 1: 3, 2: 5},
...         "C": {0: 2, 1: 4, 2: 6},
...     }
... )
\>>> df
A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

Copy to clipboard

\>>> df.melt(id\_vars\=\["A"\], value\_vars\=\["B"\])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

Copy to clipboard

\>>> df.melt(id\_vars\=\["A"\], value\_vars\=\["B", "C"\])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
3  a        C      2
4  b        C      4
5  c        C      6

Copy to clipboard

The names of ‘variable’ and ‘value’ columns can be customized:

\>>> df.melt(
...     id\_vars\=\["A"\],
...     value\_vars\=\["B"\],
...     var\_name\="myVarname",
...     value\_name\="myValname",
... )
A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5

Copy to clipboard

Original index values can be kept around:

\>>> df.melt(id\_vars\=\["A"\], value\_vars\=\["B", "C"\], ignore\_index\=False)
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
0  a        C      2
1  b        C      4
2  c        C      6

Copy to clipboard

If you have multi-index columns:

\>>> df.columns \= \[list("ABC"), list("DEF")\]
\>>> df
A  B  C
D  E  F
0  a  1  2
1  b  3  4
2  c  5  6

Copy to clipboard

\>>> df.melt(col\_level\=0, id\_vars\=\["A"\], value\_vars\=\["B"\])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

Copy to clipboard

\>>> df.melt(id\_vars\=\[("A", "D")\], value\_vars\=\[("B", "E")\])
(A, D) variable\_0 variable\_1  value
0      a          B          E      1
1      b          B          E      3
2      c          B          E      5

Copy to clipboard

On this page