[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.codes.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.codes[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.codes.html#pandas-categoricalindex-codes "Link to this heading")

=======================================================================================================================================================================

property CategoricalIndex.codes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L167-L195)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.codes.html#pandas.CategoricalIndex.codes "Link to this definition")

The category codes of this categorical index.

Codes are an array of integers which are the positions of the actual values in the categories array. There is no setter.

Returns:

ndarray\[int\]

A non-writable view of the `codes` array.

See also

[`Categorical.from_codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")

Make a Categorical from codes.

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")

An Index with an underlying `Categorical`.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a", "b", "c"\])
\>>> ci.codes
array(\[0, 1, 2, 0, 1, 2\], dtype=int8)

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "c"\], categories\=\["c", "b", "a"\])
\>>> ci.codes
array(\[2, 0\], dtype=int8)

Copy to clipboard

On this page