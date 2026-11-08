[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_decreasing.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_is\_monotonic\_decreasing[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_decreasing.html#pandas-api-extensions-extensionarray-is-monotonic-decreasing "Link to this heading")

=========================================================================================================================================================================================================================================================================

property ExtensionArray.\_is\_monotonic\_decreasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2775-L2799)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_decreasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_decreasing "Link to this definition")

Return True if the array values are monotonically decreasing.

Subclasses can override this for performance. The default implementation falls back to computing ranks via `_rank`.

Returns:

bool

Whether the array values are monotonically decreasing.

See also

[`ExtensionArray._is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_increasing "pandas.api.extensions.ExtensionArray._is_monotonic_increasing")

Check for monotonically increasing values.

Examples

\>>> arr \= pd.array(\[3, 2, 1\])
\>>> arr.\_is\_monotonic\_decreasing
True

Copy to clipboard

On this page