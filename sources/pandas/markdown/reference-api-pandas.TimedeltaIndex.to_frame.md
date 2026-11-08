[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.to\_frame[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html#pandas-timedeltaindex-to-frame "Link to this heading")

===========================================================================================================================================================================

TimedeltaIndex.to\_frame(_index\=True_, _name\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1766-L1831)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html#pandas.TimedeltaIndex.to_frame "Link to this definition")

Create a DataFrame with a column containing the Index.

This method wraps the Index values into a single-column DataFrame, optionally preserving the original Index as the new DataFrame’s index.

Parameters:

**index**bool, default True

Set the index of the returned DataFrame as the original Index.

**name**Hashable, defaults to index.name

The passed name should substitute for the index name (if it has one).

Returns:

DataFrame

DataFrame containing the original Index data.

See also

[`Index.to_series`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_series.html#pandas.Index.to_series "pandas.Index.to_series")

Convert an Index to a Series.

[`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")

Convert Series to DataFrame.

Examples

\>>> idx \= pd.Index(\["Ant", "Bear", "Cow"\], name\="animal")
\>>> idx.to\_frame()
       animal
animal
Ant       Ant
Bear     Bear
Cow       Cow

Copy to clipboard

By default, the original Index is reused. To enforce a new Index:

\>>> idx.to\_frame(index\=False)
    animal
0   Ant
1  Bear
2   Cow

Copy to clipboard

To override the name of the resulting column, specify name:

\>>> idx.to\_frame(index\=False, name\="zoo")
    zoo
0   Ant
1  Bear
2   Cow

Copy to clipboard

On this page