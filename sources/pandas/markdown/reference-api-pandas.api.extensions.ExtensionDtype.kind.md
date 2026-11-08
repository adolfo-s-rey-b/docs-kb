[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.kind.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionDtype.kind.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionDtype.kind[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.kind.html#pandas-api-extensions-extensiondtype-kind "Link to this heading")

===========================================================================================================================================================================================================

property ExtensionDtype.kind[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L198-L212)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.kind.html#pandas.api.extensions.ExtensionDtype.kind "Link to this definition")

A character code (one of ‘biufcmMOSUV’), default ‘O’

This should match the NumPy dtype used when the array is converted to an ndarray, which is probably ‘O’ for object if the extension type cannot be represented as a built-in NumPy type.

See also

[`numpy.dtype.kind`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy.dtype.kind "(in NumPy v2.5)")

On this page