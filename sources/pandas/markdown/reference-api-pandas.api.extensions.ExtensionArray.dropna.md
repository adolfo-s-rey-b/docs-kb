[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.dropna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.dropna[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html#pandas-api-extensions-extensionarray-dropna "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.dropna()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1470-L1498)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html#pandas.api.extensions.ExtensionArray.dropna "Link to this definition")

Return ExtensionArray without NA values.

This method removes all missing values from the array, returning a new ExtensionArray containing only non-NA values.

Returns:

Self

An ExtensionArray of the same type as the original but with all NA values removed.

See also

`Series.dropna`

Remove missing values from a Series.

`DataFrame.dropna`

Remove missing values from a DataFrame.

`api.extensions.ExtensionArray.isna`

Check for missing values in an ExtensionArray.

Examples

\>>> pd.array(\[1, 2, np.nan\]).dropna()
<IntegerArray>
\[1, 2\]
Length: 2, dtype: Int64

Copy to clipboard

On this page