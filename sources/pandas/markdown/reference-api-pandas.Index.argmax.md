[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.argmax[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#pandas-index-argmax "Link to this heading")

=========================================================================================================================================

Index.argmax(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L8012-L8073)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#pandas.Index.argmax "Link to this definition")

Return int position of the largest value in the Index.

If the maximum is achieved in multiple locations, the first row position is returned.

Parameters:

**axis**None

Unused. Parameter needed for compatibility with DataFrame.

**skipna**bool, default True

Exclude NA/null values. If the entire Series is NA, or if `skipna=False` and there is an NA value, this method will raise a `ValueError`.

**\*args, \*\*kwargs**

Additional arguments and keywords for compatibility with NumPy.

Returns:

int

Row position of the maximum value.

See also

[`Series.argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas.Series.argmax "pandas.Series.argmax")

Return position of the maximum value.

[`Series.argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas.Series.argmin "pandas.Series.argmin")

Return position of the minimum value.

[`numpy.ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "(in NumPy v2.5)")

Equivalent method for numpy arrays.

[`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")

Return index label of the maximum values.

[`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")

Return index label of the minimum values.

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