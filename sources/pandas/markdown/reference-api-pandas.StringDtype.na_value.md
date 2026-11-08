[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.StringDtype.na_value.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.StringDtype.na_value.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.StringDtype.na_value.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.StringDtype.na_value.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.StringDtype.na_value.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.StringDtype.na_value.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.StringDtype.na_value.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.StringDtype.na_value.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.StringDtype.na_value.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.StringDtype.na_value.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.StringDtype.na_value.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.StringDtype.na_value.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.StringDtype.na\_value[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html#pandas-stringdtype-na-value "Link to this heading")

==================================================================================================================================================================

property StringDtype.na\_value[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/string_.py#L149-L171)
[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html#pandas.StringDtype.na_value "Link to this definition")

The missing value representation for this dtype.

This value indicates which missing value semantics are used by this dtype. Returns `np.nan` for the default string dtype with NumPy semantics, and `pd.NA` for the opt-in string dtype with pandas NA semantics.

See also

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Detect missing values.

[`NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")

Missing value indicator for nullable dtypes.

Examples

\>>> ser \= pd.Series(\["a", "b"\])
\>>> ser.dtype
<StringDtype(na\_value=nan)>
\>>> ser.dtype.na\_value
nan

Copy to clipboard

On this page