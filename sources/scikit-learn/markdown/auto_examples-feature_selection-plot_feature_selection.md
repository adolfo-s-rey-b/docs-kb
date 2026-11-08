[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_feature_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_feature_selection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_feature_selection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_feature_selection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_feature_selection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_feature_selection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#sphx-glr-download-auto-examples-feature-selection-plot-feature-selection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Univariate Feature Selection[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#univariate-feature-selection "Link to this heading")

=================================================================================================================================================================================

This notebook is an example of using univariate feature selection to improve classification accuracy on a noisy dataset.

In this example, some noisy (non informative) features are added to the iris dataset. Support vector machine (SVM) is used to classify the dataset both before and after applying univariate feature selection. For each feature, we plot the p-values for the univariate feature selection and the corresponding weights of SVMs. With this, we will compare model accuracy and examine the impact of univariate feature selection on model weights.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#generate-sample-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

\# The iris dataset
X, y \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(return\_X\_y\=True)

\# Some noisy data not correlated
E \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42).uniform(0, 0.1, size\=(X.shape\[0\], 20))

\# Add the noisy data to the informative features
X \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((X, E))

\# Split dataset to select feature and evaluate the classifier
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=0)

Copy to clipboard

Univariate feature selection[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#id1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Univariate feature selection with F-test for feature scoring. We use the default selection function to select the four most significant features.

from sklearn.feature\_selection import [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
, [f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")

selector \= [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
([f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")
, k\=4)
selector.fit(X\_train, y\_train)
scores \= \-[np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
(selector.pvalues\_)
scores /= scores.max()

Copy to clipboard

import matplotlib.pyplot as plt

X\_indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[\-1\])
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()
[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(X\_indices \- 0.05, scores, width\=0.2)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Feature univariate score")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Feature number")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
(r"Univariate score ($-Log(p\_{value})$)")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Feature univariate score](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_001.png)

In the total set of features, only the 4 of the original features are significant. We can see that they have the highest score with univariate feature selection.

Compare with SVMs[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html#compare-with-svms "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Without univariate feature selection

from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

clf \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
())
clf.fit(X\_train, y\_train)
print(
    "Classification accuracy without selecting features: {:.3f}".format(
        clf.score(X\_test, y\_test)
    )
)

svm\_weights \= np.abs(clf\[\-1\].coef\_).sum(axis\=0)
svm\_weights /= svm\_weights.sum()

Copy to clipboard

Classification accuracy without selecting features: 0.789

Copy to clipboard

After univariate feature selection

clf\_selected \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
([f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")
, k\=4), [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
())
clf\_selected.fit(X\_train, y\_train)
print(
    "Classification accuracy after univariate feature selection: {:.3f}".format(
        clf\_selected.score(X\_test, y\_test)
    )
)

svm\_weights\_selected \= np.abs(clf\_selected\[\-1\].coef\_).sum(axis\=0)
svm\_weights\_selected /= svm\_weights\_selected.sum()

Copy to clipboard

Classification accuracy after univariate feature selection: 0.868

Copy to clipboard

[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(
    X\_indices \- 0.45, scores, width\=0.2, label\=r"Univariate score ($-Log(p\_{value})$)"
)

[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(X\_indices \- 0.25, svm\_weights, width\=0.2, label\="SVM weight")

[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(
    X\_indices\[selector.get\_support()\] \- 0.05,
    svm\_weights\_selected,
    width\=0.2,
    label\="SVM weights after selection",
)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparing feature selection")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Feature number")
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Comparing feature selection](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_002.png)

Without univariate feature selection, the SVM assigns a large weight to the first 4 original significant features, but also selects many of the non-informative features. Applying univariate feature selection before the SVM increases the SVM weight attributed to the significant features, and will thus improve classification.

**Total running time of the script:** (0 minutes 0.189 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_feature_selection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_feature_selection.ipynb)

[`Download Jupyter notebook: plot_feature_selection.ipynb`](https://scikit-learn.org/stable/_downloads/fe71806a900680d092025bf56d0dfcb3/plot_feature_selection.ipynb)

[`Download Python source code: plot_feature_selection.py`](https://scikit-learn.org/stable/_downloads/62397dcd82eb2478e27036ac96fe2ab9/plot_feature_selection.py)

[`Download zipped: plot_feature_selection.zip`](https://scikit-learn.org/stable/_downloads/f6d77c1d67a1e980437128d300e94c4e/plot_feature_selection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/62397dcd82eb2478e27036ac96fe2ab9/plot_feature_selection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fe71806a900680d092025bf56d0dfcb3/plot_feature_selection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f6d77c1d67a1e980437128d300e94c4e/plot_feature_selection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_feature_selection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_feature_selection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)