[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.hasnans.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.hasnans.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.hasnans.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.hasnans.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.hasnans.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.hasnans.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.hasnans.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.hasnans.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.hasnans.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.hasnans.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.hasnans.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.hasnans.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.hasnans[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html#pandas-series-hasnans "Link to this heading")

===============================================================================================================================================

property Series.hasnans[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1020-L1050)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html#pandas.Series.hasnans "Link to this definition")

Return True if there are any NaNs.

Enables various performance speedups.

Returns:

bool

See also

[`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")

Detect missing values.

[`Series.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")

Detect existing (non-missing) values.

Examples

\>>> s \= pd.Series(\[1, 2, 3, None\])
\>>> s
0    1.0
1    2.0
2    3.0
3    NaN
dtype: float64
\>>> s.hasnans
True

Copy to clipboard

On this page