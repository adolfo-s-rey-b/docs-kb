[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.nbytes[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html#pandas-api-extensions-extensionarray-nbytes "Link to this heading")

=================================================================================================================================================================================================================

property ExtensionArray.nbytes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L810-L830)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html#pandas.api.extensions.ExtensionArray.nbytes "Link to this definition")

The number of bytes needed to store this object in memory.

If computing this is expensive, implementations may return an approximate lower bound on the number of bytes needed.

See also

[`ExtensionArray.shape`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shape.html#pandas.api.extensions.ExtensionArray.shape "pandas.api.extensions.ExtensionArray.shape")

Return a tuple of the array dimensions.

`ExtensionArray.size`

The number of elements in the array.

Examples

\>>> pd.array(\[1, 2, 3\]).nbytes
27

Copy to clipboard

On this page