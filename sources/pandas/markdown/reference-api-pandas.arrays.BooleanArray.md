[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.BooleanArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.BooleanArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.BooleanArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.BooleanArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.BooleanArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.BooleanArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.BooleanArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.BooleanArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.BooleanArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.BooleanArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.BooleanArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.BooleanArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.BooleanArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas-arrays-booleanarray "Link to this heading")

==============================================================================================================================================================

class pandas.arrays.BooleanArray(_values_, _mask_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/boolean.py#L267-L455)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "Link to this definition")

Array of boolean (True/False) data with missing values.

This is a pandas Extension array for boolean data, under the hood represented by 2 numpy arrays: a boolean array with the data and a boolean array with the mask (True indicating missing).

BooleanArray implements Kleene logic (sometimes called three-value logic) for logical operations. See [Kleene logical operations](https://pandas.pydata.org/docs/user_guide/boolean.html#boolean-kleene)
 for more.

To construct a BooleanArray from generic array-like input, use [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 specifying `dtype="boolean"` (see examples below).

Warning

BooleanArray is considered experimental. The implementation and parts of the API may change without warning.

Parameters:

**values**numpy.ndarray

A 1-d boolean-dtype array with the data.

**mask**numpy.ndarray

A 1-d boolean-dtype array indicating missing values (True indicates missing).

**copy**bool, default False

Whether to copy the values and mask arrays.

Returns:

BooleanArray

See also

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Create an array from data with the appropriate dtype.

`BooleanDtype`

Extension dtype for boolean data.

`Series`

One-dimensional ndarray with axis labels (including time series).

`DataFrame`

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Examples

Create a BooleanArray with [`pandas.array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
:

\>>> pd.array(\[True, False, None\], dtype\="boolean")
<BooleanArray>
\[True, False, <NA>\]
Length: 3, dtype: boolean

Copy to clipboard

On this page