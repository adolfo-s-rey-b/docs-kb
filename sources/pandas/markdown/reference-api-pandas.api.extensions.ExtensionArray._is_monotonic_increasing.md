[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_is\_monotonic\_increasing[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html#pandas-api-extensions-extensionarray-is-monotonic-increasing "Link to this heading")

=========================================================================================================================================================================================================================================================================

property ExtensionArray.\_is\_monotonic\_increasing[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2749-L2773)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_increasing "Link to this definition")

Return True if the array values are monotonically increasing.

Subclasses can override this for performance. The default implementation falls back to computing ranks via `_rank`.

Returns:

bool

Whether the array values are monotonically increasing.

See also

[`ExtensionArray._is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_decreasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_decreasing "pandas.api.extensions.ExtensionArray._is_monotonic_decreasing")

Check for monotonically decreasing values.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.\_is\_monotonic\_increasing
True

Copy to clipboard

On this page