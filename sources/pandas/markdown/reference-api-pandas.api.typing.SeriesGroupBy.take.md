[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.take.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.take.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.take.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.take[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.take.html#pandas-api-typing-seriesgroupby-take "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.take(_indices_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1256-L1347)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.take.html#pandas.api.typing.SeriesGroupBy.take "Link to this definition")

Return the elements in the given _positional_ indices in each group.

This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.

If a requested index does not exist for some group, this method will raise. To get similar behavior that ignores indices that don’t exist, see [`SeriesGroupBy.nth()`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nth.html#pandas.api.typing.SeriesGroupBy.nth "pandas.api.typing.SeriesGroupBy.nth")
.

Parameters:

**indices**array-like

An array of ints indicating which positions to take in each group.

**\*\*kwargs**

For compatibility with `numpy.take()`. Has no effect on the output.

Deprecated since version 3.1.0: Passing `**kwargs` to SeriesGroupBy.take is deprecated and will be removed in a future version of pandas.

Returns:

Series

A Series containing the elements taken from each group.

See also

`Series.take`

Take elements from a Series along an axis.

`Series.loc`

Select a subset of a DataFrame by labels.

`Series.iloc`

Select a subset of a DataFrame by positions.

[`numpy.take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "(in NumPy v2.5)")

Take elements from an array along an axis.

[`SeriesGroupBy.nth`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nth.html#pandas.api.typing.SeriesGroupBy.nth "pandas.api.typing.SeriesGroupBy.nth")

Similar to take, won’t raise if indices don’t exist.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         ("falcon", "bird", 389.0),\
...         ("parrot", "bird", 24.0),\
...         ("lion", "mammal", 80.5),\
...         ("monkey", "mammal", np.nan),\
...         ("rabbit", "mammal", 15.0),\
...     \],
...     columns\=\["name", "class", "max\_speed"\],
...     index\=\[4, 3, 2, 1, 0\],
... )
\>>> df
     name   class  max\_speed
4  falcon    bird      389.0
3  parrot    bird       24.0
2    lion  mammal       80.5
1  monkey  mammal        NaN
0  rabbit  mammal       15.0
\>>> gb \= df\["name"\].groupby(\[1, 1, 2, 2, 2\])

Copy to clipboard

Take elements at rows 0 and 1 in each group.

\>>> gb.take(\[0, 1\])
1  4    falcon
   3    parrot
2  2      lion
   1    monkey
Name: name, dtype: str

Copy to clipboard

We may take elements using negative integers for positive indices, starting from the end of the object, just like with Python lists.

\>>> gb.take(\[\-1, \-2\])
1  3    parrot
   4    falcon
2  0    rabbit
   1    monkey
Name: name, dtype: str

Copy to clipboard

On this page