[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.tree.export_graphviz.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.tree.export_graphviz.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.tree.export_graphviz.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.tree.export_graphviz.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.tree.export_graphviz.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.tree.export_graphviz.html)

Collapse Sidebar Expand Sidebar

export\_graphviz[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#export-graphviz "Link to this heading")

================================================================================================================================================

sklearn.tree.export\_graphviz(_decision\_tree_, _out\_file\=None_, _\*_, _max\_depth\=None_, _feature\_names\=None_, _class\_names\=None_, _label\='all'_, _filled\=False_, _leaves\_parallel\=False_, _impurity\=True_, _node\_ids\=False_, _proportion\=False_, _rotate\=False_, _rounded\=False_, _special\_characters\=False_, _precision\=3_, _fontname\='helvetica'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_export.py#L774)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "Link to this definition")

Export a decision tree in DOT format.

This function generates a GraphViz representation of the decision tree, which is then written into `out_file`. Once exported, graphical renderings can be generated using, for example:

$ dot -Tps tree.dot -o tree.ps      (PostScript format)
$ dot -Tpng tree.dot -o tree.png    (PNG format)

Copy to clipboard

The sample counts that are shown are weighted with any sample\_weights that might be present.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree)
.

Parameters:

**decision\_tree**object

The decision tree estimator to be exported to GraphViz.

**out\_file**object or str, default=None

Handle or name of the output file. If `None`, the result is returned as a string.

Changed in version 0.20: Default of out\_file changed from “tree.dot” to None.

**max\_depth**int, default=None

The maximum depth of the representation. If None, the tree is fully generated.

**feature\_names**array-like of shape (n\_features,), default=None

An array containing the feature names. If None, generic names will be used (“x\[0\]”, “x\[1\]”, …).

**class\_names**array-like of shape (n\_classes,) or bool, default=None

Names of each of the target classes in ascending numerical order. Only relevant for classification and not supported for multi-output. If `True`, shows a symbolic representation of the class name.

**label**{‘all’, ‘root’, ‘none’}, default=’all’

Whether to show informative labels for impurity, etc. Options include ‘all’ to show at every node, ‘root’ to show only at the top root node, or ‘none’ to not show at any node.

**filled**bool, default=False

When set to `True`, paint nodes to indicate majority class for classification, extremity of values for regression, or purity of node for multi-output.

**leaves\_parallel**bool, default=False

When set to `True`, draw all leaf nodes at the bottom of the tree.

**impurity**bool, default=True

When set to `True`, show the impurity at each node.

**node\_ids**bool, default=False

When set to `True`, show the ID number on each node.

**proportion**bool, default=False

When set to `True`, change the display of ‘values’ and/or ‘samples’ to be proportions and percentages respectively.

**rotate**bool, default=False

When set to `True`, orient tree left to right rather than top-down.

**rounded**bool, default=False

When set to `True`, draw node boxes with rounded corners.

**special\_characters**bool, default=False

When set to `False`, ignore special characters for PostScript compatibility.

**precision**int, default=3

Number of digits of precision for floating point in the values of impurity, threshold and value attributes of each node.

**fontname**str, default=’helvetica’

Name of font used to render text.

Returns:

**dot\_data**str

String representation of the input tree in GraphViz dot format. Only returned if `out_file` is None.

Added in version 0.18.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn import tree

Copy to clipboard

\>>> clf \= tree.DecisionTreeClassifier()
\>>> iris \= load\_iris()

Copy to clipboard

\>>> clf \= clf.fit(iris.data, iris.target)
\>>> tree.export\_graphviz(clf)
'digraph Tree {...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)