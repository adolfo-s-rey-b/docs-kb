[Skip to main content](https://scikit-learn.org/stable/modules/tree.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/tree.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/tree.html)
[1.8.0](https://scikit-learn.org/1.8/modules/tree.html)
[1.7.2](https://scikit-learn.org/1.7/modules/tree.html)
[1.6.1](https://scikit-learn.org/1.6/modules/tree.html)
[1.5.2](https://scikit-learn.org/1.5/modules/tree.html)
[1.4.2](https://scikit-learn.org/1.4/modules/tree.html)

Collapse Sidebar Expand Sidebar

1.10. Decision Trees[#](https://scikit-learn.org/stable/modules/tree.html#decision-trees "Link to this heading")

=================================================================================================================

**Decision Trees (DTs)** are a non-parametric supervised learning method used for [classification](https://scikit-learn.org/stable/modules/tree.html#tree-classification)
 and [regression](https://scikit-learn.org/stable/modules/tree.html#tree-regression)
. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features. A tree can be seen as a piecewise constant approximation.

For instance, in the example below, decision trees learn from data to approximate a sine curve with a set of if-then-else decision rules. The deeper the tree, the more complex the decision rules and the fitter the model.

[![../_images/sphx_glr_plot_tree_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Some advantages of decision trees are:

*   Simple to understand and to interpret. Trees can be visualized.
    
*   Requires little data preparation. Other techniques often require data normalization, dummy variables need to be created and blank values to be removed. Some tree and algorithm combinations support [missing values](https://scikit-learn.org/stable/modules/tree.html#tree-missing-value-support)
    .
    
*   The cost of using the tree (i.e., predicting data) is logarithmic in the number of data points used to train the tree.
    
*   Able to handle both numerical and categorical data. However, the scikit-learn implementation does not support categorical variables for now. Other techniques are usually specialized in analyzing datasets that have only one type of variable. See [algorithms](https://scikit-learn.org/stable/modules/tree.html#tree-algorithms)
     for more information.
    
*   Able to handle multi-output problems.
    
*   Uses a white box model. If a given situation is observable in a model, the explanation for the condition is easily explained by boolean logic. By contrast, in a black box model (e.g., in an artificial neural network), results may be more difficult to interpret.
    
*   Possible to validate a model using statistical tests. That makes it possible to account for the reliability of the model.
    
*   Performs well even if its assumptions are somewhat violated by the true model from which the data were generated.
    

The disadvantages of decision trees include:

*   Decision-tree learners can create over-complex trees that do not generalize the data well. This is called overfitting. Mechanisms such as pruning, setting the minimum number of samples required at a leaf node or setting the maximum depth of the tree are necessary to avoid this problem.
    
*   Decision trees can be unstable because small variations in the data might result in a completely different tree being generated. This problem is mitigated by using decision trees within an ensemble.
    
*   Predictions of decision trees are neither smooth nor continuous, but piecewise constant approximations as seen in the above figure. Therefore, they are not good at extrapolation.
    
*   The problem of learning an optimal decision tree is known to be NP-complete under several aspects of optimality and even for simple concepts. Consequently, practical decision-tree learning algorithms are based on heuristic algorithms such as the greedy algorithm where locally optimal decisions are made at each node. Such algorithms cannot guarantee to return the globally optimal decision tree. This can be mitigated by training multiple trees in an ensemble learner, where the features and samples are randomly sampled with replacement.
    
*   There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems.
    
*   Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.
    

1.10.1. Classification[#](https://scikit-learn.org/stable/modules/tree.html#classification "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 is a class capable of performing multi-class classification on a dataset.

As with other classifiers, [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 takes as input two arrays: an array X, sparse or dense, of shape `(n_samples, n_features)` holding the training samples, and an array Y of integer values, shape `(n_samples,)`, holding the class labels for the training samples:

\>>> from sklearn import tree
\>>> X \= \[\[0, 0\], \[1, 1\]\]
\>>> Y \= \[0, 1\]
\>>> clf \= tree.DecisionTreeClassifier()
\>>> clf \= clf.fit(X, Y)

Copy to clipboard

After being fitted, the model can then be used to predict the class of samples:

\>>> clf.predict(\[\[2., 2.\]\])
array(\[1\])

Copy to clipboard

In case that there are multiple classes with the same and highest probability, the classifier will predict the class with the lowest index amongst those classes.

As an alternative to outputting a specific class, the probability of each class can be predicted, which is the fraction of training samples of the class in a leaf:

\>>> clf.predict\_proba(\[\[2., 2.\]\])
array(\[\[0., 1.\]\])

Copy to clipboard

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 is capable of both binary (where the labels are \[-1, 1\]) classification and multiclass (where the labels are \[0, …, K-1\]) classification.

Using the Iris dataset, we can construct a tree as follows:

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn import tree
\>>> iris \= load\_iris()
\>>> X, y \= iris.data, iris.target
\>>> clf \= tree.DecisionTreeClassifier()
\>>> clf \= clf.fit(X, y)

Copy to clipboard

Once trained, you can plot the tree with the [`plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
 function:

\>>> tree.plot\_tree(clf)
\[...\]

Copy to clipboard

[![../_images/sphx_glr_plot_iris_dtc_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_002.png)](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Alternative ways to export trees[#](https://scikit-learn.org/stable/modules/tree.html#alternative-ways-to-export-trees "Link to this dropdown")

We can also export the tree in [Graphviz](https://www.graphviz.org/)
 format using the [`export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
 exporter. If you use the [conda](https://conda.io/)
 package manager, the graphviz binaries and the python package can be installed with `conda install python-graphviz`.

Alternatively binaries for graphviz can be downloaded from the graphviz project homepage, and the Python wrapper installed from pypi with `pip install graphviz`.

Below is an example graphviz export of the above tree trained on the entire iris dataset; the results are saved in an output file `iris.pdf`:

\>>> import graphviz
\>>> dot\_data \= tree.export\_graphviz(clf, out\_file\=None)
\>>> graph \= graphviz.Source(dot\_data)
\>>> graph.render("iris")

Copy to clipboard

The [`export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
 exporter also supports a variety of aesthetic options, including coloring nodes by their class (or value for regression) and using explicit variable and class names if desired. Jupyter notebooks also render these plots inline automatically:

\>>> dot\_data \= tree.export\_graphviz(clf, out\_file\=None,
...                      feature\_names\=iris.feature\_names,
...                      class\_names\=iris.target\_names,
...                      filled\=True, rounded\=True,
...                      special\_characters\=True)
\>>> graph \= graphviz.Source(dot\_data)
\>>> graph

Copy to clipboard

![../_images/iris.svg](https://scikit-learn.org/stable/_images/iris.svg)

[![../_images/sphx_glr_plot_iris_dtc_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_001.png)](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Alternatively, the tree can also be exported in textual format with the function [`export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")
. This method doesn’t require the installation of external libraries and is more compact:

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> from sklearn.tree import export\_text
\>>> iris \= load\_iris()
\>>> decision\_tree \= DecisionTreeClassifier(random\_state\=0, max\_depth\=2)
\>>> decision\_tree \= decision\_tree.fit(iris.data, iris.target)
\>>> r \= export\_text(decision\_tree, feature\_names\=iris\['feature\_names'\])
\>>> print(r)
|--- petal width (cm) <= 0.80
|   |--- class: 0
|--- petal width (cm) >  0.80
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2

Copy to clipboard

Examples

*   [Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#sphx-glr-auto-examples-tree-plot-iris-dtc-py)
    
*   [Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)
    

1.10.2. Regression[#](https://scikit-learn.org/stable/modules/tree.html#regression "Link to this heading")

-----------------------------------------------------------------------------------------------------------

[![../_images/sphx_glr_plot_tree_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision trees can also be applied to regression problems, using the [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
 class.

As in the classification setting, the fit method will take as argument arrays X and y, only that in this case y is expected to have floating point values instead of integer values:

\>>> from sklearn import tree
\>>> X \= \[\[0, 0\], \[2, 2\]\]
\>>> y \= \[0.5, 2.5\]
\>>> clf \= tree.DecisionTreeRegressor()
\>>> clf \= clf.fit(X, y)
\>>> clf.predict(\[\[1, 1\]\])
array(\[0.5\])

Copy to clipboard

Examples

*   [Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py)
    

1.10.3. Multi-output problems[#](https://scikit-learn.org/stable/modules/tree.html#multi-output-problems "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

A multi-output problem is a supervised learning problem with several outputs to predict, that is when Y is a 2d array of shape `(n_samples, n_outputs)`.

When there is no correlation between the outputs, a very simple way to solve this kind of problem is to build n independent models, i.e. one for each output, and then to use those models to independently predict each one of the n outputs. However, because it is likely that the output values related to the same input are themselves correlated, an often better way is to build a single model capable of predicting simultaneously all n outputs. First, it requires lower training time since only a single estimator is built. Second, the generalization accuracy of the resulting estimator may often be increased.

With regard to decision trees, this strategy can readily be used to support multi-output problems. This requires the following changes:

*   Store n output values in leaves, instead of 1;
    
*   Use splitting criteria that compute the average reduction across all n outputs.
    

This module offers support for multi-output problems by implementing this strategy in both [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 and [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
. If a decision tree is fit on an output array Y of shape `(n_samples, n_outputs)` then the resulting estimator will:

*   Output n\_output values upon `predict`;
    
*   Output a list of n\_output arrays of class probabilities upon `predict_proba`.
    

The use of multi-output trees for regression is demonstrated in [Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py)
. In this example, the input X is a single real value and the outputs Y are the sine and cosine of X.

[![../_images/sphx_glr_plot_tree_regression_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_002.png)](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

The use of multi-output trees for classification is demonstrated in [Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-auto-examples-miscellaneous-plot-multioutput-face-completion-py)
. In this example, the inputs X are the pixels of the upper half of faces and the outputs Y are the pixels of the lower half of those faces.

[![../_images/sphx_glr_plot_multioutput_face_completion_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html)

Examples

*   [Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-auto-examples-miscellaneous-plot-multioutput-face-completion-py)
    

References

*   M. Dumont et al, [Fast multi-class image annotation with random subwindows and multiple output randomized trees](https://www.montefiore.ulg.ac.be/services/stochastic/pubs/2009/DMWG09/dumont-visapp09-shortpaper.pdf)
    , International Conference on Computer Vision Theory and Applications 2009
    

1.10.4. Complexity[#](https://scikit-learn.org/stable/modules/tree.html#complexity "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The following table shows the worst-case complexity estimates for a balanced binary tree:

| Splitter | Total training cost | Total inference cost |
| --- | --- | --- |
| “best” | O(nfeaturesnsamples2log⁡(nsamples)) | O(log⁡(nsamples)) |
| “random” | O(nfeaturesnsamples2) | O(log⁡(nsamples)) |

In general, the training cost to construct a balanced binary tree **at each node** is

O(nfeaturesnsampleslog⁡(nsamples))+O(nfeaturesnsamples)

The first term is the cost of sorting nsamples repeated for nfeatures. The second term is the linear scan over candidate split points to find the feature that offers the largest reduction in the impurity criterion. The latter is sub-leading for the greedy splitter strategy “best”, and is therefore typically discarded.

Regardless of the splitting strategy, after summing the cost over **all internal nodes**, the total complexity scales linearly with nnodes\=nleaves−1, which is O(nsamples) in the worst-case complexity, that is, when the tree is grown until each sample ends up in its own leaf.

Many implementations such as scikit-learn use efficient caching tricks to keep track of the general order of indices at each node such that the features do not need to be re-sorted at each node; hence, the time complexity of these implementations is just O(nfeaturesnsampleslog⁡(nsamples)) [\[1\]](https://scikit-learn.org/stable/modules/tree.html#id2)
.

Inference cost is independent of the splitter strategy. It depends only on the tree depth, O(depth). In an approximately balanced binary tree, each split halves the data, and then the number of such halvings grows with the depth as powers of two. If this process continues until each sample is isolated in its own leaf, the resulting depth is O(log⁡(nsamples)).

References

1.10.5. Tips on practical use[#](https://scikit-learn.org/stable/modules/tree.html#tips-on-practical-use "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

*   Decision trees tend to overfit on data with a large number of features. Getting the right ratio of samples to number of features is important, since a tree with few samples in high dimensional space is very likely to overfit.
    
*   Consider performing dimensionality reduction ([PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca)
    , [ICA](https://scikit-learn.org/stable/modules/decomposition.html#ica)
    , or [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
    ) beforehand to give your tree a better chance of finding features that are discriminative.
    
*   [Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)
     will help in gaining more insights about how the decision tree makes predictions, which is important for understanding the important features in the data.
    
*   Visualize your tree as you are training by using the `export` function. Use `max_depth=3` as an initial tree depth to get a feel for how the tree is fitting to your data, and then increase the depth.
    
*   Remember that the number of samples required to populate the tree doubles for each additional level the tree grows to. Use `max_depth` to control the size of the tree to prevent overfitting.
    
*   Use `min_samples_split` or `min_samples_leaf` to ensure that multiple samples inform every decision in the tree, by controlling which splits will be considered. A very small number will usually mean the tree will overfit, whereas a large number will prevent the tree from learning the data. Try `min_samples_leaf=5` as an initial value. If the sample size varies greatly, a float number can be used as percentage in these two parameters. While `min_samples_split` can create arbitrarily small leaves, `min_samples_leaf` guarantees that each leaf has a minimum size, avoiding low-variance, over-fit leaf nodes in regression problems. For classification with few classes, `min_samples_leaf=1` is often the best choice.
    
    Note that `min_samples_split` considers samples directly and independent of `sample_weight`, if provided (e.g. a node with m weighted samples is still treated as having exactly m samples). Consider `min_weight_fraction_leaf` or `min_impurity_decrease` if accounting for sample weights is required at splits.
    
*   Balance your dataset before training to prevent the tree from being biased toward the classes that are dominant. Class balancing can be done by sampling an equal number of samples from each class, or preferably by normalizing the sum of the sample weights (`sample_weight`) for each class to the same value. Also note that weight-based pre-pruning criteria, such as `min_weight_fraction_leaf`, will then be less biased toward dominant classes than criteria that are not aware of the sample weights, like `min_samples_leaf`.
    
*   If the samples are weighted, it will be easier to optimize the tree structure using weight-based pre-pruning criterion such as `min_weight_fraction_leaf`, which ensures that leaf nodes contain at least a fraction of the overall sum of the sample weights.
    
*   All decision trees use `np.float32` arrays internally. If training data is not in this format, a copy of the dataset will be made.
    
*   If the input matrix X is very sparse, it is recommended to convert to sparse `csc_matrix` before calling fit and sparse `csr_matrix` before calling predict. Training time can be orders of magnitude faster for a sparse matrix input compared to a dense matrix when features have zero values in most of the samples.
    

1.10.6. Tree algorithms: ID3, C4.5, C5.0 and CART[#](https://scikit-learn.org/stable/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

What are all the various decision tree algorithms and how do they differ from each other? Which one is implemented in scikit-learn?

Various decision tree algorithms[#](https://scikit-learn.org/stable/modules/tree.html#various-decision-tree-algorithms "Link to this dropdown")

[ID3](https://en.wikipedia.org/wiki/ID3_algorithm)
 (Iterative Dichotomiser 3) was developed in 1986 by Ross Quinlan. The algorithm creates a multiway tree, finding for each node (i.e. in a greedy manner) the categorical feature that will yield the largest information gain for categorical targets. Trees are grown to their maximum size and then a pruning step is usually applied to improve the ability of the tree to generalize to unseen data.

C4.5 is the successor to ID3 and removed the restriction that features must be categorical by dynamically defining a discrete attribute (based on numerical variables) that partitions the continuous attribute value into a discrete set of intervals. C4.5 converts the trained trees (i.e. the output of the ID3 algorithm) into sets of if-then rules. The accuracy of each rule is then evaluated to determine the order in which they should be applied. Pruning is done by removing a rule’s precondition if the accuracy of the rule improves without it.

C5.0 is Quinlan’s latest version release under a proprietary license. It uses less memory and builds smaller rulesets than C4.5 while being more accurate.

CART (Classification and Regression Trees) is very similar to C4.5, but it differs in that it supports numerical target variables (regression) and does not compute rule sets. CART constructs binary trees using the feature and threshold that yield the largest information gain at each node.

scikit-learn uses an optimized version of the CART algorithm; however, the scikit-learn implementation does not support categorical variables for now.

1.10.7. Mathematical formulation[#](https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Given training vectors xi∈Rn, i=1,…, l and a label vector y∈Rl, a decision tree recursively partitions the feature space such that the samples with the same labels or similar target values are grouped together.

Let the data at node m be represented by Qm with nm samples. For each candidate split θ\=(j,tm) consisting of a feature j and threshold tm, partition the data into Qmleft(θ) and Qmright(θ) subsets

Qmleft(θ)\={(x,y)|xj≤tm}Qmright(θ)\=Qm∖Qmleft(θ)

The quality of a candidate split of node m is then computed using an impurity function or loss function H(), the choice of which depends on the task being solved (classification or regression)

G(Qm,θ)\=nmleftnmH(Qmleft(θ))+nmrightnmH(Qmright(θ))

Select the parameters that minimises the impurity

θ∗\=argminθG(Qm,θ)

The strategy to choose the split at each node is controlled by the `splitter` parameter:

*   With the **best splitter** (default, `splitter='best'`), θ∗ is found by performing a **greedy exhaustive search** over all available features and all possible thresholds tm (i.e. midpoints between sorted, distinct feature values), selecting the pair that exactly minimizes G(Qm,θ).
    
*   With the **random splitter** (`splitter='random'`), θ∗ is found by sampling a **single random candidate threshold** for each available feature. This performs a stochastic approximation of the greedy search, effectively reducing computation time (see [Complexity](https://scikit-learn.org/stable/modules/tree.html#tree-complexity)
    ).
    

[`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
 and [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
 use `splitter='random'` by default and share the same implementation as their corresponding decision tree estimators, apart from default parameter values.

After choosing the optimal split θ∗ at node m, the same splitting procedure is then applied recursively to each partition Qmleft(θ∗) and Qmright(θ∗) until a stopping condition is reached, such as:

*   the maximum allowable depth is reached (`max_depth`);
    
*   nm is smaller than `min_samples_split`;
    
*   the impurity decrease for this split is smaller than `min_impurity_decrease`.
    

See the respective estimator docstring for other stopping conditions.

### 1.10.7.1. Classification criteria[#](https://scikit-learn.org/stable/modules/tree.html#classification-criteria "Link to this heading")

If a target is a classification outcome taking on values 0,1,…,K-1, for node m, let

pmk\=1nm∑y∈QmI(y\=k)

be the proportion of class k observations in node m. If m is a terminal node, `predict_proba` for this region is set to pmk. Common measures of impurity are the following.

Gini:

H(Qm)\=∑kpmk(1−pmk)

Log Loss or Entropy:

H(Qm)\=−∑kpmklog⁡(pmk)

Shannon entropy[#](https://scikit-learn.org/stable/modules/tree.html#shannon-entropy "Link to this dropdown")

The entropy criterion computes the Shannon entropy of the possible classes. It takes the class frequencies of the training data points that reached a given leaf m as their probability. Using the **Shannon entropy as tree node splitting criterion is equivalent to minimizing the log loss** (also known as cross-entropy and multinomial deviance) between the true labels yi and the probabilistic predictions Tk(xi) of the tree model T for class k.

To see this, first recall that the log loss of a tree model T computed on a dataset D is defined as follows:

LL(D,T)\=−1n∑(xi,yi)∈D∑kI(yi\=k)log⁡(Tk(xi))

where D is a training dataset of n pairs (xi,yi).

In a classification tree, the predicted class probabilities within leaf nodes are constant, that is: for all (xi,yi)∈Qm, one has: Tk(xi)\=pmk for each class k.

This property makes it possible to rewrite LL(D,T) as the sum of the Shannon entropies computed for each leaf of T weighted by the number of training data points that reached each leaf:

LL(D,T)\=∑m∈TnmnH(Qm)

### 1.10.7.2. Regression criteria[#](https://scikit-learn.org/stable/modules/tree.html#regression-criteria "Link to this heading")

If the target is a continuous value, then for node m, common criteria to minimize as for determining locations for future splits are Mean Squared Error (MSE or L2 error), Poisson deviance as well as Mean Absolute Error (MAE or L1 error). MSE and Poisson deviance both set the predicted value of terminal nodes to the learned mean value y¯m of the node whereas the MAE sets the predicted value of terminal nodes to the median median(y)m.

Mean Squared Error:

y¯m\=1nm∑y∈QmyH(Qm)\=1nm∑y∈Qm(y−y¯m)2

Mean Poisson deviance:

H(Qm)\=2nm∑y∈Qm(ylog⁡yy¯m−y+y¯m)

Setting `criterion="poisson"` might be a good choice if your target is a count or a frequency (count per some unit). In any case, y\>=0 is a necessary condition to use this criterion. For performance reasons the actual implementation minimizes the half mean poisson deviance, i.e. the mean poisson deviance divided by 2.

Mean Absolute Error:

median(y)m\=mediany∈Qm(y)H(Qm)\=1nm∑y∈Qm|y−median(y)m|

Note that it is 3–6× slower to fit than the MSE criterion as of version 1.8.

1.10.8. Missing Values Support[#](https://scikit-learn.org/stable/modules/tree.html#missing-values-support "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
, [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
 have built-in support for missing values using `splitter='best'`, where the splits are determined in a greedy fashion. [`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
, and [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
 have built-in support for missing values for `splitter='random'`, where the splits are determined randomly. For more details on how the splitter differs on non-missing values, see the [Forest section](https://scikit-learn.org/stable/modules/ensemble.html#forest)
.

First we will describe how [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
, [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
 handle missing-values in the data.

For each potential threshold on the non-missing data, the splitter will evaluate the split with all the missing values going to the left node or the right node.

Decisions are made as follows:

*   By default when predicting, the samples with missing values are classified with the class used in the split found during training:
    
    \>>> from sklearn.tree import DecisionTreeClassifier
    \>>> import numpy as np
    
    \>>> X \= np.array(\[0, 1, 6, np.nan\]).reshape(\-1, 1)
    \>>> y \= \[0, 0, 1, 1\]
    
    \>>> tree \= DecisionTreeClassifier(random\_state\=0).fit(X, y)
    \>>> tree.predict(X)
    array(\[0, 0, 1, 1\])
    
    Copy to clipboard
    
*   If the criterion evaluation is the same for both nodes, then the tie for missing value at predict time is broken by going to the right node. The splitter also checks the split where all the missing values go to one child and non-missing values go to the other:
    
    \>>> from sklearn.tree import DecisionTreeClassifier
    \>>> import numpy as np
    
    \>>> X \= np.array(\[np.nan, \-1, np.nan, 1\]).reshape(\-1, 1)
    \>>> y \= \[0, 0, 1, 1\]
    
    \>>> tree \= DecisionTreeClassifier(random\_state\=0, max\_depth\=1).fit(X, y)
    
    \>>> X\_test \= np.array(\[np.nan\]).reshape(\-1, 1)
    \>>> tree.predict(X\_test)
    array(\[1\])
    
    Copy to clipboard
    
*   If no missing values are seen during training for a given feature, then during prediction missing values are mapped to the child with the most samples:
    
    \>>> from sklearn.tree import DecisionTreeClassifier
    \>>> import numpy as np
    
    \>>> X \= np.array(\[0, 1, 2, 3\]).reshape(\-1, 1)
    \>>> y \= \[0, 1, 1, 1\]
    
    \>>> tree \= DecisionTreeClassifier(random\_state\=0).fit(X, y)
    
    \>>> X\_test \= np.array(\[np.nan\]).reshape(\-1, 1)
    \>>> tree.predict(X\_test)
    array(\[1\])
    
    Copy to clipboard
    

[`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
, and [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
 handle missing values in a slightly different way. When splitting a node, a random threshold will be chosen to split the non-missing values on. Then the non-missing values will be sent to the left and right child based on the randomly selected threshold, while the missing values will also be randomly sent to the left or right child. This is repeated for every feature considered at each split. The best split among these is chosen.

During prediction, the treatment of missing-values is the same as that of the decision tree:

*   By default when predicting, the samples with missing values are classified with the class used in the split found during training.
    
*   If no missing values are seen during training for a given feature, then during prediction missing values are mapped to the child with the most samples.
    

1.10.9. Minimal Cost-Complexity Pruning[#](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Minimal cost-complexity pruning is an algorithm used to prune a tree to avoid over-fitting, described in Chapter 3 of [\[BRE\]](https://scikit-learn.org/stable/modules/tree.html#bre)
. This algorithm is parameterized by α≥0 known as the complexity parameter. The complexity parameter is used to define the cost-complexity measure, Rα(T) of a given tree T:

Rα(T)\=R(T)+α|T~|

where |T~| is the number of terminal nodes in T and R(T) is traditionally defined as the total misclassification rate of the terminal nodes. Alternatively, scikit-learn uses the total sample weighted impurity of the terminal nodes for R(T). As shown above, the impurity of a node depends on the criterion. Minimal cost-complexity pruning finds the subtree of T that minimizes Rα(T).

The cost complexity measure of a single node is Rα(t)\=R(t)+α. The branch, Tt, is defined to be a tree where node t is its root. In general, the impurity of a node is greater than the sum of impurities of its terminal nodes, R(Tt)<R(t). However, the cost complexity measure of a node, t, and its branch, Tt, can be equal depending on α. We define the effective α of a node to be the value where they are equal, Rα(Tt)\=Rα(t) or αeff(t)\=R(t)−R(Tt)|T|−1. A non-terminal node with the smallest value of αeff is the weakest link and will be pruned. This process stops when the pruned tree’s minimal αeff is greater than the `ccp_alpha` parameter.

Examples

*   [Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)
    

References

\[[BRE](https://scikit-learn.org/stable/modules/tree.html#id5)\
\]

L. Breiman, J. Friedman, R. Olshen, and C. Stone. Classification and Regression Trees. Wadsworth, Belmont, CA, 1984.

*   [https://en.wikipedia.org/wiki/Decision\_tree\_learning](https://en.wikipedia.org/wiki/Decision_tree_learning)
    
*   [https://en.wikipedia.org/wiki/Predictive\_analytics](https://en.wikipedia.org/wiki/Predictive_analytics)
    
*   J.R. Quinlan. C4. 5: programs for machine learning. Morgan Kaufmann, 1993.
    
*   T. Hastie, R. Tibshirani and J. Friedman. Elements of Statistical Learning, Springer, 2009.
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)