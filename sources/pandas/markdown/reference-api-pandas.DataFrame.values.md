[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.values[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas-dataframe-values "Link to this heading")

=====================================================================================================================================================

property DataFrame.values[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L20209-L20320)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas.DataFrame.values "Link to this definition")

Return a Numpy representation of the DataFrame.

Warning

We recommend using [`DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")
 instead. `.values` offers no way to control the output `dtype`, copy semantics, or the value used to fill missing entries, while [`DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")
 exposes those as the `dtype`, `copy`, and `na_value` arguments. The mutability of the result also depends on the DataFrame’s internal block layout: when the DataFrame is backed by a single block the result is a read-only view (writes raise); when there are multiple blocks the result is a writable copy whose mutations do not propagate back to the DataFrame.

Only the values in the DataFrame will be returned, the axes labels will be removed.

Returns:

numpy.ndarray

The values of the DataFrame.

See also

[`DataFrame.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")

Recommended alternative to this method.

[`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index")

Retrieve the index labels.

[`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")

Retrieving the column names.

Notes

The returned array is not intended to be written to. When the DataFrame is backed by a single NumPy array (single dtype, single block), the result is a read-only view; when the DataFrame has multiple internal blocks (e.g. after adding a new column), the result is a copy and modifications to it will not be reflected in the original DataFrame. Use [`DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")
 for more explicit control over copy behavior, or use [`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")
 to modify values in-place.

The dtype will be a lower-common-denominator dtype (implicit upcasting); that is to say if the dtypes (even of numeric types) are mixed, the one that accommodates all will be chosen. Use this with care if you are not dealing with the blocks.

e.g. If the dtypes are float16 and float32, dtype will be upcast to float32. If dtypes are int32 and uint8, dtype will be upcast to int32. By `numpy.find_common_type()` convention, mixing int64 and uint64 will result in a float64 dtype.

Examples

A DataFrame where all columns are the same type (e.g., int64) results in an array of the same type.

\>>> df \= pd.DataFrame(
...     {"age": \[3, 29\], "height": \[94, 170\], "weight": \[31, 115\]}
... )
\>>> df
   age  height  weight
0    3      94      31
1   29     170     115
\>>> df.dtypes
age       int64
height    int64
weight    int64
dtype: object
\>>> df.values
array(\[\[  3,  94,  31\],\
       \[ 29, 170, 115\]\])

Copy to clipboard

A DataFrame with mixed type columns(e.g., str/object, int64, float32) results in an ndarray of the broadest type that accommodates these mixed types (e.g., object).

\>>> df2 \= pd.DataFrame(
...     \[\
...         ("parrot", 24.0, "second"),\
...         ("lion", 80.5, 1),\
...         ("monkey", np.nan, None),\
...     \],
...     columns\=("name", "max\_speed", "rank"),
... )
\>>> df2.dtypes
name             str
max\_speed    float64
rank          object
dtype: object
\>>> df2.values
array(\[\['parrot', 24.0, 'second'\],\
       \['lion', 80.5, 1\],\
       \['monkey', nan, None\]\], dtype=object)

Copy to clipboard

`DataFrame.to_numpy` produces the same array by default, but lets you choose how missing values are represented and request a guaranteed copy:

\>>> df3 \= pd.DataFrame({"a": \[1, 2\], "b": \[3.0, np.nan\]})
\>>> df3.values
array(\[\[ 1.,  3.\],\
       \[ 2., nan\]\])
\>>> df3.to\_numpy(na\_value\=-1)
array(\[\[ 1.,  3.\],\
       \[ 2., -1.\]\])
\>>> df3.to\_numpy(dtype\="float32", copy\=True)
array(\[\[ 1.,  3.\],\
       \[ 2., nan\]\], dtype=float32)

Copy to clipboard

On this page