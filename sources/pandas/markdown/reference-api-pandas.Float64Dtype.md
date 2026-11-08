[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Float64Dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Float64Dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Float64Dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Float64Dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Float64Dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Float64Dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Float64Dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Float64Dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Float64Dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Float64Dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Float64Dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Float64Dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Float64Dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas-float64dtype "Link to this heading")

=========================================================================================================================================

class pandas.Float64Dtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/floating.py#L181-L186)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "Link to this definition")

An ExtensionDtype for float64 data.

This dtype uses `pd.NA` as missing value indicator.

See also

[`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")

Type for categorical data with the categories and orderedness.

`IntegerDtype`

An ExtensionDtype to hold a single size & kind of integer dtype.

[`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")

An ExtensionDtype for string data.

Examples

For Float32Dtype:

\>>> ser \= pd.Series(\[2.25, pd.NA\], dtype\=pd.Float32Dtype())
\>>> ser.dtype
Float32Dtype()

Copy to clipboard

For Float64Dtype:

\>>> ser \= pd.Series(\[2.25, pd.NA\], dtype\=pd.Float64Dtype())
\>>> ser.dtype
Float64Dtype()

Copy to clipboard

On this page