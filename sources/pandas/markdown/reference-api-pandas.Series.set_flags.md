[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.set_flags.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.set_flags.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.set_flags.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.set_flags.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.set_flags.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.set_flags.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.set_flags.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.set_flags.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.set_flags.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.set_flags.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.set_flags.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.set_flags.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.set\_flags[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html#pandas-series-set-flags "Link to this heading")

======================================================================================================================================================

Series.set\_flags(_\*_, _copy\=<no\_default>_, _allows\_duplicate\_labels\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L416-L485)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html#pandas.Series.set_flags "Link to this definition")

Return a new object with updated flags.

This method creates a shallow copy of the original object, preserving its underlying data while modifying its global flags. In particular, it allows you to update properties such as whether duplicate labels are permitted. This behavior is especially useful in method chains, where one wishes to adjust DataFrame or Series characteristics without altering the original object.

Parameters:

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**allows\_duplicate\_labels**bool, optional

Whether the returned object allows duplicate labels.

Returns:

Series or DataFrame

The same type as the caller.

See also

[`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")

Global metadata applying to this dataset.

`DataFrame.flags`

Global flags applying to this object.

Notes

This method returns a new object that’s a view on the same data as the input. Mutating the input or the output values will be reflected in the other.

This method is intended to be used in method chains.

“Flags” differ from “metadata”. Flags reflect properties of the pandas object (the Series or DataFrame). Metadata refer to properties of the dataset, and should be stored in [`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")
.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\]})
\>>> df.flags.allows\_duplicate\_labels
True
\>>> df2 \= df.set\_flags(allows\_duplicate\_labels\=False)
\>>> df2.flags.allows\_duplicate\_labels
False

Copy to clipboard

On this page