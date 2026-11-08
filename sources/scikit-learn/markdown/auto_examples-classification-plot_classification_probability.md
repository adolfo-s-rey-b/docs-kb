[Skip to main content](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/classification/plot_classification_probability.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/classification/plot_classification_probability.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/classification/plot_classification_probability.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/classification/plot_classification_probability.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/classification/plot_classification_probability.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/classification/plot_classification_probability.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-download-auto-examples-classification-plot-classification-probability-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot classification probability[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#plot-classification-probability "Link to this heading")

=============================================================================================================================================================================================

This example illustrates the use of [`sklearn.inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
 to plot the predicted class probabilities of various classifiers in a 2D feature space, mostly for didactic purposes.

The first three columns show the predicted probability for varying values of the two features. Round markers represent the test data that was predicted to belong to that class.

In the last column, all three classes are represented on each plot; the class with the highest predicted probability at each point is plotted. The round markers show the test data and are colored by their true label.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm

from sklearn import datasets
from sklearn.ensemble import [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
, [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
, [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import (
    [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
,
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
,
    [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
,
)

Copy to clipboard

Data: 2D projection of the iris dataset[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#data-2d-projection-of-the-iris-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data\[:, 0:2\]  \# we only take the first two features for visualization
y \= iris.target

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.5, random\_state\=42
)

Copy to clipboard

Probabilistic classifiers[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#probabilistic-classifiers "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will plot the decision boundaries of several classifiers that have a `predict_proba` method. This will allow us to visualize the uncertainty of the classifier in regions where it is not certain of its prediction.

classifiers \= {
    "Logistic regression\\n(C=0.1)": [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=0.1),
    "Logistic regression\\n(C=100)": [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=100),
    "Gaussian Process": [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(\[1.0, 1.0\])),
    "Logistic regression\\n(RBF features)": [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
(kernel\="rbf", gamma\=5e-1, n\_components\=50, random\_state\=1),
        [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
    ),
    "Gradient Boosting": [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
(random\_state\=42),
    "Logistic regression\\n(binned features)": [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
(n\_bins\=5, quantile\_method\="averaged\_inverted\_cdf"),
        [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(interaction\_only\=True),
        [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
    ),
    "Logistic regression\\n(spline features)": [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(n\_knots\=5),
        [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(interaction\_only\=True),
        [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
    ),
}

Copy to clipboard

Plotting the decision boundaries[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#plotting-the-decision-boundaries "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For each classifier, we plot the per-class probabilities on the first three columns and the probabilities of the most likely class on the last column.

n\_classifiers \= len(classifiers)
scatter\_kwargs \= {
    "s": 25,
    "marker": "o",
    "linewidths": 0.8,
    "edgecolor": "k",
    "alpha": 0.7,
}
y\_unique \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y)

\# Ensure legend not cut off
[mpl.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
\["savefig.bbox"\] \= "tight"
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    nrows\=n\_classifiers,
    ncols\=len(iris.target\_names) + 1,
    figsize\=(4 \* 2.2, n\_classifiers \* 2.2),
)
evaluation\_results \= \[\]
levels \= 100
for classifier\_idx, (name, classifier) in enumerate(classifiers.items()):
    y\_pred \= classifier.fit(X\_train, y\_train).predict(X\_test)
    y\_pred\_proba \= classifier.predict\_proba(X\_test)
    accuracy\_test \= [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\_test, y\_pred)
    roc\_auc\_test \= [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(y\_test, y\_pred\_proba, multi\_class\="ovr")
    log\_loss\_test \= [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\_test, y\_pred\_proba)
    evaluation\_results.append(
        {
            "name": name.replace("\\n", " "),
            "accuracy": accuracy\_test,
            "roc\_auc": roc\_auc\_test,
            "log\_loss": log\_loss\_test,
        }
    )
    for label in y\_unique:
        \# plot the probability estimate provided by the classifier
        disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
            classifier,
            X\_train,
            response\_method\="predict\_proba",
            class\_of\_interest\=label,
            ax\=axes\[classifier\_idx, label\],
            vmin\=0,
            vmax\=1,
            cmap\="Blues",
            levels\=levels,
        )
        axes\[classifier\_idx, label\].set\_title(f"Class {iris.target\_names\[label\]}")
        \# plot data predicted to belong to given class
        mask\_y\_pred \= y\_pred \== label
        axes\[classifier\_idx, label\].scatter(
            X\_test\[mask\_y\_pred, 0\], X\_test\[mask\_y\_pred, 1\], c\="w", \*\*scatter\_kwargs
        )

        axes\[classifier\_idx, label\].set(xticks\=(), yticks\=())
    \# add column that shows all classes by plotting class with max 'predict\_proba'
    max\_class\_disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        classifier,
        X\_train,
        response\_method\="predict\_proba",
        class\_of\_interest\=None,
        ax\=axes\[classifier\_idx, len(y\_unique)\],
        vmin\=0,
        vmax\=1,
        levels\=levels,
    )
    for label in y\_unique:
        mask\_label \= y\_test \== label
        max\_col \= len(y\_unique)
        axes\[classifier\_idx, max\_col\].scatter(
            X\_test\[mask\_label, 0\],
            X\_test\[mask\_label, 1\],
            c\=max\_class\_disp.multiclass\_colors\_\[\[label\], :\],
            \*\*scatter\_kwargs,
        )

    axes\[classifier\_idx, 3\].set(xticks\=(), yticks\=())
    axes\[classifier\_idx, 3\].set\_title("Max class")
    axes\[classifier\_idx, 0\].set\_ylabel(name)

\# colorbar for single class plots
ax\_single \= fig.add\_axes(\[0.15, 0.01, 0.5, 0.02\])
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Probability")
\_ \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(
    [cm.ScalarMappable](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
(norm\=None, cmap\=disp.surface\_.cmap),
    cax\=ax\_single,
    orientation\="horizontal",
)

\# colorbars for max probability class column
max\_class\_cmaps \= \[s.cmap for s in max\_class\_disp.surface\_\]

for label in y\_unique:
    ax\_max \= fig.add\_axes(\[0.73, (0.06 \- (label \* 0.04)), 0.16, 0.015\])
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(f"Probability class {label}", fontsize\=10)
    \_ \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(
        [cm.ScalarMappable](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
(norm\=None, cmap\=max\_class\_cmaps\[label\]),
        cax\=ax\_max,
        orientation\="horizontal",
    )
    if label in (0, 1):
        ax\_max.set(xticks\=(), yticks\=())

Copy to clipboard

![Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Class setosa, Class versicolor, Class virginica, Max class, Probability, Probability class 0, Probability class 1, Probability class 2](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_001.png)

Quantitative evaluation[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#quantitative-evaluation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(evaluation\_results).round(2)

Copy to clipboard

|     | name | accuracy | roc\_auc | log\_loss |
| --- | --- | --- | --- | --- |
| 0   | Logistic regression (C=0.1) | 0.83 | 0.92 | 0.71 |
| 1   | Logistic regression (C=100) | 0.81 | 0.93 | 0.36 |
| 2   | Gaussian Process | 0.80 | 0.93 | 0.54 |
| 3   | Logistic regression (RBF features) | 0.77 | 0.93 | 0.40 |
| 4   | Gradient Boosting | 0.83 | 0.92 | 0.40 |
| 5   | Logistic regression (binned features) | 0.81 | 0.92 | 0.48 |
| 6   | Logistic regression (spline features) | 0.79 | 0.92 | 0.42 |

  
  

Analysis[#](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#analysis "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

The two logistic regression models fitted on the original features display linear decision boundaries as expected. For this particular problem, this does not seem to be detrimental as both models are competitive with the non-linear models when quantitatively evaluated on the test set. We can observe that the amount of regularization influences the model confidence: lighter colors for the strongly regularized model with a lower value of `C`. Regularization also impacts the orientation of decision boundary leading to slightly different ROC AUC.

The log-loss on the other hand evaluates both sharpness and calibration and as a result strongly favors the weakly regularized logistic-regression model, probably because the strongly regularized model is under-confident. This could be confirmed by looking at the calibration curve using [`sklearn.calibration.CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
.

The logistic regression model with RBF features has a “blobby” decision boundary that is non-linear in the original feature space and is quite similar to the decision boundary of the Gaussian process classifier which is configured to use an RBF kernel.

The logistic regression model fitted on binned features with interactions has a decision boundary that is non-linear in the original feature space and is quite similar to the decision boundary of the gradient boosting classifier: both models favor axis-aligned decisions when extrapolating to unseen region of the feature space.

The logistic regression model fitted on spline features with interactions has a similar axis-aligned extrapolation behavior but a smoother decision boundary in the dense region of the feature space than the two previous models.

To conclude, it is interesting to observe that feature engineering for logistic regression models can be used to mimic some of the inductive bias of various non-linear models. However, for this particular dataset, using the raw features is enough to train a competitive model. This would not necessarily the case for other datasets.

**Total running time of the script:** (0 minutes 2.328 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_classification_probability.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_classification_probability.ipynb)

[`Download Jupyter notebook: plot_classification_probability.ipynb`](https://scikit-learn.org/stable/_downloads/07960f9087d379e9d0da6350d6ee3f41/plot_classification_probability.ipynb)

[`Download Python source code: plot_classification_probability.py`](https://scikit-learn.org/stable/_downloads/f42d0af747657c8328f34a4238d49800/plot_classification_probability.py)

[`Download zipped: plot_classification_probability.zip`](https://scikit-learn.org/stable/_downloads/9d886125f15994580789a53f5790be5f/plot_classification_probability.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f42d0af747657c8328f34a4238d49800/plot_classification_probability.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/07960f9087d379e9d0da6350d6ee3f41/plot_classification_probability.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/9d886125f15994580789a53f5790be5f/plot_classification_probability.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_classification_probability.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_classification_probability.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)