[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sort_values.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sort_values.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sort_values.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sort_values.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sort_values.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sort_values.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sort_values.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sort_values.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sort_values.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sort_values.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sort_values.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sort_values.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sort\_values[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas-dataframe-sort-values "Link to this heading")

=====================================================================================================================================================================

DataFrame.sort\_values(_by_, _\*_, _axis\=0_, _ascending\=True_, _inplace\=<no\_default>_, _kind\='quicksort'_, _na\_position\='last'_, _ignore\_index\=False_, _key\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L9086-L9372)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "Link to this definition")

Sort by the values along either axis.

This method sorts the DataFrame by the values in one or more columns or by index/column labels.

Parameters:

**by**str or list of str

Name or list of names to sort by.

*   if axis is 0 or ‘index’ then by may contain index levels and/or column labels.
    
*   if axis is 1 or ‘columns’ then by may contain column levels and/or index labels.
    

**axis**“{0 or ‘index’, 1 or ‘columns’}”, default 0

Axis to be sorted.

**ascending**bool or list of bool, default True

Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.

**inplace**bool, default False

If True, perform operation in-place.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Choice of sorting algorithm. See also [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "(in NumPy v2.5)")
 for more information. The sort order is deterministic for a given input. mergesort and stable are the only stable algorithms, which preserve the relative order of equal keys. For DataFrames, this option is only applied when sorting on a single column or label.

**na\_position**{‘first’, ‘last’}, default ‘last’

Puts NaNs at the beginning if first; last puts NaNs at the end.

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

**key**callable, optional

Apply the key function to the values before sorting. This is similar to the key argument in the builtin `sorted()` function, with the notable difference that this key function should be _vectorized_. It should expect a `Series` and return a Series with the same shape as the input. It will be applied to each column in by independently. The values in the returned Series will be used as the keys for sorting.

Returns:

DataFrame or None

DataFrame with sorted values or None if `inplace=True`.

See also

[`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")

Sort a DataFrame by the index.

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Similar method for a Series.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "col1": \["A", "A", "B", np.nan, "D", "C"\],
...         "col2": \[2, 1, 9, 8, 7, 4\],
...         "col3": \[0, 1, 9, 4, 2, 3\],
...         "col4": \["a", "B", "c", "D", "e", "F"\],
...     }
... )
\>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

Copy to clipboard

**Sort by a single column**

In this case, we are sorting the rows according to values in `col1`:

\>>> df.sort\_values(by\=\["col1"\])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

Copy to clipboard

**Sort by multiple columns**

You can also provide multiple columns to `by` argument, as shown below. In this example, the rows are first sorted according to `col1`, and then the rows that have an identical value in `col1` are sorted according to `col2`.

\>>> df.sort\_values(by\=\["col1", "col2"\])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

Copy to clipboard

**Sort in a descending order**

The sort order can be reversed using `ascending` argument, as shown below:

\>>> df.sort\_values(by\="col1", ascending\=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D

Copy to clipboard

**Placing any** `NA` **first**

Note that in the above example, the rows that contain an `NA` value in their `col1` are placed at the end of the dataframe. This behavior can be modified via `na_position` argument, as shown below:

\>>> df.sort\_values(by\="col1", ascending\=False, na\_position\="first")
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B

Copy to clipboard

**Customized sort order**

The `key` argument allows for a further customization of sorting behaviour. For example, you may want to ignore the [letter’s case](https://en.wikipedia.org/wiki/Letter_case)
 when sorting strings:

\>>> df.sort\_values(by\="col4", key\=lambda col: col.str.lower())
   col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

Copy to clipboard

Another typical example is [natural sorting](https://en.wikipedia.org/wiki/Natural_sort_order)
. This can be done using `natsort` [package](https://github.com/SethMMorton/natsort)
, which provides a function to generate a key to sort data in their natural order:

\>>> df \= pd.DataFrame(
...     {
...         "hours": \["0hr", "128hr", "0hr", "64hr", "64hr", "128hr"\],
...         "mins": \[\
...             "10mins",\
...             "40mins",\
...             "40mins",\
...             "40mins",\
...             "10mins",\
...             "10mins",\
...         \],
...         "value": \[10, 20, 30, 40, 50, 60\],
...     }
... )
\>>> df
   hours    mins  value
0    0hr  10mins     10
1  128hr  40mins     20
2    0hr  40mins     30
3   64hr  40mins     40
4   64hr  10mins     50
5  128hr  10mins     60
\>>> from natsort import natsort\_keygen
\>>> df.sort\_values(
...     by\=\["hours", "mins"\],
...     key\=natsort\_keygen(),
... )
   hours    mins  value
0    0hr  10mins     10
2    0hr  40mins     30
4   64hr  10mins     50
3   64hr  40mins     40
5  128hr  10mins     60
1  128hr  40mins     20

Copy to clipboard

On this page