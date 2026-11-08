[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.swaplevel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.swaplevel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.swaplevel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.swaplevel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.swaplevel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.swaplevel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.swaplevel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.swaplevel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.swaplevel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.swaplevel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.swaplevel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.swaplevel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.swaplevel[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas-dataframe-swaplevel "Link to this heading")

==============================================================================================================================================================

DataFrame.swaplevel(_i\=\-2_, _j\=\-1_, _axis\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L9964-L10052)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "Link to this definition")

Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
.

Default is to swap the two innermost levels of the index.

Parameters:

**i, j**int or str

Levels of the indices to be swapped. Can pass level name as string.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to swap levels on. 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.

Returns:

DataFrame

DataFrame with levels swapped in MultiIndex.

See also

[`DataFrame.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "pandas.DataFrame.reorder_levels")

Reorder levels of MultiIndex.

[`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")

Sort MultiIndex.

Examples

\>>> df \= pd.DataFrame(
...     {"Grade": \["A", "B", "A", "C"\]},
...     index\=\[\
...         \["Final exam", "Final exam", "Coursework", "Coursework"\],\
...         \["History", "Geography", "History", "Geography"\],\
...         \["January", "February", "March", "April"\],\
...     \],
... )
\>>> df
                                    Grade
Final exam  History     January      A
            Geography   February     B
Coursework  History     March        A
            Geography   April        C

Copy to clipboard

In the following example, we will swap the levels of the indices. Here, we will swap the levels column-wise, but levels can be swapped row-wise in a similar manner. Note that column-wise is the default behaviour. By not supplying any arguments for i and j, we swap the last and second to last indices.

\>>> df.swaplevel()
                                    Grade
Final exam  January     History         A
            February    Geography       B
Coursework  March       History         A
            April       Geography       C

Copy to clipboard

By supplying one argument, we can choose which index to swap the last index with. We can for example swap the first index with the last one as follows.

\>>> df.swaplevel(0)
                                    Grade
January     History     Final exam      A
February    Geography   Final exam      B
March       History     Coursework      A
April       Geography   Coursework      C

Copy to clipboard

We can also define explicitly which indices we want to swap by supplying values for both i and j. Here, we for example swap the first and second indices.

\>>> df.swaplevel(0, 1)
                                    Grade
History     Final exam  January         A
Geography   Final exam  February        B
History     Coursework  March           A
Geography   Coursework  April           C

Copy to clipboard

On this page