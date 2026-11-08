[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalDtype.ordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalDtype.ordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalDtype.ordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalDtype.ordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalDtype.ordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalDtype.ordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalDtype.ordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalDtype.ordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalDtype.ordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalDtype.ordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalDtype.ordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalDtype.ordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalDtype.ordered[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html#pandas-categoricaldtype-ordered "Link to this heading")

=============================================================================================================================================================================

property CategoricalDtype.ordered[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L656-L678)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html#pandas.CategoricalDtype.ordered "Link to this definition")

Whether the categories have an ordered relationship.

When `True`, comparison operations on the resulting Categorical are valid and sort in the order of the categories.

See also

[`categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.categories.html#pandas.CategoricalDtype.categories "pandas.CategoricalDtype.categories")

An Index containing the unique categories allowed.

Examples

\>>> cat\_type \= pd.CategoricalDtype(categories\=\["a", "b"\], ordered\=True)
\>>> cat\_type.ordered
True

Copy to clipboard

\>>> cat\_type \= pd.CategoricalDtype(categories\=\["a", "b"\], ordered\=False)
\>>> cat\_type.ordered
False

Copy to clipboard

On this page