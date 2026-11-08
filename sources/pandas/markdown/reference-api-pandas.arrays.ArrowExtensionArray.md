[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.ArrowExtensionArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.ArrowExtensionArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.ArrowExtensionArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.ArrowExtensionArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.ArrowExtensionArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.ArrowExtensionArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.ArrowExtensionArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.ArrowExtensionArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas-arrays-arrowextensionarray "Link to this heading")

===================================================================================================================================================================================

class pandas.arrays.ArrowExtensionArray(_values_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/array.py#L471-L4720)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "Link to this definition")

Pandas ExtensionArray backed by a PyArrow ChunkedArray.

Warning

ArrowExtensionArray is considered experimental. The implementation and parts of the API may change without warning.

Parameters:

**values**pyarrow.Array or pyarrow.ChunkedArray

The input data to initialize the ArrowExtensionArray.

Returns:

ArrowExtensionArray

See also

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Create a Pandas array with a specified dtype.

`DataFrame.to_feather`

Write a DataFrame to the binary Feather format.

`read_feather`

Load a feather-format object from the file path.

Notes

Most methods are implemented using [pyarrow compute functions.](https://arrow.apache.org/docs/python/api/compute.html)
 Some methods may either raise an exception or raise a `PerformanceWarning` if an associated compute function is not available based on the installed version of PyArrow.

Please install the latest version of PyArrow to enable the best functionality and avoid potential bugs in prior versions of PyArrow.

Examples

Create an ArrowExtensionArray with [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
:

\>>> pd.array(\[1, 1, None\], dtype\="int64\[pyarrow\]")
<ArrowExtensionArray>
\[1, 1, <NA>\]
Length: 3, dtype: int64\[pyarrow\]

Copy to clipboard

On this page