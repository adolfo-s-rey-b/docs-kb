[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.drop.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.drop.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.drop.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.drop.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.drop.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.drop.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.drop.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.drop.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.drop.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.drop.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.drop.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.drop.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.drop[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas-dataframe-drop "Link to this heading")

===============================================================================================================================================

DataFrame.drop(_labels\=None_, _\*_, _axis\=0_, _index\=None_, _columns\=None_, _level\=None_, _inplace\=<no\_default>_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6806-L6982)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "Link to this definition")

Drop specified labels from rows or columns.

Remove rows or columns by specifying label names and corresponding axis, or by directly specifying index or column names. When using a multi-index, labels on different levels can be removed by specifying the level. See the [user guide](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-shown-levels)
 for more information about the now unused levels.

Parameters:

**labels**single label or iterable of labels

Index or column labels to drop. A tuple will be used as a single label and not treated as an iterable.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).

**index**single label or iterable of labels

Alternative to specifying axis (`labels, axis=0` is equivalent to `index=labels`).

**columns**single label or iterable of labels

Alternative to specifying axis (`labels, axis=1` is equivalent to `columns=labels`).

**level**int or level name, optional

For MultiIndex, level from which the labels will be removed.

**inplace**bool, default False

If False, return a copy. Otherwise, do operation in place and return None.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**errors**{‘ignore’, ‘raise’}, default ‘raise’

If ‘ignore’, suppress error and only existing labels are dropped.

Returns:

DataFrame or None

Returns DataFrame or None DataFrame with the specified index or column labels removed or None if inplace=True.

Raises:

KeyError

If any of the labels is not found in the selected axis.

See also

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Label-location based indexer for selection by label.

[`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")

Return DataFrame with labels on given axis omitted where (all or any) data are missing.

[`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")

Return DataFrame with duplicate rows removed, optionally only considering certain columns.

[`Series.drop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas.Series.drop "pandas.Series.drop")

Return Series with specified index labels removed.

Examples

\>>> df \= pd.DataFrame(np.arange(12).reshape(3, 4), columns\=\["A", "B", "C", "D"\])
\>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

Copy to clipboard

Drop columns

\>>> df.drop(\["B", "C"\], axis\=1)
   A   D
0  0   3
1  4   7
2  8  11

Copy to clipboard

\>>> df.drop(columns\=\["B", "C"\])
   A   D
0  0   3
1  4   7
2  8  11

Copy to clipboard

Drop a row by index

\>>> df.drop(\[0, 1\])
   A  B   C   D
2  8  9  10  11

Copy to clipboard

Drop columns and/or rows of MultiIndex DataFrame

\>>> midx \= pd.MultiIndex(
...     levels\=\[\["llama", "cow", "falcon"\], \["speed", "weight", "length"\]\],
...     codes\=\[\[0, 0, 0, 1, 1, 1, 2, 2, 2\], \[0, 1, 2, 0, 1, 2, 0, 1, 2\]\],
... )
\>>> df \= pd.DataFrame(
...     index\=midx,
...     columns\=\["big", "small"\],
...     data\=\[\
...         \[45, 30\],\
...         \[200, 100\],\
...         \[1.5, 1\],\
...         \[30, 20\],\
...         \[250, 150\],\
...         \[1.5, 0.8\],\
...         \[320, 250\],\
...         \[1, 0.8\],\
...         \[0.3, 0.2\],\
...     \],
... )
\>>> df
                big     small
llama   speed   45.0    30.0
        weight  200.0   100.0
        length  1.5     1.0
cow     speed   30.0    20.0
        weight  250.0   150.0
        length  1.5     0.8
falcon  speed   320.0   250.0
        weight  1.0     0.8
        length  0.3     0.2

Copy to clipboard

Drop a specific index combination from the MultiIndex DataFrame, i.e., drop the combination `'falcon'` and `'weight'`, which deletes only the corresponding row

\>>> df.drop(index\=("falcon", "weight"))
                big     small
llama   speed   45.0    30.0
        weight  200.0   100.0
        length  1.5     1.0
cow     speed   30.0    20.0
        weight  250.0   150.0
        length  1.5     0.8
falcon  speed   320.0   250.0
        length  0.3     0.2

Copy to clipboard

\>>> df.drop(index\="cow", columns\="small")
                big
llama   speed   45.0
        weight  200.0
        length  1.5
falcon  speed   320.0
        weight  1.0
        length  0.3

Copy to clipboard

\>>> df.drop(index\="length", level\=1)
                big     small
llama   speed   45.0    30.0
        weight  200.0   100.0
cow     speed   30.0    20.0
        weight  250.0   150.0
falcon  speed   320.0   250.0
        weight  1.0     0.8

Copy to clipboard

On this page