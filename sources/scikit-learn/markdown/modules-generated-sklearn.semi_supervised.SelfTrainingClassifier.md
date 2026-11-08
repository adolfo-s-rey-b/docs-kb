[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)

Collapse Sidebar Expand Sidebar

SelfTrainingClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#selftrainingclassifier "Link to this heading")

===============================================================================================================================================================================

class sklearn.semi\_supervised.SelfTrainingClassifier(_estimator\=None_, _threshold\=0.75_, _criterion\='threshold'_, _k\_best\=10_, _max\_iter\=10_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L32)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "Link to this definition")

Self-training classifier.

This [metaestimator](https://scikit-learn.org/stable/glossary.html#term-metaestimator)
 allows a given supervised classifier to function as a semi-supervised classifier, allowing it to learn from unlabeled data. It does this by iteratively predicting pseudo-labels for the unlabeled data and adding them to the training set.

The classifier will continue iterating until either max\_iter is reached, or no pseudo-labels were added to the training set in the previous iteration.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/semi_supervised.html#self-training)
.

Parameters:

**estimator**estimator object

An estimator object implementing `fit` and `predict_proba`. Invoking the `fit` method will fit a clone of the passed estimator, which will be stored in the `estimator_` attribute.

Added in version 1.6: `estimator` was added to replace `base_estimator`.

**threshold**float, default=0.75

The decision threshold for use with `criterion='threshold'`. Should be in \[0, 1). When using the `'threshold'` criterion, a [well calibrated classifier](https://scikit-learn.org/stable/modules/calibration.html#calibration)\
 should be used.\
\
**criterion**{‘threshold’, ‘k\_best’}, default=’threshold’\
\
The selection criterion used to select which labels to add to the training set. If `'threshold'`, pseudo-labels with prediction probabilities above `threshold` are added to the dataset. If `'k_best'`, the `k_best` pseudo-labels with highest prediction probabilities are added to the dataset. When using the ‘threshold’ criterion, a [well calibrated classifier](https://scikit-learn.org/stable/modules/calibration.html#calibration)\
 should be used.\
\
**k\_best**int, default=10\
\
The amount of samples to add in each iteration. Only used when `criterion='k_best'`.\
\
**max\_iter**int or None, default=10\
\
Maximum number of iterations allowed. Should be greater than or equal to 0. If it is `None`, the classifier will continue to predict labels until no new pseudo-labels are added, or all unlabeled samples have been labeled.\
\
**verbose**bool, default=False\
\
Enable verbose output.\
\
Attributes:\
\
**estimator\_**estimator object\
\
The fitted estimator.\
\
**classes\_**ndarray or list of ndarray of shape (n\_classes,)\
\
Class labels for each output. (Taken from the trained `estimator_`).\
\
**transduction\_**ndarray of shape (n\_samples,)\
\
The labels used for the final fit of the classifier, including pseudo-labels added during fit.\
\
**labeled\_iter\_**ndarray of shape (n\_samples,)\
\
The iteration in which each sample was labeled. When a sample has iteration 0, the sample was already labeled in the original dataset. When a sample has iteration -1, the sample was not labeled in any iteration.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
**n\_iter\_**int\
\
The number of rounds of self-training, that is the number of times the base estimator is fitted on relabeled variants of the training set.\
\
**termination\_condition\_**{‘max\_iter’, ‘no\_change’, ‘all\_labeled’}\
\
The reason that fitting was stopped.\
\
*   `'max_iter'`: `n_iter_` reached `max_iter`.\
    \
*   `'no_change'`: no new labels were predicted.\
    \
*   `'all_labeled'`: all unlabeled samples were labeled before `max_iter` was reached.\
    \
\
See also\
\
[`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")\
\
Label propagation classifier.\
\
[`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")\
\
Label spreading model for semi-supervised learning.\
\
References\
\
[David Yarowsky. 1995. Unsupervised word sense disambiguation rivaling supervised methods. In Proceedings of the 33rd annual meeting on Association for Computational Linguistics (ACL ‘95). Association for Computational Linguistics, Stroudsburg, PA, USA, 189-196.](https://doi.org/10.3115/981658.981684)\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn import datasets\
\>>> from sklearn.semi\_supervised import SelfTrainingClassifier\
\>>> from sklearn.linear\_model import LogisticRegression\
\>>> rng \= np.random.RandomState(42)\
\>>> iris \= datasets.load\_iris()\
\>>> random\_unlabeled\_points \= rng.rand(iris.target.shape\[0\]) < 0.3\
\>>> iris.target\[random\_unlabeled\_points\] \= \-1\
\>>> clf \= LogisticRegression()\
\>>> self\_training\_model \= SelfTrainingClassifier(clf)\
\>>> self\_training\_model.fit(iris.data, iris.target)\
SelfTrainingClassifier(...)\
\
Copy to clipboard\
\
decision\_function(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L413)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.decision_function "Link to this definition")\
\
Call decision function of the `estimator`.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**\*\*params**dict of str -> object\
\
Parameters to pass to the underlying estimator’s `decision_function` method.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**y**ndarray of shape (n\_samples, n\_features)\
\
Result of the decision function of the `estimator`.\
\
fit(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L189)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.fit "Link to this definition")\
\
Fit self-training classifier using `X`, `y` as training data.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**y**{array-like, sparse matrix} of shape (n\_samples,)\
\
Array representing the labels. Unlabeled samples should have the label -1.\
\
**\*\*params**dict\
\
Parameters to pass to the underlying estimators.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**self**object\
\
Fitted estimator.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L548)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Added in version 1.6.\
\
Returns:\
\
**routing**MetadataRouter\
\
A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
predict(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L328)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict "Link to this definition")\
\
Predict the classes of `X`.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**\*\*params**dict of str -> object\
\
Parameters to pass to the underlying estimator’s `predict` method.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**y**ndarray of shape (n\_samples,)\
\
Array with predicted labels.\
\
predict\_log\_proba(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L458)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict_log_proba "Link to this definition")\
\
Predict log probability for each possible outcome.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**\*\*params**dict of str -> object\
\
Parameters to pass to the underlying estimator’s `predict_log_proba` method.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**y**ndarray of shape (n\_samples, n\_features)\
\
Array with log prediction probabilities.\
\
predict\_proba(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L370)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict_proba "Link to this definition")\
\
Predict probability for each possible outcome.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**\*\*params**dict of str -> object\
\
Parameters to pass to the underlying estimator’s `predict_proba` method.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**y**ndarray of shape (n\_samples, n\_features)\
\
Array with prediction probabilities.\
\
score(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_self_training.py#L503)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.score "Link to this definition")\
\
Call score on the `estimator`.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Array representing the data.\
\
**y**array-like of shape (n\_samples,)\
\
Array representing the labels.\
\
**\*\*params**dict of str -> object\
\
Parameters to pass to the underlying estimator’s `score` method.\
\
Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 for more details.\
\
Returns:\
\
**score**float\
\
Result of calling score on the `estimator`.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#gallery-examples "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)\
\
Release Highlights for scikit-learn 0.24\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)\
\
[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)\
\
Effect of varying threshold for self-training\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)\
\
[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)\
\
Semi-supervised Classification on a Text Dataset\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)\
\
[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)\
\
Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)