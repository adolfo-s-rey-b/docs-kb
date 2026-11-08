[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.repeat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.repeat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.repeat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.repeat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.repeat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.repeat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.repeat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.repeat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.repeat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.repeat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.repeat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.repeat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.repeat[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#pandas-index-repeat "Link to this heading")

=========================================================================================================================================

Index.repeat(_repeats_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1330-L1372)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#pandas.Index.repeat "Link to this definition")

Repeat elements of an Index.

Returns a new Index where each element of the current Index is repeated consecutively a given number of times.

Parameters:

**repeats**int or array of ints

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty Index.

**axis**None

Must be `None`. Has no effect but is accepted for compatibility with numpy.

Returns:

Index

Newly created Index with repeated elements.

See also

[`Series.repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas.Series.repeat "pandas.Series.repeat")

Equivalent function for Series.

[`numpy.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "(in NumPy v2.5)")

Similar method for [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
.

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx
Index(\['a', 'b', 'c'\], dtype='str')
\>>> idx.repeat(2)
Index(\['a', 'a', 'b', 'b', 'c', 'c'\], dtype='str')
\>>> idx.repeat(\[1, 2, 3\])
Index(\['a', 'b', 'b', 'c', 'c', 'c'\], dtype='str')

Copy to clipboard

On this page