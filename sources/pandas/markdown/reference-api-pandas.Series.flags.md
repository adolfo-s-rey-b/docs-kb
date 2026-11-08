[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.flags.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.flags.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.flags.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.flags.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.flags.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.flags.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.flags.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.flags.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.flags.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.flags.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.flags.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.flags.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.flags[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html#pandas-series-flags "Link to this heading")

=========================================================================================================================================

property Series.flags[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L375-L414)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html#pandas.Series.flags "Link to this definition")

Get the properties associated with this pandas object.

The available flags are

*   `Flags.allows_duplicate_labels`
    

See also

[`Flags`](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#pandas.Flags "pandas.Flags")

Flags that apply to pandas objects.

[`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")

Global metadata applying to this dataset.

Notes

“Flags” differ from “metadata”. Flags reflect properties of the pandas object (the Series or DataFrame). Metadata refer to properties of the dataset, and should be stored in [`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")
.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\]})
\>>> df.flags
<Flags(allows\_duplicate\_labels=True)>

Copy to clipboard

Flags can be get or set using `.`

\>>> df.flags.allows\_duplicate\_labels
True
\>>> df.flags.allows\_duplicate\_labels \= False

Copy to clipboard

Or by slicing with a key

\>>> df.flags\["allows\_duplicate\_labels"\]
False
\>>> df.flags\["allows\_duplicate\_labels"\] \= True

Copy to clipboard

On this page