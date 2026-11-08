[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_frame.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_frame.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_frame.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_frame.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_frame.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_frame.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_frame.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_frame.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_frame.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_frame.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_frame.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_frame.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_frame[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas-series-to-frame "Link to this heading")

===================================================================================================================================================

Series.to\_frame(_name\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1986-L2031)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "Link to this definition")

Convert Series to DataFrame.

The resulting DataFrame contains a single column. The name of the column can be set using the `name` parameter; otherwise it defaults to the Series’ name.

Parameters:

**name**object, optional

The passed name should substitute for the series name (if it has one).

Returns:

DataFrame

DataFrame representation of Series.

See also

[`Series.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict "pandas.Series.to_dict")

Convert Series to dict object.

Examples

\>>> s \= pd.Series(\["a", "b", "c"\], name\="vals")
\>>> s.to\_frame()
  vals
0    a
1    b
2    c

Copy to clipboard

On this page