[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.unique.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.unique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.unique.html#pandas-api-extensions-extensionarray-unique "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.unique()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1604-L1632)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.unique.html#pandas.api.extensions.ExtensionArray.unique "Link to this definition")

Compute the ExtensionArray of unique values.

This method returns a new ExtensionArray containing the distinct values from the original array, preserving the order of first appearance.

Returns:

pandas.api.extensions.ExtensionArray

With unique values from the input array.

See also

`Index.unique`

Return unique values in the index.

`Series.unique`

Return unique values of Series object.

[`unique`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.unique.html#pandas.api.extensions.ExtensionArray.unique "pandas.api.extensions.ExtensionArray.unique")

Return unique values based on a hash table.

Examples

\>>> arr \= pd.array(\[1, 2, 3, 1, 2, 3\])
\>>> arr.unique()
<IntegerArray>
\[1, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

On this page