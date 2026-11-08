[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.register_extension_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.register_extension_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.register_extension_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.register_extension_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.register_extension_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.register_extension_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.register_extension_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.register\_extension\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html#pandas-api-extensions-register-extension-dtype "Link to this heading")

============================================================================================================================================================================================================================

pandas.api.extensions.register\_extension\_dtype(_cls_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L533-L570)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html#pandas.api.extensions.register_extension_dtype "Link to this definition")

Register an ExtensionType with pandas as class decorator.

This enables operations like `.astype(name)` for the name of the ExtensionDtype.

Returns:

callable

A class decorator.

See also

`api.extensions.ExtensionDtype`

The base class for creating custom pandas data types.

`Series`

One-dimensional array with axis labels.

`DataFrame`

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Examples

\>>> from pandas.api.extensions import register\_extension\_dtype, ExtensionDtype
\>>> @register\_extension\_dtype
... class MyExtensionDtype(ExtensionDtype):
...     name \= "myextension"

Copy to clipboard

On this page