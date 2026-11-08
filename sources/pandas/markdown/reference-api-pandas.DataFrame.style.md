[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.style.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.style.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.style.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.style.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.style.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.style.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.style.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.style.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.style.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.style.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.style.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.style.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.style[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#pandas-dataframe-style "Link to this heading")

==================================================================================================================================================

property DataFrame.style[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1235-L1262)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#pandas.DataFrame.style "Link to this definition")

Returns a Styler object.

Contains methods for building a styled HTML representation of the DataFrame.

See also

[`io.formats.style.Styler`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html#pandas.io.formats.style.Styler "pandas.io.formats.style.Styler")

Helps style a DataFrame or Series according to the data with HTML and CSS.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\]})
\>>> df.style

Copy to clipboard

Please see [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page