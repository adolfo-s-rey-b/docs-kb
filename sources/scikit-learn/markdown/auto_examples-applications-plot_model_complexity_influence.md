[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_model_complexity_influence.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_model_complexity_influence.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_model_complexity_influence.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_model_complexity_influence.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_model_complexity_influence.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_model_complexity_influence.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#sphx-glr-download-auto-examples-applications-plot-model-complexity-influence-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Model Complexity Influence[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#model-complexity-influence "Link to this heading")

=================================================================================================================================================================================

Demonstrate how model complexity influences both prediction accuracy and computational performance.

We will be using two datasets:

*   [Diabetes dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)
     for regression. This dataset consists of 10 measurements taken from diabetes patients. The task is to predict disease progression;
    
*   [The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
     for classification. This dataset consists of newsgroup posts. The task is to predict on which topic (out of 20 topics) the post is written about.
    

We will model the complexity influence on three different estimators:

*   [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     (for classification data) which implements stochastic gradient descent learning;
    
*   [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
     (for regression data) which implements Nu support vector regression;
    
*   [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     builds an additive model in a forward stage-wise fashion. Notice that [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     is much faster than [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     starting with intermediate datasets (`n_samples >= 10_000`), which is not the case for this example.
    

We make the model complexity vary through the choice of relevant model parameters in each of our selected models. Next, we will measure the influence on both computational performance (latency) and predictive power (MSE or Hamming Loss).

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.ensemble import [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
from sklearn.metrics import [hamming\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
, [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.svm import [NuSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")

\# Initialize random generator
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

Copy to clipboard

Load the data[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#load-the-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

First we load both datasets.

Note

We are using [`fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
 to download 20 newsgroups dataset. It returns ready-to-use features.

Note

`X` of the 20 newsgroups dataset is a sparse matrix while `X` of diabetes dataset is a numpy array.

def generate\_data(case):
    """Generate regression/classification data."""
    if case \== "regression":
        X, y \= [datasets.load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)
        train\_size \= 0.8
    elif case \== "classification":
        X, y \= [datasets.fetch\_20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
(subset\="all", return\_X\_y\=True)
        train\_size \= 0.4  \# to make the example run faster

    X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
        X, y, train\_size\=train\_size, random\_state\=0
    )

    data \= {"X\_train": X\_train, "X\_test": X\_test, "y\_train": y\_train, "y\_test": y\_test}
    return data

regression\_data \= generate\_data("regression")
classification\_data \= generate\_data("classification")

Copy to clipboard

Benchmark influence[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#benchmark-influence "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we can calculate the influence of the parameters on the given estimator. In each round, we will set the estimator with the new value of `changing_param` and we will be collecting the prediction times, prediction performance and complexities to see how those changes affect the estimator. We will calculate the complexity using `complexity_computer` passed as a parameter.

def benchmark\_influence(conf):
    """
    Benchmark influence of \`changing\_param\` on both MSE and latency.
    """
    prediction\_times \= \[\]
    prediction\_powers \= \[\]
    complexities \= \[\]
    for param\_value in conf\["changing\_param\_values"\]:
        conf\["tuned\_params"\]\[conf\["changing\_param"\]\] \= param\_value
        estimator \= conf\["estimator"\](\*\*conf\["tuned\_params"\])

        print("Benchmarking %s" % estimator)
        estimator.fit(conf\["data"\]\["X\_train"\], conf\["data"\]\["y\_train"\])
        conf\["postfit\_hook"\](estimator)
        complexity \= conf\["complexity\_computer"\](estimator)
        complexities.append(complexity)
        start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        for \_ in range(conf\["n\_samples"\]):
            y\_pred \= estimator.predict(conf\["data"\]\["X\_test"\])
        elapsed\_time \= ([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time) / float(conf\["n\_samples"\])
        prediction\_times.append(elapsed\_time)
        pred\_score \= conf\["prediction\_performance\_computer"\](
            conf\["data"\]\["y\_test"\], y\_pred
        )
        prediction\_powers.append(pred\_score)
        print(
            "Complexity: %d | %s: %.4f | Pred. Time: %fs\\n"
            % (
                complexity,
                conf\["prediction\_performance\_label"\],
                pred\_score,
                elapsed\_time,
            )
        )
    return prediction\_powers, prediction\_times, complexities

Copy to clipboard

Choose parameters[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#choose-parameters "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

We choose the parameters for each of our estimators by making a dictionary with all the necessary values. `changing_param` is the name of the parameter which will vary in each estimator. Complexity will be defined by the `complexity_label` and calculated using `complexity_computer`. Also note that depending on the estimator type we are passing different data.

def \_count\_nonzero\_coefficients(estimator):
    a \= estimator.coef\_.toarray()
    return [np.count\_nonzero](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "numpy.count_nonzero")
(a)

configurations \= \[\
    {\
        "estimator": [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")\
,\
        "tuned\_params": {\
            "penalty": "elasticnet",\
            "alpha": 0.001,\
            "loss": "modified\_huber",\
            "fit\_intercept": True,\
            "tol": 1e-1,\
            "n\_iter\_no\_change": 2,\
        },\
        "changing\_param": "l1\_ratio",\
        "changing\_param\_values": \[0.25, 0.5, 0.75, 0.9\],\
        "complexity\_label": "non\_zero coefficients",\
        "complexity\_computer": \_count\_nonzero\_coefficients,\
        "prediction\_performance\_computer": [hamming\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")\
,\
        "prediction\_performance\_label": "Hamming Loss (Misclassification Ratio)",\
        "postfit\_hook": lambda x: x.sparsify(),\
        "data": classification\_data,\
        "n\_samples": 5,\
    },\
    {\
        "estimator": [NuSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")\
,\
        "tuned\_params": {"C": 1e3, "gamma": 2\*\*-15},\
        "changing\_param": "nu",\
        "changing\_param\_values": \[0.05, 0.1, 0.2, 0.35, 0.5\],\
        "complexity\_label": "n\_support\_vectors",\
        "complexity\_computer": lambda x: len(x.support\_vectors\_),\
        "data": regression\_data,\
        "postfit\_hook": lambda x: x,\
        "prediction\_performance\_computer": [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")\
,\
        "prediction\_performance\_label": "MSE",\
        "n\_samples": 15,\
    },\
    {\
        "estimator": [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")\
,\
        "tuned\_params": {\
            "loss": "squared\_error",\
            "learning\_rate": 0.05,\
            "max\_depth": 2,\
        },\
        "changing\_param": "n\_estimators",\
        "changing\_param\_values": \[10, 25, 50, 75, 100\],\
        "complexity\_label": "n\_trees",\
        "complexity\_computer": lambda x: x.n\_estimators,\
        "data": regression\_data,\
        "postfit\_hook": lambda x: x,\
        "prediction\_performance\_computer": [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")\
,\
        "prediction\_performance\_label": "MSE",\
        "n\_samples": 15,\
    },\
\]

Copy to clipboard

Run the code and plot the results[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#run-the-code-and-plot-the-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We defined all the functions required to run our benchmark. Now, we will loop over the different configurations that we defined previously. Subsequently, we can analyze the plots obtained from the benchmark: Relaxing the `L1` penalty in the SGD classifier reduces the prediction error but leads to an increase in the training time. We can draw a similar analysis regarding the training time which increases with the number of support vectors with a Nu-SVR. However, we observed that there is an optimal number of support vectors which reduces the prediction error. Indeed, too few support vectors lead to an under-fitted model while too many support vectors lead to an over-fitted model. The exact same conclusion can be drawn for the gradient-boosting model. The only the difference with the Nu-SVR is that having too many trees in the ensemble is not as detrimental.

def plot\_influence(conf, mse\_values, prediction\_times, complexities):
    """
    Plot influence of model complexity on both accuracy and latency.
    """

    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    fig.subplots\_adjust(right\=0.75)

    \# first axes (prediction error)
    ax1 \= fig.add\_subplot(111)
    line1 \= ax1.plot(complexities, mse\_values, c\="tab:blue", ls\="-")\[0\]
    ax1.set\_xlabel("Model Complexity (%s)" % conf\["complexity\_label"\])
    y1\_label \= conf\["prediction\_performance\_label"\]
    ax1.set\_ylabel(y1\_label)

    ax1.spines\["left"\].set\_color(line1.get\_color())
    ax1.yaxis.label.set\_color(line1.get\_color())
    ax1.tick\_params(axis\="y", colors\=line1.get\_color())

    \# second axes (latency)
    ax2 \= fig.add\_subplot(111, sharex\=ax1, frameon\=False)
    line2 \= ax2.plot(complexities, prediction\_times, c\="tab:orange", ls\="-")\[0\]
    ax2.yaxis.tick\_right()
    ax2.yaxis.set\_label\_position("right")
    y2\_label \= "Time (s)"
    ax2.set\_ylabel(y2\_label)
    ax1.spines\["right"\].set\_color(line2.get\_color())
    ax2.yaxis.label.set\_color(line2.get\_color())
    ax2.tick\_params(axis\="y", colors\=line2.get\_color())

    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
        (line1, line2), ("prediction error", "prediction latency"), loc\="upper center"
    )

    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "Influence of varying '%s' on %s"
        % (conf\["changing\_param"\], conf\["estimator"\].\_\_name\_\_)
    )

for conf in configurations:
    prediction\_performances, prediction\_times, complexities \= benchmark\_influence(conf)
    plot\_influence(conf, prediction\_performances, prediction\_times, complexities)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Influence of varying 'l1_ratio' on SGDClassifier](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_001.png)
*   ![Influence of varying 'nu' on NuSVR](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_002.png)
*   ![Influence of varying 'n_estimators' on GradientBoostingRegressor](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_003.png)

Benchmarking SGDClassifier(alpha=0.001, l1\_ratio=0.25, loss='modified\_huber',
              n\_iter\_no\_change=2, penalty='elasticnet', tol=0.1)
Complexity: 4944 | Hamming Loss (Misclassification Ratio): 0.2687 | Pred. Time: 0.033885s

Benchmarking SGDClassifier(alpha=0.001, l1\_ratio=0.5, loss='modified\_huber',
              n\_iter\_no\_change=2, penalty='elasticnet', tol=0.1)
Complexity: 1847 | Hamming Loss (Misclassification Ratio): 0.3264 | Pred. Time: 0.026301s

Benchmarking SGDClassifier(alpha=0.001, l1\_ratio=0.75, loss='modified\_huber',
              n\_iter\_no\_change=2, penalty='elasticnet', tol=0.1)
Complexity: 997 | Hamming Loss (Misclassification Ratio): 0.3383 | Pred. Time: 0.021675s

Benchmarking SGDClassifier(alpha=0.001, l1\_ratio=0.9, loss='modified\_huber',
              n\_iter\_no\_change=2, penalty='elasticnet', tol=0.1)
Complexity: 799 | Hamming Loss (Misclassification Ratio): 0.3481 | Pred. Time: 0.019442s

Benchmarking NuSVR(C=1000.0, gamma=3.0517578125e-05, nu=0.05)
Complexity: 18 | MSE: 5558.7313 | Pred. Time: 0.000224s

Benchmarking NuSVR(C=1000.0, gamma=3.0517578125e-05, nu=0.1)
Complexity: 36 | MSE: 5289.8022 | Pred. Time: 0.000318s

Benchmarking NuSVR(C=1000.0, gamma=3.0517578125e-05, nu=0.2)
Complexity: 72 | MSE: 5193.8353 | Pred. Time: 0.000475s

Benchmarking NuSVR(C=1000.0, gamma=3.0517578125e-05, nu=0.35)
Complexity: 124 | MSE: 5131.3279 | Pred. Time: 0.000724s

Benchmarking NuSVR(C=1000.0, gamma=3.0517578125e-05)
Complexity: 178 | MSE: 5149.0779 | Pred. Time: 0.001037s

Benchmarking GradientBoostingRegressor(learning\_rate=0.05, max\_depth=2, n\_estimators=10)
Complexity: 10 | MSE: 4066.4812 | Pred. Time: 0.000315s

Benchmarking GradientBoostingRegressor(learning\_rate=0.05, max\_depth=2, n\_estimators=25)
Complexity: 25 | MSE: 3551.1723 | Pred. Time: 0.000357s

Benchmarking GradientBoostingRegressor(learning\_rate=0.05, max\_depth=2, n\_estimators=50)
Complexity: 50 | MSE: 3445.2171 | Pred. Time: 0.000353s

Benchmarking GradientBoostingRegressor(learning\_rate=0.05, max\_depth=2, n\_estimators=75)
Complexity: 75 | MSE: 3433.0358 | Pred. Time: 0.000335s

Benchmarking GradientBoostingRegressor(learning\_rate=0.05, max\_depth=2)
Complexity: 100 | MSE: 3456.0602 | Pred. Time: 0.000354s

Copy to clipboard

Conclusion[#](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html#conclusion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

As a conclusion, we can deduce the following insights:

*   a model which is more complex (or expressive) will require a larger training time;
    
*   a more complex model does not guarantee to reduce the prediction error.
    

These aspects are related to model generalization and avoiding model under-fitting or over-fitting.

**Total running time of the script:** (0 minutes 4.904 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_model_complexity_influence.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_model_complexity_influence.ipynb)

[`Download Jupyter notebook: plot_model_complexity_influence.ipynb`](https://scikit-learn.org/stable/_downloads/3ed102fa8211c8d36f2331f0c5e1dcef/plot_model_complexity_influence.ipynb)

[`Download Python source code: plot_model_complexity_influence.py`](https://scikit-learn.org/stable/_downloads/ddd79923ba48c7f71fb17697baa1a22b/plot_model_complexity_influence.py)

[`Download zipped: plot_model_complexity_influence.zip`](https://scikit-learn.org/stable/_downloads/3d2c40ab2cfee918c269fd63cd2bc466/plot_model_complexity_influence.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ddd79923ba48c7f71fb17697baa1a22b/plot_model_complexity_influence.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3ed102fa8211c8d36f2331f0c5e1dcef/plot_model_complexity_influence.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3d2c40ab2cfee918c269fd63cd2bc466/plot_model_complexity_influence.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_model_complexity_influence.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_model_complexity_influence.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)