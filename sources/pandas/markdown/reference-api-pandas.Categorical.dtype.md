[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html#pandas-categorical-dtype "Link to this heading")

========================================================================================================================================================

property Categorical.dtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L527-L549)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html#pandas.Categorical.dtype "Link to this definition")

The `CategoricalDtype` for this instance.

This property returns the CategoricalDtype which contains information about the categories and whether the categorical is ordered.

See also

`astype`

Cast argument to a specified dtype.

[`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")

Type for categorical data.

Examples

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> cat
\['a', 'b'\]
Categories (2, str): \['a' < 'b'\]
\>>> cat.dtype
CategoricalDtype(categories=\['a', 'b'\], ordered=True, categories\_dtype=str)

Copy to clipboard

On this page