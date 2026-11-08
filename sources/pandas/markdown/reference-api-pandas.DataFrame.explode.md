[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.explode[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas-dataframe-explode "Link to this heading")

========================================================================================================================================================

DataFrame.explode(_column_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14394-L14524)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "Link to this definition")

Transform each element of a list-like to a row, replicating index values.

This method is useful for expanding nested data structures like lists into separate rows while maintaining the relationship with other columns.

Parameters:

**column**IndexLabel

Column(s) to explode. For multiple columns, specify a non-empty list with each element be str or tuple, and all specified columns their list-like data on same row of the frame must have matching length.

**ignore\_index**bool, default False

If True, the resulting index will be labeled 0, 1, …, n - 1.

Returns:

DataFrame

Exploded lists to rows of the subset columns; index will be duplicated for these rows.

Raises:

ValueError

*   If columns of the frame are not unique.
    
*   If specified columns to explode is empty list.
    
*   If specified columns to explode have not matching count of elements rowwise in the frame.
    

See also

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Pivot a level of the (necessarily hierarchical) index labels.

[`DataFrame.melt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas.DataFrame.melt "pandas.DataFrame.melt")

Unpivot a DataFrame from wide format to long format.

[`Series.explode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas.Series.explode "pandas.Series.explode")

Explode a DataFrame from list-like columns to long format.

Notes

This routine will explode list-likes including lists, tuples, sets, Series, and np.ndarray. The result dtype of the subset rows will be object. Scalars will be returned unchanged, and empty list-likes will result in a np.nan for that row. In addition, the ordering of rows in the output will be non-deterministic when exploding sets.

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-explode)
 for more examples.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "A": \[\[0, 1, 2\], "foo", \[\], \[3, 4\]\],
...         "B": 1,
...         "C": \[\["a", "b", "c"\], np.nan, \[\], \["d", "e"\]\],
...     }
... )
\>>> df
           A  B          C
0  \[0, 1, 2\]  1  \[a, b, c\]
1        foo  1        NaN
2         \[\]  1         \[\]
3     \[3, 4\]  1     \[d, e\]

Copy to clipboard

Single-column explode.

\>>> df.explode("A")
     A  B          C
0    0  1  \[a, b, c\]
0    1  1  \[a, b, c\]
0    2  1  \[a, b, c\]
1  foo  1        NaN
2  NaN  1         \[\]
3    3  1     \[d, e\]
3    4  1     \[d, e\]

Copy to clipboard

Multi-column explode.

\>>> df.explode(list("AC"))
     A  B    C
0    0  1    a
0    1  1    b
0    2  1    c
1  foo  1  NaN
2  NaN  1  NaN
3    3  1    d
3    4  1    e

Copy to clipboard

On this page