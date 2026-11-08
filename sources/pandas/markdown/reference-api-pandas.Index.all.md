[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.all.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.all.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.all.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.all.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.all.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.all.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.all.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.all.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.all.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.all.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.all.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.all.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.all[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#pandas-index-all "Link to this heading")

================================================================================================================================

Index.all(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7889-L7938)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#pandas.Index.all "Link to this definition")

Return whether all elements are Truthy.

This is equivalent to calling `bool(self.all())`. An empty Index will return True.

Parameters:

**\*args**

Required for compatibility with numpy.

**\*\*kwargs**

Required for compatibility with numpy.

Returns:

bool or array-like (if axis is specified)

A single element array-like may be converted to bool.

See also

[`Index.any`](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#pandas.Index.any "pandas.Index.any")

Return whether any element in an Index is True.

[`Series.any`](https://pandas.pydata.org/docs/reference/api/pandas.Series.any.html#pandas.Series.any "pandas.Series.any")

Return whether any element in a Series is True.

[`Series.all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")

Return whether all elements in a Series are True.

Notes

Not a Number (NaN), positive infinity and negative infinity evaluate to True because these are not equal to zero.

Examples

True, because nonzero integers are considered True.

\>>> pd.Index(\[1, 2, 3\]).all()
True

Copy to clipboard

False, because `0` is considered False.

\>>> pd.Index(\[0, 1, 2\]).all()
False

Copy to clipboard

On this page