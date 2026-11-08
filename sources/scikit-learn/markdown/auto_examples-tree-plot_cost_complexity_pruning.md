[Skip to main content](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/tree/plot_cost_complexity_pruning.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/tree/plot_cost_complexity_pruning.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-download-auto-examples-tree-plot-cost-complexity-pruning-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Post pruning decision trees with cost complexity pruning[#](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#post-pruning-decision-trees-with-cost-complexity-pruning "Link to this heading")

==================================================================================================================================================================================================================================

The [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 provides parameters such as `min_samples_leaf` and `max_depth` to prevent a tree from overfitting. Cost complexity pruning provides another option to control the size of a tree. In [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
, this pruning technique is parameterized by the cost complexity parameter, `ccp_alpha`. Greater values of `ccp_alpha` increase the number of nodes pruned. Here we only show the effect of `ccp_alpha` on regularizing the trees and how to choose a `ccp_alpha` based on validation scores.

See also [Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)
 for details on pruning.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

Copy to clipboard

Total impurity of leaves vs effective alphas of pruned tree[#](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#total-impurity-of-leaves-vs-effective-alphas-of-pruned-tree "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Minimal cost complexity pruning recursively finds the node with the “weakest link”. The weakest link is characterized by an effective alpha, where the nodes with the smallest effective alpha are pruned first. To get an idea of what values of `ccp_alpha` could be appropriate, scikit-learn provides [`DecisionTreeClassifier.cost_complexity_pruning_path`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.cost_complexity_pruning_path "sklearn.tree.DecisionTreeClassifier.cost_complexity_pruning_path")
 that returns the effective alphas and the corresponding total leaf impurities at each step of the pruning process. As alpha increases, more of the tree is pruned, which increases the total impurity of its leaves.

X, y \= [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
(return\_X\_y\=True)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

clf \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(random\_state\=0)
path \= clf.cost\_complexity\_pruning\_path(X\_train, y\_train)
ccp\_alphas, impurities \= path.ccp\_alphas, path.impurities

Copy to clipboard

In the following plot, the maximum effective alpha value is removed, because it is the trivial tree with only one node.

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.plot(ccp\_alphas\[:\-1\], impurities\[:\-1\], marker\="o", drawstyle\="steps-post")
ax.set\_xlabel("effective alpha")
ax.set\_ylabel("total impurity of leaves")
ax.set\_title("Total Impurity vs effective alpha for training set")

Copy to clipboard

![Total Impurity vs effective alpha for training set](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_001.png)

Text(0.5, 1.0, 'Total Impurity vs effective alpha for training set')

Copy to clipboard

Next, we train a decision tree using the effective alphas. The last value in `ccp_alphas` is the alpha value that prunes the whole tree, leaving the tree, `clfs[-1]`, with one node.

clfs \= \[\]
for ccp\_alpha in ccp\_alphas:
    clf \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(random\_state\=0, ccp\_alpha\=ccp\_alpha)
    clf.fit(X\_train, y\_train)
    clfs.append(clf)
print(
    "Number of nodes in the last tree is: {} with ccp\_alpha: {}".format(
        clfs\[\-1\].tree\_.node\_count, ccp\_alphas\[\-1\]
    )
)

Copy to clipboard

Number of nodes in the last tree is: 1 with ccp\_alpha: 0.3272984419327777

Copy to clipboard

For the remainder of this example, we remove the last element in `clfs` and `ccp_alphas`, because it is the trivial tree with only one node. Here we show that the number of nodes and tree depth decreases as alpha increases.

clfs \= clfs\[:\-1\]
ccp\_alphas \= ccp\_alphas\[:\-1\]

node\_counts \= \[clf.tree\_.node\_count for clf in clfs\]
depth \= \[clf.tree\_.max\_depth for clf in clfs\]
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1)
ax\[0\].plot(ccp\_alphas, node\_counts, marker\="o", drawstyle\="steps-post")
ax\[0\].set\_xlabel("alpha")
ax\[0\].set\_ylabel("number of nodes")
ax\[0\].set\_title("Number of nodes vs alpha")
ax\[1\].plot(ccp\_alphas, depth, marker\="o", drawstyle\="steps-post")
ax\[1\].set\_xlabel("alpha")
ax\[1\].set\_ylabel("depth of tree")
ax\[1\].set\_title("Depth vs alpha")
fig.tight\_layout()

Copy to clipboard

![Number of nodes vs alpha, Depth vs alpha](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_002.png)

Accuracy vs alpha for training and testing sets[#](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#accuracy-vs-alpha-for-training-and-testing-sets "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When `ccp_alpha` is set to zero and keeping the other default parameters of [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
, the tree overfits, leading to a 100% training accuracy and 88% testing accuracy. As alpha increases, more of the tree is pruned, thus creating a decision tree that generalizes better. In this example, setting `ccp_alpha=0.015` maximizes the testing accuracy.

train\_scores \= \[clf.score(X\_train, y\_train) for clf in clfs\]
test\_scores \= \[clf.score(X\_test, y\_test) for clf in clfs\]

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.set\_xlabel("alpha")
ax.set\_ylabel("accuracy")
ax.set\_title("Accuracy vs alpha for training and testing sets")
ax.plot(ccp\_alphas, train\_scores, marker\="o", label\="train", drawstyle\="steps-post")
ax.plot(ccp\_alphas, test\_scores, marker\="o", label\="test", drawstyle\="steps-post")
ax.legend()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Accuracy vs alpha for training and testing sets](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_003.png)

**Total running time of the script:** (0 minutes 0.447 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_cost_complexity_pruning.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_cost_complexity_pruning.ipynb)

[`Download Jupyter notebook: plot_cost_complexity_pruning.ipynb`](https://scikit-learn.org/stable/_downloads/29998264311e172e4afe243096ca2c93/plot_cost_complexity_pruning.ipynb)

[`Download Python source code: plot_cost_complexity_pruning.py`](https://scikit-learn.org/stable/_downloads/93c278871f99c92a918dac30ee44a6a3/plot_cost_complexity_pruning.py)

[`Download zipped: plot_cost_complexity_pruning.zip`](https://scikit-learn.org/stable/_downloads/b77b3494346415433e29621203cd753c/plot_cost_complexity_pruning.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_unveil_tree_structure_thumb.png)

[Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)

Understanding the decision tree structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/93c278871f99c92a918dac30ee44a6a3/plot_cost_complexity_pruning.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/29998264311e172e4afe243096ca2c93/plot_cost_complexity_pruning.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b77b3494346415433e29621203cd753c/plot_cost_complexity_pruning.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_cost_complexity_pruning.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_cost_complexity_pruning.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)