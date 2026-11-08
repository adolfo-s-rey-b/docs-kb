[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_re.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_re.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_re.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_re.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_re.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_re.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_re.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_re.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_re.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_re.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_re.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_re.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_re[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re.html#pandas-api-types-is-re "Link to this heading")

===================================================================================================================================================

pandas.api.types.is\_re(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L148-L185)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re.html#pandas.api.types.is_re "Link to this definition")

Check if the object is a regex pattern instance.

This function tests whether `obj` is an instance of a compiled regular expression pattern, as created by [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.15)")
.

Parameters:

**obj**object

The object to check for being a regex pattern. Typically, this would be an object that you expect to be a compiled pattern from the re module.

Returns:

bool

Whether obj is a regex pattern.

See also

`api.types.is_float`

Return True if given object is float.

`api.types.is_iterator`

Check if the object is an iterator.

`api.types.is_integer`

Return True if given object is integer.

`api.types.is_re_compilable`

Check if the object can be compiled into a regex pattern instance.

Examples

\>>> from pandas.api.types import is\_re
\>>> import re
\>>> is\_re(re.compile(".\*"))
True
\>>> is\_re("foo")
False

Copy to clipboard

On this page