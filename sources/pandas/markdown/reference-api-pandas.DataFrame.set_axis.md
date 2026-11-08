[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.set_axis.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.set_axis.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.set_axis.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.set_axis.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.set_axis.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.set_axis.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.set_axis.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.set_axis.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.set_axis.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.set_axis.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.set_axis.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.set_axis.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.set\_axis[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html#pandas-dataframe-set-axis "Link to this heading")

============================================================================================================================================================

DataFrame.set\_axis(_labels_, _\*_, _axis\=0_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6441-L6505)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html#pandas.DataFrame.set_axis "Link to this definition")

Assign desired index to given axis.

Indexes for column or row labels can be changed by assigning a list-like or Index.

Parameters:

**labels**list-like, Index

The values for the new index.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to update. The value 0 identifies the rows. For Series this parameter is unused and defaults to 0.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

DataFrame

An object of type DataFrame.

See also

[`DataFrame.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "pandas.DataFrame.rename_axis")

Alter the name of the index or columns.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[4, 5, 6\]})

Copy to clipboard

Change the row labels.

\>>> df.set\_axis(\["a", "b", "c"\], axis\="index")
    A  B
a  1  4
b  2  5
c  3  6

Copy to clipboard

Change the column labels.

\>>> df.set\_axis(\["I", "II"\], axis\="columns")
    I  II
0  1   4
1  2   5
2  3   6

Copy to clipboard

On this page