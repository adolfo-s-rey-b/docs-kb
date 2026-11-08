[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.loc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.loc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.loc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.loc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.loc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.loc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.loc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.loc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.loc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.loc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.loc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.loc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.loc[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas-dataframe-loc "Link to this heading")

============================================================================================================================================

property DataFrame.loc[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexing.py#L360-L696)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "Link to this definition")

Access a group of rows and columns by label(s) or a boolean array.

`.loc[]` is primarily label based, but may also be used with a boolean array.

Allowed inputs are:

*   A single label, e.g. `5` or `'a'`, (note that `5` is interpreted as a _label_ of the index, and **never** as an integer position along the index).
    
*   A list or array of labels, e.g. `['a', 'b', 'c']`.
    
*   A slice object with labels, e.g. `'a':'f'`.
    
    Warning
    
    Note that contrary to usual python slices, **both** the start and the stop are included
    
*   A boolean array of the same length as the axis being sliced, e.g. `[True, False, True]`.
    
*   An alignable boolean Series. The index of the key will be aligned before masking.
    
*   An alignable Index. The Index of the returned selection will be the input.
    
*   A `callable` function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above)
    

See more at [Selection by Label](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label)
.

Raises:

KeyError

If any items are not found.

IndexingError

If an indexed key is passed and its index is unalignable to the frame index.

See also

[`DataFrame.at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")

Access a single value for a row/column label pair.

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Access group of rows and columns by integer position(s).

[`DataFrame.xs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas.DataFrame.xs "pandas.DataFrame.xs")

Returns a cross-section (row(s) or column(s)) from the Series/DataFrame.

[`Series.loc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas.Series.loc "pandas.Series.loc")

Access group of values using labels.

Examples

**Getting values**

\>>> df \= pd.DataFrame(
...     \[\[1, 2\], \[4, 5\], \[7, 8\]\],
...     index\=\["cobra", "viper", "sidewinder"\],
...     columns\=\["max\_speed", "shield"\],
... )
\>>> df
            max\_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8

Copy to clipboard

Single label. Note this returns the row as a Series.

\>>> df.loc\["viper"\]
max\_speed    4
shield       5
Name: viper, dtype: int64

Copy to clipboard

List of labels. Note using `[[]]` returns a DataFrame.

\>>> df.loc\[\["viper", "sidewinder"\]\]
            max\_speed  shield
viper               4       5
sidewinder          7       8

Copy to clipboard

Single label for row and column

\>>> df.loc\["cobra", "shield"\]
2

Copy to clipboard

Slice with labels for row and single label for column. As mentioned above, note that both the start and stop of the slice are included.

\>>> df.loc\["cobra":"viper", "max\_speed"\]
cobra    1
viper    4
Name: max\_speed, dtype: int64

Copy to clipboard

Boolean list with the same length as the row axis

\>>> df.loc\[\[False, False, True\]\]
            max\_speed  shield
sidewinder          7       8

Copy to clipboard

Alignable boolean Series:

\>>> df.loc\[\
...     pd.Series(\[False, True, False\], index\=\["viper", "sidewinder", "cobra"\])\
... \]
                     max\_speed  shield
sidewinder          7       8

Copy to clipboard

Conditional that returns a boolean Series

\>>> df.loc\[df\["shield"\] \> 6\]
            max\_speed  shield
sidewinder          7       8

Copy to clipboard

Conditional that returns a boolean Series with column labels specified

\>>> df.loc\[df\["shield"\] \> 6, \["max\_speed"\]\]
            max\_speed
sidewinder          7

Copy to clipboard

Multiple conditional using `&` that returns a boolean Series

\>>> df.loc\[(df\["max\_speed"\] \> 1) & (df\["shield"\] < 8)\]
            max\_speed  shield
viper          4       5

Copy to clipboard

Multiple conditional using `|` that returns a boolean Series

\>>> df.loc\[(df\["max\_speed"\] \> 4) | (df\["shield"\] < 5)\]
            max\_speed  shield
cobra               1       2
sidewinder          7       8

Copy to clipboard

Please ensure that each condition is wrapped in parentheses `()`. See the [user guide](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-boolean)
 for more details and explanations of Boolean indexing.

Note

If you find yourself using 3 or more conditionals in `.loc[]`, consider using [advanced indexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-advanced-hierarchical)
.

See below for using `.loc[]` on MultiIndex DataFrames.

Callable that returns a boolean Series

\>>> df.loc\[lambda df: df\["shield"\] \== 8\]
            max\_speed  shield
sidewinder          7       8

Copy to clipboard

**Selecting along an explicit axis**

`.loc` can be called with an `axis` argument to apply a single indexer to that axis.

\>>> df.loc(axis\=0)\["viper"\]
max\_speed    4
shield       5
Name: viper, dtype: int64

Copy to clipboard

\>>> df.loc(axis\=1)\["shield"\]
cobra         2
viper         5
sidewinder    8
Name: shield, dtype: int64

Copy to clipboard

**Setting values**

Set value for all items matching the list of labels

\>>> df.loc\[\["viper", "sidewinder"\], \["shield"\]\] \= 50
\>>> df
            max\_speed  shield
cobra               1       2
viper               4      50
sidewinder          7      50

Copy to clipboard

Set value for an entire row

\>>> df.loc\["cobra"\] \= 10
\>>> df
            max\_speed  shield
cobra              10      10
viper               4      50
sidewinder          7      50

Copy to clipboard

Set value for an entire column

\>>> df.loc\[:, "max\_speed"\] \= 30
\>>> df
            max\_speed  shield
cobra              30      10
viper              30      50
sidewinder         30      50

Copy to clipboard

Set value for rows matching callable condition

\>>> df.loc\[df\["shield"\] \> 35\] \= 0
\>>> df
            max\_speed  shield
cobra              30      10
viper               0       0
sidewinder          0       0

Copy to clipboard

Add value matching location

\>>> df.loc\["viper", "shield"\] += 5
\>>> df
            max\_speed  shield
cobra              30      10
viper               0       5
sidewinder          0       0

Copy to clipboard

Setting using a `Series` or a `DataFrame` sets the values matching the index labels, not the index positions.

\>>> shuffled\_df \= df.loc\[\["viper", "cobra", "sidewinder"\]\]
\>>> df.loc\[:\] += shuffled\_df
\>>> df
            max\_speed  shield
cobra              60      20
viper               0      10
sidewinder          0       0

Copy to clipboard

**Getting values on a DataFrame with an index that has integer labels**

Another example using integers for the index

\>>> df \= pd.DataFrame(
...     \[\[1, 2\], \[4, 5\], \[7, 8\]\],
...     index\=\[7, 8, 9\],
...     columns\=\["max\_speed", "shield"\],
... )
\>>> df
   max\_speed  shield
7          1       2
8          4       5
9          7       8

Copy to clipboard

Slice with integer labels for rows. As mentioned above, note that both the start and stop of the slice are included.

\>>> df.loc\[7:9\]
   max\_speed  shield
7          1       2
8          4       5
9          7       8

Copy to clipboard

**Getting values with a MultiIndex**

A number of examples using a DataFrame with a MultiIndex

\>>> tuples \= \[\
...     ("cobra", "mark i"),\
...     ("cobra", "mark ii"),\
...     ("sidewinder", "mark i"),\
...     ("sidewinder", "mark ii"),\
...     ("viper", "mark ii"),\
...     ("viper", "mark iii"),\
... \]
\>>> index \= pd.MultiIndex.from\_tuples(tuples)
\>>> values \= \[\[12, 2\], \[0, 4\], \[10, 20\], \[1, 4\], \[7, 1\], \[16, 36\]\]
\>>> df \= pd.DataFrame(values, columns\=\["max\_speed", "shield"\], index\=index)
\>>> df
                     max\_speed  shield
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36

Copy to clipboard

Single label. Note this returns a DataFrame with a single index.

\>>> df.loc\["cobra"\]
         max\_speed  shield
mark i          12       2
mark ii          0       4

Copy to clipboard

Single index tuple. Note this returns a Series.

\>>> df.loc\[("cobra", "mark ii")\]
max\_speed    0
shield       4
Name: (cobra, mark ii), dtype: int64

Copy to clipboard

Single label for row and column. Similar to passing in a tuple, this returns a Series.

\>>> df.loc\["cobra", "mark i"\]
max\_speed    12
shield        2
Name: (cobra, mark i), dtype: int64

Copy to clipboard

Single tuple. Note using `[[]]` returns a DataFrame.

\>>> df.loc\[\[("cobra", "mark ii")\]\]
               max\_speed  shield
cobra mark ii          0       4

Copy to clipboard

Single tuple for the index with a single label for the column

\>>> df.loc\[("cobra", "mark i"), "shield"\]
2

Copy to clipboard

Slice from index tuple to single label

\>>> df.loc\[("cobra", "mark i") : "viper"\]
                     max\_speed  shield
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36

Copy to clipboard

Slice from index tuple to index tuple

\>>> df.loc\[("cobra", "mark i") : ("viper", "mark ii")\]
                    max\_speed  shield
cobra      mark i          12       2
           mark ii          0       4
sidewinder mark i          10      20
           mark ii          1       4
viper      mark ii          7       1

Copy to clipboard

Please see the [user guide](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-advanced-hierarchical)
 for more details and explanations of advanced indexing.

**Assignment with Series**

When assigning a Series to .loc\[row\_indexer, col\_indexer\], pandas aligns the Series by index labels, not by order or position.

Series assignment with .loc and index alignment:

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\]}, index\=\[0, 1, 2\])
\>>> s \= pd.Series(\[10, 20\], index\=\[1, 0\])  \# Note reversed order
\>>> df.loc\[:, "B"\] \= s  \# Aligns by index, not order
\>>> df
   A   B
0  1  20.0
1  2  10.0
2  3 NaN

Copy to clipboard

On this page