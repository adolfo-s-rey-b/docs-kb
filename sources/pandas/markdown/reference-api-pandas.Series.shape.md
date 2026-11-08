[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.shape.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.shape.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.shape.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.shape.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.shape.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.shape.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.shape.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.shape.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.shape.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.shape.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.shape.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.shape.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.shape[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#pandas-series-shape "Link to this heading")

=========================================================================================================================================

property Series.shape[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L351-L372)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#pandas.Series.shape "Link to this definition")

Return a tuple of the shape of the underlying data.

For a Series this is `(length,)`; for a 1D Index, likewise a single-element tuple. Useful for compatibility with NumPy and other array-like APIs.

See also

[`Series.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ndim.html#pandas.Series.ndim "pandas.Series.ndim")

Number of dimensions of the underlying data.

[`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size")

Return the number of elements in the underlying data.

[`Series.nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nbytes.html#pandas.Series.nbytes "pandas.Series.nbytes")

Return the number of bytes in the underlying data.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.shape
(3,)

Copy to clipboard

On this page