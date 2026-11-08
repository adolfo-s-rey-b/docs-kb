[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.shape.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.shape.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.shape.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.shape.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.shape.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.shape.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.shape.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.shape.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.shape.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.shape.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.shape.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.shape.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.shape[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas-dataframe-shape "Link to this heading")

==================================================================================================================================================

property DataFrame.shape[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L804-L827)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape "Link to this definition")

Return a tuple representing the dimensionality of the DataFrame.

Unlike the len() method, which only returns the number of rows, shape provides both row and column counts, making it a more informative method for understanding dataset size.

See also

[`numpy.ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "(in NumPy v2.5)")

Tuple of array dimensions.

Examples

\>>> df \= pd.DataFrame({"col1": \[1, 2\], "col2": \[3, 4\]})
\>>> df.shape
(2, 2)

Copy to clipboard

\>>> df \= pd.DataFrame({"col1": \[1, 2\], "col2": \[3, 4\], "col3": \[5, 6\]})
\>>> df.shape
(2, 3)

Copy to clipboard

On this page