[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.argmax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.argmax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.argmax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.argmax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.argmax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.argmax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.argmax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.argmax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.argmax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.argmax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.argmax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.argmax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.argmax[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas-series-argmax "Link to this heading")

============================================================================================================================================

Series.argmax(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L798-L871)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas.Series.argmax "Link to this definition")

Return int position of the largest value in the Series.

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