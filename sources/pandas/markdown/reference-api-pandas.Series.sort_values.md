[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sort_values.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sort_values.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sort_values.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sort_values.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sort_values.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sort_values.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sort_values.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sort_values.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sort_values.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sort_values.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sort_values.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sort_values.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sort\_values[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas-series-sort-values "Link to this heading")

============================================================================================================================================================

Series.sort\_values(_\*_, _axis\=0_, _ascending\=True_, _inplace\=<no\_default>_, _kind\='quicksort'_, _na\_position\='last'_, _ignore\_index\=False_, _key\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4052-L4258)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "Link to this definition")

Sort by the values.

Sort a Series in ascending or descending order by some criterion.

Parameters:

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**ascending**bool or list of bools, default True

If True, sort values in ascending order, otherwise descending.

**inplace**bool, default False

If True, perform operation in-place.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Choice of sorting algorithm. See also [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "(in NumPy v2.5)")
 for more information. The sort order is deterministic for a given input. mergesort and stable are the only stable algorithms, which preserve the relative order of equal keys.

**na\_position**{‘first’ or ‘last’}, default ‘last’

Argument ‘first’ puts NaNs at the beginning, ‘last’ puts NaNs at the end.

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

**key**callable, optional

If not None, apply the key function to the series values before sorting. This is similar to the key argument in the builtin `sorted()` function, with the notable difference that this key function should be _vectorized_. It should expect a `Series` and return an array-like.

Returns:

Series or None

Series ordered by values or None if `inplace=True`.

See also

[`Series.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")

Sort by the Series indices.

[`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")

Sort DataFrame by the values along either axis.

[`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")

Sort DataFrame by indices.

Examples

\>>> s \= pd.Series(\[np.nan, 1, 3, 10, 5\])
\>>> s
0     NaN
1     1.0
2     3.0
3     10.0
4     5.0
dtype: float64

Copy to clipboard

Sort values ascending order (default behavior)

\>>> s.sort\_values(ascending\=True)
1     1.0
2     3.0
4     5.0
3    10.0
0     NaN
dtype: float64

Copy to clipboard

Sort values descending order

\>>> s.sort\_values(ascending\=False)
3    10.0
4     5.0
2     3.0
1     1.0
0     NaN
dtype: float64

Copy to clipboard

Sort values putting NAs first

\>>> s.sort\_values(na\_position\="first")
0     NaN
1     1.0
2     3.0
4     5.0
3    10.0
dtype: float64

Copy to clipboard

Sort a series of strings

\>>> s \= pd.Series(\["z", "b", "d", "a", "c"\])
\>>> s
0    z
1    b
2    d
3    a
4    c
dtype: str

Copy to clipboard

\>>> s.sort\_values()
3    a
1    b
4    c
2    d
0    z
dtype: str

Copy to clipboard

Sort using a key function. Your key function will be given the `Series` of values and should return an array-like.

\>>> s \= pd.Series(\["a", "B", "c", "D", "e"\])
\>>> s.sort\_values()
1    B
3    D
0    a
2    c
4    e
dtype: str
\>>> s.sort\_values(key\=lambda x: x.str.lower())
0    a
1    B
2    c
3    D
4    e
dtype: str

Copy to clipboard

NumPy ufuncs work well here. For example, we can sort by the `sin` of the value

\>>> s \= pd.Series(\[\-4, \-2, 0, 2, 4\])
\>>> s.sort\_values(key\=np.sin)
1   -2
4    4
2    0
0   -4
3    2
dtype: int64

Copy to clipboard

More complicated user-defined functions can be used, as long as they expect a Series and return an array-like

\>>> s.sort\_values(key\=lambda x: np.tan(x.cumsum()))
0   -4
3    2
4    4
1   -2
2    0
dtype: int64

Copy to clipboard

On this page