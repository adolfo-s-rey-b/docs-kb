[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.FloatingArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#pandas-arrays-floatingarray "Link to this heading")

=================================================================================================================================================================

class pandas.arrays.FloatingArray(_values_, _mask_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/floating.py#L66-L133)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#pandas.arrays.FloatingArray "Link to this definition")

Array of floating (optional missing) values.

Warning

FloatingArray is currently experimental, and its API or internal implementation may change without warning. Especially the behaviour regarding NaN (distinct from NA missing values) is subject to change.

We represent a FloatingArray with 2 numpy arrays:

*   data: contains a numpy float array of the appropriate dtype
    
*   mask: a boolean array holding a mask on the data, True is missing
    

To construct a FloatingArray from generic array-like input, use [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 with one of the float dtypes (see examples).

See [Nullable integer data type](https://pandas.pydata.org/docs/user_guide/integer_na.html#integer-na)
 for more.

Parameters:

**values**numpy.ndarray

A 1-d float-dtype array.

**mask**numpy.ndarray

A 1-d boolean-dtype array indicating missing values.

**copy**bool, default False

Whether to copy the values and mask.

Returns:

FloatingArray

See also

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Create an array.

`Float32Dtype`

Float32 dtype for FloatingArray.

`Float64Dtype`

Float64 dtype for FloatingArray.

`Series`

One-dimensional labeled array capable of holding data.

`DataFrame`

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Examples

Create a FloatingArray with [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
:

\>>> pd.array(\[0.1, None, 0.3\], dtype\=pd.Float32Dtype())
<FloatingArray>
\[0.1, <NA>, 0.3\]
Length: 3, dtype: Float32

Copy to clipboard

String aliases for the dtypes are also available. They are capitalized.

\>>> pd.array(\[0.1, None, 0.3\], dtype\="Float32")
<FloatingArray>
\[0.1, <NA>, 0.3\]
Length: 3, dtype: Float32

Copy to clipboard

On this page