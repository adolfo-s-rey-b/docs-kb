[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Flags.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Flags.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Flags.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Flags.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Flags.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Flags.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Flags.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Flags.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Flags.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Flags.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Flags.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Flags.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Flags[#](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#pandas-flags "Link to this heading")

====================================================================================================================

class pandas.Flags(_obj_, _\*_, _allows\_duplicate\_labels_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/flags.py#L12-L129)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#pandas.Flags "Link to this definition")

Flags that apply to pandas objects.

“Flags” differ from “metadata”. Flags reflect properties of the pandas object (the Series or DataFrame). Metadata refer to properties of the dataset, and should be stored in DataFrame.attrs.

Parameters:

**obj**Series or DataFrame

The object these flags are associated with.

**allows\_duplicate\_labels**bool, default True

Whether to allow duplicate labels in this object. By default, duplicate labels are permitted. Setting this to `False` will cause an [`errors.DuplicateLabelError`](https://pandas.pydata.org/docs/reference/api/pandas.errors.DuplicateLabelError.html#pandas.errors.DuplicateLabelError "pandas.errors.DuplicateLabelError")
 to be raised when index (or columns for DataFrame) is not unique, or any subsequent operation on introduces duplicates. See [Disallowing Duplicate Labels](https://pandas.pydata.org/docs/user_guide/duplicates.html#duplicates-disallow)
 for more.

Warning

This is an experimental feature. Currently, many methods fail to propagate the `allows_duplicate_labels` value. In future versions it is expected that every method taking or returning one or more DataFrame or Series objects will propagate `allows_duplicate_labels`.

See also

[`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")

Dictionary of global attributes of this dataset.

[`Series.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.attrs.html#pandas.Series.attrs "pandas.Series.attrs")

Dictionary of global attributes of this dataset.

Examples

Attributes can be set in two ways:

\>>> df \= pd.DataFrame()
\>>> df.flags
<Flags(allows\_duplicate\_labels=True)>
\>>> df.flags.allows\_duplicate\_labels \= False
\>>> df.flags
<Flags(allows\_duplicate\_labels=False)>

Copy to clipboard

\>>> df.flags\["allows\_duplicate\_labels"\] \= True
\>>> df.flags
<Flags(allows\_duplicate\_labels=True)>

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| `allows_duplicate_labels` | Whether this object allows duplicate labels. |

Methods

On this page