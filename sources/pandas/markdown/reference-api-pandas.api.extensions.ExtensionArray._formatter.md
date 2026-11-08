[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._formatter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._formatter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_formatter[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._formatter.html#pandas-api-extensions-extensionarray-formatter "Link to this heading")

=============================================================================================================================================================================================================================

ExtensionArray.\_formatter(_boxed\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2201-L2248)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._formatter.html#pandas.api.extensions.ExtensionArray._formatter "Link to this definition")

Formatting function for scalar values.

This is used in the default ‘\_\_repr\_\_’. The returned formatting function receives instances of your scalar type.

Parameters:

**boxed**bool, default False

An indicator for whether or not your array is being printed within a Series, DataFrame, or Index (True), or just by itself (False). This may be useful if you want scalar values to appear differently within a Series versus on its own (e.g. quoted or not).

Returns:

Callable\[\[Any\], str\]

A callable that gets instances of the scalar type and returns a string. By default, [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "(in Python v3.15)")
 is used when `boxed=False` and `str()` is used when `boxed=True`.

See also

`api.extensions.ExtensionArray._concat_same_type`

Concatenate multiple array of this dtype.

`api.extensions.ExtensionArray._explode`

Transform each element of list-like to a row.

`api.extensions.ExtensionArray._from_factorized`

Reconstruct an ExtensionArray after factorization.

`api.extensions.ExtensionArray._from_sequence`

Construct a new ExtensionArray from a sequence of scalars.

Examples

\>>> class MyExtensionArray(pd.arrays.NumpyExtensionArray):
...     def \_formatter(self, boxed\=False):
...         return lambda x: "\*" + str(x) + "\*"
\>>> MyExtensionArray(np.array(\[1, 2, 3, 4\]))
<MyExtensionArray>
\[\*1\*, \*2\*, \*3\*, \*4\*\]
Length: 4, dtype: int64

Copy to clipboard

On this page