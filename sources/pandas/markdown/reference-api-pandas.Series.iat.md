[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.iat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.iat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.iat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.iat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.iat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.iat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.iat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.iat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.iat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.iat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.iat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.iat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.iat[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas-series-iat "Link to this heading")

===================================================================================================================================

property Series.iat[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexing.py#L766-L813)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas.Series.iat "Link to this definition")

Access a single value for a row/column pair by integer position.

Similar to `iloc`, in that both provide integer-based lookups. Use `iat` if you only need to get or set a single value in a DataFrame or Series.

Raises:

IndexError

When integer position is out of bounds.

See also

[`DataFrame.at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")

Access a single value for a row/column label pair.

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Access a group of rows and columns by label(s).

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Access a group of rows and columns by integer position(s).

Examples

\>>> df \= pd.DataFrame(
...     \[\[0, 2, 3\], \[0, 4, 1\], \[10, 20, 30\]\], columns\=\["A", "B", "C"\]
... )
\>>> df
    A   B   C
0   0   2   3
1   0   4   1
2  10  20  30

Copy to clipboard

Get value at specified row/column pair

\>>> df.iat\[1, 2\]
1

Copy to clipboard

Set value at specified row/column pair

\>>> df.iat\[1, 2\] \= 10
\>>> df.iat\[1, 2\]
10

Copy to clipboard

Get value within a series

\>>> df.loc\[0\].iat\[1\]
2

Copy to clipboard

On this page