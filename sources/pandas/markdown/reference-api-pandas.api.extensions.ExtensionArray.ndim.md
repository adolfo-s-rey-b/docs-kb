[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ndim.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.ndim.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.ndim[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ndim.html#pandas-api-extensions-extensionarray-ndim "Link to this heading")

===========================================================================================================================================================================================================

property ExtensionArray.ndim[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L789-L808)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ndim.html#pandas.api.extensions.ExtensionArray.ndim "Link to this definition")

Extension Arrays are only allowed to be 1-dimensional.

This property always returns 1 for ExtensionArrays, as they are constrained to a single dimension by design.

See also

[`ExtensionArray.shape`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shape.html#pandas.api.extensions.ExtensionArray.shape "pandas.api.extensions.ExtensionArray.shape")

Return a tuple of the array dimensions.

`ExtensionArray.size`

The number of elements in the array.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.ndim
1

Copy to clipboard

On this page