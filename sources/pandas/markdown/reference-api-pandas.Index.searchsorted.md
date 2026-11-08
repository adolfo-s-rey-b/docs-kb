[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.searchsorted.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.searchsorted.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.searchsorted.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.searchsorted.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.searchsorted.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.searchsorted.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.searchsorted.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.searchsorted.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.searchsorted.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.searchsorted.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.searchsorted.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.searchsorted.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.searchsorted[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html#pandas-index-searchsorted "Link to this heading")

===========================================================================================================================================================

Index.searchsorted(_value_, _side\='left'_, _sorter\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1566-L1687)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html#pandas.Index.searchsorted "Link to this definition")

Find indices where elements should be inserted to maintain order.

Find the indices into a sorted Index self such that, if the corresponding elements in value were inserted before the indices, the order of self would be preserved.

Note

The Index _must_ be monotonically sorted, otherwise wrong locations will likely be returned. Pandas does _not_ check this for you.

Parameters:

**value**array-like or scalar

Values to insert into self.

**side**{‘left’, ‘right’}, optional

If ‘left’, the index of the first suitable location found is given. If ‘right’, return the last such index. If there is no suitable index, return either 0 or N (where N is the length of self).

**sorter**1-D array-like, optional

Optional array of integer indices that sort self into ascending order. They are typically the result of `np.argsort`.

Returns:

int or array of int

A scalar or array of insertion points with the same shape as value.

See also

[`sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "pandas.Index.sort_values")

Sort by the values along either axis.

[`numpy.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "(in NumPy v2.5)")

Similar method from NumPy.

Notes

Binary search is used to find the required insertion points.

Examples

\>>> ser \= pd.Series(\[1, 2, 3\])
\>>> ser
0    1
1    2
2    3
dtype: int64

Copy to clipboard

\>>> ser.searchsorted(4)
3

Copy to clipboard

\>>> ser.searchsorted(\[0, 4\])
array(\[0, 3\])

Copy to clipboard

\>>> ser.searchsorted(\[1, 3\], side\="left")
array(\[0, 2\])

Copy to clipboard

\>>> ser.searchsorted(\[1, 3\], side\="right")
array(\[1, 3\])

Copy to clipboard

\>>> ser \= pd.Series(pd.to\_datetime(\["3/11/2000", "3/12/2000", "3/13/2000"\]))
\>>> ser
0   2000-03-11
1   2000-03-12
2   2000-03-13
dtype: datetime64\[us\]

Copy to clipboard

\>>> ser.searchsorted("3/14/2000")
3

Copy to clipboard

\>>> ser \= pd.Categorical(
...     \["apple", "bread", "bread", "cheese", "milk"\], ordered\=True
... )
\>>> ser
\['apple', 'bread', 'bread', 'cheese', 'milk'\]
Categories (4, str): \['apple' < 'bread' < 'cheese' < 'milk'\]

Copy to clipboard

\>>> ser.searchsorted("bread")
np.int64(1)

Copy to clipboard

\>>> ser.searchsorted(\["bread"\], side\="right")
array(\[3\])

Copy to clipboard

If the values are not monotonically sorted, wrong locations may be returned:

\>>> ser \= pd.Series(\[2, 1, 3\])
\>>> ser
0    2
1    1
2    3
dtype: int64

Copy to clipboard

\>>> ser.searchsorted(1)
0  # wrong result, correct would be 1

Copy to clipboard

On this page