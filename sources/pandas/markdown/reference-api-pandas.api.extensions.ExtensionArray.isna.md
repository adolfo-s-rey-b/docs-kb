[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.isna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.isna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.isna[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isna.html#pandas-api-extensions-extensionarray-isna "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.isna()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L929-L965)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isna.html#pandas.api.extensions.ExtensionArray.isna "Link to this definition")

A 1-D array indicating if each value is missing.

This method returns a boolean array where `True` indicates that the corresponding value is missing (NA/NaN).

Returns:

numpy.ndarray or pandas.api.extensions.ExtensionArray

In most cases, this should return a NumPy ndarray. For exceptional cases like `SparseArray`, where returning an ndarray would be expensive, an ExtensionArray may be returned.

See also

[`ExtensionArray.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html#pandas.api.extensions.ExtensionArray.dropna "pandas.api.extensions.ExtensionArray.dropna")

Return ExtensionArray without NA values.

[`ExtensionArray.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html#pandas.api.extensions.ExtensionArray.fillna "pandas.api.extensions.ExtensionArray.fillna")

Fill NA/NaN values using the specified method.

Notes

If returning an ExtensionArray, then

*   `na_values._is_boolean` should be True
    
*   `na_values` should implement [`ExtensionArray._reduce()`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html#pandas.api.extensions.ExtensionArray._reduce "pandas.api.extensions.ExtensionArray._reduce")
    
*   `na_values` should implement [`ExtensionArray._accumulate()`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html#pandas.api.extensions.ExtensionArray._accumulate "pandas.api.extensions.ExtensionArray._accumulate")
    
*   `na_values.any`, `na_values.all`, `na_values.sum`, and `na_values.__invert__` should be implemented
    

Examples

\>>> arr \= pd.array(\[1, 2, np.nan, np.nan\])
\>>> arr.isna()
array(\[False, False,  True,  True\])

Copy to clipboard

On this page