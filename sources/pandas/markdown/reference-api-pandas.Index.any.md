[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.any[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#pandas-index-any "Link to this heading")

================================================================================================================================

Index.any(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7841-L7887)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#pandas.Index.any "Link to this definition")

Return whether any element is Truthy.

This is equivalent to calling `bool(self.any())`. An empty Index will return False.

Parameters:

**\*args**

Required for compatibility with numpy.

**\*\*kwargs**

Required for compatibility with numpy.

Returns:

bool or array-like (if axis is specified)

A single element array-like may be converted to bool.

See also

[`Index.all`](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#pandas.Index.all "pandas.Index.all")

Return whether all elements are True.

[`Series.all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")

Return whether all elements are True.

Notes

Not a Number (NaN), positive infinity and negative infinity evaluate to True because these are not equal to zero.

Examples

\>>> index \= pd.Index(\[0, 1, 2\])
\>>> index.any()
True

Copy to clipboard

\>>> index \= pd.Index(\[0, 0, 0\])
\>>> index.any()
False

Copy to clipboard

On this page