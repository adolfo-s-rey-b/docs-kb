[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionDtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionDtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionDtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionDtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionDtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionDtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionDtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html#pandas-api-extensions-extensiondtype "Link to this heading")

============================================================================================================================================================================================

class pandas.api.extensions.ExtensionDtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L48-L497)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html#pandas.api.extensions.ExtensionDtype "Link to this definition")

A custom data type, to be paired with an ExtensionArray.

This enables support for third-party and custom dtypes within the pandas ecosystem. By implementing this interface and pairing it with a custom ExtensionArray, users can create rich data types that integrate cleanly with pandas operations, such as grouping, joining, or aggregation.

Attributes

|     |     |
| --- | --- |
| [`kind`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.kind.html#pandas.api.extensions.ExtensionDtype.kind "pandas.api.extensions.ExtensionDtype.kind") | A character code (one of 'biufcmMOSUV'), default 'O' |
| [`na_value`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.na_value.html#pandas.api.extensions.ExtensionDtype.na_value "pandas.api.extensions.ExtensionDtype.na_value") | Default NA value to use for this type. |
| [`name`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.name.html#pandas.api.extensions.ExtensionDtype.name "pandas.api.extensions.ExtensionDtype.name") | A string identifying the data type. |
| [`names`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.names.html#pandas.api.extensions.ExtensionDtype.names "pandas.api.extensions.ExtensionDtype.names") | Ordered list of field names, or None if there are no fields. |
| [`type`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.type.html#pandas.api.extensions.ExtensionDtype.type "pandas.api.extensions.ExtensionDtype.type") | The scalar type for the array, e.g. `int`. |

Methods

|     |     |
| --- | --- |
| [`construct_array_type`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_array_type.html#pandas.api.extensions.ExtensionDtype.construct_array_type "pandas.api.extensions.ExtensionDtype.construct_array_type")<br>() | Return the array type associated with this dtype. |
| [`construct_from_string`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html#pandas.api.extensions.ExtensionDtype.construct_from_string "pandas.api.extensions.ExtensionDtype.construct_from_string")<br>(string) | Construct this type from a string. |
| [`is_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.is_dtype.html#pandas.api.extensions.ExtensionDtype.is_dtype "pandas.api.extensions.ExtensionDtype.is_dtype")<br>(dtype) | Check if we match 'dtype'. |

See also

`extensions.register_extension_dtype`

Register an ExtensionType with pandas as class decorator.

`extensions.ExtensionArray`

Abstract base class for custom 1-D array types.

Notes

The interface includes the following abstract methods that must be implemented by subclasses:

*   type
    
*   name
    
*   construct\_array\_type
    

The following attributes and methods influence the behavior of the dtype in pandas operations

*   \_is\_numeric
    
*   \_is\_boolean
    
*   \_get\_common\_dtype
    

The na\_value class attribute can be used to set the default NA value for this type. `numpy.nan` is used by default.

ExtensionDtypes are required to be hashable. The base class provides a default implementation, which relies on the `_metadata` class attribute. `_metadata` should be a tuple containing the strings that define your data type. For example, with `PeriodDtype` that’s the `freq` attribute.

**If you have a parametrized dtype you should set the \`\`\_metadata\`\` class property**.

Ideally, the attributes in `_metadata` will match the parameters to your `ExtensionDtype.__init__` (if any). If any of the attributes in `_metadata` don’t implement the standard `__eq__` or `__hash__`, the default implementations here will not work.

Examples

For interaction with Apache Arrow (pyarrow), a `__from_arrow__` method can be implemented: this method receives a pyarrow Array or ChunkedArray as only argument and is expected to return the appropriate pandas ExtensionArray for this dtype and the passed values:

\>>> import pyarrow
\>>> from pandas.api.extensions import ExtensionArray
\>>> class ExtensionDtype:
...     def \_\_from\_arrow\_\_(
...         self, array: pyarrow.Array | pyarrow.ChunkedArray
...     ) \-> ExtensionArray: ...

Copy to clipboard

This class does not inherit from ‘abc.ABCMeta’ for performance reasons. Methods and properties required by the interface raise `pandas.errors.AbstractMethodError` and no `register` method is provided for registering virtual subclasses.

On this page