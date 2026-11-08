[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.max.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.max.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.max.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.max.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.max.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.max.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.max.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.max.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.max.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.max.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.max.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.max.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.max[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#pandas-index-max "Link to this heading")

================================================================================================================================

Index.max(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L8149-L8222)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#pandas.Index.max "Link to this definition")

Return the maximum value of the Index.

The maximum is computed by comparing all values in the Index. NA/null values are excluded by default.

Parameters:

**axis**int, optional

For compatibility with NumPy. Only 0 or None are allowed.

**skipna**bool, default True

Exclude NA/null values when showing the result.

**\*args, \*\*kwargs**

Additional arguments and keywords for compatibility with NumPy.

Returns:

scalar

Maximum value.

See also

[`Index.min`](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#pandas.Index.min "pandas.Index.min")

Return the minimum value in an Index.

[`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")

Return the maximum value in a Series.

[`DataFrame.max`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max "pandas.DataFrame.max")

Return the maximum values in a DataFrame.

Examples

\>>> idx \= pd.Index(\[3, 2, 1\])
\>>> idx.max()
3

Copy to clipboard

\>>> idx \= pd.Index(\["c", "b", "a"\])
\>>> idx.max()
'c'

Copy to clipboard

For a MultiIndex, the maximum is determined lexicographically.

\>>> idx \= pd.MultiIndex.from\_product(\[("a", "b"), (2, 1)\])
\>>> idx.max()
('b', 2)

Copy to clipboard

On this page