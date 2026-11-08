[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.ArrowStringArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.ArrowStringArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.ArrowStringArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.ArrowStringArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.ArrowStringArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.ArrowStringArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.ArrowStringArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.ArrowStringArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.ArrowStringArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.ArrowStringArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.ArrowStringArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.ArrowStringArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.ArrowStringArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html#pandas-arrays-arrowstringarray "Link to this heading")

==========================================================================================================================================================================

class pandas.arrays.ArrowStringArray(_values_, _\*_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/string_arrow.py#L90-L655)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html#pandas.arrays.ArrowStringArray "Link to this definition")

Extension array for string data in a `pyarrow.ChunkedArray`.

Warning

ArrowStringArray is considered experimental. The implementation and parts of the API may change without warning.

Parameters:

**values**pyarrow.Array or pyarrow.ChunkedArray

The array of data.

**dtype**StringDtype

The dtype for the array.

See also

`array()`

The recommended function for creating an ArrowStringArray.

`Series.str`

The string methods are available on Series backed by an ArrowStringArray.

Notes

ArrowStringArray returns a BooleanArray for comparison methods.

Examples

\>>> pd.array(\["This is", "some text", None, "data."\], dtype\="string\[pyarrow\]")
<ArrowStringArray>
\['This is', 'some text', <NA>, 'data.'\]
Length: 4, dtype: string

Copy to clipboard

On this page