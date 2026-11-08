[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntegerArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntegerArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntegerArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntegerArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntegerArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntegerArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntegerArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntegerArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntegerArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntegerArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntegerArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntegerArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntegerArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas-arrays-integerarray "Link to this heading")

==============================================================================================================================================================

class pandas.arrays.IntegerArray(_values_, _mask_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/integer.py#L76-L148)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas.arrays.IntegerArray "Link to this definition")

Array of integer (optional missing) values.

Uses [`pandas.NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")
 as the missing value.

Warning

IntegerArray is currently experimental, and its API or internal implementation may change without warning.

We represent an IntegerArray with 2 numpy arrays:

*   data: contains a numpy integer array of the appropriate dtype
    
*   mask: a boolean array holding a mask on the data, True is missing
    

To construct an IntegerArray from generic array-like input, use [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 with one of the integer dtypes (see examples).

See [Nullable integer data type](https://pandas.pydata.org/docs/user_guide/integer_na.html#integer-na)
 for more.

Parameters:

**values**numpy.ndarray

A 1-d integer-dtype array.

**mask**numpy.ndarray

A 1-d boolean-dtype array indicating missing values.

**copy**bool, default False

Whether to copy the values and mask.

Returns:

IntegerArray

See also

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Create an array using the appropriate dtype, including `IntegerArray`.

`Int32Dtype`

An ExtensionDtype for int32 integer data.

`UInt16Dtype`

An ExtensionDtype for uint16 integer data.

Examples

Create an IntegerArray with [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
.

\>>> int\_array \= pd.array(\[1, None, 3\], dtype\=pd.Int32Dtype())
\>>> int\_array
<IntegerArray>
\[1, <NA>, 3\]
Length: 3, dtype: Int32

Copy to clipboard

String aliases for the dtypes are also available. They are capitalized.

\>>> pd.array(\[1, None, 3\], dtype\="Int32")
<IntegerArray>
\[1, <NA>, 3\]
Length: 3, dtype: Int32

Copy to clipboard

\>>> pd.array(\[1, None, 3\], dtype\="UInt16")
<IntegerArray>
\[1, <NA>, 3\]
Length: 3, dtype: UInt16

Copy to clipboard

On this page