[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_roc.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_roc.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_roc.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_roc.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_roc.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_roc.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-download-auto-examples-model-selection-plot-roc-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multiclass Receiver Operating Characteristic (ROC)[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#multiclass-receiver-operating-characteristic-roc "Link to this heading")

===========================================================================================================================================================================================================

This example describes the use of the Receiver Operating Characteristic (ROC) metric to evaluate the quality of multiclass classifiers.

ROC curves typically feature true positive rate (TPR) on the Y axis, and false positive rate (FPR) on the X axis. This means that the top left corner of the plot is the “ideal” point - a FPR of zero, and a TPR of one. This is not very realistic, but it does mean that a larger area under the curve (AUC) is usually better. The “steepness” of ROC curves is also important, since it is ideal to maximize the TPR while minimizing the FPR.

ROC curves are typically used in binary classification, where the TPR and FPR can be defined unambiguously. In the case of multiclass classification, a notion of TPR or FPR is obtained only after binarizing the output. This can be done in 2 different ways:

*   the One-vs-Rest scheme compares each class against all the others (assumed as one);
    
*   the One-vs-One scheme compares every unique pairwise combination of classes.
    

In this example we explore both schemes and demo the concepts of micro and macro averaging as different ways of summarizing the information of the multiclass ROC curves.

Note

See [Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html#sphx-glr-auto-examples-model-selection-plot-roc-crossval-py)
 for an extension of the present example estimating the variance of the ROC curves and their respective AUC.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load and prepare data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#load-and-prepare-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

We import the [Iris plants dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)
 which contains 3 classes, each one corresponding to a type of iris plant. One class is linearly separable from the other 2; the latter are **not** linearly separable from each other.

Here we binarize the output and add noisy features to make the problem harder.

import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
target\_names \= iris.target\_names
X, y \= iris.data, iris.target
y \= iris.target\_names\[y\]

random\_state \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
n\_samples, n\_features \= X.shape
n\_classes \= len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y))
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[X, random\_state.randn(n\_samples, 200 \* n\_features)\], axis\=1)
(
    X\_train,
    X\_test,
    y\_train,
    y\_test,
) \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5, stratify\=y, random\_state\=0)

Copy to clipboard

We train a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 model which can naturally handle multiclass problems, thanks to the use of the multinomial formulation.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")

classifier \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
y\_score \= classifier.fit(X\_train, y\_train).predict\_proba(X\_test)

Copy to clipboard

