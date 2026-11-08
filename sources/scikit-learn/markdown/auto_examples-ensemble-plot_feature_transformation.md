[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_feature_transformation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_feature_transformation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_feature_transformation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_feature_transformation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_feature_transformation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_feature_transformation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html#sphx-glr-download-auto-examples-ensemble-plot-feature-transformation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Feature transformations with ensembles of trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html#feature-transformations-with-ensembles-of-trees "Link to this heading")

===================================================================================================================================================================================================================

Transform your features into a higher dimensional, sparse space. Then train a linear model on these features.

First fit an ensemble of trees (totally random trees, a random forest, or gradient boosted trees) on the training set. Then each leaf of each tree in the ensemble is assigned a fixed arbitrary feature index in a new feature space. These leaf indices are then encoded in a one-hot fashion.

Each sample goes through the decisions of each tree of the ensemble and ends up in one leaf per tree. The sample is encoded by setting feature values for these leaves to 1 and the other feature values to 0.

The resulting transformer has then learned a supervised, sparse, high-dimensional categorical embedding of the data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

First, we will create a large dataset and split it into three sets:

*   a set to train the ensemble methods which are later used to as a feature engineering transformer;
    
*   a set to train the linear model;
    
*   a set to test the linear model.
    

It is important to split the data in such way to avoid overfitting by leaking data.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=80\_000, random\_state\=10)

X\_full\_train, X\_test, y\_full\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.5, random\_state\=10
)
X\_train\_ensemble, X\_train\_linear, y\_train\_ensemble, y\_train\_linear \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X\_full\_train, y\_full\_train, test\_size\=0.5, random\_state\=10
)

Copy to clipboard

For each of the ensemble methods, we will use 10 estimators and a maximum depth of 3 levels.

n\_estimators \= 10
max\_depth \= 3

Copy to clipboard

First, we will start by training the random forest and gradient boosting on the separated training set

