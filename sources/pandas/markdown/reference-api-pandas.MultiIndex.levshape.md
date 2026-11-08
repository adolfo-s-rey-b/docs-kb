[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.levshape.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.levshape.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.levshape.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.levshape.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.levshape.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.levshape.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.levshape.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.levshape.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.levshape.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.levshape.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.levshape.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.levshape.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.levshape[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html#pandas-multiindex-levshape "Link to this heading")

==============================================================================================================================================================

property MultiIndex.levshape[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1127-L1153)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html#pandas.MultiIndex.levshape "Link to this definition")

A tuple representing the length of each level in the MultiIndex.

In a MultiIndex, each level can contain multiple unique values. The levshape property provides a quick way to assess the size of each level by returning a tuple where each entry represents the number of unique values in that specific level. This is particularly useful in scenarios where you need to understand the structure and distribution of your index levels, such as when working with multidimensional data.

See also

`MultiIndex.shape`

Return a tuple of the shape of the MultiIndex.

[`MultiIndex.levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "pandas.MultiIndex.levels")

Returns the levels of the MultiIndex.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a"\], \["b"\], \["c"\]\])
\>>> mi
MultiIndex(\[('a', 'b', 'c')\],
           )
\>>> mi.levshape
(1, 1, 1)

Copy to clipboard

On this page