[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.convert\_dtypes[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas-dataframe-convert-dtypes "Link to this heading")

==============================================================================================================================================================================

DataFrame.convert\_dtypes(_infer\_objects\=<no\_default>_, _convert\_string\=<no\_default>_, _convert\_integer\=<no\_default>_, _convert\_boolean\=<no\_default>_, _convert\_floating\=<no\_default>_, _dtype\_backend\='numpy\_nullable'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6982-L7186)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "Link to this definition")

Convert columns from numpy dtypes to the best dtypes that support `pd.NA`.

This methods converts columns using default NumPy dtypes to nullable dtypes (using `pd.NA` as missing value indicator).

Parameters:

**infer\_objects**bool, default True

Whether object dtypes should be converted to the best possible types.

Deprecated since version 3.1.0: The `infer_objects` keyword is deprecated and will be removed in a future version.

**convert\_string**bool, default True

Whether object dtypes should be converted to `StringDtype()`.

Deprecated since version 3.1.0: The `convert_string` keyword is deprecated and will be removed in a future version.

**convert\_integer**bool, default True

Whether, if possible, conversion can be done to integer extension types.

Deprecated since version 3.1.0: The `convert_integer` keyword is deprecated and will be removed in a future version.

**convert\_boolean**bool, defaults True

Whether object dtypes should be converted to `BooleanDtypes()`.

Deprecated since version 3.1.0: The `convert_boolean` keyword is deprecated and will be removed in a future version.

**convert\_floating**bool, defaults True

Whether, if possible, conversion can be done to floating extension types. If convert\_integer is also True, preference will be give to integer dtypes if the floats can be faithfully casted to integers.

Deprecated since version 3.1.0: The `convert_floating` keyword is deprecated and will be removed in a future version.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}, default ‘numpy\_nullable’

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 (still experimental). Behaviour is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
     or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    .
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
     or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    .
    

Added in version 2.0.

Returns:

Series or DataFrame

Copy of input object with new dtype.

See also

[`infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html#pandas.DataFrame.infer_objects "pandas.DataFrame.infer_objects")

Infer dtypes of objects.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`to_numeric`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric "pandas.to_numeric")

Convert argument to a numeric type.

Notes

By default, `convert_dtypes` will attempt to convert a Series (or each Series in a DataFrame) to dtypes that support `pd.NA`.

For object-dtyped columns, if `infer_objects` is `True`, use the inference rules as during normal Series/DataFrame construction. Then, if possible, convert to `StringDtype`, `BooleanDtype` or an appropriate integer or floating extension type, otherwise leave as `object`.

If the dtype is integer, convert to an appropriate integer extension type.

If the dtype is numeric, and consists of all integers, convert to an appropriate integer extension type. Otherwise, convert to an appropriate floating extension type.

In the future, as new dtypes are added that support `pd.NA`, the results of this method will change to support those new dtypes.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "a": pd.Series(\[1, 2, 3\], dtype\=np.dtype("int32")),
...         "b": pd.Series(\["x", "y", "z"\], dtype\=np.dtype("O")),
...         "c": pd.Series(\[True, False, np.nan\], dtype\=np.dtype("O")),
...         "d": pd.Series(\["h", "i", np.nan\], dtype\=np.dtype("O")),
...         "e": pd.Series(\[10, np.nan, 20\], dtype\=np.dtype("float")),
...         "f": pd.Series(\[np.nan, 100.5, 200\], dtype\=np.dtype("float")),
...     }
... )

Copy to clipboard

Start with a DataFrame with default dtypes.

\>>> df
   a  b      c    d     e      f
0  1  x   True    h  10.0    NaN
1  2  y  False    i   NaN  100.5
2  3  z    NaN  NaN  20.0  200.0

Copy to clipboard

\>>> df.dtypes
a      int32
b     object
c     object
d     object
e    float64
f    float64
dtype: object

Copy to clipboard

Convert the DataFrame to use best possible dtypes.

\>>> dfn \= df.convert\_dtypes()
\>>> dfn
   a  b      c     d     e      f
0  1  x   True     h    10   <NA>
1  2  y  False     i  <NA>  100.5
2  3  z   <NA>  <NA>    20  200.0

Copy to clipboard

\>>> dfn.dtypes
a      Int32
b     string
c    boolean
d     string
e      Int64
f    Float64
dtype: object

Copy to clipboard

Start with a Series of strings and missing data represented by `np.nan`.

\>>> s \= pd.Series(\["a", "b", np.nan\])
\>>> s
0      a
1      b
2    NaN
dtype: str

Copy to clipboard

Obtain a Series with dtype `StringDtype`.

\>>> s.convert\_dtypes()
0       a
1       b
2    <NA>
dtype: string

Copy to clipboard

On this page