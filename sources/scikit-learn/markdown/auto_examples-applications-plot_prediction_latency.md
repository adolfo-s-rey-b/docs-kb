[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_prediction_latency.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_prediction_latency.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_prediction_latency.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_prediction_latency.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_prediction_latency.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_prediction_latency.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#sphx-glr-download-auto-examples-applications-plot-prediction-latency-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Prediction Latency[#](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#prediction-latency "Link to this heading")

=========================================================================================================================================================

This is an example showing the prediction latency of various scikit-learn estimators.

The goal is to measure the latency one can expect when doing predictions either in bulk or atomic (i.e. one by one) mode.

The plots represent the distribution of the prediction latency as a boxplot.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import gc
import time
from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
, [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
from sklearn.utils import [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")

def \_not\_in\_sphinx():
    \# Hack to detect whether we are running by the sphinx builder
    return "\_\_file\_\_" in globals()

Copy to clipboard

Benchmark and plot helper functions[#](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#benchmark-and-plot-helper-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def atomic\_benchmark\_estimator(estimator, X\_test, verbose\=False):
    """Measure runtime prediction of each instance."""
    n\_instances \= X\_test.shape\[0\]
    runtimes \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_instances, dtype\=float)
    for i in range(n\_instances):
        instance \= X\_test\[\[i\], :\]
        start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        estimator.predict(instance)
        runtimes\[i\] \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
    if verbose:
        print(
            "atomic\_benchmark runtimes:",
            min(runtimes),
            [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
(runtimes, 50),
            max(runtimes),
        )
    return runtimes

def bulk\_benchmark\_estimator(estimator, X\_test, n\_bulk\_repeats, verbose):
    """Measure runtime prediction of the whole input."""
    n\_instances \= X\_test.shape\[0\]
    runtimes \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_bulk\_repeats, dtype\=float)
    for i in range(n\_bulk\_repeats):
        start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        estimator.predict(X\_test)
        runtimes\[i\] \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
    runtimes \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(list(map(lambda x: x / float(n\_instances), runtimes)))
    if verbose:
        print(
            "bulk\_benchmark runtimes:",
            min(runtimes),
            [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
(runtimes, 50),
            max(runtimes),
        )
    return runtimes

def benchmark\_estimator(estimator, X\_test, n\_bulk\_repeats\=30, verbose\=False):
    """
    Measure runtimes of prediction in both atomic and bulk mode.

    Parameters
    ----------
    estimator : already trained estimator supporting \`predict()\`
    X\_test : test input
    n\_bulk\_repeats : how many times to repeat when evaluating bulk mode

    Returns
    -------
    atomic\_runtimes, bulk\_runtimes : a pair of \`np.array\` which contain the
    runtimes in seconds.

    """
    atomic\_runtimes \= atomic\_benchmark\_estimator(estimator, X\_test, verbose)
    bulk\_runtimes \= bulk\_benchmark\_estimator(estimator, X\_test, n\_bulk\_repeats, verbose)
    return atomic\_runtimes, bulk\_runtimes

def generate\_dataset(n\_train, n\_test, n\_features, noise\=0.1, verbose\=False):
    """Generate a regression dataset with the given parameters."""
    if verbose:
        print("generating dataset...")

    X, y, coef \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
        n\_samples\=n\_train + n\_test, n\_features\=n\_features, noise\=noise, coef\=True
    )

    random\_seed \= 13
    X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
        X, y, train\_size\=n\_train, test\_size\=n\_test, random\_state\=random\_seed
    )
    X\_train, y\_train \= [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")
(X\_train, y\_train, random\_state\=random\_seed)

    X\_scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
    X\_train \= X\_scaler.fit\_transform(X\_train)
    X\_test \= X\_scaler.transform(X\_test)

    y\_scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
    y\_train \= y\_scaler.fit\_transform(y\_train\[:, None\])\[:, 0\]
    y\_test \= y\_scaler.transform(y\_test\[:, None\])\[:, 0\]

    [gc.collect](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
()
    if verbose:
        print("ok")
    return X\_train, y\_train, X\_test, y\_test

def boxplot\_runtimes(runtimes, pred\_type, configuration):
    """
    Plot a new \`Figure\` with boxplots of prediction runtimes.

    Parameters
    ----------
    runtimes : list of \`np.array\` of latencies in micro-seconds
    cls\_names : list of estimator class names that generated the runtimes
    pred\_type : 'bulk' or 'atomic'

    """

    fig, ax1 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 6))
    bp \= [plt.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
(
        runtimes,
    )

    cls\_infos \= \[\
        "%s\\n(%d %s)"\
        % (\
            estimator\_conf\["name"\],\
            estimator\_conf\["complexity\_computer"\](estimator\_conf\["instance"\]),\
            estimator\_conf\["complexity\_label"\],\
        )\
        for estimator\_conf in configuration\["estimators"\]\
    \]
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(ax1, xticklabels\=cls\_infos)
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(bp\["boxes"\], color\="black")
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(bp\["whiskers"\], color\="black")
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(bp\["fliers"\], color\="red", marker\="+")

    ax1.yaxis.grid(True, linestyle\="-", which\="major", color\="lightgrey", alpha\=0.5)

    ax1.set\_axisbelow(True)
    ax1.set\_title(
        "Prediction Time per Instance - %s, %d feats."
        % (pred\_type.capitalize(), configuration\["n\_features"\])
    )
    ax1.set\_ylabel("Prediction Time (us)")

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

def benchmark(configuration):
    """Run the whole benchmark."""
    X\_train, y\_train, X\_test, y\_test \= generate\_dataset(
        configuration\["n\_train"\], configuration\["n\_test"\], configuration\["n\_features"\]
    )

    stats \= {}
    for estimator\_conf in configuration\["estimators"\]:
        print("Benchmarking", estimator\_conf\["instance"\])
        estimator\_conf\["instance"\].fit(X\_train, y\_train)
        [gc.collect](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
()
        a, b \= benchmark\_estimator(estimator\_conf\["instance"\], X\_test)
        stats\[estimator\_conf\["name"\]\] \= {"atomic": a, "bulk": b}

    cls\_names \= \[\
        estimator\_conf\["name"\] for estimator\_conf in configuration\["estimators"\]\
    \]
    runtimes \= \[1e6 \* stats\[clf\_name\]\["atomic"\] for clf\_name in cls\_names\]
    boxplot\_runtimes(runtimes, "atomic", configuration)
    runtimes \= \[1e6 \* stats\[clf\_name\]\["bulk"\] for clf\_name in cls\_names\]
    boxplot\_runtimes(runtimes, "bulk (%d)" % configuration\["n\_test"\], configuration)

def n\_feature\_influence(estimators, n\_train, n\_test, n\_features, percentile):
    """
    Estimate influence of the number of features on prediction time.

    Parameters
    ----------

    estimators : dict of (name (str), estimator) to benchmark
    n\_train : nber of training instances (int)
    n\_test : nber of testing instances (int)
    n\_features : list of feature-space dimensionality to test (int)
    percentile : percentile at which to measure the speed (int \[0-100\])

    Returns:
    --------

    percentiles : dict(estimator\_name,
                       dict(n\_features, percentile\_perf\_in\_us))

    """
    percentiles \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
([defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
)
    for n in n\_features:
        print("benchmarking with %d features" % n)
        X\_train, y\_train, X\_test, y\_test \= generate\_dataset(n\_train, n\_test, n)
        for cls\_name, estimator in estimators.items():
            estimator.fit(X\_train, y\_train)
            [gc.collect](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
()
            runtimes \= bulk\_benchmark\_estimator(estimator, X\_test, 30, False)
            percentiles\[cls\_name\]\[n\] \= 1e6 \* [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
(runtimes, percentile)
    return percentiles

def plot\_n\_features\_influence(percentiles, percentile):
    fig, ax1 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 6))
    colors \= \["r", "g", "b"\]
    for i, cls\_name in enumerate(percentiles.keys()):
        x \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(sorted(percentiles\[cls\_name\].keys()))
        y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[percentiles\[cls\_name\]\[n\] for n in x\])
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
            x,
            y,
            color\=colors\[i\],
        )
    ax1.yaxis.grid(True, linestyle\="-", which\="major", color\="lightgrey", alpha\=0.5)
    ax1.set\_axisbelow(True)
    ax1.set\_title("Evolution of Prediction Time with #Features")
    ax1.set\_xlabel("#Features")
    ax1.set\_ylabel("Prediction Time at %d%%\-ile (us)" % percentile)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

def benchmark\_throughputs(configuration, duration\_secs\=0.1):
    """benchmark throughput for different estimators."""
    X\_train, y\_train, X\_test, y\_test \= generate\_dataset(
        configuration\["n\_train"\], configuration\["n\_test"\], configuration\["n\_features"\]
    )
    throughputs \= dict()
    for estimator\_config in configuration\["estimators"\]:
        estimator\_config\["instance"\].fit(X\_train, y\_train)
        start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        n\_predictions \= 0
        while ([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time) < duration\_secs:
            estimator\_config\["instance"\].predict(X\_test\[\[0\]\])
            n\_predictions += 1
        throughputs\[estimator\_config\["name"\]\] \= n\_predictions / duration\_secs
    return throughputs

def plot\_benchmark\_throughput(throughputs, configuration):
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 6))
    colors \= \["r", "g", "b"\]
    cls\_infos \= \[\
        "%s\\n(%d %s)"\
        % (\
            estimator\_conf\["name"\],\
            estimator\_conf\["complexity\_computer"\](estimator\_conf\["instance"\]),\
            estimator\_conf\["complexity\_label"\],\
        )\
        for estimator\_conf in configuration\["estimators"\]\
    \]
    cls\_values \= \[\
        throughputs\[estimator\_conf\["name"\]\]\
        for estimator\_conf in configuration\["estimators"\]\
    \]
    [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(range(len(throughputs)), cls\_values, width\=0.5, color\=colors)
    ax.set\_xticks([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.25, len(throughputs) \- 0.75, len(throughputs)))
    ax.set\_xticklabels(cls\_infos, fontsize\=10)
    ymax \= max(cls\_values) \* 1.2
    ax.set\_ylim((0, ymax))
    ax.set\_ylabel("Throughput (predictions/sec)")
    ax.set\_title(
        "Prediction Throughput for different estimators (%d features)"
        % configuration\["n\_features"\]
    )
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

Benchmark bulk/atomic prediction speed for various regressors[#](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#benchmark-bulk-atomic-prediction-speed-for-various-regressors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

configuration \= {
    "n\_train": int(1e3),
    "n\_test": int(1e2),
    "n\_features": int(1e2),
    "estimators": \[\
        {\
            "name": "Linear Model",\
            "instance": [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")\
(\
                penalty\="elasticnet", alpha\=0.01, l1\_ratio\=0.25, tol\=1e-4\
            ),\
            "complexity\_label": "non-zero coefficients",\
            "complexity\_computer": lambda clf: [np.count\_nonzero](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "numpy.count_nonzero")\
(clf.coef\_),\
        },\
        {\
            "name": "RandomForest",\
            "instance": [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")\
(),\
            "complexity\_label": "estimators",\
            "complexity\_computer": lambda clf: clf.n\_estimators,\
        },\
        {\
            "name": "SVR",\
            "instance": [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")\
(kernel\="rbf"),\
            "complexity\_label": "support vectors",\
            "complexity\_computer": lambda clf: len(clf.support\_vectors\_),\
        },\
    \],
}
benchmark(configuration)

Copy to clipboard

*   ![Prediction Time per Instance - Atomic, 100 feats.](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_001.png)
*   ![Prediction Time per Instance - Bulk (100), 100 feats.](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_002.png)

Benchmarking SGDRegressor(alpha=0.01, l1\_ratio=0.25, penalty='elasticnet', tol=0.0001)
Benchmarking RandomForestRegressor()
Benchmarking SVR()

Copy to clipboard

Benchmark n\_features influence on prediction speed[#](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#benchmark-n-features-influence-on-prediction-speed "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

percentile \= 90
percentiles \= n\_feature\_influence(
    {"ridge": [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
()},
    configuration\["n\_train"\],
    configuration\["n\_test"\],
    \[100, 250, 500\],
    percentile,
)
plot\_n\_features\_influence(percentiles, percentile)

Copy to clipboard

![Evolution of Prediction Time with #Features](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_003.png)

benchmarking with 100 features
benchmarking with 250 features
benchmarking with 500 features

Copy to clipboard

Benchmark throughput[#](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#benchmark-throughput "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

throughputs \= benchmark\_throughputs(configuration)
plot\_benchmark\_throughput(throughputs, configuration)

Copy to clipboard

![Prediction Throughput for different estimators (100 features)](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_004.png)

**Total running time of the script:** (0 minutes 12.800 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_prediction_latency.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_prediction_latency.ipynb)

[`Download Jupyter notebook: plot_prediction_latency.ipynb`](https://scikit-learn.org/stable/_downloads/2c8efe31be0d68b7945dbfbff0788dd3/plot_prediction_latency.ipynb)

[`Download Python source code: plot_prediction_latency.py`](https://scikit-learn.org/stable/_downloads/5f054219fb38e926537d741fe5832e8c/plot_prediction_latency.py)

[`Download zipped: plot_prediction_latency.zip`](https://scikit-learn.org/stable/_downloads/5afb7e185d86921e913f71e03a88ba38/plot_prediction_latency.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_thumb.png)

[Out-of-core classification of text documents](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html)

Out-of-core classification of text documents

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5f054219fb38e926537d741fe5832e8c/plot_prediction_latency.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2c8efe31be0d68b7945dbfbff0788dd3/plot_prediction_latency.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5afb7e185d86921e913f71e03a88ba38/plot_prediction_latency.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_prediction_latency.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_prediction_latency.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)