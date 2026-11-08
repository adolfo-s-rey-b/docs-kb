[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.is_.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.is_.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.is_.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.is_.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.is_.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.is_.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.is_.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.is_.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.is_.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.is_.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.is_.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.is_.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.is\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html#pandas-index-is "Link to this heading")

================================================================================================================================

final Index.is\_(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L802-L840)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html#pandas.Index.is_ "Link to this definition")

More flexible, faster check like `is` but that works through views.

Note: this is _not_ the same as `Index.identical()`, which checks that metadata is also the same.

Parameters:

**other**Index

Other Index to compare against.

Returns:

bool

True if both have same underlying data, False otherwise.

See also

[`Index.identical`](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas.Index.identical "pandas.Index.identical")

Works like `Index.is_` but also checks metadata.

Examples

\>>> idx1 \= pd.Index(\["1", "2", "3"\])
\>>> idx1.is\_(idx1.view())
True

Copy to clipboard

\>>> idx1.is\_(idx1.copy())
False

Copy to clipboard

On this page