One-vs-Rest multiclass ROC[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#one-vs-rest-multiclass-roc "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

The One-vs-the-Rest (OvR) multiclass strategy, also known as one-vs-all, consists in computing a ROC curve per each of the `n_classes`. In each step, a given class is regarded as the positive class and the remaining classes are regarded as the negative class as a bulk.

Note

One should not confuse the OvR strategy used for the **evaluation** of multiclass classifiers with the OvR strategy used to **train** a multiclass classifier by fitting a set of binary classifiers (for instance via the [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 meta-estimator). The OvR ROC evaluation can be used to scrutinize any kind of classification models irrespectively of how they were trained (see [Multiclass and multioutput algorithms](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
).

In this section we use a [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
 to binarize the target by one-hot-encoding in a OvR fashion. This means that the target of shape (`n_samples`,) is mapped to a target of shape (`n_samples`, `n_classes`).

from sklearn.preprocessing import [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")

label\_binarizer \= [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
().fit(y\_train)
y\_onehot\_test \= label\_binarizer.transform(y\_test)
y\_onehot\_test.shape  \# (n\_samples, n\_classes)

Copy to clipboard

(75, 3)

Copy to clipboard

We can as well easily check the encoding of a specific class:

label\_binarizer.transform(\["virginica"\])

Copy to clipboard

array(\[\[0, 0, 1\]\])

Copy to clipboard

### ROC curve showing a specific class[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#roc-curve-showing-a-specific-class "Link to this heading")

In the following plot we show the resulting ROC curve when regarding the iris flowers as either “virginica” (`class_id=2`) or “non-virginica” (the rest).

class\_of\_interest \= "virginica"
class\_id \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(label\_binarizer.classes\_ \== class\_of\_interest)\[0\]
class\_id

Copy to clipboard

np.int64(2)

Copy to clipboard

import matplotlib.pyplot as plt

from sklearn.metrics import RocCurveDisplay

display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
    y\_onehot\_test\[:, class\_id\],
    y\_score\[:, class\_id\],
    name\=f"{class\_of\_interest} vs the rest",
    curve\_kwargs\=dict(color\="darkorange"),
    plot\_chance\_level\=True,
    despine\=True,
)
\_ \= display.ax\_.set(
    xlabel\="False Positive Rate",
    ylabel\="True Positive Rate",
    title\="One-vs-Rest ROC curves:\\nVirginica vs (Setosa & Versicolor)",
)

Copy to clipboard

![One-vs-Rest ROC curves: Virginica vs (Setosa & Versicolor)](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_001.png)

### ROC curve using micro-averaged OvR[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#roc-curve-using-micro-averaged-ovr "Link to this heading")

Micro-averaging aggregates the contributions from all the classes (using [`numpy.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "(in NumPy v2.5)")
) to compute the average metrics as follows:

TPR\=∑cTPc∑c(TPc+FNc) ;

FPR\=∑cFPc∑c(FPc+TNc) .

We can briefly demo the effect of [`numpy.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "(in NumPy v2.5)")
:

print(f"y\_score:\\n{y\_score\[0:2, :\]}")
print()
print(f"y\_score.ravel():\\n{y\_score\[0:2, :\].ravel()}")

Copy to clipboard

y\_score:
\[\[0.38 0.05 0.57\]\
 \[0.07 0.28 0.65\]\]

y\_score.ravel():
\[0.38 0.05 0.57 0.07 0.28 0.65\]

Copy to clipboard

In a multi-class classification setup with highly imbalanced classes, micro-averaging is preferable over macro-averaging. In such cases, one can alternatively use a weighted macro-averaging, not demonstrated here.

display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
    y\_onehot\_test.ravel(),
    y\_score.ravel(),
    name\="micro-average OvR",
    curve\_kwargs\=dict(color\="darkorange"),
    plot\_chance\_level\=True,
    despine\=True,
)
\_ \= display.ax\_.set(
    xlabel\="False Positive Rate",
    ylabel\="True Positive Rate",
    title\="Micro-averaged One-vs-Rest\\nReceiver Operating Characteristic",
)

Copy to clipboard

![Micro-averaged One-vs-Rest Receiver Operating Characteristic](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_002.png)

In the case where the main interest is not the plot but the ROC-AUC score itself, we can reproduce the value shown in the plot using [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
.

from sklearn.metrics import [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

micro\_roc\_auc\_ovr \= [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(
    y\_test,
    y\_score,
    multi\_class\="ovr",
    average\="micro",
)

print(f"Micro-averaged One-vs-Rest ROC AUC score:\\n{micro\_roc\_auc\_ovr:.2f}")

Copy to clipboard

Micro-averaged One-vs-Rest ROC AUC score:
0.77

Copy to clipboard

This is equivalent to computing the ROC curve with [`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
 and then the area under the curve with [`auc`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
 for the raveled true and predicted classes.

from sklearn.metrics import [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
, [roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

\# store the fpr, tpr, and roc\_auc for all averaging strategies
fpr, tpr, roc\_auc \= dict(), dict(), dict()
\# Compute micro-average ROC curve and ROC area
fpr\["micro"\], tpr\["micro"\], \_ \= [roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
(y\_onehot\_test.ravel(), y\_score.ravel())
roc\_auc\["micro"\] \= [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(fpr\["micro"\], tpr\["micro"\])

print(f"Micro-averaged One-vs-Rest ROC AUC score:\\n{roc\_auc\['micro'\]:.2f}")

Copy to clipboard

Micro-averaged One-vs-Rest ROC AUC score:
0.77

Copy to clipboard

Note

By default, the computation of the ROC curve adds a single point at the maximal false positive rate by using linear interpolation and the McClish correction \[[Analyzing a portion of the ROC curve Med Decis Making. 1989 Jul-Sep; 9(3):190-5.](https://doi.org/10.1177/0272989x8900900307)\
\].

### ROC curve using the OvR macro-average[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#roc-curve-using-the-ovr-macro-average "Link to this heading")

Obtaining the macro-average requires computing the metric independently for each class and then taking the average over them, hence treating all classes equally a priori. We first aggregate the true/false positive rates per class:

TPR\=1C∑cTPcTPc+FNc ;

FPR\=1C∑cFPcFPc+TNc .

where `C` is the total number of classes.

for i in range(n\_classes):
    fpr\[i\], tpr\[i\], \_ \= [roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
(y\_onehot\_test\[:, i\], y\_score\[:, i\])
    roc\_auc\[i\] \= [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(fpr\[i\], tpr\[i\])

fpr\_grid \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, 1000)

\# Interpolate all ROC curves at these points
mean\_tpr \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(fpr\_grid)

for i in range(n\_classes):
    mean\_tpr += [np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")
(fpr\_grid, fpr\[i\], tpr\[i\])  \# linear interpolation

\# Average it and compute AUC
mean\_tpr /= n\_classes

fpr\["macro"\] \= fpr\_grid
tpr\["macro"\] \= mean\_tpr
roc\_auc\["macro"\] \= [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(fpr\["macro"\], tpr\["macro"\])

print(f"Macro-averaged One-vs-Rest ROC AUC score:\\n{roc\_auc\['macro'\]:.2f}")

Copy to clipboard

Macro-averaged One-vs-Rest ROC AUC score:
0.78

Copy to clipboard

This computation is equivalent to simply calling

macro\_roc\_auc\_ovr \= [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(
    y\_test,
    y\_score,
    multi\_class\="ovr",
    average\="macro",
)

print(f"Macro-averaged One-vs-Rest ROC AUC score:\\n{macro\_roc\_auc\_ovr:.2f}")

Copy to clipboard

Macro-averaged One-vs-Rest ROC AUC score:
0.78

Copy to clipboard

### Plot all OvR ROC curves together[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#plot-all-ovr-roc-curves-together "Link to this heading")

from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    fpr\["micro"\],
    tpr\["micro"\],
    label\=f"micro-average ROC curve (AUC = {roc\_auc\['micro'\]:.2f})",
    color\="deeppink",
    linestyle\=":",
    linewidth\=4,
)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    fpr\["macro"\],
    tpr\["macro"\],
    label\=f"macro-average ROC curve (AUC = {roc\_auc\['macro'\]:.2f})",
    color\="navy",
    linestyle\=":",
    linewidth\=4,
)

colors \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["aqua", "darkorange", "cornflowerblue"\])
for class\_id, color in zip(range(n\_classes), colors):
    [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        y\_onehot\_test\[:, class\_id\],
        y\_score\[:, class\_id\],
        name\=f"ROC curve for {target\_names\[class\_id\]}",
        curve\_kwargs\=dict(color\=color),
        ax\=ax,
        plot\_chance\_level\=(class\_id \== 2),
        despine\=True,
    )

\_ \= ax.set(
    xlabel\="False Positive Rate",
    ylabel\="True Positive Rate",
    title\="Extension of Receiver Operating Characteristic\\nto One-vs-Rest multiclass",
)

Copy to clipboard

![Extension of Receiver Operating Characteristic to One-vs-Rest multiclass](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_003.png)

One-vs-One multiclass ROC[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#one-vs-one-multiclass-roc "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

The One-vs-One (OvO) multiclass strategy consists in fitting one classifier per class pair. Since it requires to train `n_classes` \* (`n_classes` - 1) / 2 classifiers, this method is usually slower than One-vs-Rest due to its O(`n_classes` ^2) complexity.

In this section, we demonstrate the macro-averaged AUC using the OvO scheme for the 3 possible combinations in the [Iris plants dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)
: “setosa” vs “versicolor”, “versicolor” vs “virginica” and “virginica” vs “setosa”. Notice that micro-averaging is not defined for the OvO scheme.

### ROC curve using the OvO macro-average[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#roc-curve-using-the-ovo-macro-average "Link to this heading")

In the OvO scheme, the first step is to identify all possible unique combinations of pairs. The computation of scores is done by treating one of the elements in a given pair as the positive class and the other element as the negative class, then re-computing the score by inversing the roles and taking the mean of both scores.

from itertools import [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations")

pair\_list \= list([combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations")
([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y), 2))
print(pair\_list)

Copy to clipboard

\[(np.str\_('setosa'), np.str\_('versicolor')), (np.str\_('setosa'), np.str\_('virginica')), (np.str\_('versicolor'), np.str\_('virginica'))\]

Copy to clipboard

pair\_scores \= \[\]
mean\_tpr \= dict()

for ix, (label\_a, label\_b) in enumerate(pair\_list):
    a\_mask \= y\_test \== label\_a
    b\_mask \= y\_test \== label\_b
    ab\_mask \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(a\_mask, b\_mask)

    a\_true \= a\_mask\[ab\_mask\]
    b\_true \= b\_mask\[ab\_mask\]

    idx\_a \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(label\_binarizer.classes\_ \== label\_a)\[0\]
    idx\_b \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(label\_binarizer.classes\_ \== label\_b)\[0\]

    fpr\_a, tpr\_a, \_ \= [roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
(a\_true, y\_score\[ab\_mask, idx\_a\])
    fpr\_b, tpr\_b, \_ \= [roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
(b\_true, y\_score\[ab\_mask, idx\_b\])

    mean\_tpr\[ix\] \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(fpr\_grid)
    mean\_tpr\[ix\] += [np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")
(fpr\_grid, fpr\_a, tpr\_a)
    mean\_tpr\[ix\] += [np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")
(fpr\_grid, fpr\_b, tpr\_b)
    mean\_tpr\[ix\] /= 2
    mean\_score \= [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(fpr\_grid, mean\_tpr\[ix\])
    pair\_scores.append(mean\_score)

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        fpr\_grid,
        mean\_tpr\[ix\],
        label\=f"Mean {label\_a} vs {label\_b} (AUC = {mean\_score:.2f})",
        linestyle\=":",
        linewidth\=4,
    )
    [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        a\_true,
        y\_score\[ab\_mask, idx\_a\],
        ax\=ax,
        name\=f"{label\_a} as positive class",
    )
    [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        b\_true,
        y\_score\[ab\_mask, idx\_b\],
        ax\=ax,
        name\=f"{label\_b} as positive class",
        plot\_chance\_level\=True,
        despine\=True,
    )
    ax.set(
        xlabel\="False Positive Rate",
        ylabel\="True Positive Rate",
        title\=f"{target\_names\[idx\_a\]} vs {label\_b} ROC curves",
    )

print(f"Macro-averaged One-vs-One ROC AUC score:\\n{[np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(pair\_scores):.2f}")

Copy to clipboard

*   ![setosa vs versicolor ROC curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_004.png)
*   ![setosa vs virginica ROC curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_005.png)
*   ![versicolor vs virginica ROC curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_006.png)

Macro-averaged One-vs-One ROC AUC score:
0.78

Copy to clipboard

One can also assert that the macro-average we computed “by hand” is equivalent to the implemented `average="macro"` option of the [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
 function.

macro\_roc\_auc\_ovo \= [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(
    y\_test,
    y\_score,
    multi\_class\="ovo",
    average\="macro",
)

print(f"Macro-averaged One-vs-One ROC AUC score:\\n{macro\_roc\_auc\_ovo:.2f}")

Copy to clipboard

Macro-averaged One-vs-One ROC AUC score:
0.78

Copy to clipboard

### Plot all OvO ROC curves together[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#plot-all-ovo-roc-curves-together "Link to this heading")

ovo\_tpr \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(fpr\_grid)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
for ix, (label\_a, label\_b) in enumerate(pair\_list):
    ovo\_tpr += mean\_tpr\[ix\]
    ax.plot(
        fpr\_grid,
        mean\_tpr\[ix\],
        label\=f"Mean {label\_a} vs {label\_b} (AUC = {pair\_scores\[ix\]:.2f})",
    )

ovo\_tpr /= sum(1 for pair in enumerate(pair\_list))

ax.plot(
    fpr\_grid,
    ovo\_tpr,
    label\=f"One-vs-One macro-average (AUC = {macro\_roc\_auc\_ovo:.2f})",
    linestyle\=":",
    linewidth\=4,
)
ax.plot(\[0, 1\], \[0, 1\], "k--", label\="Chance level (AUC = 0.5)")
\_ \= ax.set(
    xlabel\="False Positive Rate",
    ylabel\="True Positive Rate",
    title\="Extension of Receiver Operating Characteristic\\nto One-vs-One multiclass",
    aspect\="equal",
    xlim\=(\-0.01, 1.01),
    ylim\=(\-0.01, 1.01),
)

Copy to clipboard

![Extension of Receiver Operating Characteristic to One-vs-One multiclass](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_007.png)

We confirm that the classes “versicolor” and “virginica” are not well identified by a linear classifier. Notice that the “virginica”-vs-the-rest ROC-AUC score (0.77) is between the OvO ROC-AUC scores for “versicolor” vs “virginica” (0.64) and “setosa” vs “virginica” (0.90). Indeed, the OvO strategy gives additional information on the confusion between a pair of classes, at the expense of computational cost when the number of classes is large.

The OvO strategy is recommended if the user is mainly interested in correctly identifying a particular class or subset of classes, whereas evaluating the global performance of a classifier can still be summarized via a given averaging strategy.

When dealing with imbalanced datasets, choosing the appropriate metric based on the business context or problem you are addressing is crucial. It is also essential to select an appropriate averaging method (micro vs. macro) depending on the desired outcome:

*   Micro-averaging aggregates metrics across all instances, treating each individual instance equally, regardless of its class. This approach is useful when evaluating overall performance, but note that it can be dominated by the majority class in imbalanced datasets.
    
*   Macro-averaging calculates metrics for each class independently and then averages them, giving equal weight to each class. This is particularly useful when you want under-represented classes to be considered as important as highly populated classes.
    

**Total running time of the script:** (0 minutes 0.782 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_roc.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_roc.ipynb)

[`Download Jupyter notebook: plot_roc.ipynb`](https://scikit-learn.org/stable/_downloads/40f4aad91af595a370d7582e3a23bed7/plot_roc.ipynb)

[`Download Python source code: plot_roc.py`](https://scikit-learn.org/stable/_downloads/80fef09514fd851560e999a5b7daa303/plot_roc.py)

[`Download zipped: plot_roc.zip`](https://scikit-learn.org/stable/_downloads/24e6ec210b28537f67bbf0b9a883e04b/plot_roc.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/80fef09514fd851560e999a5b7daa303/plot_roc.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/40f4aad91af595a370d7582e3a23bed7/plot_roc.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/24e6ec210b28537f67bbf0b9a883e04b/plot_roc.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_roc.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_roc.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)