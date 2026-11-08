[Skip to main content](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/calibration/plot_compare_calibration.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/calibration/plot_compare_calibration.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/calibration/plot_compare_calibration.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/calibration/plot_compare_calibration.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/calibration/plot_compare_calibration.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/calibration/plot_compare_calibration.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#sphx-glr-download-auto-examples-calibration-plot-compare-calibration-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of Calibration of Classifiers[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#comparison-of-calibration-of-classifiers "Link to this heading")

=====================================================================================================================================================================================================

Well calibrated classifiers are probabilistic classifiers for which the output of [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 can be directly interpreted as a confidence level. For instance, a well calibrated (binary) classifier should classify the samples such that for the samples to which it gave a [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 value close to 0.8, approximately 80% actually belong to the positive class.

In this example we will compare the calibration of four different models: [Logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
, [Gaussian Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes)
, [Random Forest Classifier](https://scikit-learn.org/stable/modules/ensemble.html#forest)
 and [Linear SVM](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

We will use a synthetic binary classification dataset with 100,000 samples and 20 features. Of the 20 features, only 2 are informative, 2 are redundant (random combinations of the informative features) and the remaining 16 are uninformative (random numbers).

Of the 100,000 samples, 100 will be used for model fitting and the remaining for testing. Note that this split is quite unusual: the goal is to obtain stable calibration curve estimates for models that are potentially prone to overfitting. In practice, one should rather use cross-validation with more balanced splits but this would make the code of this example more complicated to follow.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=100\_000, n\_features\=20, n\_informative\=2, n\_redundant\=2, random\_state\=42
)

train\_samples \= 100  \# Samples used for training the models
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X,
    y,
    shuffle\=False,
    test\_size\=100\_000 \- train\_samples,
)

Copy to clipboard

Calibration curves[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#calibration-curves "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Below, we train each of the four models with the small training dataset, then plot calibration curves (also known as reliability diagrams) using predicted probabilities of the test dataset. Calibration curves are created by binning predicted probabilities, then plotting the mean predicted probability in each bin against the observed frequency (‘fraction of positives’). Below the calibration curve, we plot a histogram showing the distribution of the predicted probabilities or more specifically, the number of samples in each predicted probability bin.

import numpy as np

from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

class NaivelyCalibratedLinearSVC([LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
):
    """LinearSVC with \`predict\_proba\` method that naively scales
    \`decision\_function\` output."""

    def fit(self, X, y):
        super().fit(X, y)
        df \= self.decision\_function(X)
        self.df\_min\_ \= df.min()
        self.df\_max\_ \= df.max()

    def predict\_proba(self, X):
        """Min-max scale output of \`decision\_function\` to \[0,1\]."""
        df \= self.decision\_function(X)
        calibrated\_df \= (df \- self.df\_min\_) / (self.df\_max\_ \- self.df\_min\_)
        proba\_pos\_class \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(calibrated\_df, 0, 1)
        proba\_neg\_class \= 1 \- proba\_pos\_class
        proba \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[proba\_neg\_class, proba\_pos\_class\]
        return proba

Copy to clipboard

from sklearn.calibration import CalibrationDisplay
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.linear\_model import [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
from sklearn.naive\_bayes import [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")

\# Define the classifiers to be compared in the study.
#
\# Note that we use a variant of the logistic regression model that can
\# automatically tune its regularization parameter.
#
\# For a fair comparison, we should run a hyper-parameter search for all the
\# classifiers but we don't do it here for the sake of keeping the example code
\# concise and fast to execute.
lr \= [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
(
    Cs\=[np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-6, 6, 101),
    cv\=10,
    l1\_ratios\=(0,),
    scoring\="neg\_log\_loss",
    max\_iter\=1\_000,
    use\_legacy\_attributes\=False,
)
gnb \= [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
()
svc \= NaivelyCalibratedLinearSVC(C\=1.0)
rfc \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=42)

clf\_list \= \[\
    (lr, "Logistic Regression"),\
    (gnb, "Naive Bayes"),\
    (svc, "SVC"),\
    (rfc, "Random forest"),\
\]

Copy to clipboard

import matplotlib.pyplot as plt
from matplotlib.gridspec import [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
gs \= [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(4, 2)
colors \= [plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
("Dark2")

ax\_calibration\_curve \= fig.add\_subplot(gs\[:2, :2\])
calibration\_displays \= {}
markers \= \["^", "v", "s", "o"\]
for i, (clf, name) in enumerate(clf\_list):
    clf.fit(X\_train, y\_train)
    display \= [CalibrationDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")
(
        clf,
        X\_test,
        y\_test,
        n\_bins\=10,
        name\=name,
        ax\=ax\_calibration\_curve,
        color\=colors(i),
        marker\=markers\[i\],
    )
    calibration\_displays\[name\] \= display

ax\_calibration\_curve.grid()
ax\_calibration\_curve.set\_title("Calibration plots")

\# Add histogram
grid\_positions \= \[(2, 0), (2, 1), (3, 0), (3, 1)\]
for i, (\_, name) in enumerate(clf\_list):
    row, col \= grid\_positions\[i\]
    ax \= fig.add\_subplot(gs\[row, col\])

    ax.hist(
        calibration\_displays\[name\].y\_prob,
        range\=(0, 1),
        bins\=10,
        label\=name,
        color\=colors(i),
    )
    ax.set(title\=name, xlabel\="Mean predicted probability", ylabel\="Count")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Calibration plots, Logistic Regression, Naive Bayes, SVC, Random forest](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_001.png)

Analysis of the results[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#analysis-of-the-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 returns reasonably well calibrated predictions despite the small training set size: its reliability curve is the closest to the diagonal among the four models.

Logistic regression is trained by minimizing the log-loss which is a strictly proper scoring rule: in the limit of infinite training data, strictly proper scoring rules are minimized by the model that predicts the true conditional probabilities. That (hypothetical) model would therefore be perfectly calibrated. However, using a proper scoring rule as training objective is not sufficient to guarantee a well-calibrated model by itself: even with a very large training set, logistic regression could still be poorly calibrated, if it was too strongly regularized or if the choice and preprocessing of input features made this model misspecified (e.g. if the true decision boundary of the dataset is a highly non-linear function of the input features).

In this example the training set was intentionally kept very small. In this setting, optimizing the log-loss can still lead to poorly calibrated models because of overfitting. To mitigate this, the [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 class was configured to tune the `C` regularization parameter to also minimize the log-loss via inner cross-validation so as to find the best compromise for this model in the small training set setting.

Because of the finite training set size and the lack of guarantee for well-specification, we observe that the calibration curve of the logistic regression model is close but not perfectly on the diagonal. The shape of the calibration curve of this model can be interpreted as slightly under-confident: the predicted probabilities are a bit too close to 0.5 compared to the true fraction of positive samples.

The other methods all output less well calibrated probabilities:

*   [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     tends to push probabilities to 0 or 1 (see histogram) on this particular dataset (over-confidence). This is mainly because the naive Bayes equation only provides correct estimate of probabilities when the assumption that features are conditionally independent holds [\[2\]](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#id6)
    . However, features can be correlated and this is the case with this dataset, which contains 2 features generated as random linear combinations of the informative features. These correlated features are effectively being ‘counted twice’, resulting in pushing the predicted probabilities towards 0 and 1 [\[3\]](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#id7)
    . Note, however, that changing the seed used to generate the dataset can lead to widely varying results for the naive Bayes estimator.
    
*   [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     is not a natural probabilistic classifier. In order to interpret its prediction as such, we naively scaled the output of the [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
     into \[0, 1\] by applying min-max scaling in the `NaivelyCalibratedLinearSVC` wrapper class defined above. This estimator shows a typical sigmoid-shaped calibration curve on this data: predictions larger than 0.5 correspond to samples with an even larger effective positive class fraction (above the diagonal), while predictions below 0.5 corresponds to even lower positive class fractions (below the diagonal). This under-confident predictions are typical for maximum-margin methods [\[1\]](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#id5)
    .
    
*   [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    ’s prediction histogram shows peaks at approx. 0.2 and 0.9 probability, while probabilities close to 0 or 1 are very rare. An explanation for this is given by [\[1\]](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#id5)
    : “Methods such as bagging and random forests that average predictions from a base set of models can have difficulty making predictions near 0 and 1 because variance in the underlying base models will bias predictions that should be near zero or one away from these values. Because predictions are restricted to the interval \[0, 1\], errors caused by variance tend to be one-sided near zero and one. For example, if a model should predict p = 0 for a case, the only way bagging can achieve this is if all bagged trees predict zero. If we add noise to the trees that bagging is averaging over, this noise will cause some trees to predict values larger than 0 for this case, thus moving the average prediction of the bagged ensemble away from 0. We observe this effect most strongly with random forests because the base-level trees trained with random forests have relatively high variance due to feature subsetting.” This effect can make random forests under-confident. Despite this possible bias, note that the trees themselves are fit by minimizing either the Gini or Entropy criterion, both of which lead to splits that minimize proper scoring rules: the Brier score or the log-loss respectively. See [the user guide](https://scikit-learn.org/stable/modules/tree.html#tree-mathematical-formulation)
     for more details. This can explain why this model shows a good enough calibration curve on this particular example dataset. Indeed the Random Forest model is not significantly more under-confident than the Logistic Regression model.
    

Feel free to re-run this example with different random seeds and other dataset generation parameters to see how different the calibration plots can look. In general, Logistic Regression and Random Forest will tend to be the best calibrated classifiers, while SVC will often display the typical under-confident miscalibration. The naive Bayes model is also often poorly calibrated but the general shape of its calibration curve can vary widely depending on the dataset.

Finally, note that for some dataset seeds, all models are poorly calibrated, even when tuning the regularization parameter as above. This is bound to happen when the training size is too small or when the model is severely misspecified.

References[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#references "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

**Total running time of the script:** (0 minutes 3.763 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_compare_calibration.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_compare_calibration.ipynb)

[`Download Jupyter notebook: plot_compare_calibration.ipynb`](https://scikit-learn.org/stable/_downloads/757941223692da355c1f7de747af856d/plot_compare_calibration.ipynb)

[`Download Python source code: plot_compare_calibration.py`](https://scikit-learn.org/stable/_downloads/a126bc8be59b9a8c240264570cda0bcb/plot_compare_calibration.py)

[`Download zipped: plot_compare_calibration.zip`](https://scikit-learn.org/stable/_downloads/2216a33072e644eaf7be587530c2726d/plot_compare_calibration.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/a126bc8be59b9a8c240264570cda0bcb/plot_compare_calibration.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/757941223692da355c1f7de747af856d/plot_compare_calibration.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2216a33072e644eaf7be587530c2726d/plot_compare_calibration.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_compare_calibration.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_compare_calibration.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)