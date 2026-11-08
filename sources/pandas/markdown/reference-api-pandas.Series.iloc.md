[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.iloc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.iloc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.iloc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.iloc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.iloc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.iloc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.iloc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.iloc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.iloc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.iloc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.iloc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.iloc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.iloc[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas-series-iloc "Link to this heading")

======================================================================================================================================

property Series.iloc[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexing.py#L196-L358)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "Link to this definition")

Purely integer-location based indexing for selection by position.

Changed in version 3.0: Callables which return a tuple are deprecated as input.

`.iloc[]` is primarily integer position based (from `0` to `length-1` of the axis), but may also be used with a boolean array.

Allowed inputs are:

*   An integer, e.g. `5`.
    
*   A list or array of integers, e.g. `[4, 3, 0]`.
    
*   A slice object with ints, e.g. `1:7`.
    
*   A boolean array.
    
*   A `callable` function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above). This is useful in method chains, when you don’t have a reference to the calling object, but would like to base your selection on some value.
    
*   A tuple of row and column indexes. The tuple elements consist of one of the above inputs, e.g. `(0, 1)`.
    

`.iloc` will raise `IndexError` if a requested indexer is out-of-bounds, except _slice_ indexers which allow out-of-bounds indexing (this conforms with python/numpy _slice_ semantics).

See more at [Selection by Position](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer)
.

See also

[`DataFrame.iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat")

Fast integer location scalar accessor.

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Purely label-location based indexer for selection by label.

[`Series.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "pandas.Series.iloc")

Purely integer-location based indexing for selection by position.

Examples

\>>> mydict \= \[\
...     {"a": 1, "b": 2, "c": 3, "d": 4},\
...     {"a": 100, "b": 200, "c": 300, "d": 400},\
...     {"a": 1000, "b": 2000, "c": 3000, "d": 4000},\
... \]
\>>> df \= pd.DataFrame(mydict)
\>>> df
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

Copy to clipboard

**Indexing just the rows**

With a scalar integer.

\>>> type(df.iloc\[0\])
<class 'pandas.Series'>
\>>> df.iloc\[0\]
a    1
b    2
c    3
d    4
Name: 0, dtype: int64

Copy to clipboard

With a list of integers.

\>>> df.iloc\[\[0\]\]
   a  b  c  d
0  1  2  3  4
\>>> type(df.iloc\[\[0\]\])
<class 'pandas.DataFrame'>

Copy to clipboard

\>>> df.iloc\[\[0, 1\]\]
     a    b    c    d
0    1    2    3    4
1  100  200  300  400

Copy to clipboard

With a slice object.

\>>> df.iloc\[:3\]
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

Copy to clipboard

With a boolean mask the same length as the index.

\>>> df.iloc\[\[True, False, True\]\]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000

Copy to clipboard

With a callable, useful in method chains. The x passed to the `lambda` is the DataFrame being sliced. This selects the rows whose index label even.

\>>> df.iloc\[lambda x: x.index % 2 \== 0\]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000

Copy to clipboard

**Indexing both axes**

You can mix the indexer types for the index and columns. Use `:` to select the entire axis.

With scalar integers.

\>>> df.iloc\[0, 1\]
2

Copy to clipboard

With lists of integers.

\>>> df.iloc\[\[0, 2\], \[1, 3\]\]
      b     d
0     2     4
2  2000  4000

Copy to clipboard

With slice objects.

\>>> df.iloc\[1:3, 0:3\]
      a     b     c
1   100   200   300
2  1000  2000  3000

Copy to clipboard

With a boolean array whose length matches the columns.

\>>> df.iloc\[:, \[True, False, True, False\]\]
      a     c
0     1     3
1   100   300
2  1000  3000

Copy to clipboard

With a callable function that expects the Series or DataFrame.

\>>> df.iloc\[:, lambda df: \[0, 2\]\]
      a     c
0     1     3
1   100   300
2  1000  3000

Copy to clipboard

**Selecting along an explicit axis**

`.iloc` can be called with an `axis` argument to apply a single indexer to that axis.

\>>> df.iloc(axis\=0)\[1\]
a    100
b    200
c    300
d    400
Name: 1, dtype: int64

Copy to clipboard

\>>> df.iloc(axis\=1)\[1\]
0       2
1     200
2    2000
Name: b, dtype: int64

Copy to clipboard

On this page