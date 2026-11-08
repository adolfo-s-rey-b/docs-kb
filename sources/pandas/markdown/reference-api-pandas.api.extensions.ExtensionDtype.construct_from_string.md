[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionDtype.construct\_from\_string[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html#pandas-api-extensions-extensiondtype-construct-from-string "Link to this heading")

================================================================================================================================================================================================================================================================

classmethod ExtensionDtype.construct\_from\_string(_string_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/base.py#L260-L320)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.construct_from_string.html#pandas.api.extensions.ExtensionDtype.construct_from_string "Link to this definition")

Construct this type from a string.

This is useful mainly for data types that accept parameters. For example, a period dtype accepts a frequency parameter that can be set as `period[h]` (where H means hourly frequency).

By default, in the abstract class, just the name of the type is expected. But subclasses can overwrite this method to accept parameters.

Parameters:

**string**str

The name of the type, for example `category`.

Returns:

ExtensionDtype

Instance of the dtype.

Raises:

TypeError

If a class cannot be constructed from this ‘string’.

Examples

For extension dtypes with arguments the following may be an adequate implementation.

\>>> import re
\>>> @classmethod
... def construct\_from\_string(cls, string):
...     pattern \= re.compile(r"^my\_type\\\[(?P<arg\_name>.+)\\\]$")
...     match \= pattern.match(string)
...     if match:
...         return cls(\*\*match.groupdict())
...     else:
...         raise TypeError(
...             f"Cannot construct a '{cls.\_\_name\_\_}' from '{string}'"
...         )

Copy to clipboard

On this page