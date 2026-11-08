[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html#sphx-glr-download-auto-examples-semi-supervised-plot-self-training-varying-threshold-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Effect of varying threshold for self-training[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html#effect-of-varying-threshold-for-self-training "Link to this heading")

===============================================================================================================================================================================================================================

This example illustrates the effect of a varying threshold on self-training. The `breast_cancer` dataset is loaded, and labels are deleted such that only 50 out of 569 samples have labels. A `SelfTrainingClassifier` is fitted on this dataset, with varying thresholds.

The upper graph shows the amount of labeled samples that the classifier has available by the end of fit, and the accuracy of the classifier. The lower graph shows the last iteration in which a sample was labeled. All values are cross validated with 3 folds.

At low thresholds (in \[0.4, 0.5\]), the classifier learns from samples that were labeled with a low confidence. These low-confidence samples are likely have incorrect predicted labels, and as a result, fitting on these incorrect labels produces a poor accuracy. Note that the classifier labels almost all of the samples, and only takes one iteration.

For very high thresholds (in \[0.9, 1)) we observe that the classifier does not augment its dataset (the amount of self-labeled samples is 0). As a result, the accuracy achieved with a threshold of 0.9999 is the same as a normal supervised classifier would achieve.\
\
The optimal accuracy lies in between both of these extremes at a threshold of around 0.7.\
\
![plot self training varying threshold](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_001.png)\
\
\# Authors: The scikit-learn developers\
\# SPDX-License-Identifier: BSD-3-Clause\
\
import matplotlib.pyplot as plt\
import numpy as np\
\
from sklearn import datasets\
from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")\
from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")\
from sklearn.model\_selection import [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")\
from sklearn.semi\_supervised import [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")\
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")\
from sklearn.utils import [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")\
\
n\_splits \= 3\
\
X, y \= [datasets.load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")\
(return\_X\_y\=True)\
X, y \= [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")\
(X, y, random\_state\=42)\
y\_true \= y.copy()\
y\[50:\] \= \-1\
total\_samples \= y.shape\[0\]\
\
base\_classifier \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")\
([SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")\
(gamma\=0.001, random\_state\=42))\
\
x\_values \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(0.4, 1.05, 0.05)\
x\_values \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")\
(x\_values, 0.99999)\
scores \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")\
((x\_values.shape\[0\], n\_splits))\
amount\_labeled \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")\
((x\_values.shape\[0\], n\_splits))\
amount\_iterations \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")\
((x\_values.shape\[0\], n\_splits))\
\
for i, threshold in enumerate(x\_values):\
    self\_training\_clf \= [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")\
(base\_classifier, threshold\=threshold)\
\
    \# We need manual cross validation so that we don't treat -1 as a separate\
    \# class when computing accuracy\
    skfolds \= [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")\
(n\_splits\=n\_splits)\
    for fold, (train\_index, test\_index) in enumerate(skfolds.split(X, y)):\
        X\_train \= X\[train\_index\]\
        y\_train \= y\[train\_index\]\
        X\_test \= X\[test\_index\]\
        y\_test \= y\[test\_index\]\
        y\_test\_true \= y\_true\[test\_index\]\
\
        self\_training\_clf.fit(X\_train, y\_train)\
\
        \# The amount of labeled samples that at the end of fitting\
        amount\_labeled\[i, fold\] \= (\
            total\_samples\
            \- [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")\
(self\_training\_clf.labeled\_iter\_, return\_counts\=True)\[1\]\[0\]\
        )\
        \# The last iteration the classifier labeled a sample in\
        amount\_iterations\[i, fold\] \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")\
(self\_training\_clf.labeled\_iter\_)\
\
        y\_pred \= self\_training\_clf.predict(X\_test)\
        scores\[i, fold\] \= [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")\
(y\_test\_true, y\_pred)\
\
ax1 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")\
(211)\
ax1.errorbar(\
    x\_values, scores.mean(axis\=1), yerr\=scores.std(axis\=1), capsize\=2, color\="b"\
)\
ax1.set\_ylabel("Accuracy", color\="b")\
ax1.tick\_params("y", colors\="b")\
\
ax2 \= ax1.twinx()\
ax2.errorbar(\
    x\_values,\
    amount\_labeled.mean(axis\=1),\
    yerr\=amount\_labeled.std(axis\=1),\
    capsize\=2,\
    color\="g",\
)\
ax2.set\_ylim(bottom\=0)\
ax2.set\_ylabel("Amount of labeled samples", color\="g")\
ax2.tick\_params("y", colors\="g")\
\
ax3 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")\
(212, sharex\=ax1)\
ax3.errorbar(\
    x\_values,\
    amount\_iterations.mean(axis\=1),\
    yerr\=amount\_iterations.std(axis\=1),\
    capsize\=2,\
    color\="b",\
)\
ax3.set\_ylim(bottom\=0)\
ax3.set\_ylabel("Amount of iterations")\
ax3.set\_xlabel("Threshold")\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
**Total running time of the script:** (0 minutes 9.841 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_self_training_varying_threshold.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_self_training_varying_threshold.ipynb)\
\
[`Download Jupyter notebook: plot_self_training_varying_threshold.ipynb`](https://scikit-learn.org/stable/_downloads/7394345a6f70a1637fe759e076256013/plot_self_training_varying_threshold.ipynb)\
\
[`Download Python source code: plot_self_training_varying_threshold.py`](https://scikit-learn.org/stable/_downloads/966c9902a309bfbf613d6ab3cde2a9b8/plot_self_training_varying_threshold.py)\
\
[`Download zipped: plot_self_training_varying_threshold.zip`](https://scikit-learn.org/stable/_downloads/dbb11e3bf79f5227c33c4f2a04ec206a/plot_self_training_varying_threshold.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)\
\
[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)\
\
Post-hoc tuning the cut-off point of decision function\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)\
\
[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)\
\
Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)\
\
[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)\
\
Permutation Importance with Multicollinear or Correlated Features\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)\
\
[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)\
\
Semi-supervised Classification on a Text Dataset\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
[Download source code](https://scikit-learn.org/stable/_downloads/966c9902a309bfbf613d6ab3cde2a9b8/plot_self_training_varying_threshold.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7394345a6f70a1637fe759e076256013/plot_self_training_varying_threshold.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/dbb11e3bf79f5227c33c4f2a04ec206a/plot_self_training_varying_threshold.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_self_training_varying_threshold.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_self_training_varying_threshold.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)