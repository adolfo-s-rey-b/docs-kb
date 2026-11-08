[Skip to main content](https://pandas.pydata.org/docs/reference/extensions.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Extensions[#](https://pandas.pydata.org/docs/reference/extensions.html#extensions "Link to this heading")

==========================================================================================================

These are primarily intended for library authors looking to extend pandas objects.

|     |     |
| --- | --- |
| [`api.extensions.register_extension_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html#pandas.api.extensions.register_extension_dtype "pandas.api.extensions.register_extension_dtype")<br>(cls) | Register an ExtensionType with pandas as class decorator. |
| [`api.extensions.register_dataframe_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html#pandas.api.extensions.register_dataframe_accessor "pandas.api.extensions.register_dataframe_accessor")<br>(name) | Register a custom accessor on DataFrame objects. |
| [`api.extensions.register_series_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_series_accessor.html#pandas.api.extensions.register_series_accessor "pandas.api.extensions.register_series_accessor")<br>(name) | Register a custom accessor on Series objects. |
| [`api.extensions.register_index_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html#pandas.api.extensions.register_index_accessor "pandas.api.extensions.register_index_accessor")<br>(name) | Register a custom accessor on Index objects. |

|     |     |
| --- | --- |
| [`api.extensions.ExtensionDtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html#pandas.api.extensions.ExtensionDtype "pandas.api.extensions.ExtensionDtype")<br>() | A custom data type, to be paired with an ExtensionArray. |
| [`api.extensions.ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")<br>() | Abstract base class for custom 1-D array types. |
| [`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")<br>(values\[, copy\]) | A pandas ExtensionArray for NumPy data. |

Additionally, we have some utility methods for ensuring your object behaves correctly.

|     |     |
| --- | --- |
| [`api.indexers.check_array_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.check_array_indexer.html#pandas.api.indexers.check_array_indexer "pandas.api.indexers.check_array_indexer")<br>(array, indexer) | Check if indexer is a valid array indexer for array. |

The sentinel `pandas.api.extensions.no_default` is used as the default value in some methods. Use an `is` comparison to check if the user provides a non-default value.