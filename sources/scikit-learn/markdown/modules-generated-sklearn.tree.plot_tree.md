[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.tree.plot_tree.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.tree.plot_tree.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.tree.plot_tree.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.tree.plot_tree.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.tree.plot_tree.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.tree.plot_tree.html)

Collapse Sidebar Expand Sidebar

plot\_tree[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#plot-tree "Link to this heading")

==============================================================================================================================

sklearn.tree.plot\_tree(_decision\_tree_, _\*_, _max\_depth\=None_, _feature\_names\=None_, _class\_names\=None_, _label\='all'_, _filled\=False_, _impurity\=True_, _node\_ids\=False_, _proportion\=False_, _rounded\=False_, _precision\=3_, _ax\=None_, _fontsize\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_export.py#L86)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "Link to this definition")

Plot a decision tree.

The sample counts that are shown are weighted with any sample\_weights that might be present.

The visualization is fit automatically to the size of the axis. Use the `figsize` or `dpi` arguments of `plt.figure` to control the size of the rendering.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree)
.

Added in version 0.21.

Parameters:

**decision\_tree**decision tree regressor or classifier

The decision tree to be plotted.

**max\_depth**int, default=None

The maximum depth of the representation. If None, the tree is fully generated.

**feature\_names**array-like of str, default=None

Names of each of the features. If None, generic names will be used (“x\[0\]”, “x\[1\]”, …).

**class\_names**array-like of str or True, default=None

Names of each of the target classes in ascending numerical order. Only relevant for classification and not supported for multi-output. If `True`, shows a symbolic representation of the class name.

**label**{‘all’, ‘root’, ‘none’}, default=’all’

Whether to show informative labels for impurity, etc. Options include ‘all’ to show at every node, ‘root’ to show only at the top root node, or ‘none’ to not show at any node.

**filled**bool, default=False

When set to `True`, paint nodes to indicate majority class for classification, extremity of values for regression, or purity of node for multi-output.

**impurity**bool, default=True

When set to `True`, show the impurity at each node.

**node\_ids**bool, default=False

When set to `True`, show the ID number on each node.

**proportion**bool, default=False

When set to `True`, change the display of ‘values’ and/or ‘samples’ to be proportions and percentages respectively.

**rounded**bool, default=False

When set to `True`, draw node boxes with rounded corners and use Helvetica fonts instead of Times-Roman.

**precision**int, default=3

Number of digits of precision for floating point in the values of impurity, threshold and value attributes of each node.

**ax**matplotlib axis, default=None

Axes to plot to. If None, use current axis. Any previous content is cleared.

**fontsize**int, default=None

Size of text font. If None, determined automatically to fit figure.

Returns:

**annotations**list of artists

List containing the artists for the annotation boxes making up the tree.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn import tree

Copy to clipboard

\>>> clf \= tree.DecisionTreeClassifier(random\_state\=0)
\>>> iris \= load\_iris()

Copy to clipboard

\>>> clf \= clf.fit(iris.data, iris.target)
\>>> tree.plot\_tree(clf)
\[...\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_unveil_tree_structure_thumb.png)

[Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)

Understanding the decision tree structure

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)