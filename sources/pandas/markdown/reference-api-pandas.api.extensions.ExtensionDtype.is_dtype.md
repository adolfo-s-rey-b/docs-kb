[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.is_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionDtype.is\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.is_dtype.html#pandas-api-extensions-extensiondtype-is-dtype "Link to this heading")

========================================================================================================================================================================================================================

classmethod ExtensionDtype.is\_dtype(_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L322-L363)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.is_dtype.html#pandas.api.extensions.ExtensionDtype.is_dtype "Link to this definition")

Check if we match ‘dtype’.

Parameters:

**dtype**object

The object to check.

Returns:

bool

Notes

The default implementation is True if

1.  `cls.construct_from_string(dtype)` is an instance of `cls`.
    
2.  `dtype` is an object and is an instance of `cls`
    
3.  `dtype` has a `dtype` attribute, and any of the above conditions is true for `dtype.dtype`.
    

On this page