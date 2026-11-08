[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.swaplevel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.swaplevel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.swaplevel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.swaplevel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.swaplevel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.swaplevel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.swaplevel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.swaplevel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.swaplevel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.swaplevel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.swaplevel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.swaplevel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.swaplevel[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#pandas-series-swaplevel "Link to this heading")

=====================================================================================================================================================

Series.swaplevel(_i\=\-2_, _j\=\-1_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4734-L4825)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#pandas.Series.swaplevel "Link to this definition")

Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
.

Default is to swap the two innermost levels of the index.

Parameters:

**i, j**int or str

Levels of the indices to be swapped. Can pass level name as string.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

Series

Series with levels swapped in MultiIndex.

See also

[`DataFrame.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "pandas.DataFrame.swaplevel")

Swap levels i and j in a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
.

[`Series.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#pandas.Series.reorder_levels "pandas.Series.reorder_levels")

Rearrange index levels using input order.

[`MultiIndex.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "pandas.MultiIndex.swaplevel")

Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
.

Examples

\>>> s \= pd.Series(
...     \["A", "B", "A", "C"\],
...     index\=\[\
...         \["Final exam", "Final exam", "Coursework", "Coursework"\],\
...         \["History", "Geography", "History", "Geography"\],\
...         \["January", "February", "March", "April"\],\
...     \],
... )
\>>> s
Final exam  History    January     A
            Geography  February    B
Coursework  History    March       A
            Geography  April       C
dtype: str

Copy to clipboard

In the following example, we will swap the levels of the indices. Here, we will swap the levels column-wise, but levels can be swapped row-wise in a similar manner. Note that column-wise is the default behavior. By not supplying any arguments for i and j, we swap the last and second to last indices.

\>>> s.swaplevel()
Final exam  January   History       A
            February  Geography     B
Coursework  March     History       A
            April     Geography     C
dtype: str

Copy to clipboard

By supplying one argument, we can choose which index to swap the last index with. We can for example swap the first index with the last one as follows.

\>>> s.swaplevel(0)
January     History     Final exam      A
February    Geography   Final exam      B
March       History     Coursework      A
April       Geography   Coursework      C
dtype: str

Copy to clipboard

We can also define explicitly which indices we want to swap by supplying values for both i and j. Here, we for example swap the first and second indices.

\>>> s.swaplevel(0, 1)
History     Final exam  January         A
Geography   Final exam  February        B
History     Coursework  March           A
Geography   Coursework  April           C
dtype: str

Copy to clipboard

On this page