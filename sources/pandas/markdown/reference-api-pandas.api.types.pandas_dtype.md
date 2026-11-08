[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.pandas_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.pandas_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.pandas_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.pandas_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.pandas_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.pandas_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.pandas_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.pandas_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.pandas_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.pandas_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.pandas_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.pandas_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.pandas_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.pandas_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.pandas\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.pandas_dtype.html#pandas-api-types-pandas-dtype "Link to this heading")

========================================================================================================================================================================

pandas.api.types.pandas\_dtype(_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1831-L1923)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.pandas_dtype.html#pandas.api.types.pandas_dtype "Link to this definition")

Convert input into a pandas only dtype object or a numpy dtype object.

This function first checks for pandas extension types registered in the dtype registry, then falls back to NumPy dtype resolution. It accepts strings, types, numpy dtypes, and pandas ExtensionDtype instances.

Parameters:

**dtype**object

The object to be converted into a dtype.

Returns:

np.dtype or a pandas dtype

The converted dtype, which can be either a numpy dtype or a pandas dtype.

Raises:

TypeError if not a dtype

See also

`api.types.is_dtype`

Return true if the condition is satisfied for the arr\_or\_dtype.

Examples

\>>> pd.api.types.pandas\_dtype(int)
dtype('int64')

Copy to clipboard

On this page