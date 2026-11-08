[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html#pandas-series-str "Link to this heading")

===================================================================================================================================

Series.str()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L150-L4811)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html#pandas.Series.str "Link to this definition")

Vectorized string functions for Series and Index.

NAs stay NA unless handled otherwise by a particular method. Patterned after Python’s string methods, with some inspiration from R’s stringr package.

Parameters:

**data**Series or Index

The content of the Series or Index.

See also

[`Series.str`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html#pandas.Series.str "pandas.Series.str")

Vectorized string functions for Series.

[`Index.str`](https://pandas.pydata.org/docs/reference/api/pandas.Index.str.html#pandas.Index.str "pandas.Index.str")

Vectorized string functions for Index.

Examples

\>>> s \= pd.Series(\["A\_Str\_Series"\])
\>>> s
0    A\_Str\_Series
dtype: str

Copy to clipboard

\>>> s.str.split("\_")
0    \[A, Str, Series\]
dtype: object

Copy to clipboard

\>>> s.str.replace("\_", "")
0    AStrSeries
dtype: str

Copy to clipboard

On this page