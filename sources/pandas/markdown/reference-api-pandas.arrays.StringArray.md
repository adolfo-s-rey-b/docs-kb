[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.StringArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.StringArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.StringArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.StringArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.StringArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.StringArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.StringArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.StringArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.StringArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.StringArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.StringArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.StringArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.StringArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas-arrays-stringarray "Link to this heading")

===========================================================================================================================================================

class pandas.arrays.StringArray(_values_, _\*_, _dtype\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/string_.py#L616-L1322)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas.arrays.StringArray "Link to this definition")

Extension array for string data.

Warning

StringArray is considered experimental. The implementation and parts of the API may change without warning.

Parameters:

**values**array-like

The array of data.

Warning

Currently, this expects an object-dtype ndarray where the elements are Python strings or nan-likes (`None`, `np.nan`, `NA`). This may change without warning in the future. Use [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 with `dtype="string"` for a stable way of creating a StringArray from any sequence.

StringArray accepts array-likes containing nan-likes(`None`, `np.nan`) for the `values` parameter in addition to strings and [`pandas.NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")

**dtype**StringDtype

Dtype for the array.

**copy**bool, default False

Whether to copy the array of data.

See also

`array()`

The recommended function for creating a StringArray.

`Series.str`

The string methods are available on Series backed by a StringArray.

Notes

StringArray returns a BooleanArray for comparison methods.

Examples

\>>> pd.array(\["This is", "some text", None, "data."\], dtype\="string")
<ArrowStringArray>
\['This is', 'some text', <NA>, 'data.'\]
Length: 4, dtype: string

Copy to clipboard

Unlike arrays instantiated with `dtype="object"`, `StringArray` will convert the values to strings.

\>>> pd.array(\["1", 1\], dtype\="object")
<NumpyExtensionArray>
\['1', 1\]
Length: 2, dtype: object
\>>> pd.array(\["1", 1\], dtype\="string")
<ArrowStringArray>
\['1', '1'\]
Length: 2, dtype: string

Copy to clipboard

However, instantiating StringArrays directly with non-strings will raise an error.

For comparison methods, StringArray returns a `pandas.BooleanArray`:

\>>> pd.array(\["a", None, "c"\], dtype\="string\[python\]") \== "a"
<BooleanArray>
\[True, <NA>, False\]
Length: 3, dtype: boolean

Copy to clipboard

On this page