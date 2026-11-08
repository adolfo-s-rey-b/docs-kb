[Skip to main content](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/frozen/plot_frozen_examples.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/frozen/plot_frozen_examples.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/frozen/plot_frozen_examples.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/frozen/plot_frozen_examples.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/frozen/plot_frozen_examples.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/frozen/plot_frozen_examples.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#sphx-glr-download-auto-examples-frozen-plot-frozen-examples-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Examples of Using `FrozenEstimator`[#](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#examples-of-using-frozenestimator "Link to this heading")

================================================================================================================================================================================

This example showcases some use cases of [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
.

[`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
 is a utility class that allows to freeze a fitted estimator. This is useful, for instance, when we want to pass a fitted estimator to a meta-estimator, such as [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
 without letting the meta-estimator refit the estimator.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Setting a decision threshold for a pre-fitted classifier[#](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#setting-a-decision-threshold-for-a-pre-fitted-classifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fitted classifiers in scikit-learn use an arbitrary decision threshold to decide which class the given sample belongs to. The decision threshold is either `0.0` on the value returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
, or `0.5` on the probability returned by [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
.

However, one might want to set a custom decision threshold. We can do this by using [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
 and wrapping the classifier with [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.frozen import [FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
, [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=1000, random\_state\=0)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)
classifier \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
().fit(X\_train, y\_train)

print(
    "Probability estimates for three data points:\\n"
    f"{classifier.predict\_proba(X\_test\[\-3:\]).round(3)}"
)
print(
    "Predicted class for the same three data points:\\n"
    f"{classifier.predict(X\_test\[\-3:\])}"
)

Copy to clipboard

Probability estimates for three data points:
\[\[0.18 0.82\]\
 \[0.29 0.71\]\
 \[0.   1.  \]\]
Predicted class for the same three data points:
\[1 1 1\]

Copy to clipboard

Now imagine you’d want to set a different decision threshold on the probability estimates. We can do this by wrapping the classifier with [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
 and passing it to [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
.

threshold\_classifier \= [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
(
    estimator\=[FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
(classifier), threshold\=0.9
)

Copy to clipboard

Note that in the above piece of code, calling `fit` on [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
 does not refit the underlying classifier.

Now, let’s see how the predictions changed with respect to the probability threshold.

print(
    "Probability estimates for three data points with FixedThresholdClassifier:\\n"
    f"{threshold\_classifier.predict\_proba(X\_test\[\-3:\]).round(3)}"
)
print(
    "Predicted class for the same three data points with FixedThresholdClassifier:\\n"
    f"{threshold\_classifier.predict(X\_test\[\-3:\])}"
)

Copy to clipboard

Probability estimates for three data points with FixedThresholdClassifier:
\[\[0.18 0.82\]\
 \[0.29 0.71\]\
 \[0.   1.  \]\]
Predicted class for the same three data points with FixedThresholdClassifier:
\[0 0 1\]

Copy to clipboard

We see that the probability estimates stay the same, but since a different decision threshold is used, the predicted classes are different.

Please refer to [Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#sphx-glr-auto-examples-model-selection-plot-cost-sensitive-learning-py)
 to learn about cost-sensitive learning and decision threshold tuning.

Calibration of a pre-fitted classifier[#](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html#calibration-of-a-pre-fitted-classifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
 to calibrate a pre-fitted classifier using [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
.

from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
from sklearn.metrics import [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")

calibrated\_classifier \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(
    estimator\=[FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
(classifier)
).fit(X\_train, y\_train)

prob\_pos\_clf \= classifier.predict\_proba(X\_test)\[:, 1\]
clf\_score \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
(y\_test, prob\_pos\_clf)
print(f"No calibration: {clf\_score:.3f}")

prob\_pos\_calibrated \= calibrated\_classifier.predict\_proba(X\_test)\[:, 1\]
calibrated\_score \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
(y\_test, prob\_pos\_calibrated)
print(f"With calibration: {calibrated\_score:.3f}")

Copy to clipboard

No calibration: 0.033
With calibration: 0.032

Copy to clipboard

**Total running time of the script:** (0 minutes 0.020 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo14.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/frozen/plot_frozen_examples.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo14.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/frozen/plot_frozen_examples.ipynb)

[`Download Jupyter notebook: plot_frozen_examples.ipynb`](https://scikit-learn.org/stable/_downloads/f1268276b88d7501262b137a5c139a16/plot_frozen_examples.ipynb)

[`Download Python source code: plot_frozen_examples.py`](https://scikit-learn.org/stable/_downloads/46bf843d1ac1595b6026da7280f10e7c/plot_frozen_examples.py)

[`Download zipped: plot_frozen_examples.zip`](https://scikit-learn.org/stable/_downloads/8c6c0b05c72467c8a5dd82b81fce1ce3/plot_frozen_examples.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/46bf843d1ac1595b6026da7280f10e7c/plot_frozen_examples.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f1268276b88d7501262b137a5c139a16/plot_frozen_examples.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8c6c0b05c72467c8a5dd82b81fce1ce3/plot_frozen_examples.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo14.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/frozen/plot_frozen_examples.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo14.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/frozen/plot_frozen_examples.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)