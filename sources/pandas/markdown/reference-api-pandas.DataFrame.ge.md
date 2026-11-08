[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.ge.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.ge.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.ge.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.ge.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.ge.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.ge.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.ge.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.ge.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.ge.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.ge.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.ge.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.ge.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.ge[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#pandas-dataframe-ge "Link to this heading")

=========================================================================================================================================

DataFrame.ge(_other_, _axis\='columns'_, _level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L11207-L11354)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#pandas.DataFrame.ge "Link to this definition")

Get Greater than or equal to of dataframe and other, element-wise (binary operator ge).

Among flexible wrappers (eq, ne, le, lt, ge, gt) to comparison operators.

Equivalent to `>=` with support to choose axis (rows or columns) and level for comparison.

Parameters:

**other**scalar, sequence, Series, or DataFrame

Any single or multiple element data structure, or list-like object.

**axis**{0 or ‘index’, 1 or ‘columns’}, default ‘columns’

Whether to compare by the index (0 or ‘index’) or columns (1 or ‘columns’).

**level**int or label

Broadcast across a level, matching Index values on the passed MultiIndex level.

Returns:

DataFrame of bool

Result of the comparison.

See also

[`DataFrame.eq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html#pandas.DataFrame.eq "pandas.DataFrame.eq")

Compare DataFrames for equality elementwise.

[`DataFrame.ne`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ne.html#pandas.DataFrame.ne "pandas.DataFrame.ne")

Compare DataFrames for inequality elementwise.

[`DataFrame.le`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.le.html#pandas.DataFrame.le "pandas.DataFrame.le")

Compare DataFrames for less than inequality or equality elementwise.

[`DataFrame.lt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.lt.html#pandas.DataFrame.lt "pandas.DataFrame.lt")

Compare DataFrames for strictly less than inequality elementwise.

[`DataFrame.ge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#pandas.DataFrame.ge "pandas.DataFrame.ge")

Compare DataFrames for greater than inequality or equality elementwise.

[`DataFrame.gt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.gt.html#pandas.DataFrame.gt "pandas.DataFrame.gt")

Compare DataFrames for strictly greater than inequality elementwise.

Notes

Mismatched indices will be unioned together. NaN values are considered different (i.e. NaN != NaN).

Examples

\>>> df \= pd.DataFrame({'cost': \[250, 150, 100\],
...                    'revenue': \[100, 250, 300\]},
...                   index\=\['A', 'B', 'C'\])
\>>> df
   cost  revenue
A   250      100
B   150      250
C   100      300

Copy to clipboard

Comparison with a scalar, using either the operator or method:

\>>> df \>= 100
   cost  revenue
A  True     True
B  True     True
C  True     True

Copy to clipboard

\>>> df.ge(100)
   cost  revenue
A  True     True
B  True     True
C  True     True

Copy to clipboard

When other is a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, the columns of a DataFrame are aligned with the index of other and broadcast:

\>>> df \>= pd.Series(\[100, 250\], index\=\["cost", "revenue"\])
   cost  revenue
A  True    False
B  True     True
C  True     True

Copy to clipboard

Use the method to control the broadcast axis:

\>>> df.ge(pd.Series(\[100, 300\], index\=\["A", "D"\]), axis\='index')
    cost  revenue
A   True     True
B  False    False
C  False    False
D  False    False

Copy to clipboard

When comparing to an arbitrary sequence, the number of columns must match the number elements in other:

\>>> df \>= \[250, 100\]
    cost  revenue
A   True     True
B  False     True
C  False     True

Copy to clipboard

Use the method to control the axis:

\>>> df.ge(\[250, 250, 100\], axis\='index')
    cost  revenue
A   True    False
B  False     True
C   True     True

Copy to clipboard

Compare to a DataFrame of different shape.

\>>> other \= pd.DataFrame({'revenue': \[300, 250, 100, 150\]},
...                      index\=\['A', 'B', 'C', 'D'\])
\>>> other
   revenue
A      300
B      250
C      100
D      150

Copy to clipboard

\>>> df.ge(other)
    cost  revenue
A  False    False
B  False     True
C  False     True
D  False    False

Copy to clipboard

Compare to a MultiIndex by level.

\>>> df\_multindex \= pd.DataFrame({'cost': \[250, 150, 100, 150, 300, 220\],
...                              'revenue': \[100, 250, 300, 200, 175, 225\]},
...                             index\=\[\['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2'\],\
...                                    \['A', 'B', 'C', 'A', 'B', 'C'\]\])
\>>> df\_multindex
      cost  revenue
Q1 A   250      100
   B   150      250
   C   100      300
Q2 A   150      200
   B   300      175
   C   220      225

Copy to clipboard

\>>> df.ge(df\_multindex, level\=1)
       cost  revenue
Q1 A   True     True
   B   True     True
   C   True     True
Q2 A   True    False
   B  False     True
   C  False     True

Copy to clipboard

On this page