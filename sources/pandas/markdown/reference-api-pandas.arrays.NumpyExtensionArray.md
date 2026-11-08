[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.NumpyExtensionArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.NumpyExtensionArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.NumpyExtensionArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.NumpyExtensionArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.NumpyExtensionArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.NumpyExtensionArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.NumpyExtensionArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.NumpyExtensionArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas-arrays-numpyextensionarray "Link to this heading")

===================================================================================================================================================================================

class pandas.arrays.NumpyExtensionArray(_values_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/numpy_.py#L69-L706)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "Link to this definition")

A pandas ExtensionArray for NumPy data.

This is mostly for internal compatibility, and is not especially useful on its own.

Parameters:

**values**ndarray

The NumPy ndarray to wrap. Must be 1-dimensional.

**copy**bool, default False

Whether to copy values.

See also

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Create an array.

`Series.to_numpy`

Convert a Series to a NumPy array.

Examples

\>>> pd.arrays.NumpyExtensionArray(np.array(\[0, 1, 2, 3\]))
<NumpyExtensionArray>
\[0, 1, 2, 3\]
Length: 4, dtype: int64

Copy to clipboard

On this page