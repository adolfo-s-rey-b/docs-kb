[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.argsort.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.argsort.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.argsort.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.argsort.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.argsort.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.argsort.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.argsort.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.argsort.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.argsort.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.argsort.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.argsort.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.argsort.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.argsort[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html#pandas-series-argsort "Link to this heading")

===============================================================================================================================================

Series.argsort(_axis\=0_, _kind\='quicksort'_, _order\=None_, _stable\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4460-L4513)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html#pandas.Series.argsort "Link to this definition")

Return the integer indices that would sort the Series values.

Override ndarray.argsort. Argsorts the value, omitting NA/null values, and places the result in the same locations as the non-NA values.

Parameters:

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**kind**{‘mergesort’, ‘quicksort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Choice of sorting algorithm. See [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "(in NumPy v2.5)")
 for more information. ‘mergesort’ and ‘stable’ are the only stable algorithms.

**order**None

Has no effect but is accepted for compatibility with numpy.

**stable**None

Has no effect but is accepted for compatibility with numpy.

Returns:

Series\[np.intp\]

Positions of values within the sort order with -1 indicating nan values.

See also

[`numpy.ndarray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html#numpy.ndarray.argsort "(in NumPy v2.5)")

Returns the indices that would sort this array.

Examples

\>>> s \= pd.Series(\[3, 2, 1\])
\>>> s.argsort()
0    2
1    1
2    0
dtype: int64

Copy to clipboard

On this page