[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_permutation_tests_for_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#sphx-glr-download-auto-examples-model-selection-plot-permutation-tests-for-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Test with permutations the significance of a classification score[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#test-with-permutations-the-significance-of-a-classification-score "Link to this heading")

============================================================================================================================================================================================================================================================================

This example demonstrates the use of [`permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
 to evaluate the significance of a cross-validated score using permutations.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#dataset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

We will use the [Iris plants dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)
, which consists of measurements taken from 3 Iris species. Our model will use the measurements to predict the iris species.

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target

Copy to clipboard

For comparison, we also generate some random feature data (i.e., 20 features), uncorrelated with the class labels in the iris dataset.

import numpy as np

n\_uncorrelated\_features \= 20
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed\=0)
\# Use same number of samples as in iris and 20 features
X\_rand \= rng.normal(size\=(X.shape\[0\], n\_uncorrelated\_features))

Copy to clipboard

Permutation test score[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#permutation-test-score "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we calculate the [`permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
 for both, the original iris dataset (where there’s a strong relationship between features and labels) and the randomly generated features with iris labels (where no dependency between features and labels is expected). We use the [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 classifier and [Accuracy score](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
 to evaluate the model at each round.

[`permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
 generates a null distribution by calculating the accuracy of the classifier on 1000 different permutations of the dataset, where features remain the same but labels undergo different random permutations. This is the distribution for the null hypothesis which states there is no dependency between the features and labels. An empirical p-value is then calculated as the proportion of permutations, for which the score obtained by the model trained on the permutation, is greater than or equal to the score obtained using the original data.

from sklearn.model\_selection import [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
, [permutation\_test\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

clf \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", random\_state\=7)
cv \= [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
(n\_splits\=2, shuffle\=True, random\_state\=0)

score\_iris, perm\_scores\_iris, pvalue\_iris \= [permutation\_test\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
(
    clf, X, y, scoring\="accuracy", cv\=cv, n\_permutations\=1000
)

score\_rand, perm\_scores\_rand, pvalue\_rand \= [permutation\_test\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
(
    clf, X\_rand, y, scoring\="accuracy", cv\=cv, n\_permutations\=1000
)

Copy to clipboard

### Original data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#original-data "Link to this heading")

Below we plot a histogram of the permutation scores (the null distribution). The red line indicates the score obtained by the classifier on the original data (without permuted labels). The score is much better than those obtained by using permuted data and the p-value is thus very low. This indicates that there is a low likelihood that this good score would be obtained by chance alone. It provides evidence that the iris dataset contains real dependency between features and labels and the classifier was able to utilize this to obtain good results. The low p-value can lead us to reject the null hypothesis.

import matplotlib.pyplot as plt

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

ax.hist(perm\_scores\_iris, bins\=20, density\=True)
ax.axvline(score\_iris, ls\="--", color\="r")
score\_label \= (
    f"Score on original\\niris data: {score\_iris:.2f}\\n(p-value: {pvalue\_iris:.3f})"
)
ax.text(0.7, 10, score\_label, fontsize\=12)
ax.set\_xlabel("Accuracy score")
\_ \= ax.set\_ylabel("Probability density")

Copy to clipboard

![plot permutation tests for classification](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_001.png)

### Random data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#random-data "Link to this heading")

Below we plot the null distribution for the randomized data. The permutation scores are similar to those obtained using the original iris dataset because the permutation always destroys any feature-label dependency present. The score obtained on the randomized data in this case though, is very poor. This results in a large p-value, confirming that there was no feature-label dependency in the randomized data.

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

ax.hist(perm\_scores\_rand, bins\=20, density\=True)
ax.set\_xlim(0.13)
ax.axvline(score\_rand, ls\="--", color\="r")
score\_label \= (
    f"Score on original\\nrandom data: {score\_rand:.2f}\\n(p-value: {pvalue\_rand:.3f})"
)
ax.text(0.14, 7.5, score\_label, fontsize\=12)
ax.set\_xlabel("Accuracy score")
ax.set\_ylabel("Probability density")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot permutation tests for classification](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_002.png)

Another possible reason for obtaining a high p-value could be that the classifier was not able to use the structure in the data. In this case, the p-value would only be low for classifiers that are able to utilize the dependency present. In our case above, where the data is random, all classifiers would have a high p-value as there is no structure present in the data. We might or might not fail to reject the null hypothesis depending on whether the p-value is high on a more appropriate estimator as well.

Finally, note that this test has been shown to produce low p-values even if there is only weak structure in the data [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html#id2)
.

References

**Total running time of the script:** (0 minutes 14.120 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_permutation_tests_for_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_permutation_tests_for_classification.ipynb)

[`Download Jupyter notebook: plot_permutation_tests_for_classification.ipynb`](https://scikit-learn.org/stable/_downloads/8ed2480d8058dc8515097893b64d815b/plot_permutation_tests_for_classification.ipynb)

[`Download Python source code: plot_permutation_tests_for_classification.py`](https://scikit-learn.org/stable/_downloads/be7fb5ee9d7dc0c4fb277110eef3566a/plot_permutation_tests_for_classification.py)

[`Download zipped: plot_permutation_tests_for_classification.zip`](https://scikit-learn.org/stable/_downloads/32b1787884d41cf7a0b36640001d381f/plot_permutation_tests_for_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/be7fb5ee9d7dc0c4fb277110eef3566a/plot_permutation_tests_for_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8ed2480d8058dc8515097893b64d815b/plot_permutation_tests_for_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/32b1787884d41cf7a0b36640001d381f/plot_permutation_tests_for_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_permutation_tests_for_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_permutation_tests_for_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)