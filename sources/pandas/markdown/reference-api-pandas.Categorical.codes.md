[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.codes[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#pandas-categorical-codes "Link to this heading")

========================================================================================================================================================

property Categorical.codes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1058-L1099)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#pandas.Categorical.codes "Link to this definition")

The category codes of this categorical index.

Codes are an array of integers which are the positions of the actual values in the categories array.

There is no setter, use the other categorical methods and the normal item setter to change values in the categorical.

Returns:

ndarray\[int\]

A non-writable view of the `codes` array.

See also

[`Categorical.from_codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")

Make a Categorical from codes.

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")

An Index with an underlying `Categorical`.

Examples

For [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
:

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> cat.codes
array(\[0, 1\], dtype=int8)

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a", "b", "c"\])
\>>> ci.codes
array(\[0, 1, 2, 0, 1, 2\], dtype=int8)

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "c"\], categories\=\["c", "b", "a"\])
\>>> ci.codes
array(\[2, 0\], dtype=int8)

Copy to clipboard

On this page