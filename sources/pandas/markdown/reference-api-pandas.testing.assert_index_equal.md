[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_index_equal.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.testing.assert\_index\_equal[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_index_equal.html#pandas-testing-assert-index-equal "Link to this heading")

=====================================================================================================================================================================================

pandas.testing.assert\_index\_equal(_left_, _right_, _exact\=<no\_default>_, _check\_names\=True_, _check\_exact\=True_, _check\_categorical\=True_, _check\_order\=True_, _rtol\=1e-05_, _atol\=1e-08_, _obj\=None_, _\*_, _check\_freq\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_testing/asserters.py#L218-L499)
[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_index_equal.html#pandas.testing.assert_index_equal "Link to this definition")

Check that left and right Index are equal.

This function compares two Index objects and raises an `AssertionError` if they are not equal. It provides fine-grained control over which attributes to check, including dtype, names, and categorical properties.

Parameters:

**left**Index

The first index to compare.

**right**Index

The second index to compare.

**exact**bool or {‘equiv’}, default ‘equiv’

Whether to check the Index class, dtype and inferred\_type are identical. If ‘equiv’, then RangeIndex can be substituted for Index with an int64 dtype as well.

Deprecated since version 3.1.0: The default value of ‘equiv’ has been deprecated and will be changed to True in the future.

**check\_names**bool, default True

Whether to check the names attribute.

**check\_exact**bool, default True

Whether to compare number exactly.

**check\_categorical**bool, default True

Whether to compare internal Categorical exactly.

**check\_order**bool, default True

Whether to compare the order of index entries as well as their values. If True, both indexes must contain the same elements, in the same order. If False, both indexes must contain the same elements, but in any order.

**rtol**float, default 1e-5

Relative tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**atol**float, default 1e-8

Absolute tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**obj**str, default ‘Index’ or ‘MultiIndex’

Specify object name being compared, internally used to show appropriate assertion message.

**check\_freq**bool, default True

Whether to check the `freq` attribute on a DatetimeIndex or TimedeltaIndex. This check is skipped when `check_order=False`, as sorting does not preserve `freq`.

Added in version 3.1.0.

Deprecated since version 3.1.0: Currently a `freq` mismatch only warns; in a future version `check_freq=True` will be the default and mismatches will raise. Pass `check_freq` explicitly to silence the warning.

See also

`testing.assert_series_equal`

Check that two Series are equal.

`testing.assert_frame_equal`

Check that two DataFrames are equal.

Examples

\>>> from pandas import testing as tm
\>>> a \= pd.Index(\[1, 2, 3\])
\>>> b \= pd.Index(\[1, 2, 3\])
\>>> tm.assert\_index\_equal(a, b)

Copy to clipboard

On this page