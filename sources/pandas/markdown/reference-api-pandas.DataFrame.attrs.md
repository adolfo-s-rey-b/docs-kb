[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.attrs[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas-dataframe-attrs "Link to this heading")

==================================================================================================================================================

property DataFrame.attrs[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L324-L369)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "Link to this definition")

Dictionary of global attributes of this dataset.

Warning

attrs is experimental and may change without warning.

See also

`DataFrame.flags`

Global flags applying to this object.

Notes

Many operations that create new datasets will copy `attrs`. Copies are always deep so that changing `attrs` will only affect the present dataset. [`pandas.concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
 and [`pandas.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")
 will only copy `attrs` if all input datasets have the same `attrs`.

`attrs` is a property of a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 as a whole, not of an individual column. The [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 constructor does not extract `attrs` from a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 it is built from, and assigning a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 as a column of an existing [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (e.g. `df[col] = ser`) does not modify [`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")
. Methods that build a new [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 from a single [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 (such as [`Series.to_frame()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")
) do propagate the source `attrs`.

Examples

For Series:

\>>> ser \= pd.Series(\[1, 2, 3\])
\>>> ser.attrs \= {"A": \[10, 20, 30\]}
\>>> ser.attrs
{'A': \[10, 20, 30\]}

Copy to clipboard

For DataFrame:

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> df.attrs \= {"A": \[10, 20, 30\]}
\>>> df.attrs
{'A': \[10, 20, 30\]}

Copy to clipboard

On this page