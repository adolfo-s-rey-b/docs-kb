[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.searchsorted[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html#pandas-api-extensions-extensionarray-searchsorted "Link to this heading")

===================================================================================================================================================================================================================================

ExtensionArray.searchsorted(_value_, _side\='left'_, _sorter\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1634-L1692)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html#pandas.api.extensions.ExtensionArray.searchsorted "Link to this definition")

Find indices where elements should be inserted to maintain order.

Find the indices into a sorted array self (a) such that, if the corresponding elements in value were inserted before the indices, the order of self would be preserved.

Assuming that self is sorted:

| side | returned index i satisfies |
| --- | --- |
| left | `self[i-1] < value <= self[i]` |
| right | `self[i-1] <= value < self[i]` |

Parameters:

**value**array-like, list or scalar

Value(s) to insert into self.

**side**{‘left’, ‘right’}, optional

If ‘left’, the index of the first suitable location found is given. If ‘right’, return the last such index. If there is no suitable index, return either 0 or N (where N is the length of self).

**sorter**1-D array-like, optional

Optional array of integer indices that sort array a into ascending order. They are typically the result of argsort.

Returns:

array of ints or int

If value is array-like, array of insertion points. If value is scalar, a single integer.

See also

[`numpy.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "(in NumPy v2.5)")

Similar method from NumPy.

Examples

\>>> arr \= pd.array(\[1, 2, 3, 5\])
\>>> arr.searchsorted(\[4\])
array(\[3\])

Copy to clipboard

On this page