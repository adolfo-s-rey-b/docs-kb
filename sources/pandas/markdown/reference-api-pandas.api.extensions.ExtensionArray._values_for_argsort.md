[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_values\_for\_argsort[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html#pandas-api-extensions-extensionarray-values-for-argsort "Link to this heading")

==========================================================================================================================================================================================================================================================

ExtensionArray.\_values\_for\_argsort()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L977-L1014)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html#pandas.api.extensions.ExtensionArray._values_for_argsort "Link to this definition")

Return values for sorting.

This method provides the underlying values that should be used when sorting the ExtensionArray. The returned values should maintain the same relative ordering as the original array.

Returns:

ndarray

The transformed values should maintain the ordering between values within the array.

See also

[`ExtensionArray.argsort`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas.api.extensions.ExtensionArray.argsort "pandas.api.extensions.ExtensionArray.argsort")

Return the indices that would sort this array.

Notes

The caller is responsible for _not_ modifying these values in-place, so it is safe for implementers to give views on `self`.

Functions that use this (e.g. `ExtensionArray.argsort`) should ignore entries with missing values in the original array (according to `self.isna()`). This means that the corresponding entries in the returned array don’t need to be modified to sort correctly.

Examples

In most cases, this is the underlying Numpy array of the `ExtensionArray`:

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.\_values\_for\_argsort()
array(\[1, 2, 3\])

Copy to clipboard

On this page