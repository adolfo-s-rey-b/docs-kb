[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.merge_ordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.merge_ordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.merge_ordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.merge_ordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.merge_ordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.merge_ordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.merge_ordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.merge_ordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.merge_ordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.merge_ordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.merge_ordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.merge_ordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.merge\_ordered[#](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html#pandas-merge-ordered "Link to this heading")

=============================================================================================================================================

pandas.merge\_ordered(_left_, _right_, _on\=None_, _left\_on\=None_, _right\_on\=None_, _left\_by\=None_, _right\_by\=None_, _fill\_method\=None_, _suffixes\=('\_x', '\_y')_, _how\='outer'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/merge.py#L502-L643)
[#](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html#pandas.merge_ordered "Link to this definition")

Perform a merge for ordered data with optional filling/interpolation.

Designed for ordered data like time series data. Optionally perform group-wise merge (see examples).

Parameters:

**left**DataFrame or named Series

First pandas object to merge.

**right**DataFrame or named Series

Second pandas object to merge.

**on**Hashable or a sequence of the previous

Field names to join on. Must be found in both DataFrames.

**left\_on**Hashable or a sequence of the previous, or array-like

Field names to join on in left DataFrame. Can be a vector or list of vectors of the length of the DataFrame to use a particular vector as the join key instead of columns.

**right\_on**Hashable or a sequence of the previous, or array-like

Field names to join on in right DataFrame or vector/list of vectors per left\_on docs.

**left\_by**column name or list of column names

Group left DataFrame by group columns and merge piece by piece with right DataFrame. Must be None if either left or right are a Series.

**right\_by**column name or list of column names

Group right DataFrame by group columns and merge piece by piece with left DataFrame. Must be None if either left or right are a Series.

**fill\_method**{‘ffill’, None}, default None

Interpolation method for data.

**suffixes**list-like, default is (“\_x”, “\_y”)

A length-2 sequence where each element is optionally a string indicating the suffix to add to overlapping column names in left and right respectively. Pass a value of None instead of a string to indicate that the column name from left or right should be left as-is, with no suffix. At least one of the values must not be None.

**how**{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘outer’

*   left: use only keys from left frame (SQL: left outer join)
    
*   right: use only keys from right frame (SQL: right outer join)
    
*   outer: use union of keys from both frames (SQL: full outer join)
    
*   inner: use intersection of keys from both frames (SQL: inner join).
    

Returns:

DataFrame

The merged DataFrame output type will be the same as ‘left’, if it is a subclass of DataFrame.

See also

[`merge`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")

Merge with a database-style join.

[`merge_asof`](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof")

Merge on nearest keys.

Examples

\>>> from pandas import merge\_ordered
\>>> df1 \= pd.DataFrame(
...     {
...         "key": \["a", "c", "e", "a", "c", "e"\],
...         "lvalue": \[1, 2, 3, 1, 2, 3\],
...         "group": \["a", "a", "a", "b", "b", "b"\],
...     }
... )
\>>> df1
  key  lvalue group
0   a       1     a
1   c       2     a
2   e       3     a
3   a       1     b
4   c       2     b
5   e       3     b

Copy to clipboard

\>>> df2 \= pd.DataFrame({"key": \["b", "c", "d"\], "rvalue": \[1, 2, 3\]})
\>>> df2
  key  rvalue
0   b       1
1   c       2
2   d       3

Copy to clipboard

\>>> merge\_ordered(df1, df2, fill\_method\="ffill", left\_by\="group")
  key  lvalue group  rvalue
0   a       1     a     NaN
1   b       1     a     1.0
2   c       2     a     2.0
3   d       2     a     3.0
4   e       3     a     3.0
5   a       1     b     NaN
6   b       1     b     1.0
7   c       2     b     2.0
8   d       2     b     3.0
9   e       3     b     3.0

Copy to clipboard

On this page