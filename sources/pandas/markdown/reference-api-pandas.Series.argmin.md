[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.argmin[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas-series-argmin "Link to this heading")

============================================================================================================================================

Series.argmin(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L873-L946)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas.Series.argmin "Link to this definition")

Return int position of the smallest value in the Series.

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

\>>> s \= pd.Series(
...     \[100.0, 110.0, 120.0, 110.0\],
...     index\=\[\
...         "Corn Flakes",\
...         "Almond Delight",\
...         "Cinnamon Toast Crunch",\
...         "Cocoa Puff",\
...     \],
... )
\>>> s
Corn Flakes              100.0
Almond Delight           110.0
Cinnamon Toast Crunch    120.0
Cocoa Puff               110.0
dtype: float64

Copy to clipboard

\>>> s.argmax()
2
\>>> s.argmin()
0

Copy to clipboard

The maximum cereal calories is the third element and the minimum cereal calories is the first element, since series is zero-indexed.

On this page