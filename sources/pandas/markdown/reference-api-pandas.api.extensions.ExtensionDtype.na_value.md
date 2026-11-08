[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.na_value.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionDtype.na\_value[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.na_value.html#pandas-api-extensions-extensiondtype-na-value "Link to this heading")

========================================================================================================================================================================================================================

property ExtensionDtype.na\_value[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L175-L184)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.na_value.html#pandas.api.extensions.ExtensionDtype.na_value "Link to this definition")

Default NA value to use for this type.

This is used in e.g. ExtensionArray.take. This should be the user-facing “boxed” version of the NA value, not the physical NA value for storage. e.g. for JSONArray, this is an empty dictionary.

On this page