[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ravel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.ravel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.ravel[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ravel.html#pandas-api-extensions-extensionarray-ravel "Link to this heading")

==============================================================================================================================================================================================================

ExtensionArray.ravel(_order\='C'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2278-L2311)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ravel.html#pandas.api.extensions.ExtensionArray.ravel "Link to this definition")

Return a flattened view on this array.

Since ExtensionArrays are 1-dimensional, this method returns the array itself. The `order` parameter is accepted for compatibility with NumPy but is ignored.

Parameters:

**order**{None, ‘C’, ‘F’, ‘A’, ‘K’}, default ‘C’

Returns:

ExtensionArray

A flattened view on the array.

See also

[`ExtensionArray.tolist`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.tolist.html#pandas.api.extensions.ExtensionArray.tolist "pandas.api.extensions.ExtensionArray.tolist")

Return a list of the values.

Notes

*   Because ExtensionArrays are 1D-only, this is a no-op.
    
*   The “order” argument is ignored, is for compatibility with NumPy.
    

Examples

\>>> pd.array(\[1, 2, 3\]).ravel()
<IntegerArray>
\[1, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

On this page