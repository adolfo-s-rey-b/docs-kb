[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._hash_pandas_object.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_hash\_pandas\_object[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._hash_pandas_object.html#pandas-api-extensions-extensionarray-hash-pandas-object "Link to this heading")

==========================================================================================================================================================================================================================================================

ExtensionArray.\_hash\_pandas\_object(_\*_, _encoding_, _hash\_key_, _categorize_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2542-L2583)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._hash_pandas_object.html#pandas.api.extensions.ExtensionArray._hash_pandas_object "Link to this definition")

Hook for hash\_pandas\_object.

Default is to use the values returned by \_values\_for\_factorize.

Parameters:

**encoding**str

Encoding for data & key when strings.

**hash\_key**str

Hash\_key for string key to encode.

**categorize**bool

Whether to first categorize object arrays before hashing. This is more efficient when the array contains duplicate values.

Returns:

np.ndarray\[uint64\]

An array of hashed values.

See also

`api.extensions.ExtensionArray._values_for_factorize`

Return an array and missing value suitable for factorization.

`util.hash_array`

Given a 1d array, return an array of hashed values.

Examples

\>>> pd.array(\[1, 2\]).\_hash\_pandas\_object(
...     encoding\="utf-8", hash\_key\="1000000000000000", categorize\=False
... )
array(\[ 6238072747940578789, 15839785061582574730\], dtype=uint64)

Copy to clipboard

On this page