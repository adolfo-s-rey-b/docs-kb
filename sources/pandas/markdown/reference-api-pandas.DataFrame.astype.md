[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.astype[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas-dataframe-astype "Link to this heading")

=====================================================================================================================================================

DataFrame.astype(_dtype_, _copy\=<no\_default>_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6591-L6798)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "Link to this definition")

Cast a pandas object to a specified dtype `dtype`.

This method allows the conversion of the data types of pandas objects, including DataFrames and Series, to the specified dtype. It supports casting entire objects to a single data type or applying different data types to individual columns using a mapping.

Parameters:

**dtype**str, data type, Series or Mapping of column name -> data type

Use a str, numpy.dtype, pandas.ExtensionDtype or Python type to cast entire pandas object to the same type. Alternatively, use a mapping, e.g. {col: dtype, …}, where col is a column label and dtype is a numpy.dtype or Python type to cast one or more of the DataFrame’s columns to column-specific types. The mapping may be a `dict` or a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 indexed by column label; columns whose labels are absent from the mapping are left unchanged. A Python type (e.g. `int`, `float`, `str`, `bool`) is mapped to the corresponding dtype; a type with no such mapping, such as `datetime.datetime`, raises `TypeError`.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**errors**{‘raise’, ‘ignore’}, default ‘raise’

Control raising of exceptions on invalid data for provided dtype.

*   `raise` : allow exceptions to be raised
    
*   `ignore` : suppress exceptions. On error return original object.
    

This does not apply to keys in a `dtype` mapping that are not column labels (or, for a Series, not its name); those always raise `KeyError`.

Returns:

same type as caller

The pandas object casted to the specified `dtype`.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`to_numeric`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric "pandas.to_numeric")

Convert argument to a numeric type.

[`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "(in NumPy v2.5)")

Cast a numpy array to a specified type.

Notes

Changed in version 2.0.0: Using `astype` to convert from timezone-naive dtype to timezone-aware dtype will raise an exception. Use [`Series.dt.tz_localize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize "pandas.Series.dt.tz_localize")
 instead.

Examples

Create a DataFrame:

\>>> d \= {"col1": \[1, 2\], "col2": \[3, 4\]}
\>>> df \= pd.DataFrame(data\=d)
\>>> df.dtypes
col1    int64
col2    int64
dtype: object

Copy to clipboard

Cast all columns to int32:

\>>> df.astype("int32").dtypes
col1    int32
col2    int32
dtype: object

Copy to clipboard

Cast col1 to int32 using a dictionary:

\>>> df.astype({"col1": "int32"}).dtypes
col1    int32
col2    int64
dtype: object

Copy to clipboard

Create a series:

\>>> ser \= pd.Series(\[1, 2\], dtype\="int32")
\>>> ser
0    1
1    2
dtype: int32
\>>> ser.astype("int64")
0    1
1    2
dtype: int64

Copy to clipboard

Convert to categorical type:

\>>> ser.astype("category")
0    1
1    2
dtype: category
Categories (2, int32): \[1, 2\]

Copy to clipboard

Convert to ordered categorical type with custom ordering:

\>>> from pandas.api.types import CategoricalDtype
\>>> cat\_dtype \= CategoricalDtype(categories\=\[2, 1\], ordered\=True)
\>>> ser.astype(cat\_dtype)
0    1
1    2
dtype: category
Categories (2, int64): \[2 < 1\]

Copy to clipboard

Create a series of dates:

\>>> ser\_date \= pd.Series(pd.date\_range("20200101", periods\=3))
\>>> ser\_date
0   2020-01-01
1   2020-01-02
2   2020-01-03
dtype: datetime64\[us\]

Copy to clipboard

On this page