[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.argsort.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.argsort[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas-api-extensions-extensionarray-argsort "Link to this heading")

====================================================================================================================================================================================================================

ExtensionArray.argsort(_\*_, _ascending\=True_, _kind\='quicksort'_, _na\_position\='last'_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1016-L1073)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas.api.extensions.ExtensionArray.argsort "Link to this definition")

Return the indices that would sort this array.

This method computes the indices that would produce a sorted version of the array when used with indexing.

Parameters:

**ascending**bool, default True

Whether the indices should result in an ascending or descending sort.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional

Sorting algorithm.

**na\_position**{‘first’, ‘last’}, default ‘last’

If `'first'`, put `NaN` values at the beginning. If `'last'`, put `NaN` values at the end.

**\*\*kwargs**

Passed through to [`numpy.argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "(in NumPy v2.5)")
.

Returns:

np.ndarray\[np.intp\]

Array of indices that sort `self`. If NaN values are contained, NaN values are placed at the end.

See also

[`numpy.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "(in NumPy v2.5)")

Sorting implementation used internally.

Examples

\>>> arr \= pd.array(\[3, 1, 2, 5, 4\])
\>>> arr.argsort()
array(\[1, 2, 0, 4, 3\])

Copy to clipboard

On this page