[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.explode.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.explode.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.explode.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.explode.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.explode.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.explode.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.explode.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.explode.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.explode.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.explode.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.explode.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.explode.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.explode[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas-series-explode "Link to this heading")

===============================================================================================================================================

Series.explode(_ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4880-L4950)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas.Series.explode "Link to this definition")

Transform each element of a list-like to a row.

This method expands list-like elements so that each item in the list gets its own row, while non-list-like elements remain unchanged. The index is duplicated for the expanded rows.

Parameters:

**ignore\_index**bool, default False

If True, the resulting index will be labeled 0, 1, …, n - 1.

Returns:

Series

Exploded lists to rows; index will be duplicated for these rows.

See also

[`Series.str.split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")

Split string values on specified separator.

[`Series.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#pandas.Series.unstack "pandas.Series.unstack")

Unstack, a.k.a. pivot, Series with MultiIndex to produce DataFrame.

[`DataFrame.melt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas.DataFrame.melt "pandas.DataFrame.melt")

Unpivot a DataFrame from wide format to long format.

[`DataFrame.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "pandas.DataFrame.explode")

Explode a DataFrame from list-like columns to long format.

Notes

This routine will explode list-likes including lists, tuples, sets, Series, and np.ndarray. The result dtype of the subset rows will be object. Scalars will be returned unchanged, and empty list-likes will result in an np.nan for that row. In addition, the ordering of elements in the output will be non-deterministic when exploding sets.

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-explode)
 for more examples.

Examples

\>>> s \= pd.Series(\[\[1, 2, 3\], "foo", \[\], \[3, 4\]\])
\>>> s
0    \[1, 2, 3\]
1          foo
2           \[\]
3       \[3, 4\]
dtype: object

Copy to clipboard

\>>> s.explode()
0      1
0      2
0      3
1    foo
2    NaN
3      3
3      4
dtype: object

Copy to clipboard

On this page