[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.items[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas-dataframe-items "Link to this heading")

==================================================================================================================================================

DataFrame.items()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1264-L1316)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "Link to this definition")

Iterate over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with the column name and the content as a Series.

Yields:

**label**object

The column names for the DataFrame being iterated over.

**content**Series

The column entries belonging to each label, as a Series.

See also

[`DataFrame.iterrows`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "pandas.DataFrame.iterrows")

Iterate over DataFrame rows as (index, Series) pairs.

[`DataFrame.itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")

Iterate over DataFrame rows as namedtuples of the values.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "species": \["bear", "bear", "marsupial"\],
...         "population": \[1864, 22000, 80000\],
...     },
...     index\=\["panda", "polar", "koala"\],
... )
\>>> df
        species   population
panda   bear      1864
polar   bear      22000
koala   marsupial 80000
\>>> for label, content in df.items():
...     print(f"label: {label}")
...     print(f"content: {content}", sep\="\\n")
label: species
content:
panda         bear
polar         bear
koala    marsupial
Name: species, dtype: str
label: population
content:
panda     1864
polar    22000
koala    80000
Name: population, dtype: int64

Copy to clipboard

On this page