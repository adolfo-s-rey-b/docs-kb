[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.count.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.count.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.count.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.count.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.count.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.count.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.count.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.count.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.count.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.count.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.count.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.count.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.count[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas-series-count "Link to this heading")

=========================================================================================================================================

Series.count()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2358-L2380)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "Link to this definition")

Return number of non-NA/null observations in the Series.

This method counts the number of elements that are not missing (i.e., not NaN or None) in the Series.

Returns:

int

Number of non-null values in the Series.

See also

[`DataFrame.count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")

Count non-NA cells for each column or row.

Examples

\>>> s \= pd.Series(\[0.0, 1.0, np.nan\])
\>>> s.count()
2

Copy to clipboard

On this page