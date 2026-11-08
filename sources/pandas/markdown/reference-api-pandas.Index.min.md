[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.min.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.min.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.min.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.min.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.min.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.min.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.min.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.min.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.min.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.min.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.min.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.min.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.min[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#pandas-index-min "Link to this heading")

================================================================================================================================

Index.min(_axis\=None_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L8075-L8147)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#pandas.Index.min "Link to this definition")

Return the minimum value of the Index.

The minimum is computed by comparing all values in the Index. NA/null values are excluded by default.

Parameters:

**axis**{None}

Dummy argument for consistency with Series.

**skipna**bool, default True

Exclude NA/null values when showing the result.

**\*args, \*\*kwargs**

Additional arguments and keywords for compatibility with NumPy.

Returns:

scalar

Minimum value.

See also

[`Index.max`](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#pandas.Index.max "pandas.Index.max")

Return the maximum value of the object.

[`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")

Return the minimum value in a Series.

[`DataFrame.min`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min "pandas.DataFrame.min")

Return the minimum values in a DataFrame.

Examples

\>>> idx \= pd.Index(\[3, 2, 1\])
\>>> idx.min()
1

Copy to clipboard

\>>> idx \= pd.Index(\["c", "b", "a"\])
\>>> idx.min()
'a'

Copy to clipboard

For a MultiIndex, the minimum is determined lexicographically.

\>>> idx \= pd.MultiIndex.from\_product(\[("a", "b"), (2, 1)\])
\>>> idx.min()
('a', 1)

Copy to clipboard

On this page