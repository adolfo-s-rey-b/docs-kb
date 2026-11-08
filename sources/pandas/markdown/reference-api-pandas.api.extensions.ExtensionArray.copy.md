[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.copy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.copy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.copy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.copy.html#pandas-api-extensions-extensionarray-copy "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.copy()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2076-L2104)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.copy.html#pandas.api.extensions.ExtensionArray.copy "Link to this definition")

Return a copy of the array.

This method creates a copy of the ExtensionArray where modifying the data in the copy will not affect the original array. This is useful when you want to manipulate data without altering the original dataset.

Returns:

ExtensionArray

A new ExtensionArray object that is a copy of the current instance.

See also

`DataFrame.copy`

Return a copy of the DataFrame.

`Series.copy`

Return a copy of the Series.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr2 \= arr.copy()
\>>> arr\[0\] \= 2
\>>> arr2
<IntegerArray>
\[1, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

On this page