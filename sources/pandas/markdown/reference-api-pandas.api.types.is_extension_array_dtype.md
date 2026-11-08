[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_extension_array_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_extension_array_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_extension_array_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_extension_array_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_extension_array_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_extension_array_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_extension_array_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_extension_array_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_extension_array_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_extension\_array\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_extension_array_dtype.html#pandas-api-types-is-extension-array-dtype "Link to this heading")

==============================================================================================================================================================================================================

pandas.api.types.is\_extension\_array\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1580-L1644)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_extension_array_dtype.html#pandas.api.types.is_extension_array_dtype "Link to this definition")

Check if an object is a pandas extension array type.

See the [Use Guide](https://pandas.pydata.org/docs/development/extending.html#extending-extension-types)
 for more.

Parameters:

**arr\_or\_dtype**object

For array-like input, the `.dtype` attribute will be extracted.

Returns:

bool

Whether the arr\_or\_dtype is an extension array type.

See also

`api.extensions.ExtensionArray`

Abstract base class for pandas extension arrays.

Notes

This checks whether an object implements the pandas extension array interface. In pandas, this includes:

*   Categorical
    
*   Sparse
    
*   Interval
    
*   Period
    
*   DatetimeArray
    
*   TimedeltaArray
    

Third-party libraries may implement arrays or types satisfying this interface as well.

Examples

\>>> from pandas.api.types import is\_extension\_array\_dtype
\>>> arr \= pd.Categorical(\["a", "b"\])
\>>> is\_extension\_array\_dtype(arr)
True
\>>> is\_extension\_array\_dtype(arr.dtype)
True

Copy to clipboard

\>>> arr \= np.array(\["a", "b"\])
\>>> is\_extension\_array\_dtype(arr.dtype)
False

Copy to clipboard

On this page