[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re_compilable.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_re\_compilable[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re_compilable.html#pandas-api-types-is-re-compilable "Link to this heading")

=====================================================================================================================================================================================

pandas.api.types.is\_re\_compilable(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L188-L223)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re_compilable.html#pandas.api.types.is_re_compilable "Link to this definition")

Check if the object can be compiled into a regex pattern instance.

This function attempts to compile `obj` as a regular expression using [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.15)")
 and returns whether the compilation succeeds.

Parameters:

**obj**The object to check

The object to check if the object can be compiled into a regex pattern instance.

Returns:

bool

Whether obj can be compiled as a regex pattern.

See also

`api.types.is_re`

Check if the object is a regex pattern instance.

Examples

\>>> from pandas.api.types import is\_re\_compilable
\>>> is\_re\_compilable(".\*")
True
\>>> is\_re\_compilable(1)
False

Copy to clipboard

On this page