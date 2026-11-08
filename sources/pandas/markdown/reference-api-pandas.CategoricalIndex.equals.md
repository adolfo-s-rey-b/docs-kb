[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.equals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.equals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.equals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.equals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.equals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.equals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.equals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.equals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.equals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.equals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.equals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.equals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.equals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.equals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.equals[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.equals.html#pandas-categoricalindex-equals "Link to this heading")

==========================================================================================================================================================================

CategoricalIndex.equals(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L801-L870)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.equals.html#pandas.CategoricalIndex.equals "Link to this definition")

Determine if two CategoricalIndex objects contain the same elements.

The order and orderedness of elements matters. The categories matter, but the order of the categories matters only when `ordered=True`.

Parameters:

**other**object

The CategoricalIndex object to compare with.

Returns:

bool

`True` if two [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
 objects have equal elements, `False` otherwise.

See also

`Categorical.equals`

Returns True if categorical arrays are equal.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a", "b", "c"\])
\>>> ci2 \= pd.CategoricalIndex(pd.Categorical(\["a", "b", "c", "a", "b", "c"\]))
\>>> ci.equals(ci2)
True

Copy to clipboard

The order of elements matters.

\>>> ci3 \= pd.CategoricalIndex(\["c", "b", "a", "a", "b", "c"\])
\>>> ci.equals(ci3)
False

Copy to clipboard

The orderedness also matters.

\>>> ci4 \= ci.as\_ordered()
\>>> ci.equals(ci4)
False

Copy to clipboard

The categories matter, but the order of the categories matters only when `ordered=True`.

\>>> ci5 \= ci.set\_categories(\["a", "b", "c", "d"\])
\>>> ci.equals(ci5)
False

Copy to clipboard

\>>> ci6 \= ci.set\_categories(\["b", "c", "a"\])
\>>> ci.equals(ci6)
True
\>>> ci\_ordered \= pd.CategoricalIndex(
...     \["a", "b", "c", "a", "b", "c"\], ordered\=True
... )
\>>> ci2\_ordered \= ci\_ordered.set\_categories(\["b", "c", "a"\])
\>>> ci\_ordered.equals(ci2\_ordered)
False

Copy to clipboard

On this page