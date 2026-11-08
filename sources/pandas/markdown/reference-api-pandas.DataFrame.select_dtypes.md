[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.select_dtypes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.select_dtypes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.select_dtypes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.select_dtypes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.select_dtypes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.select_dtypes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.select_dtypes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.select_dtypes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.select_dtypes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.select_dtypes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.select_dtypes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.select_dtypes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.select\_dtypes[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas-dataframe-select-dtypes "Link to this heading")

===========================================================================================================================================================================

DataFrame.select\_dtypes(_include\=None_, _exclude\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L5439-L6009)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "Link to this definition")

Return a subset of the DataFrame’s columns based on the column dtypes.

This method allows for filtering columns based on their data types. It is useful when working with heterogeneous DataFrames where operations need to be performed on a specific subset of data types.

Parameters:

**include, exclude**scalar or list-like

A selection of dtypes or strings to be included/excluded. At least one of these parameters must be supplied.

Returns:

DataFrame

The subset of the frame including the dtypes in `include` and excluding the dtypes in `exclude`.

Raises:

ValueError

*   If both of `include` and `exclude` are empty
    
*   If `include` and `exclude` have overlapping elements
    
*   If a datetime64/timedelta64 spec, or an interval spec’s subtype, names a resolution no column can have, e.g. `'datetime64[10s]'`
    
*   If an [`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype")
     or [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
     spec gives some of its attributes but not all, or leaves an interval subtype’s resolution unset, e.g. `pd.IntervalDtype('int64')` or `'interval[datetime64]'`
    

TypeError

*   If a numpy string or bytes dtype is passed in, e.g. `np.str_`, `'<U8'` or `bytes`
    

See also

[`DataFrame.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes "pandas.DataFrame.dtypes")

Return Series with the data type of each column.

Notes

*   To select all _numeric_ types, use `np.number` or `'number'`
    
*   To select strings, use the builtin `str`, which selects [`pandas.StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")
     columns and [`pandas.ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     `string`/`large_string` columns; the string spec `'str'` selects only the [`pandas.StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")
     ones
    
*   See the [numpy dtype hierarchy](https://numpy.org/doc/stable/reference/arrays.scalars.html)
    
*   A dtype instance (e.g. `np.dtype("int32")` or `pd.CategoricalDtype(["a", "b"])`) selects only columns with exactly that dtype, whereas a class or string selects a family of dtypes. A bare `pd.CategoricalDtype()` or `pd.IntervalDtype()` names the family too, but an instance that gives some of its attributes and not others raises, since no column has such a dtype: `pd.IntervalDtype("int64")` leaves `closed` unset, `pd.CategoricalDtype(ordered=True)` the categories
    
*   To select datetimes, use `np.datetime64`, `'datetime'` or `'datetime64'`
    
*   To select timedeltas, use `np.timedelta64`, `'timedelta'` or `'timedelta64'`
    
*   To select datetimes or timedeltas of a specific resolution, pass a unit-qualified dtype such as `'datetime64[us]'` or `'timedelta64[ms]'`; this matches only columns with exactly that resolution, whereas an unqualified spec matches every resolution
    
*   To select Pandas categorical dtypes, use `'category'`
    
*   To select all timezone-aware datetime dtypes, use `'datetimetz'` or [`pandas.DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype")
    ; a string such as `'datetime64[ns, US/Eastern]'` selects only that exact dtype
    
*   To select all period dtypes, use [`pandas.PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")
    ; a string such as `'period[D]'` selects only that frequency
    
*   An [`ExtensionDtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionDtype.html#pandas.api.extensions.ExtensionDtype "pandas.api.extensions.ExtensionDtype")
     subclass matches every instance of that subclass regardless of parametrization, e.g. `pd.ArrowDtype` selects all pyarrow-backed columns and `pd.CategoricalDtype` selects all categorical columns
    

Examples

\>>> df \= pd.DataFrame(
...     {"a": \[1, 2\] \* 3, "b": \[True, False\] \* 3, "c": \[1.0, 2.0\] \* 3}
... )
\>>> df
        a      b  c
0       1   True  1.0
1       2  False  2.0
2       1   True  1.0
3       2  False  2.0
4       1   True  1.0
5       2  False  2.0

Copy to clipboard

\>>> df.select\_dtypes(include\="bool")
   b
0  True
1  False
2  True
3  False
4  True
5  False

Copy to clipboard

\>>> df.select\_dtypes(include\=\["float64"\])
   c
0  1.0
1  2.0
2  1.0
3  2.0
4  1.0
5  2.0

Copy to clipboard

\>>> df.select\_dtypes(exclude\=\["int64"\])
       b    c
0   True  1.0
1  False  2.0
2   True  1.0
3  False  2.0
4   True  1.0
5  False  2.0

Copy to clipboard

On this page