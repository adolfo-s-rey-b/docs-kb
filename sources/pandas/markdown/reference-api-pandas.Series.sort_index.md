[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sort_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sort_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sort_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sort_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sort_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sort_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sort_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sort_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sort_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sort_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sort_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sort_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sort\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas-series-sort-index "Link to this heading")

=========================================================================================================================================================

Series.sort\_index(_\*_, _axis\=0_, _level\=None_, _ascending\=True_, _inplace\=<no\_default>_, _kind\='quicksort'_, _na\_position\='last'_, _sort\_remaining\=True_, _ignore\_index\=False_, _key\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4305-L4458)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "Link to this definition")

Sort Series by index labels.

Returns a new Series sorted by label if inplace argument is `False`, otherwise updates the original series and returns None.

Parameters:

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**level**int, optional

If not None, sort on values in specified index level(s).

**ascending**bool or list-like of bools, default True

Sort ascending vs. descending. When the index is a MultiIndex the sort direction can be controlled for each level individually.

**inplace**bool, default False

If True, perform operation in-place.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Choice of sorting algorithm. See also [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "(in NumPy v2.5)")
 for more information. The sort order is deterministic for a given input. ‘mergesort’ and ‘stable’ are the only stable algorithms, which preserve the relative order of equal keys. This option is ignored when sorting on a MultiIndex or when a level is specified.

**na\_position**{‘first’, ‘last’}, default ‘last’

If ‘first’ puts NaNs at the beginning, ‘last’ puts NaNs at the end. Not implemented for MultiIndex.

**sort\_remaining**bool, default True

If True and sorting by level and index is multilevel, sort by other levels too (in order) after sorting by specified level.

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

**key**callable, optional

If not None, apply the key function to the index values before sorting. This is similar to the key argument in the builtin `sorted()` function, with the notable difference that this key function should be _vectorized_. It should expect an `Index` and return an `Index` of the same shape.

Returns:

Series or None

The original Series sorted by the labels or None if `inplace=True`.

See also

[`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")

Sort DataFrame by the index.

[`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")

Sort DataFrame by the value.

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Sort Series by the value.

Examples

\>>> s \= pd.Series(\["a", "b", "c", "d"\], index\=\[3, 2, 1, 4\])
\>>> s.sort\_index()
1    c
2    b
3    a
4    d
dtype: str

Copy to clipboard

Sort Descending

\>>> s.sort\_index(ascending\=False)
4    d
3    a
2    b
1    c
dtype: str

Copy to clipboard

By default NaNs are put at the end, but use na\_position to place them at the beginning

\>>> s \= pd.Series(\["a", "b", "c", "d"\], index\=\[3, 2, 1, np.nan\])
\>>> s.sort\_index(na\_position\="first")
NaN     d
 1.0    c
 2.0    b
 3.0    a
dtype: str

Copy to clipboard

Specify index level to sort

\>>> arrays \= \[\
...     np.array(\["qux", "qux", "foo", "foo", "baz", "baz", "bar", "bar"\]),\
...     np.array(\["two", "one", "two", "one", "two", "one", "two", "one"\]),\
... \]
\>>> s \= pd.Series(\[1, 2, 3, 4, 5, 6, 7, 8\], index\=arrays)
\>>> s.sort\_index(level\=1)
bar  one    8
baz  one    6
foo  one    4
qux  one    2
bar  two    7
baz  two    5
foo  two    3
qux  two    1
dtype: int64

Copy to clipboard

Does not sort by remaining levels when sorting by levels

\>>> s.sort\_index(level\=1, sort\_remaining\=False)
qux  one    2
foo  one    4
baz  one    6
bar  one    8
qux  two    1
foo  two    3
baz  two    5
bar  two    7
dtype: int64

Copy to clipboard

Apply a key function before sorting

\>>> s \= pd.Series(\[1, 2, 3, 4\], index\=\["A", "b", "C", "d"\])
\>>> s.sort\_index(key\=lambda x: x.str.lower())
A    1
b    2
C    3
d    4
dtype: int64

Copy to clipboard

On this page