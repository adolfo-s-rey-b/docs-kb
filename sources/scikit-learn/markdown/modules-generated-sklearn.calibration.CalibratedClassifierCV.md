[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)

Collapse Sidebar Expand Sidebar

CalibratedClassifierCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#calibratedclassifiercv "Link to this heading")

===========================================================================================================================================================================

class sklearn.calibration.CalibratedClassifierCV(_estimator\=None_, _\*_, _method\='sigmoid'_, _cv\=None_, _n\_jobs\=None_, _ensemble\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L74)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "Link to this definition")

Calibrate probabilities using isotonic, sigmoid, or temperature scaling.

This class uses cross-validation to both estimate the parameters of a classifier and subsequently calibrate a classifier. With `ensemble=True`, for each cv split it fits a copy of the base estimator to the training subset, and calibrates it using the testing subset. For prediction, predicted probabilities are averaged across these individual calibrated classifiers. When `ensemble=False`, cross-validation is used to obtain unbiased predictions, via [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
, which are then used for calibration. For prediction, the base estimator, trained using all the data, is used. This is the prediction method implemented when `probabilities=True` for [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 estimators (see [User Guide](https://scikit-learn.org/stable/modules/svm.html#scores-probabilities)
 for details).

Already fitted classifiers can be calibrated by wrapping the model in a [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
. In this case all provided data is used for calibration. The user has to take care manually that data for model fitting and calibration are disjoint.

The calibration is based on the [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 method of the `estimator` if it exists, else on [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
. In order to learn more on the CalibratedClassifierCV class, see the following calibration examples: [Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#sphx-glr-auto-examples-calibration-plot-calibration-py)
, [Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#sphx-glr-auto-examples-calibration-plot-calibration-curve-py)
, and [Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#sphx-glr-auto-examples-calibration-plot-calibration-multiclass-py)
.

Parameters:

**estimator**estimator instance, default=None

The classifier whose output need to be calibrated to provide more accurate `predict_proba` outputs. The default classifier is a [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
.

Added in version 1.2.

**method**{‘sigmoid’, ‘isotonic’, ‘temperature’}, default=’sigmoid’

The method to use for calibration. Can be:

*   ‘sigmoid’, which corresponds to Platt’s method (i.e. a binary logistic regression model).
    
*   ‘isotonic’, which is a non-parametric approach.
    
*   ‘temperature’, temperature scaling.
    

Sigmoid and isotonic calibration methods natively support only binary classifiers and extend to multi-class classification using a One-vs-Rest (OvR) strategy with post-hoc renormalization, i.e., adjusting the probabilities after calibration to ensure they sum up to 1.

In contrast, temperature scaling naturally supports multi-class calibration by applying `softmax(classifier_logits/T)` with a value of `T` (temperature) that optimizes the log loss.

For very uncalibrated classifiers on very imbalanced datasets, sigmoid calibration might be preferred because it fits an additional intercept parameter. This helps shift decision boundaries appropriately when the classifier being calibrated is biased towards the majority class.

Isotonic calibration is not recommended when the number of calibration samples is too low `(≪1000)` since it then tends to overfit.

Changed in version 1.8: Added option ‘temperature’.

**cv**int, cross-validation generator, or iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross-validation,
    
*   integer, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if `y` is binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. If `y` is neither binary nor multiclass, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer to the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**n\_jobs**int, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors.

Base estimator clones are fitted in parallel across cross-validation iterations.

See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 0.24.

**ensemble**bool, or “auto”, default=”auto”

Determines how the calibrator is fitted.

“auto” will use `False` if the `estimator` is a [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
, and `True` otherwise.

If `True`, the `estimator` is fitted using training data, and calibrated using testing data, for each `cv` fold. The final estimator is an ensemble of `n_cv` fitted classifier and calibrator pairs, where `n_cv` is the number of cross-validation folds. The output is the average predicted probabilities of all pairs.

If `False`, `cv` is used to compute unbiased predictions, via [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
, which are then used for calibration. At prediction time, the classifier used is the `estimator` trained on all the data. Note that this method is also internally implemented in [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
 estimators with the `probabilities=True` parameter.

Added in version 0.24.

Changed in version 1.6: `"auto"` option is added and is the default.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

The class labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 1.0.

**calibrated\_classifiers\_**list (len() equal to cv or 1 if `ensemble=False`)

The list of classifier and calibrator pairs.

*   When `ensemble=True`, `n_cv` fitted `estimator` and calibrator pairs. `n_cv` is the number of cross-validation folds.
    
*   When `ensemble=False`, the `estimator`, fitted on all the data, and fitted calibrator.
    

Changed in version 0.24: Single calibrated classifier case when `ensemble=False`.

See also

[`calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")

Compute true and predicted probabilities for a calibration curve.

References

\[1\]

B. Zadrozny & C. Elkan. [Obtaining calibrated probability estimates from decision trees and naive Bayesian classifiers](https://cseweb.ucsd.edu/~elkan/calibrated.pdf)
, ICML 2001.

\[2\]

B. Zadrozny & C. Elkan. [Transforming Classifier Scores into Accurate Multiclass Probability Estimates](https://web.archive.org/web/20060720141520id_/http://www.research.ibm.com:80/people/z/zadrozny/kdd2002-Transf.pdf)
, KDD 2002.

\[3\]

J. Platt. [Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods](https://www.researchgate.net/profile/John-Platt-2/publication/2594015_Probabilistic_Outputs_for_Support_Vector_Machines_and_Comparisons_to_Regularized_Likelihood_Methods/links/004635154cff5262d6000000/Probabilistic-Outputs-for-Support-Vector-Machines-and-Comparisons-to-Regularized-Likelihood-Methods.pdf)
, 1999.

\[4\]

A. Niculescu-Mizil & R. Caruana. [Predicting Good Probabilities with Supervised Learning](https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf)
, ICML 2005.

\[5\]

Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger. [On Calibration of Modern Neural Networks](https://doi.org/10.48550/arXiv.1706.04599)
. Proceedings of the 34th International Conference on Machine Learning, PMLR 70:1321-1330, 2017.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.naive\_bayes import GaussianNB
\>>> from sklearn.calibration import CalibratedClassifierCV
\>>> X, y \= make\_classification(n\_samples\=100, n\_features\=2,
...                            n\_redundant\=0, random\_state\=42)
\>>> base\_clf \= GaussianNB()
\>>> calibrated\_clf \= CalibratedClassifierCV(base\_clf, cv\=3)
\>>> calibrated\_clf.fit(X, y)
CalibratedClassifierCV(...)
\>>> len(calibrated\_clf.calibrated\_classifiers\_)
3
\>>> calibrated\_clf.predict\_proba(X)\[:5, :\]
array(\[\[0.110, 0.889\],\
       \[0.072, 0.927\],\
       \[0.928, 0.072\],\
       \[0.928, 0.072\],\
       \[0.072, 0.928\]\])
\>>> from sklearn.model\_selection import train\_test\_split
\>>> X, y \= make\_classification(n\_samples\=100, n\_features\=2,
...                            n\_redundant\=0, random\_state\=42)
\>>> X\_train, X\_calib, y\_train, y\_calib \= train\_test\_split(
...        X, y, random\_state\=42
... )
\>>> base\_clf \= GaussianNB()
\>>> base\_clf.fit(X\_train, y\_train)
GaussianNB()
\>>> from sklearn.frozen import FrozenEstimator
\>>> calibrated\_clf \= CalibratedClassifierCV(FrozenEstimator(base\_clf))
\>>> calibrated\_clf.fit(X\_calib, y\_calib)
CalibratedClassifierCV(...)
\>>> len(calibrated\_clf.calibrated\_classifiers\_)
1
\>>> calibrated\_clf.predict\_proba(\[\[\-0.5, 0.5\]\])
array(\[\[0.936, 0.063\]\])

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L337)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.fit "Link to this definition")

Fit the calibrated model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If None, then samples are equally weighted.

**\*\*fit\_params**dict

Parameters to pass to the `fit` method of the underlying classifier.

Returns:

**self**object

Returns an instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L564)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L540)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.predict "Link to this definition")

Predict the target of new samples.

The predicted class is the class that has the highest probability, and can thus be different from the prediction of the uncalibrated classifier.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The samples, as accepted by `estimator.predict`.

Returns:

**C**ndarray of shape (n\_samples,)

The predicted class.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L511)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.predict_proba "Link to this definition")

Calibrated probabilities of classification.

This function returns calibrated probabilities of classification according to each class on an array of test vectors X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The samples, as accepted by `estimator.predict_proba`.

Returns:

**C**ndarray of shape (n\_samples, n\_classes)

The predicted probas.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)