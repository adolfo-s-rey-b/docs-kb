[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.ordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.ordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.ordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.ordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.ordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.ordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.ordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.ordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.ordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.ordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.ordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.ordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.ordered[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html#pandas-series-cat-ordered "Link to this heading")

===========================================================================================================================================================

Series.cat.ordered[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html#pandas.Series.cat.ordered "Link to this definition")

Whether the categories have an ordered relationship.

This property returns True if the categories are ordered, meaning they have a meaningful order that allows comparison operations.

See also

`set_ordered`

Set the ordered attribute.

[`as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_ordered.html#pandas.Series.cat.as_ordered "pandas.Series.cat.as_ordered")

Set the Categorical to be ordered.

[`as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_unordered.html#pandas.Series.cat.as_unordered "pandas.Series.cat.as_unordered")

Set the Categorical to be unordered.

Examples

For [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
:

\>>> ser \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")
\>>> ser.cat.ordered
False

Copy to clipboard

\>>> raw\_cat \= pd.Categorical(\["a", "b", "c", "a"\], ordered\=True)
\>>> ser \= pd.Series(raw\_cat)
\>>> ser.cat.ordered
True

Copy to clipboard

For [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
:

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> cat.ordered
True

Copy to clipboard

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=False)
\>>> cat.ordered
False

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "b"\], ordered\=True)
\>>> ci.ordered
True

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "b"\], ordered\=False)
\>>> ci.ordered
False

Copy to clipboard

On this page