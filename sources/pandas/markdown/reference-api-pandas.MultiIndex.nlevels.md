[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.nlevels[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html#pandas-multiindex-nlevels "Link to this heading")

===========================================================================================================================================================

property MultiIndex.nlevels[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1100-L1125)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html#pandas.MultiIndex.nlevels "Link to this definition")

Integer number of levels in this MultiIndex.

This property returns the count of levels (i.e., the depth of the hierarchical index), which corresponds to the number of arrays or columns used to construct the MultiIndex.

See also

[`MultiIndex.levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "pandas.MultiIndex.levels")

Get the levels of the MultiIndex.

[`MultiIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes")

Get the codes of the MultiIndex.

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert arrays to MultiIndex.

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to MultiIndex.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a"\], \["b"\], \["c"\]\])
\>>> mi
MultiIndex(\[('a', 'b', 'c')\],
           )
\>>> mi.nlevels
3

Copy to clipboard

On this page