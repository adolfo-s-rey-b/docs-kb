[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.name[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#pandas-series-name "Link to this heading")

======================================================================================================================================

property Series.name[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L702-L751)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#pandas.Series.name "Link to this definition")

Return the name of the Series.

The name of a Series becomes its index or column name if it is used to form a DataFrame. It is also used whenever displaying the Series using the interpreter.

Returns:

label (hashable object)

The name of the Series, also the column name if part of a DataFrame.

See also

[`Series.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename")

Sets the Series name when given a scalar input.

[`Index.name`](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas.Index.name "pandas.Index.name")

Corresponding Index property.

Examples

The Series name can be set initially when calling the constructor.

\>>> s \= pd.Series(\[1, 2, 3\], dtype\=np.int64, name\="Numbers")
\>>> s
0    1
1    2
2    3
Name: Numbers, dtype: int64
\>>> s.name \= "Integers"
\>>> s
0    1
1    2
2    3
Name: Integers, dtype: int64

Copy to clipboard

The name of a Series within a DataFrame is its column name.

\>>> df \= pd.DataFrame(
...     \[\[1, 2\], \[3, 4\], \[5, 6\]\], columns\=\["Odd Numbers", "Even Numbers"\]
... )
\>>> df
   Odd Numbers  Even Numbers
0            1             2
1            3             4
2            5             6
\>>> df\["Even Numbers"\].name
'Even Numbers'

Copy to clipboard

On this page