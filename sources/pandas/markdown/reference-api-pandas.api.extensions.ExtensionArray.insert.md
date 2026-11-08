[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.insert.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.insert.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.insert.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.insert[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.insert.html#pandas-api-extensions-extensionarray-insert "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.insert(_loc_, _item_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2653-L2697)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.insert.html#pandas.api.extensions.ExtensionArray.insert "Link to this definition")

Insert an item at the given position.

This method creates a new ExtensionArray with the specified item inserted at the given index. The original array is not modified.

Parameters:

**loc**int

Index where the item needs to be inserted.

**item**scalar-like

Value to be inserted.

Returns:

ExtensionArray

With item inserted at loc.

See also

`Index.insert`

Make new Index inserting new item at location.

Notes

This method should be both type and dtype-preserving. If the item cannot be held in an array of this type/dtype, either ValueError or TypeError should be raised.

The default implementation relies on \_from\_sequence to raise on invalid items.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.insert(2, \-1)
<IntegerArray>
\[1, 2, -1, 3\]
Length: 4, dtype: Int64

Copy to clipboard

On this page