[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.testing.assert\_series\_equal[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#pandas-testing-assert-series-equal "Link to this heading")

========================================================================================================================================================================================

pandas.testing.assert\_series\_equal(_left_, _right_, _check\_dtype\=True_, _check\_index\_type\='equiv'_, _check\_series\_type\=True_, _check\_names\=True_, _check\_exact\=<no\_default>_, _check\_datetimelike\_compat\=False_, _check\_categorical\=True_, _check\_category\_order\=True_, _check\_freq\=<no\_default>_, _check\_flags\=True_, _rtol\=<no\_default>_, _atol\=<no\_default>_, _obj\='Series'_, _\*_, _check\_index\=True_, _check\_like\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_testing/asserters.py#L1031-L1345)
[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#pandas.testing.assert_series_equal "Link to this definition")

Check that left and right Series are equal.

This function compares two Series and raises an `AssertionError` if they are not equal. It provides fine-grained control over which attributes to check, including dtype, index, names, and categorical properties.

Parameters:

**left**Series

First Series to compare.

**right**Series

Second Series to compare.

**check\_dtype**bool, default True

Whether to check the Series dtype is identical.

**check\_index\_type**bool or {‘equiv’}, default ‘equiv’

Whether to check the Index class, dtype and inferred\_type are identical.

**check\_series\_type**bool, default True

Whether to check the Series class is identical.

**check\_names**bool, default True

Whether to check the Series and Index names attribute.

**check\_exact**bool, default False

Whether to compare number exactly. This also applies when checking Index equivalence.

Changed in version 2.2.0: Defaults to True for integer dtypes if none of `check_exact`, `rtol` and `atol` are specified.

Changed in version 3.0.0: check\_exact for comparing the Indexes defaults to True by checking if an Index is of integer dtypes.

When `check_exact=True`, the comparison of object-dtype values containing nested [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 objects takes the type of the nested object into account. In particular, a nested `numpy.ndarray` is not considered equivalent to a Python `list`, Python `tuple`, or a pandas [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 merely because the contained values are the same.

**check\_datetimelike\_compat**bool, default False

Compare datetime-like which is comparable ignoring dtype.

Deprecated since version 3.0.

**check\_categorical**bool, default True

Whether to compare internal Categorical exactly.

**check\_category\_order**bool, default True

Whether to compare category order of internal Categoricals.

**check\_freq**bool, default True

Whether to check the freq attribute on a DatetimeIndex or TimedeltaIndex. The index check is skipped if `check_index=False` or `check_like=True`.

Deprecated since version 3.1.0: The `freq` attribute of a `DatetimeIndex`/ `TimedeltaIndex` MultiIndex level or Categorical categories is not yet checked by default; a mismatch currently only warns and will raise in a future version. Pass `check_freq` explicitly to silence the warning.

**check\_flags**bool, default True

Whether to check the flags attribute.

**rtol**float, default 1e-5

Relative tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**atol**float, default 1e-8

Absolute tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**obj**str, default ‘Series’

Specify object name being compared, internally used to show appropriate assertion message.

**check\_index**bool, default True

Whether to check index equivalence. If False, then compare only values.

**check\_like**bool, default False

If True, ignore the order of the index. Must be False if check\_index is False. Note: same labels must be with the same data.

See also

`testing.assert_index_equal`

Check that two Indexes are equal.

`testing.assert_frame_equal`

Check that two DataFrames are equal.

Examples

\>>> from pandas import testing as tm
\>>> a \= pd.Series(\[1, 2, 3, 4\])
\>>> b \= pd.Series(\[1, 2, 3, 4\])
\>>> tm.assert\_series\_equal(a, b)

Copy to clipboard

On this page