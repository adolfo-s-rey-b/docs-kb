[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-5-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.5[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#release-highlights-for-scikit-learn-1-5 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.5! Many bug fixes and improvements were added, as well as some key new features. Below we detail the highlights of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.5.html#release-notes-1-5)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

FixedThresholdClassifier: Setting the decision threshold of a binary classifier[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#fixedthresholdclassifier-setting-the-decision-threshold-of-a-binary-classifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All binary classifiers of scikit-learn use a fixed decision threshold of 0.5 to convert probability estimates (i.e. output of `predict_proba`) into class predictions. However, 0.5 is almost never the desired threshold for a given problem. [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
 allows wrapping any binary classifier and setting a custom decision threshold.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=10\_000, weights\=\[0.9, 0.1\], random\_state\=0)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

classifier\_05 \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=1e6, random\_state\=0).fit(X\_train, y\_train)
\_ \= [ConfusionMatrixDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
(classifier\_05, X\_test, y\_test)

Copy to clipboard

![plot release highlights 1 5 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_001.png)

Lowering the threshold, i.e. allowing more samples to be classified as the positive class, increases the number of true positives at the cost of more false positives (as is well known from the concavity of the ROC curve).

from sklearn.model\_selection import [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")

classifier\_01 \= [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
(classifier\_05, threshold\=0.1)
classifier\_01.fit(X\_train, y\_train)
\_ \= [ConfusionMatrixDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
(classifier\_01, X\_test, y\_test)

Copy to clipboard

![plot release highlights 1 5 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_002.png)

TunedThresholdClassifierCV: Tuning the decision threshold of a binary classifier[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#tunedthresholdclassifiercv-tuning-the-decision-threshold-of-a-binary-classifier "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The decision threshold of a binary classifier can be tuned to optimize a given metric, using [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
.

It is particularly useful to find the best decision threshold when the model is meant to be deployed in a specific application context where we can assign different gains or costs for true positives, true negatives, false positives, and false negatives.

Let’s illustrate this by considering an arbitrary case where:

*   each true positive gains 1 unit of profit, e.g. euro, year of life in good health, etc.;
    
*   true negatives gain or cost nothing;
    
*   each false negative costs 2;
    
*   each false positive costs 0.1.
    

Our metric quantifies the average profit per sample, which is defined by the following Python function:

from sklearn.metrics import [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

def custom\_score(y\_observed, y\_pred):
    tn, fp, fn, tp \= [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
(y\_observed, y\_pred, normalize\="all").ravel()
    return tp \- 2 \* fn \- 0.1 \* fp

print("Untuned decision threshold: 0.5")
print(f"Custom score: {custom\_score(y\_test, classifier\_05.predict(X\_test)):.2f}")

Copy to clipboard

Untuned decision threshold: 0.5
Custom score: -0.12

Copy to clipboard

It is interesting to observe that the average gain per prediction is negative which means that this decision system is making a loss on average.

Tuning the threshold to optimize this custom metric gives a smaller threshold that allows more samples to be classified as the positive class. As a result, the average gain per prediction improves.

from sklearn.metrics import [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
from sklearn.model\_selection import [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")

custom\_scorer \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(
    custom\_score, response\_method\="predict", greater\_is\_better\=True
)
tuned\_classifier \= [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
(
    classifier\_05, cv\=5, scoring\=custom\_scorer
).fit(X, y)

print(f"Tuned decision threshold: {tuned\_classifier.best\_threshold\_:.3f}")
print(f"Custom score: {custom\_score(y\_test, tuned\_classifier.predict(X\_test)):.2f}")

Copy to clipboard

Tuned decision threshold: 0.071
Custom score: 0.04

Copy to clipboard

We observe that tuning the decision threshold can turn a machine learning-based system that makes a loss on average into a beneficial one.

In practice, defining a meaningful application-specific metric might involve making those costs for bad predictions and gains for good predictions depend on auxiliary metadata specific to each individual data point such as the amount of a transaction in a fraud detection system.

To achieve this, [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 leverages metadata routing support ([Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
) allowing to optimize complex business metrics as detailed in [Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#sphx-glr-auto-examples-model-selection-plot-cost-sensitive-learning-py)
.

Performance improvements in PCA[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#performance-improvements-in-pca "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 has a new solver, `"covariance_eigh"`, which is up to an order of magnitude faster and more memory efficient than the other solvers for datasets with many data points and few features.

from sklearn.datasets import [make\_low\_rank\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

X \= [make\_low\_rank\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")
(
    n\_samples\=10\_000, n\_features\=100, tail\_strength\=0.1, random\_state\=0
)

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=10, svd\_solver\="covariance\_eigh").fit(X)
print(f"Explained variance: {pca.explained\_variance\_ratio\_.sum():.2f}")

Copy to clipboard

Explained variance: 0.88

Copy to clipboard

The new solver also accepts sparse input data:

from scipy.sparse import [random](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.random.html#scipy.sparse.random "scipy.sparse.random")

X \= [random](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.random.html#scipy.sparse.random "scipy.sparse.random")
(10\_000, 100, format\="csr", random\_state\=0)

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=10, svd\_solver\="covariance\_eigh").fit(X)
print(f"Explained variance: {pca.explained\_variance\_ratio\_.sum():.2f}")

Copy to clipboard

Explained variance: 0.13

Copy to clipboard

The `"full"` solver has also been improved to use less memory and allows faster transformation. The default `svd_solver="auto"` option takes advantage of the new solver and is now able to select an appropriate solver for sparse datasets.

Similarly to most other PCA solvers, the new `"covariance_eigh"` solver can leverage GPU computation if the input data is passed as a PyTorch or CuPy array by enabling the experimental support for [Array API](https://scikit-learn.org/stable/modules/array_api.html#array-api)
.

ColumnTransformer is subscriptable[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#columntransformer-is-subscriptable "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The transformers of a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 can now be directly accessed using indexing by name.

import numpy as np

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0, 1, 2\], \[3, 4, 5\]\])
column\_transformer \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[("std\_scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), \[0\]), ("one\_hot", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(), \[1, 2\])\]
)

column\_transformer.fit(X)

print(column\_transformer\["std\_scaler"\])
print(column\_transformer\["one\_hot"\])

Copy to clipboard

StandardScaler()
OneHotEncoder()

Copy to clipboard

Custom imputation strategies for the SimpleImputer[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#custom-imputation-strategies-for-the-simpleimputer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 now supports custom strategies for imputation, using a callable that computes a scalar value from the non missing values of a column vector.

from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\
        \[\-1.1, 1.1, 1.1\],\
        \[3.9, \-1.2, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\],\
        \[[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
, 1.3, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\],\
        \[\-0.1, \-1.4, \-1.4\],\
        \[\-4.9, 1.5, \-1.5\],\
        \[[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
, 1.6, 1.6\],\
    \]
)

def smallest\_abs(arr):
    """Return the smallest absolute value of a 1D array."""
    return [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(np.abs(arr))

imputer \= [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\=smallest\_abs)

imputer.fit\_transform(X)

Copy to clipboard

array(\[\[-1.1,  1.1,  1.1\],\
       \[ 3.9, -1.2,  1.1\],\
       \[ 0.1,  1.3,  1.1\],\
       \[-0.1, -1.4, -1.4\],\
       \[-4.9,  1.5, -1.5\],\
       \[ 0.1,  1.6,  1.6\]\])

Copy to clipboard

Pairwise distances with non-numeric arrays[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#pairwise-distances-with-non-numeric-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
 can now compute distances between non-numeric arrays using a callable metric.

from sklearn.metrics import [pairwise\_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")

X \= \["cat", "dog"\]
Y \= \["cat", "fox"\]

def levenshtein\_distance(x, y):
    """Return the Levenshtein distance between two strings."""
    if x \== "" or y \== "":
        return max(len(x), len(y))
    if x\[0\] \== y\[0\]:
        return levenshtein\_distance(x\[1:\], y\[1:\])
    return 1 + min(
        levenshtein\_distance(x\[1:\], y),
        levenshtein\_distance(x, y\[1:\]),
        levenshtein\_distance(x\[1:\], y\[1:\]),
    )

[pairwise\_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
(X, Y, metric\=levenshtein\_distance)

Copy to clipboard

array(\[\[0., 3.\],\
       \[3., 2.\]\])

Copy to clipboard

**Total running time of the script:** (0 minutes 0.927 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_5_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_5_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_1_5_0.ipynb`](https://scikit-learn.org/stable/_downloads/ae2d0a2ad69c5df5b93e5ea5c87d56b2/plot_release_highlights_1_5_0.ipynb)

[`Download Python source code: plot_release_highlights_1_5_0.py`](https://scikit-learn.org/stable/_downloads/ba0cfc16d7953e1c2c6912b6beca1e91/plot_release_highlights_1_5_0.py)

[`Download zipped: plot_release_highlights_1_5_0.zip`](https://scikit-learn.org/stable/_downloads/1fffb175865f0e684095ddb70724914b/plot_release_highlights_1_5_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ba0cfc16d7953e1c2c6912b6beca1e91/plot_release_highlights_1_5_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ae2d0a2ad69c5df5b93e5ea5c87d56b2/plot_release_highlights_1_5_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1fffb175865f0e684095ddb70724914b/plot_release_highlights_1_5_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_5_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_5_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)