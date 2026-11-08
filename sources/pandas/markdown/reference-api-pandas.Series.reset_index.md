[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.reset\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html#pandas-series-reset-index "Link to this heading")

============================================================================================================================================================

Series.reset\_index(_level\=None_, _\*_, _drop\=False_, _name\=<no\_default>_, _inplace\=<no\_default>_, _allow\_duplicates\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1448-L1606)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html#pandas.Series.reset_index "Link to this definition")

Generate a new DataFrame or Series with the index reset.

This is useful when the index needs to be treated as a column, or when the index is meaningless and needs to be reset to the default before another operation.

Parameters:

**level**int, str, tuple, or list, default optional

For a Series with a MultiIndex, only remove the specified levels from the index. Removes all levels by default.

**drop**bool, default False

Just reset the index, without inserting it as a column in the new DataFrame.

**name**object, optional

The name to use for the column containing the original Series values. Uses `self.name` by default. This argument is ignored when drop is True.

**inplace**bool, default False

Modify the Series in place (do not create a new object).

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**allow\_duplicates**bool, default False

Allow duplicate column labels to be created.

Returns:

Series or DataFrame or None

When drop is False (the default), a DataFrame is returned. The newly created columns will come first in the DataFrame, followed by the original Series values. When drop is True, a Series is returned. In either case, if `inplace=True`, no value is returned.

See also

[`DataFrame.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")

Analogous function for DataFrame.

Examples

\>>> s \= pd.Series(
...     \[1, 2, 3, 4\],
...     name\="foo",
...     index\=pd.Index(\["a", "b", "c", "d"\], name\="idx"),
... )

Copy to clipboard

Generate a DataFrame with default index.

\>>> s.reset\_index()
  idx  foo
0   a    1
1   b    2
2   c    3
3   d    4

Copy to clipboard

To specify the name of the new column use name.

\>>> s.reset\_index(name\="values")
  idx  values
0   a       1
1   b       2
2   c       3
3   d       4

Copy to clipboard

To generate a new Series with the default set drop to True.

\>>> s.reset\_index(drop\=True)
0    1
1    2
2    3
3    4
Name: foo, dtype: int64

Copy to clipboard

The level parameter is interesting for Series with a multi-level index.

\>>> arrays \= \[\
...     np.array(\["bar", "bar", "baz", "baz"\]),\
...     np.array(\["one", "two", "one", "two"\]),\
... \]
\>>> s2 \= pd.Series(
...     range(4),
...     name\="foo",
...     index\=pd.MultiIndex.from\_arrays(arrays, names\=\["a", "b"\]),
... )

Copy to clipboard

To remove a specific level from the Index, use level.

\>>> s2.reset\_index(level\="a")
       a  foo
b
one  bar    0
two  bar    1
one  baz    2
two  baz    3

Copy to clipboard

If level is not set, all levels are removed from the Index.

\>>> s2.reset\_index()
     a    b  foo
0  bar  one    0
1  bar  two    1
2  baz  one    2
3  baz  two    3

Copy to clipboard

On this page