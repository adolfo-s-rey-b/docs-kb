[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_concat\_same\_type[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html#pandas-api-extensions-extensionarray-concat-same-type "Link to this heading")

====================================================================================================================================================================================================================================================

classmethod ExtensionArray.\_concat\_same\_type(_to\_concat_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2313-L2354)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html#pandas.api.extensions.ExtensionArray._concat_same_type "Link to this definition")

Concatenate multiple arrays of this dtype.

This method joins a sequence of ExtensionArrays of the same dtype into a single ExtensionArray. All arrays in the sequence must have the same dtype.

Parameters:

**to\_concat**sequence of this type

An array of the same dtype to concatenate.

Returns:

ExtensionArray

See also

`api.extensions.ExtensionArray._explode`

Transform each element of list-like to a row.

`api.extensions.ExtensionArray._formatter`

Formatting function for scalar values.

`api.extensions.ExtensionArray._from_factorized`

Reconstruct an ExtensionArray after factorization.

Examples

\>>> arr1 \= pd.array(\[1, 2, 3\])
\>>> arr2 \= pd.array(\[4, 5, 6\])
\>>> pd.arrays.IntegerArray.\_concat\_same\_type(\[arr1, arr2\])
<IntegerArray>
\[1, 2, 3, 4, 5, 6\]
Length: 6, dtype: Int64

Copy to clipboard

On this page