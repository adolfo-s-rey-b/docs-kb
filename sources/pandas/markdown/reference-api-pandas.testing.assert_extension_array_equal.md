[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_extension_array_equal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.testing.assert_extension_array_equal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_extension_array_equal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.testing.assert_extension_array_equal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.testing.assert_extension_array_equal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.testing.assert_extension_array_equal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.testing.assert_extension_array_equal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.testing.assert_extension_array_equal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.testing.assert_extension_array_equal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.testing.assert\_extension\_array\_equal[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_extension_array_equal.html#pandas-testing-assert-extension-array-equal "Link to this heading")

====================================================================================================================================================================================================================

pandas.testing.assert\_extension\_array\_equal(_left_, _right_, _check\_dtype\=True_, _index\_values\=None_, _check\_exact\=<no\_default>_, _rtol\=<no\_default>_, _atol\=<no\_default>_, _obj\='ExtensionArray'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/_testing/asserters.py#L871-L1027)
[#](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_extension_array_equal.html#pandas.testing.assert_extension_array_equal "Link to this definition")

Check that left and right ExtensionArrays are equal.

This method compares two `ExtensionArray` instances for equality, including checks for missing values, the dtype of the arrays, and the exactness of the comparison (or tolerance when comparing floats).

Parameters:

**left, right**ExtensionArray

The two arrays to compare.

**check\_dtype**bool, default True

Whether to check if the ExtensionArray dtypes are identical.

**index\_values**Index | numpy.ndarray, default None

Optional index (shared by both left and right), used in output.

**check\_exact**bool, default False

Whether to compare number exactly.

Changed in version 2.2.0: Defaults to True for integer dtypes if none of `check_exact`, `rtol` and `atol` are specified.

**rtol**float, default 1e-5

Relative tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**atol**float, default 1e-8

Absolute tolerance. Only used when check\_exact is False, and only applied to numeric dtypes; values of other dtypes, such as interval, are always compared exactly.

**obj**str, default ‘ExtensionArray’

Specify object name being compared, internally used to show appropriate assertion message.

Added in version 2.0.0.

See also

`testing.assert_series_equal`

Check that left and right `Series` are equal.

`testing.assert_frame_equal`

Check that left and right `DataFrame` are equal.

`testing.assert_index_equal`

Check that left and right `Index` are equal.

Notes

Missing values are checked separately from valid values. A mask of missing values is computed for each and checked to match. The remaining all-valid values are cast to object dtype and checked.

Examples

\>>> from pandas import testing as tm
\>>> a \= pd.Series(\[1, 2, 3, 4\])
\>>> b, c \= a.array, a.array
\>>> tm.assert\_extension\_array\_equal(b, c)

Copy to clipboard

On this page