[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.set_axis.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.set_axis.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.set_axis.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.set_axis.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.set_axis.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.set_axis.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.set_axis.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.set_axis.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.set_axis.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.set_axis.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.set_axis.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.set_axis.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.set\_axis[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html#pandas-series-set-axis "Link to this heading")

===================================================================================================================================================

Series.set\_axis(_labels_, _\*_, _axis\=0_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5740-L5796)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html#pandas.Series.set_axis "Link to this definition")

Assign desired index to given axis.

Indexes for row labels can be changed by assigning a list-like or Index.

Parameters:

**labels**list-like or Index

The values for the new index.

**axis**{0 or ‘index’}, default 0

The axis to update. The value 0 identifies the rows. For Series this parameter is unused and defaults to 0.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

Series

A shallow copy of the object with axis altered to the given index.

See also

[`Series.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis "pandas.Series.rename_axis")

Alter the name of the index.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s
0    1
1    2
2    3
dtype: int64
\>>> s.set\_axis(\["a", "b", "c"\], axis\=0)
a    1
b    2
c    3
dtype: int64

Copy to clipboard

On this page