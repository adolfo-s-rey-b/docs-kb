[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.SparseDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas-sparsedtype "Link to this heading")

======================================================================================================================================

class pandas.SparseDtype(_dtype\=<class 'numpy.float64'>_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L1740-L2219)
[#](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas.SparseDtype "Link to this definition")

Dtype for data stored in `SparseArray`.

`SparseDtype` is used as the data type for `SparseArray`, enabling more efficient storage of data that contains a significant number of repetitive values typically represented by a fill value. It supports any scalar dtype as the underlying data type of the non-fill values, except that a datetime64 or timedelta64 subtype is limited to the `'s'`, `'ms'`, `'us'` and `'ns'` resolutions.

Parameters:

**dtype**str, ExtensionDtype, numpy.dtype, type, default numpy.float64

The dtype of the underlying array storing the non-fill value values.

**fill\_value**scalar, optional

The scalar value not stored in the SparseArray. By default, this depends on `dtype`.

| dtype | na\_value |
| --- | --- |
| float | `np.nan` |
| complex | `np.nan` |
| int | `0` |
| bool | `False` |
| datetime64 | `np.datetime64("NaT")` |
| timedelta64 | `np.timedelta64("NaT")` |

The default value may be overridden by specifying a `fill_value`.

See also

[`arrays.SparseArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")

The array structure that uses SparseDtype for data representation.

Examples

\>>> ser \= pd.Series(\[1, 0, 0\], dtype\=pd.SparseDtype(dtype\=int, fill\_value\=0))
\>>> ser
0    1
1    0
2    0
dtype: Sparse\[int64, 0\]
\>>> ser.sparse.density
0.3333333333333333

Copy to clipboard

On this page