[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.argmin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.argmin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.argmin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.argmin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.argmin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.argmin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.argmin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.argmin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.argmin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.argmin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.argmin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.argmin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.argmin[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#pandas-index-argmin "Link to this heading")

=========================================================================================================================================

Index.argmin(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7948-L8010)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#pandas.Index.argmin "Link to this definition")

Return int position of the smallest value in the Index.

If the minimum is achieved in multiple locations, the first row position is returned.

Parameters:

**axis**None

Unused. Parameter needed for compatibility with DataFrame.

**skipna**bool, default True

Exclude NA/null values. If the entire Series is NA, or if `skipna=False` and there is an NA value, this method will raise a `ValueError`.

**\*args, \*\*kwargs**

Additional arguments and keywords for compatibility with NumPy.

Returns:

int

Row position of the minimum value.

See also

[`Series.argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas.Series.argmin "pandas.Series.argmin")

Return position of the minimum value.

[`Series.argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas.Series.argmax "pandas.Series.argmax")

Return position of the maximum value.

[`numpy.ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "(in NumPy v2.5)")

Equivalent method for numpy arrays.

[`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")

Return index label of the minimum values.

[`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")

Return index label of the maximum values.

Examples

Consider dataset containing cereal calories

\>>> idx \= pd.Index(\[100.0, 110.0, 120.0, 110.0\])
\>>> idx
Index(\[100.0, 110.0, 120.0, 110.0\], dtype='float64')

Copy to clipboard

\>>> idx.argmax()
2
\>>> idx.argmin()
0

Copy to clipboard

The maximum cereal calories is the third element and the minimum cereal calories is the first element, since index is zero-indexed.

On this page