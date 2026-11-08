[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._explode.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._explode.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._explode.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_explode[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._explode.html#pandas-api-extensions-extensionarray-explode "Link to this heading")

=======================================================================================================================================================================================================================

ExtensionArray.\_explode()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2585-L2619)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._explode.html#pandas.api.extensions.ExtensionArray._explode "Link to this definition")

Transform each element of list-like to a row.

For arrays that do not contain list-like elements the default implementation of this method just returns a copy and an array of ones (unchanged index).

Returns:

ExtensionArray

Array with the exploded values.

np.ndarray\[uint64\]

The original lengths of each list-like for determining the resulting index.

See also

`Series.explode`

The method on the `Series` object that this extension array method is meant to support.

Examples

\>>> import pyarrow as pa
\>>> a \= pd.array(
...     \[\[1, 2, 3\], \[4\], \[5, 6\]\], dtype\=pd.ArrowDtype(pa.list\_(pa.int64()))
... )
\>>> a.\_explode()
(<ArrowExtensionArray>
\[1, 2, 3, 4, 5, 6\]
Length: 6, dtype: int64\[pyarrow\], array(\[3, 1, 2\], dtype=int32))

Copy to clipboard

On this page