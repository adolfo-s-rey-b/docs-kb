[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_accumulate[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html#pandas-api-extensions-extensionarray-accumulate "Link to this heading")

================================================================================================================================================================================================================================

ExtensionArray.\_accumulate(_name_, _\*_, _skipna\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2365-L2412)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html#pandas.api.extensions.ExtensionArray._accumulate "Link to this definition")

Return an ExtensionArray performing an accumulation operation.

The underlying data type might change.

Parameters:

**name**str

Name of the function, supported values are: - cummin - cummax - cumsum - cumprod

**skipna**bool, default True

If True, skip NA values.

**\*\*kwargs**

Additional keyword arguments passed to the accumulation function. Currently, there is no supported kwarg.

Returns:

array

An array performing the accumulation operation.

Raises:

**NotImplementedError**subclass does not define accumulations

See also

`api.extensions.ExtensionArray._concat_same_type`

Concatenate multiple array of this dtype.

`api.extensions.ExtensionArray.view`

Return a view on the array.

`api.extensions.ExtensionArray._explode`

Transform each element of list-like to a row.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.\_accumulate(name\="cumsum")
<IntegerArray>
\[1, 3, 6\]
Length: 3, dtype: Int64

Copy to clipboard

On this page