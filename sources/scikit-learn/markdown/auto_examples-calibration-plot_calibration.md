[Skip to main content](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/calibration/plot_calibration.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/calibration/plot_calibration.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/calibration/plot_calibration.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/calibration/plot_calibration.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/calibration/plot_calibration.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/calibration/plot_calibration.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#sphx-glr-download-auto-examples-calibration-plot-calibration-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Probability calibration of classifiers[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#probability-calibration-of-classifiers "Link to this heading")

=========================================================================================================================================================================================

When performing classification you often want to predict not only the class label, but also the associated probability. This probability gives you some kind of confidence on the prediction. However, not all classifiers provide well-calibrated probabilities, some being over-confident while others being under-confident. Thus, a separate calibration of predicted probabilities is often desirable as a postprocessing. This example illustrates two different methods for this calibration and evaluates the quality of the returned probabilities using Brier’s score (see [https://en.wikipedia.org/wiki/Brier\_score](https://en.wikipedia.org/wiki/Brier_score)
).

Compared are the estimated probability using a Gaussian naive Bayes classifier without calibration, with a sigmoid calibration, and with a non-parametric isotonic calibration. One can observe that only the non-parametric model is able to provide a probability calibration that returns probabilities close to the expected 0.5 for most of the samples belonging to the middle cluster with heterogeneous labels. This results in a significantly improved Brier score.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate synthetic dataset[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#generate-synthetic-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

n\_samples \= 50000

\# Generate 3 blobs with 2 classes where the second blob contains
\# half positive samples and half negative samples. Probability in this
\# blob is therefore 0.5.
centers \= \[(\-5, \-5), (0, 0), (5, 5)\]
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, centers\=centers, shuffle\=False, random\_state\=42)

y\[: n\_samples // 2\] \= 0
y\[n\_samples // 2 :\] \= 1
sample\_weight \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42).rand(y.shape\[0\])

\# split train, test for calibration
X\_train, X\_test, y\_train, y\_test, sw\_train, sw\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, sample\_weight, test\_size\=0.9, random\_state\=42
)

Copy to clipboard

Gaussian Naive-Bayes[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#gaussian-naive-bayes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
from sklearn.metrics import [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
from sklearn.naive\_bayes import [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")

\# With no calibration
clf \= [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
()
clf.fit(X\_train, y\_train)  \# GaussianNB itself does not support sample-weights
prob\_pos\_clf \= clf.predict\_proba(X\_test)\[:, 1\]

\# With isotonic calibration
clf\_isotonic \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(clf, cv\=2, method\="isotonic")
clf\_isotonic.fit(X\_train, y\_train, sample\_weight\=sw\_train)
prob\_pos\_isotonic \= clf\_isotonic.predict\_proba(X\_test)\[:, 1\]

\# With sigmoid calibration
clf\_sigmoid \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(clf, cv\=2, method\="sigmoid")
clf\_sigmoid.fit(X\_train, y\_train, sample\_weight\=sw\_train)
prob\_pos\_sigmoid \= clf\_sigmoid.predict\_proba(X\_test)\[:, 1\]

print("Brier score losses: (the smaller the better)")

clf\_score \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
(y\_test, prob\_pos\_clf, sample\_weight\=sw\_test)
print("No calibration: %1.3f" % clf\_score)

clf\_isotonic\_score \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
(y\_test, prob\_pos\_isotonic, sample\_weight\=sw\_test)
print("With isotonic calibration: %1.3f" % clf\_isotonic\_score)

clf\_sigmoid\_score \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
(y\_test, prob\_pos\_sigmoid, sample\_weight\=sw\_test)
print("With sigmoid calibration: %1.3f" % clf\_sigmoid\_score)

Copy to clipboard

Brier score losses: (the smaller the better)
No calibration: 0.104
With isotonic calibration: 0.084
With sigmoid calibration: 0.109

Copy to clipboard

Plot data and the predicted probabilities[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html#plot-data-and-the-predicted-probabilities "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import cm

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
y\_unique \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y)
colors \= cm.rainbow([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, y\_unique.size))
for this\_y, color in zip(y\_unique, colors):
    this\_X \= X\_train\[y\_train \== this\_y\]
    this\_sw \= sw\_train\[y\_train \== this\_y\]
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        this\_X\[:, 0\],
        this\_X\[:, 1\],
        s\=this\_sw \* 50,
        c\=color\[[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :\],
        alpha\=0.5,
        edgecolor\="k",
        label\="Class %s" % this\_y,
    )
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Data")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

order \= [np.lexsort](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")
((prob\_pos\_clf,))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(prob\_pos\_clf\[order\], "r", label\="No calibration (%1.3f)" % clf\_score)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    prob\_pos\_isotonic\[order\],
    "g",
    linewidth\=3,
    label\="Isotonic calibration (%1.3f)" % clf\_isotonic\_score,
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    prob\_pos\_sigmoid\[order\],
    "b",
    linewidth\=3,
    label\="Sigmoid calibration (%1.3f)" % clf\_sigmoid\_score,
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, y\_test.size, 51)\[1::2\],
    y\_test\[order\].reshape(25, \-1).mean(1),
    "k",
    linewidth\=3,
    label\=r"Empirical",
)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[\-0.05, 1.05\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Instances sorted according to predicted probability (uncalibrated GNB)")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("P(y=1)")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Gaussian naive Bayes probabilities")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Data](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_001.png)
*   ![Gaussian naive Bayes probabilities](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_002.png)

**Total running time of the script:** (0 minutes 0.408 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration.ipynb)

[`Download Jupyter notebook: plot_calibration.ipynb`](https://scikit-learn.org/stable/_downloads/0c15970ac17183d2bf864a9563081aeb/plot_calibration.ipynb)

[`Download Python source code: plot_calibration.py`](https://scikit-learn.org/stable/_downloads/0b39f715b5e32f01df3d212b6d822b82/plot_calibration.py)

[`Download zipped: plot_calibration.zip`](https://scikit-learn.org/stable/_downloads/60fcc8b24d902a4f93feb6592e544e02/plot_calibration.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/0b39f715b5e32f01df3d212b6d822b82/plot_calibration.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0c15970ac17183d2bf864a9563081aeb/plot_calibration.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/60fcc8b24d902a4f93feb6592e544e02/plot_calibration.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)