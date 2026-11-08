[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_values\_for\_factorize[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html#pandas-api-extensions-extensionarray-values-for-factorize "Link to this heading")

================================================================================================================================================================================================================================================================

ExtensionArray.\_values\_for\_factorize()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1777-L1812)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html#pandas.api.extensions.ExtensionArray._values_for_factorize "Link to this definition")

Return an array and missing value suitable for factorization.

This method provides the values and NA sentinel to use in the factorization process. Subclasses may override this to customize the factorization behavior.

Returns:

**values**ndarray

An array suitable for factorization. This should maintain order and be a supported dtype (Float64, Int64, UInt64, String, Object). By default, the extension array is cast to object dtype.

**na\_value**object

The value in values to consider missing. This will be treated as NA in the factorization routines, so it will be coded as \-1 and not included in uniques. By default, `np.nan` is used.

See also

`util.hash_pandas_object`

Hash the pandas object.

Notes

The values returned by this method are also used in [`pandas.util.hash_pandas_object()`](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html#pandas.util.hash_pandas_object "pandas.util.hash_pandas_object")
. If needed, this can be overridden in the `self._hash_pandas_object()` method.

Examples

\>>> pd.array(\[1, 2, 3\]).\_values\_for\_factorize()
(array(\[1, 2, 3\], dtype=object), nan)

Copy to clipboard

On this page