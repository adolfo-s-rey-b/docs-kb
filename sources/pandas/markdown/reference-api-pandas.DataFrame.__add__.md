[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__add__.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.\_\_add\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__add__.html#pandas-dataframe-add "Link to this heading")

========================================================================================================================================================

DataFrame.\_\_add\_\_(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arraylike.py#L121-L211)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__add__.html#pandas.DataFrame.__add__ "Link to this definition")

Get Addition of DataFrame and other, column-wise.

Equivalent to `DataFrame.add(other)`.

Parameters:

**other**scalar, sequence, Series, dict or DataFrame

Object to be added to the DataFrame.

Returns:

DataFrame

The result of adding `other` to DataFrame.

See also

[`DataFrame.add`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add")

Add a DataFrame and another object, with option for index- or column-oriented addition.

Examples

\>>> df \= pd.DataFrame(
...     {"height": \[1.5, 2.6\], "weight": \[500, 800\]}, index\=\["elk", "moose"\]
... )
\>>> df
       height  weight
elk       1.5     500
moose     2.6     800

Copy to clipboard

Adding a scalar affects all rows and columns.

\>>> df\[\["height", "weight"\]\] + 1.5
       height  weight
elk       3.0   501.5
moose     4.1   801.5

Copy to clipboard

Each element of a list is added to a column of the DataFrame, in order.

\>>> df\[\["height", "weight"\]\] + \[0.5, 1.5\]
       height  weight
elk       2.0   501.5
moose     3.1   801.5

Copy to clipboard

Keys of a dictionary are aligned to the DataFrame, based on column names; each value in the dictionary is added to the corresponding column.

\>>> df\[\["height", "weight"\]\] + {"height": 0.5, "weight": 1.5}
       height  weight
elk       2.0   501.5
moose     3.1   801.5

Copy to clipboard

When other is a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, the index of other is aligned with the columns of the DataFrame.

\>>> s1 \= pd.Series(\[0.5, 1.5\], index\=\["weight", "height"\])
\>>> df\[\["height", "weight"\]\] + s1
       height  weight
elk       3.0   500.5
moose     4.1   800.5

Copy to clipboard

Even when the index of other is the same as the index of the DataFrame, the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 will not be reoriented. If index-wise alignment is desired, [`DataFrame.add()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add")
 should be used with axis=’index’.

\>>> s2 \= pd.Series(\[0.5, 1.5\], index\=\["elk", "moose"\])
\>>> df\[\["height", "weight"\]\] + s2
       elk  height  moose  weight
elk    NaN     NaN    NaN     NaN
moose  NaN     NaN    NaN     NaN

Copy to clipboard

\>>> df\[\["height", "weight"\]\].add(s2, axis\="index")
       height  weight
elk       2.0   500.5
moose     4.1   801.5

Copy to clipboard

When other is a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, both columns names and the index are aligned.

\>>> other \= pd.DataFrame(
...     {"height": \[0.2, 0.4, 0.6\]}, index\=\["elk", "moose", "deer"\]
... )
\>>> df\[\["height", "weight"\]\] + other
       height  weight
deer      NaN     NaN
elk       1.7     NaN
moose     3.0     NaN

Copy to clipboard

On this page