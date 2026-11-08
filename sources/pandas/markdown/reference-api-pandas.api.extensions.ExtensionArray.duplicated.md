[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.duplicated[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html#pandas-api-extensions-extensionarray-duplicated "Link to this heading")

=============================================================================================================================================================================================================================

ExtensionArray.duplicated(_keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1500-L1535)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html#pandas.api.extensions.ExtensionArray.duplicated "Link to this definition")

Return boolean ndarray denoting duplicate values.

This method identifies duplicate values in the array. The keep parameter controls which occurrences are marked as duplicates.

Parameters:

**keep**{‘first’, ‘last’, False}, default ‘first’

*   `first` : Mark duplicates as `True` except for the first occurrence.
    
*   `last` : Mark duplicates as `True` except for the last occurrence.
    
*   False : Mark all duplicates as `True`.
    

Returns:

ndarray\[bool\]

With true in indices where elements are duplicated and false otherwise.

See also

`DataFrame.duplicated`

Return boolean Series denoting duplicate rows.

`Series.duplicated`

Indicate duplicate Series values.

`api.extensions.ExtensionArray.unique`

Compute the ExtensionArray of unique values.

Examples

\>>> pd.array(\[1, 1, 2, 3, 3\], dtype\="Int64").duplicated()
array(\[False,  True, False, False,  True\])

Copy to clipboard

On this page