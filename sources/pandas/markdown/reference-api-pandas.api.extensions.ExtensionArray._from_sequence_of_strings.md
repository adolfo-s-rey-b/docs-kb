[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_from\_sequence\_of\_strings[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html#pandas-api-extensions-extensionarray-from-sequence-of-strings "Link to this heading")

=============================================================================================================================================================================================================================================================================

classmethod ExtensionArray.\_from\_sequence\_of\_strings(_strings_, _\*_, _dtype_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L337-L379)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html#pandas.api.extensions.ExtensionArray._from_sequence_of_strings "Link to this definition")

Construct a new ExtensionArray from a sequence of strings.

This method is used to parse string data into the appropriate scalar type for the ExtensionArray. It is commonly used when reading data from text files via parsers like `read_csv`.

Parameters:

**strings**Sequence

Each element will be an instance of the scalar type for this array, `cls.dtype.type`.

**dtype**ExtensionDtype

Construct for this particular dtype. This should be a Dtype compatible with the ExtensionArray.

**copy**bool, default False

If True, copy the underlying data.

Returns:

ExtensionArray

See also

`api.extensions.ExtensionArray._from_sequence`

Construct a new ExtensionArray from a sequence of scalars.

`api.extensions.ExtensionArray._from_factorized`

Reconstruct an ExtensionArray after factorization.

Examples

\>>> pd.arrays.IntegerArray.\_from\_sequence\_of\_strings(
...     \["1", "2", "3"\], dtype\=pd.Int64Dtype()
... )
<IntegerArray>
\[1, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

On this page