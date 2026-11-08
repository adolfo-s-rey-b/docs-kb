[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.pivot.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.pivot.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.pivot.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.pivot.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.pivot.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.pivot.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.pivot.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.pivot.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.pivot.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.pivot.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.pivot.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.pivot.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.pivot[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas-dataframe-pivot "Link to this heading")

==================================================================================================================================================

DataFrame.pivot(_\*_, _columns_, _index\=<no\_default>_, _values\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L13799-L13948)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "Link to this definition")

Return reshaped DataFrame organized by given index / column values.

Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame. This function does not support data aggregation, multiple values will result in a MultiIndex in the columns. See the [User Guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)
 for more on reshaping.

Parameters:

**columns**Hashable or a sequence of the previous

Column to use to make new frame’s columns.

**index**Hashable or a sequence of the previous, optional

Column to use to make new frame’s index. If not given, uses existing index.

**values**Hashable or a sequence of the previous, optional

Column(s) to use for populating new frame’s values. If not specified, all remaining columns will be used and the result will have hierarchically indexed columns.

Returns:

DataFrame

Returns reshaped DataFrame.

Raises:

ValueError:

When there are any index, columns combinations with multiple values. DataFrame.pivot\_table when you need to aggregate.

See also

[`DataFrame.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")

Generalization of pivot that can handle duplicate values for one index/column pair.

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Pivot based on the index values instead of a column.

[`wide_to_long`](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#pandas.wide_to_long "pandas.wide_to_long")

Wide panel to long format. Less flexible but more user-friendly than melt.

Notes

For finer-tuned control, see hierarchical indexing documentation along with the related stack/unstack methods.

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-pivot)
 for more examples.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "foo": \["one", "one", "one", "two", "two", "two"\],
...         "bar": \["A", "B", "C", "A", "B", "C"\],
...         "baz": \[1, 2, 3, 4, 5, 6\],
...         "zoo": \["x", "y", "z", "q", "w", "t"\],
...     }
... )
\>>> df
    foo   bar  baz  zoo
0   one   A    1    x
1   one   B    2    y
2   one   C    3    z
3   two   A    4    q
4   two   B    5    w
5   two   C    6    t

Copy to clipboard

\>>> df.pivot(index\="foo", columns\="bar", values\="baz")
bar  A   B   C
foo
one  1   2   3
two  4   5   6

Copy to clipboard

\>>> df.pivot(index\="foo", columns\="bar")\["baz"\]
bar  A   B   C
foo
one  1   2   3
two  4   5   6

Copy to clipboard

\>>> df.pivot(index\="foo", columns\="bar", values\=\["baz", "zoo"\])
      baz       zoo
bar   A  B  C   A  B  C
foo
one   1  2  3   x  y  z
two   4  5  6   q  w  t

Copy to clipboard

You could also assign a list of column names or a list of index names.

\>>> df \= pd.DataFrame(
...     {
...         "lev1": \[1, 1, 1, 2, 2, 2\],
...         "lev2": \[1, 1, 2, 1, 1, 2\],
...         "lev3": \[1, 2, 1, 2, 1, 2\],
...         "lev4": \[1, 2, 3, 4, 5, 6\],
...         "values": \[0, 1, 2, 3, 4, 5\],
...     }
... )
\>>> df
    lev1 lev2 lev3 lev4 values
0   1    1    1    1    0
1   1    1    2    2    1
2   1    2    1    3    2
3   2    1    2    4    3
4   2    1    1    5    4
5   2    2    2    6    5

Copy to clipboard

\>>> df.pivot(index\="lev1", columns\=\["lev2", "lev3"\], values\="values")
lev2    1         2
lev3    1    2    1    2
lev1
1     0.0  1.0  2.0  NaN
2     4.0  3.0  NaN  5.0

Copy to clipboard

\>>> df.pivot(index\=\["lev1", "lev2"\], columns\=\["lev3"\], values\="values")
      lev3    1    2
lev1  lev2
   1     1  0.0  1.0
         2  2.0  NaN
   2     1  4.0  3.0
         2  NaN  5.0

Copy to clipboard

A ValueError is raised if there are any duplicates.

\>>> df \= pd.DataFrame(
...     {
...         "foo": \["one", "one", "two", "two"\],
...         "bar": \["A", "A", "B", "C"\],
...         "baz": \[1, 2, 3, 4\],
...     }
... )
\>>> df
   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4

Copy to clipboard

Notice that the first two rows are the same for our index and columns arguments.

\>>> df.pivot(index\="foo", columns\="bar", values\="baz")
Traceback (most recent call last):
   ...
ValueError: Index contains duplicate entries, cannot reshape

Copy to clipboard

On this page