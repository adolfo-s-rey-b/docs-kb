[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.rename_axis.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.rename_axis.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.rename_axis.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.rename_axis.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.rename_axis.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.rename_axis.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.rename_axis.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.rename_axis.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.rename_axis.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.rename_axis.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.rename_axis.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.rename_axis.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.rename\_axis[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas-series-rename-axis "Link to this heading")

============================================================================================================================================================

Series.rename\_axis(_mapper\=<no\_default>_, _\*_, _index\=<no\_default>_, _axis\=0_, _copy\=<no\_default>_, _inplace\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6078-L6166)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis "Link to this definition")

Set the name of the axis for the index.

This method sets or changes the name of the index (axis) of the Series. It can accept a scalar, list-like, or function to rename the axis.

Parameters:

**mapper**scalar, list-like, optional

Value to set the axis name attribute.

Use either `mapper` and `axis` to specify the axis to target with `mapper`, or `index`.

**index**scalar, list-like, dict-like or function, optional

A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.

**axis**{0 or ‘index’}, default 0

The axis to rename. For Series this parameter is unused and defaults to 0.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**inplace**bool, default False

Modifies the object directly, instead of creating a new Series or DataFrame.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

Returns:

Series, or None

The same type as the caller or None if `inplace=True`.

See also

[`Series.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename")

Alter Series index labels or name.

[`DataFrame.rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")

Alter DataFrame index labels or name.

[`Index.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")

Set new names on index.

Examples

\>>> s \= pd.Series(\["dog", "cat", "monkey"\])
\>>> s
0       dog
1       cat
2    monkey
dtype: str
\>>> s.rename\_axis("animal")
animal
0    dog
1    cat
2    monkey
dtype: str

Copy to clipboard

On this page