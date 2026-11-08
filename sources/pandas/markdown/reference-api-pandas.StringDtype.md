[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.StringDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas-stringdtype "Link to this heading")

======================================================================================================================================

class pandas.StringDtype(_storage\=None_, _na\_value\=<NA>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/string_.py#L100-L404)
[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "Link to this definition")

Extension dtype for string data.

Warning

StringDtype is considered experimental. The implementation and parts of the API may change without warning.

Parameters:

**storage**{“python”, “pyarrow”}, optional

If not given, the value of `pd.options.mode.string_storage`.

**na\_value**{np.nan, pd.NA}, default pd.NA

Whether the dtype follows NaN or NA missing value semantics.

Attributes

|     |     |
| --- | --- |
| [`storage`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.storage.html#pandas.StringDtype.storage "pandas.StringDtype.storage") | The storage backend for this dtype. |
| [`na_value`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html#pandas.StringDtype.na_value "pandas.StringDtype.na_value") | The missing value representation for this dtype. |

See also

[`BooleanDtype`](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype")

Extension dtype for boolean data.

Examples

\>>> pd.StringDtype()
<StringDtype(na\_value=<NA>)>

Copy to clipboard

\>>> pd.StringDtype(storage\="python")
<StringDtype(storage='python', na\_value=<NA>)>

Copy to clipboard

On this page