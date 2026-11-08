[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.as_ordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.as_ordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.as_ordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.as_ordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.as_ordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.as_ordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.as_ordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.as_ordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.as_ordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.as_ordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.as_ordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.as_ordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.as\_ordered[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#pandas-categorical-as-ordered "Link to this heading")

========================================================================================================================================================================

Categorical.as\_ordered()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1170-L1206)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#pandas.Categorical.as_ordered "Link to this definition")

Set the Categorical to be ordered.

This method returns a new Categorical with the ordered attribute set to True, enabling comparison operations between categories.

Returns:

Categorical

Ordered Categorical.

See also

[`as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#pandas.Categorical.as_unordered "pandas.Categorical.as_unordered")

Set the Categorical to be unordered.

Examples

For [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
:

\>>> ser \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")
\>>> ser.cat.ordered
False
\>>> ser \= ser.cat.as\_ordered()
\>>> ser.cat.ordered
True

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a"\])
\>>> ci.ordered
False
\>>> ci \= ci.as\_ordered()
\>>> ci.ordered
True

Copy to clipboard

On this page