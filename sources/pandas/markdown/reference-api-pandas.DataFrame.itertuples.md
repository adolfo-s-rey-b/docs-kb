[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.itertuples.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.itertuples.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.itertuples.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.itertuples.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.itertuples.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.itertuples.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.itertuples.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.itertuples.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.itertuples.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.itertuples.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.itertuples.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.itertuples.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.itertuples[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas-dataframe-itertuples "Link to this heading")

=================================================================================================================================================================

DataFrame.itertuples(_index\=True_, _name\='Pandas'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1376-L1468)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "Link to this definition")

Iterate over DataFrame rows as namedtuples.

Each row becomes a namedtuple (or plain tuple if `name` is None) with field names taken from the column names or positional names. Generally faster and more type-stable than [`iterrows()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "pandas.DataFrame.iterrows")
.

Parameters:

**index**bool, default True

If True, return the index as the first element of the tuple.

**name**str or None, default “Pandas”

The name of the returned namedtuples or None to return regular tuples.

Returns:

iterator

An object to iterate over namedtuples for each row in the DataFrame with the first field possibly being the index and following fields being the column values.

See also

[`DataFrame.iterrows`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "pandas.DataFrame.iterrows")

Iterate over DataFrame rows as (index, Series) pairs.

[`DataFrame.items`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "pandas.DataFrame.items")

Iterate over (column name, Series) pairs.

Notes

The column names will be renamed to positional names if they are invalid Python identifiers, repeated, or start with an underscore.

Examples

\>>> df \= pd.DataFrame(
...     {"num\_legs": \[4, 2\], "num\_wings": \[0, 2\]}, index\=\["dog", "hawk"\]
... )
\>>> df
      num\_legs  num\_wings
dog          4          0
hawk         2          2
\>>> for row in df.itertuples():
...     print(row)
Pandas(Index='dog', num\_legs=4, num\_wings=0)
Pandas(Index='hawk', num\_legs=2, num\_wings=2)

Copy to clipboard

By setting the index parameter to False we can remove the index as the first element of the tuple:

\>>> for row in df.itertuples(index\=False):
...     print(row)
Pandas(num\_legs=4, num\_wings=0)
Pandas(num\_legs=2, num\_wings=2)

Copy to clipboard

With the name parameter set we set a custom name for the yielded namedtuples:

\>>> for row in df.itertuples(name\="Animal"):
...     print(row)
Animal(Index='dog', num\_legs=4, num\_wings=0)
Animal(Index='hawk', num\_legs=2, num\_wings=2)

Copy to clipboard

On this page