[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_anomaly_comparison.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html#sphx-glr-download-auto-examples-miscellaneous-plot-anomaly-comparison-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing anomaly detection algorithms for outlier detection on toy datasets[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html#comparing-anomaly-detection-algorithms-for-outlier-detection-on-toy-datasets "Link to this heading")

==============================================================================================================================================================================================================================================================================

This example shows characteristics of different anomaly detection algorithms on 2D datasets. Datasets contain one or two modes (regions of high density) to illustrate the ability of algorithms to cope with multimodal data.

For each dataset, 15% of samples are generated as random uniform noise. This proportion is the value given to the nu parameter of the OneClassSVM and the contamination parameter of the other outlier detection algorithms. Decision boundaries between inliers and outliers are displayed in black except for Local Outlier Factor (LOF) as it has no predict method to be applied on new data when it is used for outlier detection.

The [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 is known to be sensitive to outliers and thus does not perform very well for outlier detection. This estimator is best suited for novelty detection when the training set is not contaminated by outliers. That said, outlier detection in high-dimension, or without any assumptions on the distribution of the inlying data is very challenging, and a One-class SVM might give useful results in these situations depending on the value of its hyperparameters.

The [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 is an implementation of the One-Class SVM based on stochastic gradient descent (SGD). Combined with kernel approximation, this estimator can be used to approximate the solution of a kernelized [`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
. We note that, although not identical, the decision boundaries of the [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 and the ones of [`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 are very similar. The main advantage of using [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 is that it scales linearly with the number of samples.

[`sklearn.covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
 assumes the data is Gaussian and learns an ellipse. It thus degrades when the data is not unimodal. Notice however that this estimator is robust to outliers.

[`IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
 and [`LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
 seem to perform reasonably well for multi-modal data sets. The advantage of [`LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
 over the other estimators is shown for the third data set, where the two modes have different densities. This advantage is explained by the local aspect of LOF, meaning that it only compares the score of abnormality of one sample with the scores of its neighbors.

Finally, for the last data set, it is hard to say that one sample is more abnormal than another sample as they are uniformly distributed in a hypercube. Except for the [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 which overfits a little, all estimators present decent solutions for this situation. In such a case, it would be wise to look more closely at the scores of abnormality of the samples as a good estimator should assign similar scores to all the samples.

While these examples give some intuition about the algorithms, this intuition might not apply to very high dimensional data.

Finally, note that parameters of the models have been here handpicked but that in practice they need to be adjusted. In the absence of labelled data, the problem is completely unsupervised so model selection can be a challenge.

![Robust covariance, One-Class SVM, One-Class SVM (SGD), Isolation Forest, Local Outlier Factor](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from sklearn import svm
from sklearn.covariance import [EllipticEnvelope](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
, [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
from sklearn.ensemble import [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
from sklearn.neighbors import [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

[matplotlib.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
\["contour.negative\_linestyle"\] \= "solid"

\# Example settings
n\_samples \= 300
outliers\_fraction \= 0.15
n\_outliers \= int(outliers\_fraction \* n\_samples)
n\_inliers \= n\_samples \- n\_outliers

\# define outlier/anomaly detection methods to be compared.
\# the SGDOneClassSVM must be used in a pipeline with a kernel approximation
\# to give similar results to the OneClassSVM
anomaly\_algorithms \= \[\
    (\
        "Robust covariance",\
        [EllipticEnvelope](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")\
(contamination\=outliers\_fraction, random\_state\=42),\
    ),\
    ("One-Class SVM", [svm.OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")\
(nu\=outliers\_fraction, kernel\="rbf", gamma\=0.1)),\
    (\
        "One-Class SVM (SGD)",\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
(gamma\=0.1, random\_state\=42, n\_components\=150),\
            [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")\
(\
                nu\=outliers\_fraction,\
                shuffle\=True,\
                fit\_intercept\=True,\
                random\_state\=42,\
                tol\=1e-6,\
            ),\
        ),\
    ),\
    (\
        "Isolation Forest",\
        [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")\
(contamination\=outliers\_fraction, random\_state\=42),\
    ),\
    (\
        "Local Outlier Factor",\
        [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")\
(n\_neighbors\=35, contamination\=outliers\_fraction),\
    ),\
\]

\# Define datasets
blobs\_params \= dict(random\_state\=0, n\_samples\=n\_inliers, n\_features\=2)
datasets \= \[\
    [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(centers\=\[\[0, 0\], \[0, 0\]\], cluster\_std\=0.5, \*\*blobs\_params)\[0\],\
    [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(centers\=\[\[2, 2\], \[\-2, \-2\]\], cluster\_std\=\[0.5, 0.5\], \*\*blobs\_params)\[0\],\
    [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(centers\=\[\[2, 2\], \[\-2, \-2\]\], cluster\_std\=\[1.5, 0.3\], \*\*blobs\_params)\[0\],\
    4.0\
    \* (\
        [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")\
(n\_samples\=n\_samples, noise\=0.05, random\_state\=0)\[0\]\
        \- [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\[0.5, 0.25\])\
    ),\
    14.0 \* ([np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
(42).rand(n\_samples, 2) \- 0.5),\
\]

\# Compare given classifiers under given settings
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-7, 7, 150), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-7, 7, 150))

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(len(anomaly\_algorithms) \* 2 + 4, 12.5))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(
    left\=0.02, right\=0.98, bottom\=0.001, top\=0.96, wspace\=0.05, hspace\=0.01
)

plot\_num \= 1
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)

for i\_dataset, X in enumerate(datasets):
    \# Add outliers
    X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[X, rng.uniform(low\=-6, high\=6, size\=(n\_outliers, 2))\], axis\=0)

    for name, algorithm in anomaly\_algorithms:
        t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        algorithm.fit(X)
        t1 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(datasets), len(anomaly\_algorithms), plot\_num)
        if i\_dataset \== 0:
            [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(name, size\=18)

        \# fit the data and tag outliers
        if name \== "Local Outlier Factor":
            y\_pred \= algorithm.fit\_predict(X)
        else:
            y\_pred \= algorithm.fit(X).predict(X)

        \# plot the levels lines and the points
        if name != "Local Outlier Factor":  \# LOF does not implement predict
            Z \= algorithm.predict([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
            Z \= Z.reshape(xx.shape)
            [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(xx, yy, Z, levels\=\[0\], linewidths\=2, colors\="black")

        colors \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["#377eb8", "#ff7f00"\])
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], s\=10, color\=colors\[(y\_pred + 1) // 2\])

        [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-7, 7)
        [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-7, 7)
        [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
        [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
        [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
            0.99,
            0.01,
            ("%.2fs" % (t1 \- t0)).lstrip("0"),
            transform\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().transAxes,
            size\=15,
            horizontalalignment\="right",
        )
        plot\_num += 1

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.698 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_anomaly_comparison.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_anomaly_comparison.ipynb)

[`Download Jupyter notebook: plot_anomaly_comparison.ipynb`](https://scikit-learn.org/stable/_downloads/1916a2a88b97d84ae7b7fb44d3f5503b/plot_anomaly_comparison.ipynb)

[`Download Python source code: plot_anomaly_comparison.py`](https://scikit-learn.org/stable/_downloads/9057446ce5a251004d1743be3a7c5f0e/plot_anomaly_comparison.py)

[`Download zipped: plot_anomaly_comparison.zip`](https://scikit-learn.org/stable/_downloads/a36aaa401f3fc0a911c024ab92f37ae4/plot_anomaly_comparison.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_thumb.png)

[Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)

Outlier detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)

[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/9057446ce5a251004d1743be3a7c5f0e/plot_anomaly_comparison.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1916a2a88b97d84ae7b7fb44d3f5503b/plot_anomaly_comparison.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a36aaa401f3fc0a911c024ab92f37ae4/plot_anomaly_comparison.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_anomaly_comparison.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_anomaly_comparison.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)