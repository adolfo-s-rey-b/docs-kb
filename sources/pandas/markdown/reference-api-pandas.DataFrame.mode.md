[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.mode[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas-dataframe-mode "Link to this heading")

===============================================================================================================================================

DataFrame.mode(_axis\=0_, _numeric\_only\=False_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19498-L19592)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas.DataFrame.mode "Link to this definition")

Get the mode(s) of each element along the selected axis.

The mode of a set of values is the value that appears most often. It can be multiple values.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to iterate over while searching for the mode:

*   0 or ‘index’ : get mode of each column
    
*   1 or ‘columns’ : get mode of each row.
    

**numeric\_only**bool, default False

If True, only apply to numeric columns.

**dropna**bool, default True

Don’t consider counts of NaN/NaT.

Returns:

DataFrame

The modes of each column or row.

See also

[`Series.mode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "pandas.Series.mode")

Return the highest frequency value in a Series.

[`Series.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")

Return the counts of values in a Series.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         ("bird", 2, 2),\
...         ("mammal", 4, np.nan),\
...         ("arthropod", 8, 0),\
...         ("bird", 2, np.nan),\
...     \],
...     index\=("falcon", "horse", "spider", "ostrich"),
...     columns\=("species", "legs", "wings"),
... )
\>>> df
           species  legs  wings
falcon        bird     2    2.0
horse       mammal     4    NaN
spider   arthropod     8    0.0
ostrich       bird     2    NaN

Copy to clipboard

By default, missing values are not considered, and the mode of wings are both 0 and 2. Because the resulting DataFrame has two rows, the second row of `species` and `legs` contains `NaN`.

\>>> df.mode()
  species  legs  wings
0    bird   2.0    0.0
1     NaN   NaN    2.0

Copy to clipboard

Setting `dropna=False` `NaN` values are considered and they can be the mode (like for wings).

\>>> df.mode(dropna\=False)
  species  legs  wings
0    bird     2    NaN

Copy to clipboard

Setting `numeric_only=True`, only the mode of numeric columns is computed, and columns of other types are ignored.

\>>> df.mode(numeric\_only\=True)
   legs  wings
0   2.0    0.0
1   NaN    2.0

Copy to clipboard

To compute the mode over columns and not rows, use the axis parameter:

\>>> df.mode(axis\="columns", numeric\_only\=True)
           0    1
falcon   2.0  NaN
horse    4.0  NaN
spider   0.0  8.0
ostrich  2.0  NaN

Copy to clipboard

On this page