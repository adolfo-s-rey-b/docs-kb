[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#sphx-glr-download-auto-examples-feature-selection-plot-rfe-with-cross-validation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Recursive feature elimination with cross-validation[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#recursive-feature-elimination-with-cross-validation "Link to this heading")

=======================================================================================================================================================================================================================================

A Recursive Feature Elimination (RFE) example with automatic tuning of the number of features selected with cross-validation.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#data-generation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

We build a classification task using 3 informative features. The introduction of 2 additional redundant (i.e. correlated) features has the effect that the selected features vary depending on the cross-validation fold. The remaining features are non-informative as they are drawn at random.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")

n\_features \= 15
feat\_names \= \[f"feature\_{i}" for i in range(15)\]

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=500,
    n\_features\=n\_features,
    n\_informative\=3,
    n\_redundant\=2,
    n\_repeated\=0,
    n\_classes\=8,
    n\_clusters\_per\_class\=1,
    class\_sep\=0.8,
    random\_state\=0,
)

Copy to clipboard

Model training and selection[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#model-training-and-selection "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We create the RFE object and compute the cross-validated scores. The scoring strategy “accuracy” optimizes the proportion of correctly classified samples.

from sklearn.feature\_selection import [RFECV](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")

min\_features\_to\_select \= 1  \# Minimum number of features to consider
clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
cv \= [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
(5)

rfecv \= [RFECV](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
(
    estimator\=clf,
    step\=1,
    cv\=cv,
    scoring\="accuracy",
    min\_features\_to\_select\=min\_features\_to\_select,
    n\_jobs\=2,
)
rfecv.fit(X, y)

print(f"Optimal number of features: {rfecv.n\_features\_}")

Copy to clipboard

Optimal number of features: 3

Copy to clipboard

In the present case, the model with 3 features (which corresponds to the true generative model) is found to be the most optimal.

Plot number of features VS. cross-validation scores[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#plot-number-of-features-vs-cross-validation-scores "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

data \= {
    key: value
    for key, value in rfecv.cv\_results\_.items()
    if key in \["n\_features", "mean\_test\_score", "std\_test\_score"\]
}
cv\_results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(data)
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Number of features selected")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Mean test accuracy")
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    x\=cv\_results\["n\_features"\],
    y\=cv\_results\["mean\_test\_score"\],
    yerr\=cv\_results\["std\_test\_score"\],
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Recursive Feature Elimination \\nwith correlated features")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Recursive Feature Elimination  with correlated features](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_001.png)

From the plot above one can further notice a plateau of equivalent scores (similar mean value and overlapping errorbars) for 3 to 5 selected features. This is the result of introducing correlated features. Indeed, the optimal model selected by the RFE can lie within this range, depending on the cross-validation technique. The test accuracy decreases above 5 selected features, this is, keeping non-informative features leads to over-fitting and is therefore detrimental for the statistical performance of the models.

import numpy as np

for i in range(cv.n\_splits):
    mask \= rfecv.cv\_results\_\[f"split{i}\_support"\]\[\
        rfecv.n\_features\_ \- 1\
    \]  \# mask of features selected by the RFE
    features\_selected \= [np.ma.compressed](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "numpy.ma.compressed")
([np.ma.masked\_array](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "numpy.ma.masked_array")
(feat\_names, mask\=1 \- mask))
    print(f"Features selected in fold {i}: {features\_selected}")

Copy to clipboard

Features selected in fold 0: \['feature\_3' 'feature\_4' 'feature\_8'\]
Features selected in fold 1: \['feature\_3' 'feature\_4' 'feature\_8'\]
Features selected in fold 2: \['feature\_3' 'feature\_4' 'feature\_8'\]
Features selected in fold 3: \['feature\_3' 'feature\_4' 'feature\_8'\]
Features selected in fold 4: \['feature\_3' 'feature\_4' 'feature\_8'\]

Copy to clipboard

In the five folds, the selected features are consistent. This is good news, it means that the selection is stable across folds, and it confirms that these features are the most informative ones.

**Total running time of the script:** (0 minutes 0.671 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_rfe_with_cross_validation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_rfe_with_cross_validation.ipynb)

[`Download Jupyter notebook: plot_rfe_with_cross_validation.ipynb`](https://scikit-learn.org/stable/_downloads/949ed208b2147ed2b3e348e81fef52be/plot_rfe_with_cross_validation.ipynb)

[`Download Python source code: plot_rfe_with_cross_validation.py`](https://scikit-learn.org/stable/_downloads/592b2521e44501266ca5339d1fb123cb/plot_rfe_with_cross_validation.py)

[`Download zipped: plot_rfe_with_cross_validation.zip`](https://scikit-learn.org/stable/_downloads/129e49615b0c1e7782384456dd7c3ec3/plot_rfe_with_cross_validation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/592b2521e44501266ca5339d1fb123cb/plot_rfe_with_cross_validation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/949ed208b2147ed2b3e348e81fef52be/plot_rfe_with_cross_validation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/129e49615b0c1e7782384456dd7c3ec3/plot_rfe_with_cross_validation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_rfe_with_cross_validation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_rfe_with_cross_validation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)