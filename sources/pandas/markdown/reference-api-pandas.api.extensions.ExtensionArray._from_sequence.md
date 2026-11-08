[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_from\_sequence[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html#pandas-api-extensions-extensionarray-from-sequence "Link to this heading")

==========================================================================================================================================================================================================================================

classmethod ExtensionArray.\_from\_sequence(_scalars_, _\*_, _dtype\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L295-L335)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html#pandas.api.extensions.ExtensionArray._from_sequence "Link to this definition")

Construct a new ExtensionArray from a sequence of scalars.

This is a required method for ExtensionArray subclasses. It is used to create a new instance of the ExtensionArray from Python scalars or objects that can be converted to the array’s scalar type.

Parameters:

**scalars**Sequence

Each element will be an instance of the scalar type for this array, `cls.dtype.type` or be converted into this type in this method.

**dtype**dtype, optional

Construct for this particular dtype. This should be a Dtype compatible with the ExtensionArray.

**copy**bool, default False

If True, copy the underlying data.

Returns:

ExtensionArray

See also

`api.extensions.ExtensionArray._from_sequence_of_strings`

Construct a new ExtensionArray from a sequence of strings.

`api.extensions.ExtensionArray._hash_pandas_object`

Hook for hash\_pandas\_object.

Examples

\>>> pd.arrays.IntegerArray.\_from\_sequence(\[4, 5\])
<IntegerArray>
\[4, 5\]
Length: 2, dtype: Int64

Copy to clipboard

On this page