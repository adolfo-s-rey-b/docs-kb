[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_anova.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_anova.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_anova.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_anova.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_anova.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_anova.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#sphx-glr-download-auto-examples-svm-plot-svm-anova-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM-Anova: SVM with univariate feature selection[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#svm-anova-svm-with-univariate-feature-selection "Link to this heading")

==================================================================================================================================================================================================

This example shows how to perform univariate feature selection before running a SVC (support vector classifier) to improve the classification scores. We use the iris dataset (4 features) and add 36 non-informative features. We can find that our model achieves best performance when we select around 10% of features.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load some data to play with[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#load-some-data-to-play-with "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

X, y \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(return\_X\_y\=True)

\# Add non-informative features
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((X, 2 \* rng.random((X.shape\[0\], 36))))

Copy to clipboard

Create the pipeline[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#create-the-pipeline "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

from sklearn.feature\_selection import [SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
, [f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

\# Create a feature-selection transform, a scaler and an instance of SVM that we
\# combine together to have a full-blown estimator

clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("anova", [SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")\
([f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")\
)),\
        ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
        ("svc", [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")\
(gamma\="auto")),\
    \]
)

Copy to clipboard

Plot the cross-validation score as a function of percentile of features[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#plot-the-cross-validation-score-as-a-function-of-percentile-of-features "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

score\_means \= list()
score\_stds \= list()
percentiles \= (1, 3, 6, 10, 15, 20, 30, 40, 60, 80, 100)

for percentile in percentiles:
    clf.set\_params(anova\_\_percentile\=percentile)
    this\_scores \= [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(clf, X, y)
    score\_means.append(this\_scores.mean())
    score\_stds.append(this\_scores.std())

[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(percentiles, score\_means, [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(score\_stds))
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Performance of the SVM-Anova varying the percentile of features selected")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 100, 11, endpoint\=True))
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Percentile")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Accuracy Score")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Performance of the SVM-Anova varying the percentile of features selected](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_001.png)

**Total running time of the script:** (0 minutes 0.397 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_anova.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_anova.ipynb)

[`Download Jupyter notebook: plot_svm_anova.ipynb`](https://scikit-learn.org/stable/_downloads/6f4a6a0d8063b616c4aa4db2865de57c/plot_svm_anova.ipynb)

[`Download Python source code: plot_svm_anova.py`](https://scikit-learn.org/stable/_downloads/41973816d3932cd07b75d8825fd2c13d/plot_svm_anova.py)

[`Download zipped: plot_svm_anova.zip`](https://scikit-learn.org/stable/_downloads/85e330311348be5bd40d46fbc15a91be/plot_svm_anova.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/41973816d3932cd07b75d8825fd2c13d/plot_svm_anova.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6f4a6a0d8063b616c4aa4db2865de57c/plot_svm_anova.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/85e330311348be5bd40d46fbc15a91be/plot_svm_anova.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_anova.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_anova.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)