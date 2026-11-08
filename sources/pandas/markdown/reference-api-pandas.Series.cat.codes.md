[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.codes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.codes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.codes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.codes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.codes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.codes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.codes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.codes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.codes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.codes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.codes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.codes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.codes[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html#pandas-series-cat-codes "Link to this heading")

=====================================================================================================================================================

Series.cat.codes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L3219-L3247)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html#pandas.Series.cat.codes "Link to this definition")

Return Series of codes as well as the index.

The codes are integer indicators for the position of each value in the categories. Uncategorized values (i.e., NaN) are assigned a code of `-1`.

See also

[`Series.cat.categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html#pandas.Series.cat.categories "pandas.Series.cat.categories")

Return the categories of this categorical.

[`Series.cat.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_ordered.html#pandas.Series.cat.as_ordered "pandas.Series.cat.as_ordered")

Set the Categorical to be ordered.

[`Series.cat.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_unordered.html#pandas.Series.cat.as_unordered "pandas.Series.cat.as_unordered")

Set the Categorical to be unordered.

Examples

\>>> raw\_cate \= pd.Categorical(\["a", "b", None, "a"\], categories\=\["a", "b"\])
\>>> ser \= pd.Series(raw\_cate)
\>>> ser.cat.codes
0   0
1   1
2  -1
3   0
dtype: int8

Copy to clipboard

On this page