[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.drop[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas-series-drop "Link to this heading")

======================================================================================================================================

Series.drop(_labels\=None_, _\*_, _axis\=0_, _index\=None_, _columns\=None_, _level\=None_, _inplace\=<no\_default>_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6207-L6321)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas.Series.drop "Link to this definition")

Return Series with specified index labels removed.

Remove elements of a Series based on specifying the index labels. When using a multi-index, labels on different levels can be removed by specifying the level.

Parameters:

**labels**single label or list-like

Index labels to drop.

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**index**single label or list-like

Redundant for application on Series, but ‘index’ can be used instead of ‘labels’.

**columns**single label or list-like

No change is made to the Series; use ‘index’ or ‘labels’ instead.

**level**int or level name, optional

For MultiIndex, level for which the labels will be removed.

**inplace**bool, default False

If True, do operation inplace and return None.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**errors**{‘ignore’, ‘raise’}, default ‘raise’

If ‘ignore’, suppress error and only existing labels are dropped.

Returns:

Series or None

Series with specified index labels removed or None if `inplace=True`.

Raises:

KeyError

If none of the labels are found in the index.

See also

[`Series.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")

Return only specified index labels of Series.

[`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")

Return series without null values.

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Return Series with duplicate values removed.

[`DataFrame.drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")

Drop specified labels from rows or columns.

Examples

\>>> s \= pd.Series(data\=np.arange(3), index\=\["A", "B", "C"\])
\>>> s
A  0
B  1
C  2
dtype: int64

Copy to clipboard

Drop labels B and C

\>>> s.drop(labels\=\["B", "C"\])
A  0
dtype: int64

Copy to clipboard

Drop 2nd level label in MultiIndex Series

\>>> midx \= pd.MultiIndex(
...     levels\=\[\["llama", "cow", "falcon"\], \["speed", "weight", "length"\]\],
...     codes\=\[\[0, 0, 0, 1, 1, 1, 2, 2, 2\], \[0, 1, 2, 0, 1, 2, 0, 1, 2\]\],
... )
\>>> s \= pd.Series(\[45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3\], index\=midx)
\>>> s
llama   speed      45.0
        weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

Copy to clipboard

\>>> s.drop(labels\="weight", level\=1)
llama   speed      45.0
        length      1.2
cow     speed      30.0
        length      1.5
falcon  speed     320.0
        length      0.3
dtype: float64

Copy to clipboard

On this page