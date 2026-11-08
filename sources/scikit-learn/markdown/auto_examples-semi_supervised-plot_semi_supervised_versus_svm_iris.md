[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#sphx-glr-download-auto-examples-semi-supervised-plot-semi-supervised-versus-svm-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#decision-boundary-of-semi-supervised-classifiers-versus-svm-on-the-iris-dataset "Link to this heading")

===================================================================================================================================================================================================================================================================================================

This example compares decision boundaries learned by two semi-supervised methods, namely [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 and [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
, while varying the proportion of labeled training data from small fractions up to the full dataset.

Both methods rely on RBF kernels: [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 uses it by default, and [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
 is paired here with [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 as base estimator (also RBF-based by default) to allow a fair comparison. With 100% labeled data, [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
 reduces to a fully supervised [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, since there are no unlabeled points left to pseudo-label.

In a second section, we explain how `predict_proba` is computed in [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 and [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
.

See [Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#sphx-glr-auto-examples-semi-supervised-plot-semi-supervised-newsgroups-py)
 for a comparison of `LabelSpreading` and `SelfTrainingClassifier` in terms of performance.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.semi\_supervised import [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
, [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data\[:, :2\]
y \= iris.target

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
y\_rand \= rng.rand(y.shape\[0\])
y\_10 \= [np.copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
(y)
y\_10\[y\_rand \> 0.1\] \= \-1  \# set random samples to be unlabeled
y\_30 \= [np.copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
(y)
y\_30\[y\_rand \> 0.3\] \= \-1

ls10 \= ([LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
().fit(X, y\_10), y\_10, "LabelSpreading with 10% labeled data")
ls30 \= ([LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
().fit(X, y\_30), y\_30, "LabelSpreading with 30% labeled data")
ls100 \= ([LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
().fit(X, y), y, "LabelSpreading with 100% labeled data")

base\_classifier \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
([SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(gamma\=0.5, random\_state\=42))
st10 \= (
    [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
(base\_classifier).fit(X, y\_10),
    y\_10,
    "Self-training with 10% labeled data",
)
st30 \= (
    [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
(base\_classifier).fit(X, y\_30),
    y\_30,
    "Self-training with 30% labeled data",
)
rbf\_svc \= (
    base\_classifier.fit(X, y),
    y,
    "SVC with rbf kernel\\n(equivalent to Self-training with 100% labeled data)",
)

classifiers \= (ls10, st10, ls30, st30, ls100, rbf\_svc)

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, ncols\=2, sharex\="col", sharey\="row", figsize\=(10, 12))
axes \= axes.ravel()
for ax, (clf, y\_train, title) in zip(axes, classifiers):
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        response\_method\="predict\_proba",
        plot\_method\="contourf",
        ax\=ax,
    )
    colors \= \[\
        (1, 1, 1, 1) if label \== \-1 else disp.multiclass\_colors\_\[label\]\
        for label in y\_train\
    \]
    ax.scatter(X\[:, 0\], X\[:, 1\], c\=colors, edgecolor\="black")
    ax.set\_title(title)
fig.suptitle(
    "Semi-supervised decision boundaries with varying fractions of labeled data", y\=1
)
handles \= \[\
    [mpatches.Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(\
        facecolor\=color, edgecolor\="black", label\=iris.target\_names\[class\_idx\]\
    )\
    for class\_idx, color in enumerate(disp.multiclass\_colors\_)\
\]
handles.append([mpatches.Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
(facecolor\="white", edgecolor\="black", label\="Unlabeled"))
fig.legend(
    handles\=handles, loc\="lower center", ncol\=len(handles), bbox\_to\_anchor\=(0.5, 0.0)
)
fig.tight\_layout(rect\=\[0, 0.03, 1, 1\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Semi-supervised decision boundaries with varying fractions of labeled data, LabelSpreading with 10% labeled data, Self-training with 10% labeled data, LabelSpreading with 30% labeled data, Self-training with 30% labeled data, LabelSpreading with 100% labeled data, SVC with rbf kernel (equivalent to Self-training with 100% labeled data)](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_001.png)

We observe that the decision boundaries are already quite similar to those using the full labeled data available for training, even when using a very small subset of the labels.

Interpretation of `predict_proba`[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#interpretation-of-predict-proba "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `predict_proba` in `LabelSpreading`[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#predict-proba-in-labelspreading "Link to this heading")

[`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 constructs a similarity graph from the data, by default using an RBF kernel. This means each sample is connected to every other with a weight that decays with their squared Euclidean distance, scaled by a parameter `gamma`.

Once we have that weighted graph, labels are propagated along the graph edges. Each sample gradually takes on a soft label distribution that reflects a weighted average of the labels of its neighbors until the process converges. These per-sample distributions are stored in `label_distributions_`.

`predict_proba` computes the class probabilities for a new point by taking a weighted average of the rows in `label_distributions_`, where the weights come from the RBF kernel similarities between the new point and the training samples. The averaged values are then renormalized so that they sum to one.

Just keep in mind that these “probabilities” are graph-based scores, not calibrated posteriors. Don’t over-interpret their absolute values.

from sklearn.metrics.pairwise import [rbf\_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")

ls \= ls100\[0\]  \# fitted LabelSpreading instance
x\_query \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[3.5, 1.5\]\])  \# point in the soft blue region

\# Step 1: similarities between query and all training samples
W \= [rbf\_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")
(x\_query, X, gamma\=ls.gamma)  \# \`gamma=20\` by default

\# Step 2: weighted average of label distributions
probs \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(W, ls.label\_distributions\_)

\# Step 3: normalize to sum to 1
probs /= probs.sum(axis\=1, keepdims\=True)

print("Manual:", probs)
print("API   :", ls.predict\_proba(x\_query))

Copy to clipboard

Manual: \[\[0.96 0.03 0.01\]\]
API   : \[\[0.96 0.03 0.01\]\]

Copy to clipboard

### `predict_proba` in `SelfTrainingClassifier`[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#predict-proba-in-selftrainingclassifier "Link to this heading")

[`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
 works by repeatedly fitting its base estimator on the currently labeled data, then adding pseudo-labels for unlabeled points whose predicted probabilities exceed a confidence threshold. This process continues until no new points can be labeled, at which point the classifier has a final fitted base estimator stored in the attribute `estimator_`.

When you call `predict_proba` on the `SelfTrainingClassifier`, it simply delegates to this final estimator.

st \= st10\[0\]
print("Manual:", st.estimator\_.predict\_proba(x\_query))
print("API   :", st.predict\_proba(x\_query))

Copy to clipboard

Manual: \[\[0.41 0.37 0.22\]\]
API   : \[\[0.41 0.37 0.22\]\]

Copy to clipboard

In both methods, semi-supervised learning can be understood as constructing a categorical distribution over classes for each sample. [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 keeps these distributions soft and updates them through graph-based propagation. Predictions (including `predict_proba`) remain tied to the training set, which must be stored for inference.

[`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
 instead uses these distributions internally to decide which unlabeled points to assign pseudo-labels during training, but at prediction time the returned probabilities come directly from the final fitted estimator, and therefore the decision rule does not require storing the training data.

**Total running time of the script:** (0 minutes 1.562 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.ipynb)

[`Download Jupyter notebook: plot_semi_supervised_versus_svm_iris.ipynb`](https://scikit-learn.org/stable/_downloads/28056df7ed8b04d495f832aaab1b8c3e/plot_semi_supervised_versus_svm_iris.ipynb)

[`Download Python source code: plot_semi_supervised_versus_svm_iris.py`](https://scikit-learn.org/stable/_downloads/8219ffabb9724762c36d14d22f80a0d5/plot_semi_supervised_versus_svm_iris.py)

[`Download zipped: plot_semi_supervised_versus_svm_iris.zip`](https://scikit-learn.org/stable/_downloads/e6b5bf0cfe4380adcb59097ff327369c/plot_semi_supervised_versus_svm_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_thumb.png)

[Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Label Propagation digits: Active learning

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/8219ffabb9724762c36d14d22f80a0d5/plot_semi_supervised_versus_svm_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/28056df7ed8b04d495f832aaab1b8c3e/plot_semi_supervised_versus_svm_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e6b5bf0cfe4380adcb59097ff327369c/plot_semi_supervised_versus_svm_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)