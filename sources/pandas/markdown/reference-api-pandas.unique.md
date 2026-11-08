[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.unique[#](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas-unique "Link to this heading")

=======================================================================================================================

pandas.unique(_values_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/algorithms.py#L328-L447)
[#](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas.unique "Link to this definition")

Return unique values based on a hash table.

Uniques are returned in order of appearance. This does NOT sort.

Significantly faster than numpy.unique for long enough sequences. Includes NA values.

Parameters:

**values**1d array-like

The input array-like object containing values from which to extract unique values.

Returns:

Index, ExtensionArray or numpy.ndarray

The return type depends on the type of the input:

*   [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
     : when the input is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
    , the result is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
     (or a subclass such as [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
    ).
    
*   `ExtensionArray` : when the input has an `ExtensionDtype` (for example [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
    , tz-aware `datetime64`, `IntervalArray`, a masked integer/boolean/float array, an Arrow-backed array, or `NumpyExtensionArray`), the result is an `ExtensionArray` of the same dtype.
    
*   [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     : for any other input (a NumPy-dtype [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    , a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    , or any other 1-D array-like), the result is a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    .
    

See also

[`Index.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "pandas.Index.unique")

Return unique values from an Index.

[`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")

Return unique values of Series object.

Notes

When working with object-dtype arrays, boolean and integer values may not be distinguished since `True == 1` and `False == 0` in Python.

\>>> pd.unique(np.array(\[True, 1, False, 0\], dtype\=object))
array(\[True, False\], dtype=object)

Copy to clipboard

Examples

\>>> pd.unique(pd.Series(\[2, 1, 3, 3\]))
array(\[2, 1, 3\])

Copy to clipboard

\>>> pd.unique(pd.Series(\[2\] + \[1\] \* 5))
array(\[2, 1\])

Copy to clipboard

\>>> pd.unique(pd.Series(\[pd.Timestamp("20160101"), pd.Timestamp("20160101")\]))
array(\['2016-01-01T00:00:00.000000'\], dtype='datetime64\[us\]')

Copy to clipboard

\>>> pd.unique(
...     pd.Series(
...         \[\
...             pd.Timestamp("20160101", tz\="US/Eastern"),\
...             pd.Timestamp("20160101", tz\="US/Eastern"),\
...         \],
...         dtype\="M8\[ns, US/Eastern\]",
...     )
... )
<DatetimeArray>
\['2016-01-01 00:00:00-05:00'\]
Length: 1, dtype: datetime64\[ns, US/Eastern\]

Copy to clipboard

\>>> pd.unique(
...     pd.Index(
...         \[\
...             pd.Timestamp("20160101", tz\="US/Eastern"),\
...             pd.Timestamp("20160101", tz\="US/Eastern"),\
...         \],
...         dtype\="M8\[ns, US/Eastern\]",
...     )
... )
DatetimeIndex(\['2016-01-01 00:00:00-05:00'\],
        dtype='datetime64\[ns, US/Eastern\]',
        freq=None)

Copy to clipboard

\>>> pd.unique(np.array(list("baabc"), dtype\="O"))
array(\['b', 'a', 'c'\], dtype=object)

Copy to clipboard

An unordered Categorical will return categories in the order of appearance.

\>>> pd.unique(pd.Series(pd.Categorical(list("baabc"))))
\['b', 'a', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

\>>> pd.unique(pd.Series(pd.Categorical(list("baabc"), categories\=list("abc"))))
\['b', 'a', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

An ordered Categorical preserves the category ordering.

\>>> pd.unique(
...     pd.Series(
...         pd.Categorical(list("baabc"), categories\=list("abc"), ordered\=True)
...     )
... )
\['b', 'a', 'c'\]
Categories (3, str): \['a' < 'b' < 'c'\]

Copy to clipboard

An array of tuples

\>>> pd.unique(pd.Series(\[("a", "b"), ("b", "a"), ("a", "c"), ("b", "a")\]).values)
array(\[('a', 'b'), ('b', 'a'), ('a', 'c')\], dtype=object)

Copy to clipboard

A NumpyExtensionArray of complex

\>>> pd.unique(pd.array(\[1 + 1j, 2, 3\]))
<NumpyExtensionArray>
\[(1+1j), (2+0j), (3+0j)\]
Length: 3, dtype: complex128

Copy to clipboard

On this page