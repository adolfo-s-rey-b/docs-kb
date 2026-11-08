[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.as\_unordered[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#pandas-categorical-as-unordered "Link to this heading")

==============================================================================================================================================================================

Categorical.as\_unordered()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1208-L1245)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#pandas.Categorical.as_unordered "Link to this definition")

Set the Categorical to be unordered.

This method returns a new Categorical with the ordered attribute set to False, disabling comparison operations between categories.

Returns:

Categorical

Unordered Categorical.

See also

[`as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#pandas.Categorical.as_ordered "pandas.Categorical.as_ordered")

Set the Categorical to be ordered.

Examples

For [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
:

\>>> raw\_cat \= pd.Categorical(\["a", "b", "c", "a"\], ordered\=True)
\>>> ser \= pd.Series(raw\_cat)
\>>> ser.cat.ordered
True
\>>> ser \= ser.cat.as\_unordered()
\>>> ser.cat.ordered
False

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a"\], ordered\=True)
\>>> ci.ordered
True
\>>> ci \= ci.as\_unordered()
\>>> ci.ordered
False

Copy to clipboard

On this page