from sklearn.ensemble import [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
, [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

random\_forest \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(
    n\_estimators\=n\_estimators, max\_depth\=max\_depth, random\_state\=10
)
random\_forest.fit(X\_train\_ensemble, y\_train\_ensemble)

gradient\_boosting \= [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
(
    n\_estimators\=n\_estimators, max\_depth\=max\_depth, random\_state\=10
)
\_ \= gradient\_boosting.fit(X\_train\_ensemble, y\_train\_ensemble)

Copy to clipboard

Notice that [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 is much faster than [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 starting with intermediate datasets (`n_samples >= 10_000`), which is not the case of the present example.

The [`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
 is an unsupervised method and thus does not required to be trained independently.

from sklearn.ensemble import [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")

random\_tree\_embedding \= [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
(
    n\_estimators\=n\_estimators, max\_depth\=max\_depth, random\_state\=0
)

Copy to clipboard

Now, we will create three pipelines that will use the above embedding as a preprocessing stage.

The random trees embedding can be directly pipelined with the logistic regression because it is a standard scikit-learn transformer.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

rt\_model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(random\_tree\_embedding, [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(max\_iter\=1000))
rt\_model.fit(X\_train\_linear, y\_train\_linear)

Copy to clipboard

Pipeline(steps=\[('randomtreesembedding',\
                 RandomTreesEmbedding(max\_depth=3, n\_estimators=10,\
                                      random\_state=0)),\
                ('logisticregression', LogisticRegression(max\_iter=1000))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('randomtreesembedding', ...), ('logisticregression', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 20  |

RandomTreesEmbedding

[?Documentation for RandomTreesEmbedding](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>Number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=n_estimators,-int%2C%20default%3D100) | 10  |
|     | [max\_depth max\_depth: int, default=5  <br>  <br>The maximum depth of each tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=max_depth,-int%2C%20default%3D5) | 3   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the generation of the random \`y\` used to fit the trees  <br>and the draw of the splits for each feature at the trees' nodes.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` is the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` is the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>Whether or not to return a sparse CSR matrix, as default behavior,  <br>or to return a dense array compatible with dense pipeline operators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`transform\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [estimator\_ estimator\_: :class:\`~sklearn.tree.ExtraTreeRegressor\` instance  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.ExtraTreeRegressor%20instance) | ExtraTreeRegressor | ExtraTreeRegressor() |
| [estimators\_ estimators\_: list of :class:\`~sklearn.tree.ExtraTreeRegressor\` instances  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=estimators_,-list%20of%20%3Aclass%3A~sklearn.tree.ExtraTreeRegressor%20instances) | list | \[ExtraTreeRegr...ate=209652396), ExtraTreeRegr...ate=398764591), ExtraTreeRegr...ate=924231285), ExtraTreeRegr...te=1478610112), ...\] |
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[ 0,..., dtype=int32), array(\[ 0,..., dtype=int32), array(\[ 0,..., dtype=int32), array(\[ 0,..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The feature importances (the higher, the more important the feature).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](20,) | \[0.03,0.08,0. ,...,0.02,0.01,0.03\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=n_features_in_,-int) | int | 20  |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=n_outputs_,-int) | int | 1   |\
| [one\_hot\_encoder\_ one\_hot\_encoder\_: OneHotEncoder instance  <br>  <br>One-hot encoder used to create the sparse embedding.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#:~:text=one_hot_encoder_,-OneHotEncoder%20instance) | OneHotEncoder | OneHotEncoder() |\
\
75 features\
\
|     |\
| --- |\
| randomtreesembedding\_0\_3 |\
| randomtreesembedding\_0\_4 |\
| randomtreesembedding\_0\_6 |\
| randomtreesembedding\_0\_7 |\
| randomtreesembedding\_0\_10 |\
| randomtreesembedding\_0\_11 |\
| randomtreesembedding\_0\_13 |\
| randomtreesembedding\_0\_14 |\
| randomtreesembedding\_1\_3 |\
| randomtreesembedding\_1\_4 |\
| randomtreesembedding\_1\_6 |\
| randomtreesembedding\_1\_7 |\
| randomtreesembedding\_1\_10 |\
| randomtreesembedding\_1\_11 |\
| randomtreesembedding\_1\_13 |\
| randomtreesembedding\_1\_14 |\
| randomtreesembedding\_2\_3 |\
| randomtreesembedding\_2\_4 |\
| randomtreesembedding\_2\_6 |\
| randomtreesembedding\_2\_7 |\
| randomtreesembedding\_2\_10 |\
| randomtreesembedding\_2\_11 |\
| randomtreesembedding\_2\_13 |\
| randomtreesembedding\_2\_14 |\
| randomtreesembedding\_3\_3 |\
| randomtreesembedding\_3\_4 |\
| randomtreesembedding\_3\_6 |\
| randomtreesembedding\_3\_7 |\
| randomtreesembedding\_3\_10 |\
| randomtreesembedding\_3\_11 |\
| randomtreesembedding\_3\_13 |\
| randomtreesembedding\_3\_14 |\
| randomtreesembedding\_4\_3 |\
| randomtreesembedding\_4\_4 |\
| randomtreesembedding\_4\_6 |\
| randomtreesembedding\_4\_7 |\
| randomtreesembedding\_4\_10 |\
| randomtreesembedding\_4\_11 |\
| randomtreesembedding\_4\_13 |\
| randomtreesembedding\_4\_14 |\
| randomtreesembedding\_5\_3 |\
| randomtreesembedding\_5\_4 |\
| randomtreesembedding\_5\_6 |\
| randomtreesembedding\_5\_7 |\
| randomtreesembedding\_5\_10 |\
| randomtreesembedding\_5\_11 |\
| randomtreesembedding\_5\_12 |\
| randomtreesembedding\_6\_3 |\
| randomtreesembedding\_6\_4 |\
| randomtreesembedding\_6\_6 |\
| randomtreesembedding\_6\_7 |\
| randomtreesembedding\_6\_9 |\
| randomtreesembedding\_6\_11 |\
| randomtreesembedding\_6\_12 |\
| randomtreesembedding\_7\_3 |\
| randomtreesembedding\_7\_4 |\
| randomtreesembedding\_7\_6 |\
| randomtreesembedding\_7\_7 |\
| randomtreesembedding\_7\_10 |\
| randomtreesembedding\_7\_11 |\
| randomtreesembedding\_7\_13 |\
| randomtreesembedding\_7\_14 |\
| randomtreesembedding\_8\_1 |\
| randomtreesembedding\_8\_4 |\
| randomtreesembedding\_8\_5 |\
| randomtreesembedding\_8\_7 |\
| randomtreesembedding\_8\_8 |\
| randomtreesembedding\_9\_3 |\
| randomtreesembedding\_9\_4 |\
| randomtreesembedding\_9\_6 |\
| randomtreesembedding\_9\_7 |\
| randomtreesembedding\_9\_10 |\
| randomtreesembedding\_9\_11 |\
| randomtreesembedding\_9\_13 |\
| randomtreesembedding\_9\_14 |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 1000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](2,) | \[0,1\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 75) | \[\[-1.15,-0.58,-0.9 ,..., 0.32, 0.11, 0.24\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[0.35\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 75  |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[36\] |\
\
  \
  \
\
Then, we can pipeline random forest or gradient boosting with a logistic regression. However, the feature transformation will happen by calling the method `apply`. The pipeline in scikit-learn expects a call to `transform`. Therefore, we wrapped the call to `apply` within a `FunctionTransformer`.\
\
from sklearn.preprocessing import [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
, [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
\
def rf\_apply(X, model):\
    return model.apply(X)\
\
rf\_leaves\_yielder \= [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
(rf\_apply, kw\_args\={"model": random\_forest})\
\
rf\_model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    rf\_leaves\_yielder,\
    [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore"),\
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=1000),\
)\
rf\_model.fit(X\_train\_linear, y\_train\_linear)\
\
Copy to clipboard\
\
Pipeline(steps=\[('functiontransformer',\
                 FunctionTransformer(func=<function rf\_apply at 0x7e1dbc2a5170>,\
                                     kw\_args={'model': RandomForestClassifier(max\_depth=3,\
                                                                              n\_estimators=10,\
                                                                              random\_state=10)})),\
                ('onehotencoder', OneHotEncoder(handle\_unknown='ignore')),\
                ('logisticregression', LogisticRegression(max\_iter=1000))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('functiontransformer', ...), ('onehotencoder', ...), ...\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 20  |\
\
rf\_apply\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function rf\_...x7e1dbc2a5170> |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | {'model': RandomForestC...ndom\_state=10)} |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 20  |\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[ 3, 4..., 11, 13, 14\]), array(\[ 3, 4..., 11, 13, 14\]), array(\[ 3, 4..., 11, 13, 14\]), array(\[ 3, 4..., 11, 13, 14\]), ...\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 10  |\
\
79 features\
\
|     |\
| --- |\
| x0\_3 |\
| x0\_4 |\
| x0\_6 |\
| x0\_7 |\
| x0\_10 |\
| x0\_11 |\
| x0\_13 |\
| x0\_14 |\
| x1\_3 |\
| x1\_4 |\
| x1\_6 |\
| x1\_7 |\
| x1\_10 |\
| x1\_11 |\
| x1\_13 |\
| x1\_14 |\
| x2\_3 |\
| x2\_4 |\
| x2\_6 |\
| x2\_7 |\
| x2\_10 |\
| x2\_11 |\
| x2\_13 |\
| x2\_14 |\
| x3\_3 |\
| x3\_4 |\
| x3\_6 |\
| x3\_7 |\
| x3\_10 |\
| x3\_11 |\
| x3\_13 |\
| x3\_14 |\
| x4\_3 |\
| x4\_4 |\
| x4\_6 |\
| x4\_7 |\
| x4\_10 |\
| x4\_11 |\
| x4\_13 |\
| x4\_14 |\
| x5\_3 |\
| x5\_4 |\
| x5\_6 |\
| x5\_7 |\
| x5\_10 |\
| x5\_11 |\
| x5\_13 |\
| x5\_14 |\
| x6\_3 |\
| x6\_4 |\
| x6\_6 |\
| x6\_7 |\
| x6\_10 |\
| x6\_11 |\
| x6\_13 |\
| x6\_14 |\
| x7\_3 |\
| x7\_4 |\
| x7\_6 |\
| x7\_7 |\
| x7\_10 |\
| x7\_11 |\
| x7\_13 |\
| x7\_14 |\
| x8\_3 |\
| x8\_4 |\
| x8\_6 |\
| x8\_7 |\
| x8\_10 |\
| x8\_11 |\
| x8\_13 |\
| x8\_14 |\
| x9\_3 |\
| x9\_4 |\
| x9\_7 |\
| x9\_10 |\
| x9\_11 |\
| x9\_13 |\
| x9\_14 |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 1000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](2,) | \[0,1\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 79) | \[\[ 0.15,-0.01, 0.59,...,-0.34, 0.7 ,-0.14\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[0.62\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 79  |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[52\] |\
\
  \
  \
\
def gbdt\_apply(X, model):\
    return model.apply(X)\[:, :, 0\]\
\
gbdt\_leaves\_yielder \= [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
(\
    gbdt\_apply, kw\_args\={"model": gradient\_boosting}\
)\
\
gbdt\_model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    gbdt\_leaves\_yielder,\
    [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore"),\
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=1000),\
)\
gbdt\_model.fit(X\_train\_linear, y\_train\_linear)\
\
Copy to clipboard\
\
Pipeline(steps=\[('functiontransformer',\
                 FunctionTransformer(func=<function gbdt\_apply at 0x7e1dbc2a6ae0>,\
                                     kw\_args={'model': GradientBoostingClassifier(n\_estimators=10,\
                                                                                  random\_state=10)})),\
                ('onehotencoder', OneHotEncoder(handle\_unknown='ignore')),\
                ('logisticregression', LogisticRegression(max\_iter=1000))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('functiontransformer', ...), ('onehotencoder', ...), ...\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 20  |\
\
gbdt\_apply\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function gbd...x7e1dbc2a6ae0> |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | {'model': GradientBoost...ndom\_state=10)} |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 20  |\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[ 4., ...1., 13., 14.\]), array(\[ 4., ...1., 13., 14.\]), array(\[ 4., ...1., 13., 14.\]), array(\[ 4., ...1., 13., 14.\]), ...\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 10  |\
\
76 features\
\
|     |\
| --- |\
| x0\_4.0 |\
| x0\_6.0 |\
| x0\_7.0 |\
| x0\_10.0 |\
| x0\_11.0 |\
| x0\_13.0 |\
| x0\_14.0 |\
| x1\_4.0 |\
| x1\_6.0 |\
| x1\_7.0 |\
| x1\_10.0 |\
| x1\_11.0 |\
| x1\_13.0 |\
| x1\_14.0 |\
| x2\_4.0 |\
| x2\_6.0 |\
| x2\_7.0 |\
| x2\_10.0 |\
| x2\_11.0 |\
| x2\_13.0 |\
| x2\_14.0 |\
| x3\_4.0 |\
| x3\_6.0 |\
| x3\_7.0 |\
| x3\_10.0 |\
| x3\_11.0 |\
| x3\_13.0 |\
| x3\_14.0 |\
| x4\_3.0 |\
| x4\_4.0 |\
| x4\_6.0 |\
| x4\_7.0 |\
| x4\_10.0 |\
| x4\_11.0 |\
| x4\_13.0 |\
| x4\_14.0 |\
| x5\_3.0 |\
| x5\_4.0 |\
| x5\_6.0 |\
| x5\_7.0 |\
| x5\_10.0 |\
| x5\_11.0 |\
| x5\_13.0 |\
| x5\_14.0 |\
| x6\_3.0 |\
| x6\_4.0 |\
| x6\_6.0 |\
| x6\_7.0 |\
| x6\_10.0 |\
| x6\_11.0 |\
| x6\_13.0 |\
| x6\_14.0 |\
| x7\_3.0 |\
| x7\_4.0 |\
| x7\_6.0 |\
| x7\_7.0 |\
| x7\_10.0 |\
| x7\_11.0 |\
| x7\_13.0 |\
| x7\_14.0 |\
| x8\_3.0 |\
| x8\_4.0 |\
| x8\_6.0 |\
| x8\_7.0 |\
| x8\_10.0 |\
| x8\_11.0 |\
| x8\_13.0 |\
| x8\_14.0 |\
| x9\_3.0 |\
| x9\_4.0 |\
| x9\_6.0 |\
| x9\_7.0 |\
| x9\_10.0 |\
| x9\_11.0 |\
| x9\_13.0 |\
| x9\_14.0 |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 1000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](2,) | \[0,1\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 76) | \[\[-0.74, 0.11, 0.18,..., 0.55, 1.65,-3.16\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.37\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 76  |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[37\] |\
\
  \
  \
\
We can finally show the different ROC curves for all the models.\
\
import matplotlib.pyplot as plt\
\
from sklearn.metrics import RocCurveDisplay\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
\
models \= \[\
    ("RT embedding -> LR", rt\_model),\
    ("RF", random\_forest),\
    ("RF embedding -> LR", rf\_model),\
    ("GBDT", gradient\_boosting),\
    ("GBDT embedding -> LR", gbdt\_model),\
\]\
\
model\_displays \= {}\
for name, pipeline in models:\
    model\_displays\[name\] \= [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")\
(\
        pipeline, X\_test, y\_test, ax\=ax, name\=name\
    )\
\_ \= ax.set\_title("ROC curve")\
\
Copy to clipboard\
\
![ROC curve](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_001.png)\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
for name, pipeline in models:\
    model\_displays\[name\].plot(ax\=ax)\
\
ax.set\_xlim(0, 0.2)\
ax.set\_ylim(0.8, 1)\
\_ \= ax.set\_title("ROC curve (zoomed in at top left)")\
\
Copy to clipboard\
\
![ROC curve (zoomed in at top left)](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_002.png)\
\
**Total running time of the script:** (0 minutes 2.184 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_feature_transformation.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_feature_transformation.ipynb)\
\
[`Download Jupyter notebook: plot_feature_transformation.ipynb`](https://scikit-learn.org/stable/_downloads/bd48035d82fe0719ccbd66ac2192f65b/plot_feature_transformation.ipynb)\
\
[`Download Python source code: plot_feature_transformation.py`](https://scikit-learn.org/stable/_downloads/3a10dcfbc1a4bf1349c7101a429aa47b/plot_feature_transformation.py)\
\
[`Download zipped: plot_feature_transformation.zip`](https://scikit-learn.org/stable/_downloads/530196dec3cf8d9c844ea06e4cbdd1be/plot_feature_transformation.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)\
\
[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)\
\
Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)\
\
[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)\
\
Decision Tree Regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)\
\
[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)\
\
Comparing Random Forests and Histogram Gradient Boosting models\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)\
\
Release Highlights for scikit-learn 0.22\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
[Download source code](https://scikit-learn.org/stable/_downloads/3a10dcfbc1a4bf1349c7101a429aa47b/plot_feature_transformation.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/bd48035d82fe0719ccbd66ac2192f65b/plot_feature_transformation.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/530196dec3cf8d9c844ea06e4cbdd1be/plot_feature_transformation.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_feature_transformation.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_feature_transformation.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)