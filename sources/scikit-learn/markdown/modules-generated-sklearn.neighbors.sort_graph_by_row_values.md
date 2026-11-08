[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html)

Collapse Sidebar Expand Sidebar

sort\_graph\_by\_row\_values[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html#sort-graph-by-row-values "Link to this heading")

===================================================================================================================================================================================

sklearn.neighbors.sort\_graph\_by\_row\_values(_graph_, _copy\=False_, _warn\_when\_not\_sorted\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L188)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html#sklearn.neighbors.sort_graph_by_row_values "Link to this definition")

Sort a sparse graph such that each row is stored with increasing values.

Added in version 1.2.

Parameters:

**graph**sparse matrix of shape (n\_samples, n\_samples)

Distance matrix to other samples, where only non-zero elements are considered neighbors. Matrix is converted to CSR format if not already.

**copy**bool, default=False

If True, the graph is copied before sorting. If False, the sorting is performed inplace. If the graph is not of CSR format, `copy` must be True to allow the conversion to CSR format, otherwise an error is raised.

**warn\_when\_not\_sorted**bool, default=True

If True, a [`EfficiencyWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EfficiencyWarning.html#sklearn.exceptions.EfficiencyWarning "sklearn.exceptions.EfficiencyWarning")
 is raised when the input graph is not sorted by row values.

Returns:

**graph**sparse matrix of shape (n\_samples, n\_samples)

Distance matrix to other samples, where only non-zero elements are considered neighbors. Matrix is in CSR format.

Examples

\>>> from scipy.sparse import csr\_array
\>>> from sklearn.neighbors import sort\_graph\_by\_row\_values
\>>> X \= csr\_array(
...     \[\[0., 3., 1.\],\
...      \[3., 0., 2.\],\
...      \[1., 2., 0.\]\])
\>>> X.data
array(\[3., 1., 3., 2., 1., 2.\])
\>>> X\_ \= sort\_graph\_by\_row\_values(X)
\>>> X\_.data
array(\[1., 3., 2., 3., 1., 2.\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)