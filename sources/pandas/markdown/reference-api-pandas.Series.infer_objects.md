[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.infer\_objects[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas-series-infer-objects "Link to this heading")

==================================================================================================================================================================

Series.infer\_objects(_copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6922-L6980)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects "Link to this definition")

Attempt to infer better dtypes for object columns.

Attempts soft conversion of object-dtyped columns, leaving non-object and unconvertible columns unchanged. The inference rules are the same as during normal Series/DataFrame construction.

Parameters:

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

same type as input object

Returns an object of the same type as the input object.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`to_numeric`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric "pandas.to_numeric")

Convert argument to numeric type.

[`convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes")

Convert argument to best possible dtype.

Examples

\>>> df \= pd.DataFrame({"A": \["a", 1, 2, 3\]})
\>>> df \= df.iloc\[1:\]
\>>> df
   A
1  1
2  2
3  3

Copy to clipboard

\>>> df.dtypes
A    object
dtype: object

Copy to clipboard

\>>> df.infer\_objects().dtypes
A    int64
dtype: object

Copy to clipboard

On this page