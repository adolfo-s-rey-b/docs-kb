[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.at.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.at.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.at.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.at.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.at.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.at.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.at.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.at.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.at.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.at.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.at.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.at.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.at[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas-series-at "Link to this heading")

================================================================================================================================

property Series.at[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexing.py#L698-L764)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas.Series.at "Link to this definition")

Access a single value for a row/column label pair.

Similar to `loc`, in that both provide label-based lookups. Use `at` if you only need to get or set a single value in a DataFrame or Series.

Raises:

KeyError

If getting a value and ‘label’ does not exist in a DataFrame or Series.

ValueError

If row/column label pair is not a tuple or if any label from the pair is not a scalar for DataFrame. If label is list-like (_excluding_ NamedTuple) for Series.

See also

[`DataFrame.at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")

Access a single value for a row/column pair by label.

[`DataFrame.iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat")

Access a single value for a row/column pair by integer position.

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Access a group of rows and columns by label(s).

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Access a group of rows and columns by integer position(s).

[`Series.at`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas.Series.at "pandas.Series.at")

Access a single value by label.

[`Series.iat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas.Series.iat "pandas.Series.iat")

Access a single value by integer position.

[`Series.loc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas.Series.loc "pandas.Series.loc")

Access a group of rows by label(s).

[`Series.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "pandas.Series.iloc")

Access a group of rows by integer position(s).

Notes

See [Fast scalar value getting and setting](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-basics-get-value)
 for more details.

Examples

\>>> df \= pd.DataFrame(
...     \[\[0, 2, 3\], \[0, 4, 1\], \[10, 20, 30\]\],
...     index\=\[4, 5, 6\],
...     columns\=\["A", "B", "C"\],
... )
\>>> df
    A   B   C
4   0   2   3
5   0   4   1
6  10  20  30

Copy to clipboard

Get value at specified row/column pair

\>>> df.at\[4, "B"\]
2

Copy to clipboard

Set value at specified row/column pair

\>>> df.at\[4, "B"\] \= 10
\>>> df.at\[4, "B"\]
10

Copy to clipboard

Get value within a Series

\>>> df.loc\[5\].at\["B"\]
4

Copy to clipboard

On this page