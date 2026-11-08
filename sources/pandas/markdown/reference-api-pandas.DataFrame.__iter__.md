[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.__iter__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.__iter__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.__iter__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.__iter__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.__iter__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.__iter__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.__iter__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.__iter__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.__iter__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.__iter__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.__iter__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.__iter__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.\_\_iter\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html#pandas-dataframe-iter "Link to this heading")

===========================================================================================================================================================

DataFrame.\_\_iter\_\_()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1824-L1850)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html#pandas.DataFrame.__iter__ "Link to this definition")

Iterate over info axis.

For a DataFrame this yields column names (labels); for a Series it yields the single name. Enables iteration over the object with `for col in df`.

Returns:

iterator

Info axis as iterator.

See also

[`DataFrame.items`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "pandas.DataFrame.items")

Iterate over (column name, Series) pairs.

[`DataFrame.itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")

Iterate over DataFrame rows as namedtuples.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[4, 5, 6\]})
\>>> for x in df:
...     print(x)
A
B

Copy to clipboard

On this page