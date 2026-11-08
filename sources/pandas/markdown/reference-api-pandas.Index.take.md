[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.take.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.take.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.take.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.take.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.take.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.take.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.take.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.take.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.take.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.take.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.take.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.take.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.take[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html#pandas-index-take "Link to this heading")

===================================================================================================================================

Index.take(_indices_, _axis\=0_, _allow\_fill\=<no\_default>_, _fill\_value\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1218-L1328)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html#pandas.Index.take "Link to this definition")

Return a new Index of the values selected by the indices.

For internal compatibility with numpy arrays.

Parameters:

**indices**array-like

Indices to be taken.

**axis**{0 or ‘index’}, optional

The axis over which to select values, always 0 or ‘index’.

**allow\_fill**bool, optional

How to handle negative values in indices.

*   False: negative values in indices indicate positional indices from the right, matching [`numpy.take()`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "(in NumPy v2.5)")
    .
    
*   True: negative values in indices indicate missing values. `-1` entries are set to `fill_value` (using the default NA value of the caller’s dtype if not supplied). Any other negative values raise a `ValueError`.
    
*   Not supplied: defaults to `allow_fill=False` unless `fill_value` is explicitly provided, in which case fill semantics apply (`allow_fill=True`).
    

**fill\_value**scalar, optional

If fill semantics apply (see `allow_fill`), indices specified by `-1` are filled with `fill_value`. Not specifying `fill_value` or passing `fill_value=None` will fill using the default NA value of the caller’s dtype. If the Index’s dtype cannot hold `fill_value`, the result is promoted to a common dtype (e.g. an integer Index + `np.nan` fill is cast to float, while an integer Index + a string fill is cast to object).

**\*\*kwargs**

Required for compatibility with numpy.

Returns:

Index

An index formed of elements at the given indices. Will be the same type as self, except for RangeIndex.

See also

[`numpy.ndarray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "(in NumPy v2.5)")

Return an array formed from the elements of a at the given indices.

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.take(\[2, 2, 1, 2\])
Index(\['c', 'c', 'b', 'c'\], dtype='str')

Copy to clipboard

On this page