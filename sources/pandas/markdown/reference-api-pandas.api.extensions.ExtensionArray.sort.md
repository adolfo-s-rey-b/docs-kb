[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.sort.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.sort[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.sort.html#pandas-api-extensions-extensionarray-sort "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.sort(_\*_, _ascending\=True_, _kind\='quicksort'_, _na\_position\='last'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1075-L1120)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.sort.html#pandas.api.extensions.ExtensionArray.sort "Link to this definition")

Sort the array in-place.

Reorders the elements of the array using [`argsort()`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas.api.extensions.ExtensionArray.argsort "pandas.api.extensions.ExtensionArray.argsort")
 and writes the sorted result back through `self[:]`. Subclasses backed by immutable storage may override this method to raise `NotImplementedError`.

Parameters:

**ascending**bool, default True

Whether to sort in ascending order.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

Sorting algorithm.

**na\_position**{‘first’, ‘last’}, default ‘last’

If ‘first’, put NaN values at the beginning. If ‘last’, put NaN values at the end.

Returns:

None

This method mutates the array in place and does not return a value.

See also

[`ExtensionArray.argsort`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas.api.extensions.ExtensionArray.argsort "pandas.api.extensions.ExtensionArray.argsort")

Return the indices that would sort this array.

Examples

\>>> arr \= pd.array(\[3, 1, 2, 5, 4\])
\>>> arr.sort()
\>>> arr
<IntegerArray>
\[1, 2, 3, 4, 5\]
Length: 5, dtype: Int64

Copy to clipboard

On this page