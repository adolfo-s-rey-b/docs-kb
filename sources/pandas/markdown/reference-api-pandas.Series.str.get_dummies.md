[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.get_dummies.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.get_dummies.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.get_dummies.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.get_dummies.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.get_dummies.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.get_dummies.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.get_dummies.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.get_dummies.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.get_dummies.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.get_dummies.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.get_dummies.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.get_dummies.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.get\_dummies[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html#pandas-series-str-get-dummies "Link to this heading")

========================================================================================================================================================================

Series.str.get\_dummies(_sep\='|'_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3008-L3075)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html#pandas.Series.str.get_dummies "Link to this definition")

Return DataFrame of dummy/indicator variables for Series.

Each string in Series is split by sep and returned as a DataFrame of dummy/indicator variables.

Parameters:

**sep**str, default “|”

String to split on.

**dtype**dtype, default np.int64

Data type for new columns. Only a single dtype is allowed.

Returns:

DataFrame

Dummy variables corresponding to values of the Series.

See also

[`get_dummies`](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas.get_dummies "pandas.get_dummies")

Convert categorical variable into dummy/indicator variables.

Examples

\>>> pd.Series(\["a|b", "a", "a|c"\]).str.get\_dummies()
   a  b  c
0  1  1  0
1  1  0  0
2  1  0  1

Copy to clipboard

\>>> pd.Series(\["a|b", np.nan, "a|c"\]).str.get\_dummies()
   a  b  c
0  1  1  0
1  0  0  0
2  1  0  1

Copy to clipboard

\>>> pd.Series(\["a|b", np.nan, "a|c"\]).str.get\_dummies(dtype\=bool)
        a      b      c
0   True   True    False
1   False  False   False
2   True   False   True

Copy to clipboard

On this page