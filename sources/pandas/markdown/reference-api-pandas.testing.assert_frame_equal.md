[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.testing.assert_frame_equal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.testing.assert_frame_equal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.testing.assert_frame_equal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.testing.assert_frame_equal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.testing.assert_frame_equal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.testing.assert_frame_equal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.testing.assert_frame_equal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.testing.assert_frame_equal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.testing.assert_frame_equal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.testing.assert_frame_equal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.testing.assert_frame_equal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.testing.assert_frame_equal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.testing.assert\_frame\_equal[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html#pandas-testing-assert-frame-equal "Link to this heading")

=====================================================================================================================================================================================

pandas.testing.assert\_frame\_equal(_left_, _right_, _check\_dtype\=True_, _check\_index\_type\='equiv'_, _check\_column\_type\='equiv'_, _check\_frame\_type\=True_, _check\_names\=True_, _by\_blocks\=False_, _check\_exact\=<no\_default>_, _check\_datetimelike\_compat\=False_, _check\_categorical\=True_, _check\_like\=False_, _check\_freq\=<no\_default>_, _check\_flags\=True_, _rtol\=<no\_default>_, _atol\=<no\_default>_, _obj\='DataFrame'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_testing/asserters.py#L1349-L1605)
[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html#pandas.testing.assert_frame_equal "Link to this definition")

Check that left and right DataFrame are equal.

This function is intended to compare two DataFrames and output any differences. It is mostly intended for use in unit tests. Additional parameters allow varying the strictness of the equality checks performed.

Parameters:

**left**DataFrame

First DataFrame to compare.

**right**DataFrame

Second DataFrame to compare.

**check\_dtype**bool, default True

Whether to check the DataFrame dtype is identical.

**check\_index\_type**bool or {‘equiv’}, default ‘equiv’

Whether to check the Index class, dtype and inferred\_type are identical.

**check\_column\_type**bool or {‘equiv’}, default ‘equiv’

Whether to check the columns class, dtype and inferred\_type are identical. Is passed as the `exact` argument of [`assert_index_equal()`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_index_equal.html#pandas.testing.assert_index_equal "pandas.testing.assert_index_equal")
.

**check\_frame\_type**bool, default True

Whether to check the DataFrame class is identical.

**check\_names**bool, default True

Whether to check that the names attribute for both the index and column attributes of the DataFrame is identical.

**by\_blocks**bool, default False

Specify how to compare internal data. If False, compare by columns. If True, compare by blocks.

Deprecated since version 3.1.

**check\_exact**bool, default False

Whether to compare number exactly. If False, the comparison uses the relative tolerance (`rtol`) and absolute tolerance (`atol`) parameters to determine if two values are considered close, according to the formula: `|a - b| <= (atol + rtol * |b|)`.

Changed in version 2.2.0: Defaults to True for integer dtypes if none of `check_exact`, `rtol` and `atol` are specified.

Changed in version 3.0.0: When `check_exact=True`, the comparison of object-dtype values containing nested [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 objects takes the type of the nested object into account. In particular, a nested `numpy.ndarray` is not considered equivalent to a Python `list`, Python `tuple`, or a pandas [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 merely because the contained values are the same.

**check\_datetimelike\_compat**bool, default False

Compare datetime-like which is comparable ignoring dtype.

Deprecated since version 3.0.

**check\_categorical**bool, default True

Whether to compare internal Categorical exactly.

**check\_like**bool, default False

If True, ignore the order of index & columns. Note: index labels must match their respective rows (same as in columns) - same labels must be with the same data.

**check\_freq**bool, default True

Whether to check the freq attribute on a DatetimeIndex or TimedeltaIndex index or columns. The index and columns checks are skipped if `check_like=True`.

Deprecated since version 3.1.0: The `freq` attribute of `DatetimeIndex`/`TimedeltaIndex` columns, MultiIndex levels, and Categorical categories is not yet checked by default; a mismatch currently only warns and will raise in a future version. Pass `check_freq` explicitly to silence the warning.

**check\_flags**bool, default True

Whether to check the flags attribute.

**rtol**float, default 1e-5

Relative tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**atol**float, default 1e-8

Absolute tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**obj**str, default ‘DataFrame’

Specify object name being compared, internally used to show appropriate assertion message.

See also

[`assert_series_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#pandas.testing.assert_series_equal "pandas.testing.assert_series_equal")

Equivalent method for asserting Series equality.

`DataFrame.equals`

Check DataFrame equality.

Examples

This example shows comparing two DataFrames that are equal but with columns of differing dtypes.

\>>> from pandas.testing import assert\_frame\_equal
\>>> df1 \= pd.DataFrame({"a": \[1, 2\], "b": \[3, 4\]})
\>>> df2 \= pd.DataFrame({"a": \[1, 2\], "b": \[3.0, 4.0\]})

Copy to clipboard

df1 equals itself.

\>>> assert\_frame\_equal(df1, df1)

Copy to clipboard

df1 differs from df2 as column ‘b’ is of a different type.

\>>> assert\_frame\_equal(df1, df2)
Traceback (most recent call last):
...
AssertionError: Attributes of DataFrame.iloc\[:, 1\] (column name="b") are different

Copy to clipboard

Attribute “dtype” are different \[left\]: int64 \[right\]: float64

Ignore differing dtypes in columns with check\_dtype.

\>>> assert\_frame\_equal(df1, df2, check\_dtype\=False)

Copy to clipboard

On this page