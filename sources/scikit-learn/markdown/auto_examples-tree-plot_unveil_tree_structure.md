[Skip to main content](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/tree/plot_unveil_tree_structure.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/tree/plot_unveil_tree_structure.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/tree/plot_unveil_tree_structure.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/tree/plot_unveil_tree_structure.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/tree/plot_unveil_tree_structure.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/tree/plot_unveil_tree_structure.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-download-auto-examples-tree-plot-unveil-tree-structure-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Understanding the decision tree structure[#](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#understanding-the-decision-tree-structure "Link to this heading")

==================================================================================================================================================================================================

The decision tree structure can be analysed to gain further insight on the relation between the features and the target to predict. In this example, we show how to retrieve:

*   the binary tree structure;
    
*   the depth of each node and whether or not it’s a leaf;
    
*   the nodes that were reached by a sample using the `decision_path` method;
    
*   the leaf that was reached by a sample using the apply method;
    
*   the rules that were used to predict a sample;
    
*   the decision path shared by a group of samples.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn import tree
from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

Copy to clipboard

Train tree classifier[#](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#train-tree-classifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

First, we fit a [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 using the [`load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
 dataset.

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

clf \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(max\_leaf\_nodes\=3, random\_state\=0)
clf.fit(X\_train, y\_train)

Copy to clipboard

DecisionTreeClassifier(max\_leaf\_nodes=3, random\_state=0)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

DecisionTreeClassifier

[?Documentation for DecisionTreeClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of the estimator. The features are always  <br>randomly permuted at each split, even if \`\`splitter\`\` is set to  <br>\`\`"best"\`\`. When \`\`max\_features < n\_features\`\`, the algorithm will  <br>select \`\`max\_features\`\` at random at each split before finding the best  <br>split among them. But the best found split may vary across different  <br>runs, even if \`\`max\_features=n\_features\`\`. That is the case, if the  <br>improvement of the criterion is identical for several splits and one  <br>split has to be selected at random. To obtain a deterministic behaviour  <br>during fitting, \`\`random\_state\`\` has to be fixed to an integer.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow a tree with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | 3   |
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini' |
|     | [splitter splitter: {"best", "random"}, default="best"  <br>  <br>The strategy used to choose the split at each node. Supported  <br>strategies are "best" to choose the best split and "random" to choose  <br>the best random split among considered features for this split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=splitter,-%7B%22best%22%2C%20%22random%22%7D%2C%20default%3D%22best%22) | 'best' |
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_features max\_features: int, float or {"sqrt", "log2"}, default=None  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at  <br>each split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>Note: splitting may inspect more than \`\`max\_features\`\` features if  <br>needed to find a valid split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=max_features,-int%2C%20float%20or%20%7B%22sqrt%22%2C%20%22log2%22%7D%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [class\_weight class\_weight: dict, list of dict or "balanced", default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If None, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=class_weight,-dict%2C%20list%20of%20dict%20or%20%22balanced%22%2C%20default%3DNone) | None |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,) or list of ndarray  <br>  <br>The classes labels (single output problem),  <br>or a list of arrays of class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20list%20of%20ndarray) | ndarray\[int64\](3,) | \[0,1,2\] |
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance \[4\]\_.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](4,) | \[0. ,0. ,0.44,0.56\] |
| [max\_features\_ max\_features\_: int  <br>  <br>The inferred value of max\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=max_features_,-int) | int | 4   |
| [n\_classes\_ n\_classes\_: int or list of int  <br>  <br>The number of classes (for single output problems),  <br>or a list containing the number of classes for each  <br>output (for multi-output problems).](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=n_classes_,-int%20or%20list%20of%20int) | int64 | np.int64(3) |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=n_features_in_,-int) | int | 4   |
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=n_outputs_,-int) | int | 1   |
| [tree\_ tree\_: Tree instance  <br>  <br>The underlying Tree object. Please refer to  <br>\`\`help(sklearn.tree.\_tree.Tree)\`\` for attributes of Tree object and  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_unveil\_tree\_structure.py\`  <br>for basic usage of these attributes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeClassifier.html#:~:text=tree_,-Tree%20instance) | Tree | <sklearn.tree...x7e1dbd6093e0> |

  
  

Tree structure[#](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#tree-structure "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The decision classifier has an attribute called `tree_` which allows access to low level attributes such as `node_count`, the total number of nodes, and `max_depth`, the maximal depth of the tree. The `tree_.compute_node_depths()` method computes the depth of each node in the tree. `tree_` also stores the entire binary tree structure, represented as a number of parallel arrays. The i-th element of each array holds information about the node `i`. Node 0 is the tree’s root. Some of the arrays only apply to either leaves or split nodes. In this case the values of the nodes of the other type is arbitrary. For example, the arrays `feature` and `threshold` only apply to split nodes. The values for leaf nodes in these arrays are therefore arbitrary.

Among these arrays, we have:

*   `children_left[i]`: id of the left child of node `i` or -1 if leaf node
    
*   `children_right[i]`: id of the right child of node `i` or -1 if leaf node
    
*   `feature[i]`: feature used for splitting node `i`
    
*   `threshold[i]`: threshold value at node `i`
    
*   `n_node_samples[i]`: the number of training samples reaching node `i`
    
*   `impurity[i]`: the impurity at node `i`
    
*   `weighted_n_node_samples[i]`: the weighted number of training samples reaching node `i`
    
*   `value[i, j, k]`: the summary of the training samples that reached node i for output j and class k (for regression tree, class is set to 1). See below for more information about `value`.
    

Using the arrays, we can traverse the tree structure to compute various properties. Below, we will compute the depth of each node and whether or not it is a leaf.

n\_nodes \= clf.tree\_.node\_count
children\_left \= clf.tree\_.children\_left
children\_right \= clf.tree\_.children\_right
feature \= clf.tree\_.feature
threshold \= clf.tree\_.threshold
values \= clf.tree\_.value

node\_depth \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(shape\=n\_nodes, dtype\=[np.int64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
)
is\_leaves \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(shape\=n\_nodes, dtype\=bool)
stack \= \[(0, 0)\]  \# start with the root node id (0) and its depth (0)
while len(stack) \> 0:
    \# \`pop\` ensures each node is only visited once
    node\_id, depth \= stack.pop()
    node\_depth\[node\_id\] \= depth

    \# If the left and right child of a node is not the same we have a split
    \# node
    is\_split\_node \= children\_left\[node\_id\] != children\_right\[node\_id\]
    \# If a split node, append left and right children and depth to \`stack\`
    \# so we can loop through them
    if is\_split\_node:
        stack.append((children\_left\[node\_id\], depth + 1))
        stack.append((children\_right\[node\_id\], depth + 1))
    else:
        is\_leaves\[node\_id\] \= True

print(
    "The binary tree structure has {n} nodes and has "
    "the following tree structure:\\n".format(n\=n\_nodes)
)
for i in range(n\_nodes):
    if is\_leaves\[i\]:
        print(
            "{space}node={node} is a leaf node with value={value}.".format(
                space\=node\_depth\[i\] \* "\\t", node\=i, value\=[np.around](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")
(values\[i\], 3)
            )
        )
    else:
        print(
            "{space}node={node} is a split node with value={value}: "
            "go to node {left} if X\[:, {feature}\] <= {threshold} "
            "else to node {right}.".format(
                space\=node\_depth\[i\] \* "\\t",
                node\=i,
                left\=children\_left\[i\],
                feature\=feature\[i\],
                threshold\=threshold\[i\],
                right\=children\_right\[i\],
                value\=[np.around](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")
(values\[i\], 3),
            )
        )

Copy to clipboard

The binary tree structure has 5 nodes and has the following tree structure:

node=0 is a split node with value=\[\[0.33  0.304 0.366\]\]: go to node 1 if X\[:, 3\] <= 0.800000011920929 else to node 2.
        node=1 is a leaf node with value=\[\[1. 0. 0.\]\].
        node=2 is a split node with value=\[\[0.    0.453 0.547\]\]: go to node 3 if X\[:, 2\] <= 4.950000047683716 else to node 4.
                node=3 is a leaf node with value=\[\[0.    0.917 0.083\]\].
                node=4 is a leaf node with value=\[\[0.    0.026 0.974\]\].

Copy to clipboard

What is the values array used here?[#](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#what-is-the-values-array-used-here "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `tree_.value` array is a 3D array of shape \[`n_nodes`, `n_classes`, `n_outputs`\] which provides the proportion of samples reaching a node for each class and for each output. Each node has a `value` array which is the proportion of weighted samples reaching this node for each output and class with respect to the parent node.

One could convert this to the absolute weighted number of samples reaching a node, by multiplying this number by `tree_.weighted_n_node_samples[node_idx]` for the given node. Note sample weights are not used in this example, so the weighted number of samples is the number of samples reaching the node because each sample has a weight of 1 by default.

For example, in the above tree built on the iris dataset, the root node has `value = [0.33, 0.304, 0.366]` indicating there are 33% of class 0 samples, 30.4% of class 1 samples, and 36.6% of class 2 samples at the root node. One can convert this to the absolute number of samples by multiplying by the number of samples reaching the root node, which is `tree_.weighted_n_node_samples[0]`. Then the root node has `value = [37, 34, 41]`, indicating there are 37 samples of class 0, 34 samples of class 1, and 41 samples of class 2 at the root node.

Traversing the tree, the samples are split and as a result, the `value` array reaching each node changes. The left child of the root node has `value = [1., 0, 0]` (or `value = [37, 0, 0]` when converted to the absolute number of samples) because all 37 samples in the left child node are from class 0.

Note: In this example, `n_outputs=1`, but the tree classifier can also handle multi-output problems. The `value` array at each node would just be a 2D array instead.

We can compare the above output to the plot of the decision tree. Here, we show the proportions of samples of each class that reach each node corresponding to the actual elements of `tree_.value` array.

[tree.plot\_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
(clf, proportion\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot unveil tree structure](https://scikit-learn.org/stable/_images/sphx_glr_plot_unveil_tree_structure_001.png)

Decision path[#](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#decision-path "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

We can also retrieve the decision path of samples of interest. The `decision_path` method outputs an indicator matrix that allows us to retrieve the nodes the samples of interest traverse through. A non zero element in the indicator matrix at position `(i, j)` indicates that the sample `i` goes through the node `j`. Or, for one sample `i`, the positions of the non zero elements in row `i` of the indicator matrix designate the ids of the nodes that sample goes through.

The leaf ids reached by samples of interest can be obtained with the `apply` method. This returns an array of the node ids of the leaves reached by each sample of interest. Using the leaf ids and the `decision_path` we can obtain the splitting conditions that were used to predict a sample or a group of samples. First, let’s do it for one sample. Note that `node_index` is a sparse matrix.

node\_indicator \= clf.decision\_path(X\_test)
leaf\_id \= clf.apply(X\_test)

sample\_id \= 0
\# obtain ids of the nodes \`sample\_id\` goes through, i.e., row \`sample\_id\`
node\_index \= node\_indicator.indices\[\
    node\_indicator.indptr\[sample\_id\] : node\_indicator.indptr\[sample\_id + 1\]\
\]

print("Rules used to predict sample {id}:\\n".format(id\=sample\_id))
for node\_id in node\_index:
    \# continue to the next node if it is a leaf node
    if leaf\_id\[sample\_id\] \== node\_id:
        continue

    \# check if value of the split feature for sample 0 is below threshold
    if X\_test\[sample\_id, feature\[node\_id\]\] <= threshold\[node\_id\]:
        threshold\_sign \= "<="
    else:
        threshold\_sign \= ">"

    print(
        "decision node {node} : (X\_test\[{sample}, {feature}\] = {value}) "
        "{inequality} {threshold})".format(
            node\=node\_id,
            sample\=sample\_id,
            feature\=feature\[node\_id\],
            value\=X\_test\[sample\_id, feature\[node\_id\]\],
            inequality\=threshold\_sign,
            threshold\=threshold\[node\_id\],
        )
    )

Copy to clipboard

Rules used to predict sample 0:

decision node 0 : (X\_test\[0, 3\] = 2.4) > 0.800000011920929)
decision node 2 : (X\_test\[0, 2\] = 5.1) > 4.950000047683716)

Copy to clipboard

For a group of samples, we can determine the common nodes the samples go through.

sample\_ids \= \[0, 1\]
\# boolean array indicating the nodes both samples go through
common\_nodes \= node\_indicator.toarray()\[sample\_ids\].sum(axis\=0) \== len(sample\_ids)
\# obtain node ids using position in array
common\_node\_id \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_nodes)\[common\_nodes\]

print(
    "\\nThe following samples {samples} share the node(s) {nodes} in the tree.".format(
        samples\=sample\_ids, nodes\=common\_node\_id
    )
)
print("This is {prop}% of all nodes.".format(prop\=100 \* len(common\_node\_id) / n\_nodes))

Copy to clipboard

The following samples \[0, 1\] share the node(s) \[0 2\] in the tree.
This is 40.0% of all nodes.

Copy to clipboard

**Total running time of the script:** (0 minutes 0.134 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_unveil_tree_structure.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_unveil_tree_structure.ipynb)

[`Download Jupyter notebook: plot_unveil_tree_structure.ipynb`](https://scikit-learn.org/stable/_downloads/f7a387851c5762610f4e8197e52bbbca/plot_unveil_tree_structure.ipynb)

[`Download Python source code: plot_unveil_tree_structure.py`](https://scikit-learn.org/stable/_downloads/21a6ff17ef2837fe1cd49e63223a368d/plot_unveil_tree_structure.py)

[`Download zipped: plot_unveil_tree_structure.zip`](https://scikit-learn.org/stable/_downloads/95f7eb8e9a7edff8210ddbf69e096837/plot_unveil_tree_structure.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_dendrogram_thumb.png)

[Plot Hierarchical Clustering Dendrogram](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html)

Plot Hierarchical Clustering Dendrogram

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_thumb.png)

[Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html)

Post pruning decision trees with cost complexity pruning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/21a6ff17ef2837fe1cd49e63223a368d/plot_unveil_tree_structure.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f7a387851c5762610f4e8197e52bbbca/plot_unveil_tree_structure.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/95f7eb8e9a7edff8210ddbf69e096837/plot_unveil_tree_structure.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_unveil_tree_structure.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_unveil_tree_structure.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)