[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_factorized.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_from\_factorized[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_factorized.html#pandas-api-extensions-extensionarray-from-factorized "Link to this heading")

================================================================================================================================================================================================================================================

classmethod ExtensionArray.\_from\_factorized(_values_, _original_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L381-L413)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_factorized.html#pandas.api.extensions.ExtensionArray._from_factorized "Link to this definition")

Reconstruct an ExtensionArray after factorization.

This method reverses the encoding applied by [`factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "pandas.api.extensions.ExtensionArray.factorize")
, recreating an ExtensionArray from the unique values and original array metadata.

Parameters:

**values**ndarray

An integer ndarray with the factorized values.

**original**ExtensionArray

The original ExtensionArray that factorize was called on.

See also

[`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "pandas.api.extensions.ExtensionArray.factorize")

Top-level factorize method that dispatches here.

[`ExtensionArray.factorize`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "pandas.api.extensions.ExtensionArray.factorize")

Encode the extension array as an enumerated type.

Examples

\>>> interv\_arr \= pd.arrays.IntervalArray(
...     \[pd.Interval(0, 1), pd.Interval(1, 5), pd.Interval(1, 5)\]
... )
\>>> codes, uniques \= pd.factorize(interv\_arr)
\>>> pd.arrays.IntervalArray.\_from\_factorized(uniques, interv\_arr)
<IntervalArray>
\[(0, 1\], (1, 5\]\]
Length: 2, dtype: interval\[int64, right\]

Copy to clipboard

On this page