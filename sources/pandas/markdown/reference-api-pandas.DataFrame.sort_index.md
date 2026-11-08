[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sort_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sort_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sort_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sort_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sort_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sort_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sort_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sort_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sort_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sort_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sort_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sort_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sort\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas-dataframe-sort-index "Link to this heading")

==================================================================================================================================================================

DataFrame.sort\_index(_\*_, _axis\=0_, _level\=None_, _ascending\=True_, _inplace\=<no\_default>_, _kind\='quicksort'_, _na\_position\='last'_, _sort\_remaining\=True_, _ignore\_index\=False_, _key\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L9419-L9538)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "Link to this definition")

Sort object by labels (along an axis).

Returns a new DataFrame sorted by label if inplace argument is `False`, otherwise updates the original DataFrame and returns None.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis along which to sort. The value 0 identifies the rows, and 1 identifies the columns.

**level**int or level name or list of ints or list of level names

If not None, sort on values in specified index level(s).

**ascending**bool or list-like of bools, default True

Sort ascending vs. descending. When the index is a MultiIndex the sort direction can be controlled for each level individually.

**inplace**bool, default False

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Choice of sorting algorithm. See also [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "(in NumPy v2.5)")
 for more information. The sort order is deterministic for a given input. ‘mergesort’ and ‘stable’ are the only stable algorithms, which preserve the relative order of equal keys. This option is ignored when sorting on a MultiIndex or when a level is specified.

**na\_position**{‘first’, ‘last’}, default ‘last’

Puts NaNs at the beginning if first; last puts NaNs at the end. Not implemented for MultiIndex.

**sort\_remaining**bool, default True

If True and sorting by level and index is multilevel, sort by other levels too (in order) after sorting by specified level.

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

**key**callable, optional

If not None, apply the key function to the index values before sorting. This is similar to the key argument in the builtin `sorted()` function, with the notable difference that this key function should be _vectorized_. It should expect an `Index` and return an `Index` of the same shape. For MultiIndex inputs, the key is applied _per level_.

Returns:

DataFrame or None

The original DataFrame sorted by the labels or None if `inplace=True`.

See also

[`Series.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")

Sort Series by the index.

[`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")

Sort DataFrame by the value.

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Sort Series by the value.

Examples

\>>> df \= pd.DataFrame(
...     \[1, 2, 3, 4, 5\], index\=\[100, 29, 234, 1, 150\], columns\=\["A"\]
... )
\>>> df.sort\_index()
     A
1    4
29   2
100  1
150  5
234  3

Copy to clipboard

By default, it sorts in ascending order, to sort in descending order, use `ascending=False`

\>>> df.sort\_index(ascending\=False)
     A
234  3
150  5
100  1
29   2
1    4

Copy to clipboard

A key function can be specified which is applied to the index before sorting. For a `MultiIndex` this is applied to each level separately.

\>>> df \= pd.DataFrame({"a": \[1, 2, 3, 4\]}, index\=\["A", "b", "C", "d"\])
\>>> df.sort\_index(key\=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4

Copy to clipboard

On this page