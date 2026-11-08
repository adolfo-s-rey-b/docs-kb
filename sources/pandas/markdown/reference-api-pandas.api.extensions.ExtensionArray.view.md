[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.view.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.view.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.view.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.view[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.view.html#pandas-api-extensions-extensionarray-view "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.view(_dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2112-L2156)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.view.html#pandas.api.extensions.ExtensionArray.view "Link to this definition")

Return a view on the array.

This method returns a new object referencing the same underlying data, without copying. Modifications to either the view or the original array will be reflected in both.

Parameters:

**dtype**str, np.dtype, or ExtensionDtype, optional

Default None.

Returns:

ExtensionArray or np.ndarray

A view on the [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
’s data.

See also

`api.extensions.ExtensionArray.ravel`

Return a flattened view on input array.

`Index.view`

Equivalent function for Index.

`ndarray.view`

New view of array with the same data.

Examples

This gives view on the underlying data of an `ExtensionArray` and is not a copy. Modifications on either the view or the original `ExtensionArray` will be reflected on the underlying data:

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr2 \= arr.view()
\>>> arr\[0\] \= 2
\>>> arr2
<IntegerArray>
\[2, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

On this page