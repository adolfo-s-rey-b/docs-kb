[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.svm.LinearSVC.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.svm.LinearSVC.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.LinearSVC.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.svm.LinearSVC.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.svm.LinearSVC.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.svm.LinearSVC.html)

Collapse Sidebar Expand Sidebar

LinearSVC[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#linearsvc "Link to this heading")

============================================================================================================================

class sklearn.svm.LinearSVC(_penalty\='l2'_, _loss\='squared\_hinge'_, _\*_, _dual\='auto'_, _tol\=0.0001_, _C\=1.0_, _multi\_class\='ovr'_, _fit\_intercept\=True_, _intercept\_scaling\=1_, _class\_weight\=None_, _verbose\=0_, _random\_state\=None_, _max\_iter\=1000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L44)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "Link to this definition")

Linear Support Vector Classification.

Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.

The main differences between [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 and [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 lie in the loss function used by default, and in the handling of intercept regularization between those two implementations.

This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
.

Parameters:

**penalty**{‘l1’, ‘l2’}, default=’l2’

Specifies the norm used in the penalization. The ‘l2’ penalty is the standard used in SVC. The ‘l1’ leads to `coef_` vectors that are sparse.

**loss**{‘hinge’, ‘squared\_hinge’}, default=’squared\_hinge’

Specifies the loss function. ‘hinge’ is the standard SVM loss (used e.g. by the SVC class) while ‘squared\_hinge’ is the square of the hinge loss. The combination of `penalty='l1'` and `loss='hinge'` is not supported.

**dual**“auto” or bool, default=”auto”

Select the algorithm to either solve the dual or primal optimization problem. Prefer dual=False when n\_samples > n\_features. `dual="auto"` will choose the value of the parameter automatically, based on the values of `n_samples`, `n_features`, `loss`, `multi_class` and `penalty`. If `n_samples` < `n_features` and optimizer supports chosen `loss`, `multi_class` and `penalty`, then dual will be set to True, otherwise it will be set to False.

Changed in version 1.3: The `"auto"` option is added in version 1.3 and will be the default in version 1.5.

**tol**float, default=1e-4

Tolerance for stopping criteria.

**C**float, default=1.0

Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive. For an intuitive visualization of the effects of scaling the regularization parameter C, see [Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#sphx-glr-auto-examples-svm-plot-svm-scale-c-py)
.

**multi\_class**{‘ovr’, ‘crammer\_singer’}, default=’ovr’

Determines the multi-class strategy if `y` contains more than two classes. `"ovr"` trains n\_classes one-vs-rest classifiers, while `"crammer_singer"` optimizes a joint objective over all classes. While `crammer_singer` is interesting from a theoretical perspective as it is consistent, it is seldom used in practice as it rarely leads to better accuracy and is more expensive to compute. If `"crammer_singer"` is chosen, the options loss, penalty and dual will be ignored.

**fit\_intercept**bool, default=True

Whether or not to fit an intercept. If set to True, the feature vector is extended to include an intercept term: `[x_1, ..., x_n, 1]`, where 1 corresponds to the intercept. If set to False, no intercept will be used in calculations (i.e. data is expected to be already centered).

**intercept\_scaling**float, default=1.0

When `fit_intercept` is True, the instance vector x becomes `[x_1, ..., x_n, intercept_scaling]`, i.e. a “synthetic” feature with a constant value equal to `intercept_scaling` is appended to the instance vector. The intercept becomes intercept\_scaling \* synthetic feature weight. Note that liblinear internally penalizes the intercept, treating it like any other term in the feature vector. To reduce the impact of the regularization on the intercept, the `intercept_scaling` parameter can be set to a value greater than 1; the higher the value of `intercept_scaling`, the lower the impact of regularization on it. Then, the weights become `[w_x_1, ..., w_x_n, w_intercept*intercept_scaling]`, where `w_x_1, ..., w_x_n` represent the feature weights and the intercept weight is scaled by `intercept_scaling`. This scaling allows the intercept term to have a different regularization behavior compared to the other features.

**class\_weight**dict or ‘balanced’, default=None

Set the parameter C of class i to `class_weight[i]*C` for SVC. If not given, all classes are supposed to have weight one. The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as `n_samples / (n_classes * np.bincount(y))`.

**verbose**int, default=0

Enable verbose output. Note that this setting takes advantage of a per-process runtime setting in liblinear that, if enabled, may not work properly in a multithreaded context.

**random\_state**int, RandomState instance or None, default=None

Controls the pseudo random number generation for shuffling the data for the dual coordinate descent (if `dual=True`). When `dual=False` the underlying implementation of [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 is not random and `random_state` has no effect on the results. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**max\_iter**int, default=1000

The maximum number of iterations to be run.

Attributes:

**coef\_**ndarray of shape (1, n\_features) if n\_classes == 2 else (n\_classes, n\_features)

Weights assigned to the features (coefficients in the primal problem).

`coef_` is a readonly property derived from `raw_coef_` that follows the internal memory layout of liblinear.

**intercept\_**ndarray of shape (1,) if n\_classes == 2 else (n\_classes,)

Constants in decision function.

**classes\_**ndarray of shape (n\_classes,)

The unique classes labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

Maximum number of iterations run across all classes.

See also

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

Implementation of Support Vector Machine classifier using libsvm: the kernel can be non-linear but its SMO algorithm does not scale to large number of samples as LinearSVC does. Furthermore SVC multi-class mode is implemented using one vs one scheme while LinearSVC uses one vs the rest. It is possible to implement one vs the rest with SVC by using the [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 wrapper. Finally SVC can fit dense data without memory copy if the input is C-contiguous. Sparse data will still incur memory copy though.

[`sklearn.linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

SGDClassifier can optimize the same cost function as LinearSVC by adjusting the penalty and loss parameters. In addition it requires less memory, allows incremental (online) learning, and implements various loss functions and regularization regimes.

Notes

The underlying C implementation uses a random number generator to select features when fitting the model. It is thus not uncommon to have slightly different results for the same input data. If that happens, try with a smaller `tol` parameter.

The underlying implementation, liblinear, uses a sparse internal representation for the data that will incur a memory copy.

Predict output may not match that of standalone liblinear in certain cases. See [differences from liblinear](https://scikit-learn.org/stable/modules/linear_model.html#liblinear-differences)
 in the narrative documentation.

References

[LIBLINEAR: A Library for Large Linear Classification](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)

Examples

\>>> from sklearn.svm import LinearSVC
\>>> from sklearn.pipeline import make\_pipeline
\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.datasets import make\_classification
\>>> X, y \= make\_classification(n\_features\=4, random\_state\=0)
\>>> clf \= make\_pipeline(StandardScaler(),
...                     LinearSVC(random\_state\=0, tol\=1e-5))
\>>> clf.fit(X, y)
Pipeline(steps=\[('standardscaler', StandardScaler()),\
                ('linearsvc', LinearSVC(random\_state=0, tol=1e-05))\])

Copy to clipboard

\>>> print(clf.named\_steps\['linearsvc'\].coef\_)
\[\[0.141   0.526 0.679 0.493\]\]

Copy to clipboard

\>>> print(clf.named\_steps\['linearsvc'\].intercept\_)
\[0.1693\]
\>>> print(clf.predict(\[\[0, 0, 0, 0\]\]))
\[1\]

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L366)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.decision_function "Link to this definition")

Predict confidence scores for samples.

The confidence score for a sample is proportional to the signed distance of that sample to the hyperplane.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the confidence scores.

Returns:

**scores**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Confidence scores per `(n_samples, n_classes)` combination. In the binary case, confidence score for `self.classes_[1]` where >0 means this class would be predicted.

densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.densify "Link to this definition")

Convert coefficient matrix to dense array format.

Converts the `coef_` member (back) to a numpy.ndarray. This is the default format of `coef_` and is required for fitting, so calling this method is only required on models that have previously been sparsified; otherwise, it is a no-op.

Returns:

self

Fitted estimator.

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L289)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.fit "Link to this definition")

Fit the model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target vector relative to X.

**sample\_weight**array-like of shape (n\_samples,), default=None

Array of weights that are assigned to individual samples. If not provided, then each sample is given unit weight.

Added in version 0.18.

Returns:

**self**object

An instance of the estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L398)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.predict "Link to this definition")

Predict class labels for samples in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the predictions.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

Vector containing the class labels for each sample.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.score "Link to this definition")

Return [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
 on provided data and labels.

In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True labels for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

Mean accuracy of `self.predict(X)` w.r.t. `y`.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm._classes.LinearSVC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm._classes.LinearSVC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.set_score_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `score` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `score`.

Returns:

**self**object

The updated object.

sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.sparsify "Link to this definition")

Convert coefficient matrix to sparse format.

Converts the `coef_` member to a scipy.sparse matrix, which for L1-regularized models can be much more memory- and storage-efficient than the usual numpy.ndarray representation.

The `intercept_` member is not converted.

Warning

This method is not supported for estimators fitted with array API inputs (i.e. when [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.predict "sklearn.svm.LinearSVC.predict")
 and other methods involving passing arrays may raise or return unexpected results.

Returns:

self

Fitted estimator.

Notes

For non-sparse models, i.e. when there are not many zeros in `coef_`, this may actually _increase_ memory usage, so use this method with care. A rule of thumb is that the number of zero elements, which can be computed with `(coef_ == 0).sum()`, must be more than 50% for this to provide significant benefits.

After calling this method, further fitting with the partial\_fit method (if any) will not work until you call densify.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)

[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)

Scalable learning with polynomial kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_thumb.png)

[Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)

Explicit feature map approximation for RBF kernels

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_thumb.png)

[Plot the support vectors in LinearSVC](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)

Plot the support vectors in LinearSVC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)