[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.unique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.unique.html#pandas-api-typing-seriesgroupby-unique "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.unique()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L2026-L2071)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.unique.html#pandas.api.typing.SeriesGroupBy.unique "Link to this definition")

Return unique values for each group.

It returns unique values for each of the grouped values. Returned in order of appearance. Hash table-based unique, therefore does NOT sort.

Returns:

Series

Unique values for each of the grouped values.

See also

`Series.unique`

Return unique values of Series object.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         ("Chihuahua", "dog", 6.1),\
...         ("Beagle", "dog", 15.2),\
...         ("Chihuahua", "dog", 6.9),\
...         ("Persian", "cat", 9.2),\
...         ("Chihuahua", "dog", 7),\
...         ("Persian", "cat", 8.8),\
...     \],
...     columns\=\["breed", "animal", "height\_in"\],
... )
\>>> df
       breed     animal   height\_in
0  Chihuahua        dog         6.1
1     Beagle        dog        15.2
2  Chihuahua        dog         6.9
3    Persian        cat         9.2
4  Chihuahua        dog         7.0
5    Persian        cat         8.8
\>>> ser \= df.groupby("animal")\["breed"\].unique()
\>>> ser
animal
cat              \[Persian\]
dog    \[Chihuahua, Beagle\]
Name: breed, dtype: object

Copy to clipboard

On this page