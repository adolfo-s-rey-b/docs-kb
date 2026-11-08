[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.SparseArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.SparseArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.SparseArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.SparseArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.SparseArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.SparseArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.SparseArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.SparseArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.SparseArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.SparseArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.SparseArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.SparseArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.SparseArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas-arrays-sparsearray "Link to this heading")

===========================================================================================================================================================

class pandas.arrays.SparseArray(_data_, _sparse\_index\=<no\_default>_, _fill\_value\=None_, _kind\='integer'_, _dtype\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/array.py#L558-L3117)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "Link to this definition")

An ExtensionArray for storing sparse data.

SparseArray efficiently stores data with a high frequency of a specific fill value (e.g., zeros), saving memory by only retaining non-fill elements and their indices. This class is particularly useful for large datasets where most values are redundant.

Parameters:

**data**array-like or scalar

A dense array of values to store in the SparseArray. This may contain fill\_value.

**sparse\_index**SparseIndex, optional

Index indicating the locations of sparse elements.

Deprecated since version 3.1.0: Use `SparseArray.from_indices()` instead.

**fill\_value**scalar, optional

Elements in data that are `fill_value` are not stored in the SparseArray. For memory savings, this should be the most common value in data. By default, fill\_value depends on the dtype of data:

| data.dtype | na\_value |
| --- | --- |
| float | `np.nan` |
| int | `0` |
| bool | False |
| datetime64 | `np.datetime64("NaT")` |
| timedelta64 | `np.timedelta64("NaT")` |

The fill value is potentially specified in three ways. In order of precedence, these are

1.  The fill\_value argument
    
2.  `dtype.fill_value` if fill\_value is None and dtype is a `SparseDtype`
    
3.  `data.dtype.fill_value` if fill\_value is None and dtype is not a `SparseDtype` and data is a `SparseArray`.
    

**kind**str

Can be ‘integer’ or ‘block’, default is ‘integer’. The type of storage for sparse locations.

*   ‘block’: Stores a block and block\_length for each contiguous _span_ of sparse values. This is best when sparse data tends to be clumped together, with large regions of `fill-value` values between sparse values.
    
*   ‘integer’: uses an integer to store the location of each sparse value.
    

**dtype**np.dtype or SparseDtype, optional

The dtype to use for the SparseArray. For numpy dtypes, this determines the dtype of `self.sp_values`. For SparseDtype, this determines `self.sp_values` and `self.fill_value`.

**copy**bool, default False

Whether to explicitly copy the incoming data array.

See also

`SparseDtype`

Dtype for sparse data.

Examples

\>>> from pandas.arrays import SparseArray
\>>> arr \= SparseArray(\[0, 0, 1, 2\])
\>>> arr
<SparseArray>
\[0, 0, 1, 2\]
Length: 4, dtype: Sparse\[int64, 0\]

Copy to clipboard

On this page