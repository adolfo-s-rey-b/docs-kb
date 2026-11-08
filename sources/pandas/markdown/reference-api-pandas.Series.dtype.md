[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas-series-dtype "Link to this heading")

=========================================================================================================================================

property Series.dtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L656-L678)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype "Link to this definition")

Return the dtype object of the underlying data.

This is the dtype of the array backing the Series (or the single dtype for a DataFrame column). For extension types, it returns the corresponding extension dtype.

See also

[`Series.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes "pandas.Series.dtypes")

Return the dtype object of the underlying data.

[`Series.astype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html#pandas.Series.astype "pandas.Series.astype")

Cast a pandas object to a specified dtype dtype.

[`Series.convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes")

Convert columns to the best possible dtypes using dtypes supporting pd.NA.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.dtype
dtype('int64')

Copy to clipboard

On this page