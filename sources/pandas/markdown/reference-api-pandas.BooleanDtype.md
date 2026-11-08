[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.BooleanDtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.BooleanDtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.BooleanDtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.BooleanDtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.BooleanDtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.BooleanDtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.BooleanDtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.BooleanDtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.BooleanDtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.BooleanDtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.BooleanDtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.BooleanDtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.BooleanDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas-booleandtype "Link to this heading")

=========================================================================================================================================

class pandas.BooleanDtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/boolean.py#L46-L179)
[#](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "Link to this definition")

Extension dtype for boolean data.

This is a pandas Extension dtype for boolean data with support for missing values. BooleanDtype is the dtype companion to [`BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray")
, which implements Kleene logic (sometimes called three-value logic) for logical operations. See [Kleene logical operations](https://pandas.pydata.org/docs/user_guide/boolean.html#boolean-kleene)
 for more.

Warning

BooleanDtype is considered experimental. The implementation and parts of the API may change without warning.

See also

[`arrays.BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray")

Array of boolean (True/False) data with missing values.

[`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")

Extension dtype for int64 integer data.

[`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")

Extension dtype for string data.

Examples

\>>> pd.BooleanDtype()
BooleanDtype

Copy to clipboard

\>>> pd.array(\[True, False, None\], dtype\=pd.BooleanDtype())
<BooleanArray>
\[True, False, <NA>\]
Length: 3, dtype: boolean

Copy to clipboard

\>>> pd.array(\[True, False, None\], dtype\="boolean")
<BooleanArray>
\[True, False, <NA>\]
Length: 3, dtype: boolean

Copy to clipboard

On this page