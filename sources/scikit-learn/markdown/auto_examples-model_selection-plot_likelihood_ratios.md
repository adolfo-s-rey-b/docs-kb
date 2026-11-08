[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_likelihood_ratios.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_likelihood_ratios.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#sphx-glr-download-auto-examples-model-selection-plot-likelihood-ratios-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Class Likelihood Ratios to measure classification performance[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#class-likelihood-ratios-to-measure-classification-performance "Link to this heading")

=================================================================================================================================================================================================================================================

This example demonstrates the [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
 function, which computes the positive and negative likelihood ratios (`LR+`, `LR-`) to assess the predictive power of a binary classifier. As we will see, these metrics are independent of the proportion between classes in the test set, which makes them very useful when the available data for a study has a different class proportion than the target application.

A typical use is a case-control study in medicine, which has nearly balanced classes while the general population has large class imbalance. In such application, the pre-test probability of an individual having the target condition can be chosen to be the prevalence, i.e. the proportion of a particular population found to be affected by a medical condition. The post-test probabilities represent then the probability that the condition is truly present given a positive test result.

In this example we first discuss the link between pre-test and post-test odds given by the [Class likelihood ratios](https://scikit-learn.org/stable/modules/model_evaluation.html#class-likelihood-ratios)
. Then we evaluate their behavior in some controlled scenarios. In the last section we plot them as a function of the prevalence of the positive class.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Pre-test vs. post-test analysis[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#pre-test-vs-post-test-analysis "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Suppose we have a population of subjects with physiological measurements `X` that can hopefully serve as indirect bio-markers of the disease and actual disease indicators `y` (ground truth). Most of the people in the population do not carry the disease but a minority (in this case around 10%) does:

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=10\_000, weights\=\[0.9, 0.1\], random\_state\=0)
print(f"Percentage of people carrying the disease: {100 \* y.mean():.2f}%")

Copy to clipboard

Percentage of people carrying the disease: 10.37%

Copy to clipboard

A machine learning model is built to diagnose if a person with some given physiological measurements is likely to carry the disease of interest. To evaluate the model, we need to assess its performance on a held-out test set:

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

Copy to clipboard

Then we can fit our diagnosis model and compute the positive likelihood ratio to evaluate the usefulness of this classifier as a disease diagnosis tool:

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import [class\_likelihood\_ratios](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")

estimator \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
().fit(X\_train, y\_train)
y\_pred \= estimator.predict(X\_test)
pos\_LR, neg\_LR \= [class\_likelihood\_ratios](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
(y\_test, y\_pred, replace\_undefined\_by\=1.0)
print(f"LR+: {pos\_LR:.3f}")

Copy to clipboard

LR+: 12.617

Copy to clipboard

Since the positive class likelihood ratio is much larger than 1.0, it means that the machine learning-based diagnosis tool is useful: the post-test odds that the condition is truly present given a positive test result are more than 12 times larger than the pre-test odds.

Cross-validation of likelihood ratios[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#cross-validation-of-likelihood-ratios "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We assess the variability of the measurements for the class likelihood ratios in some particular cases.

import pandas as pd

def scoring(estimator, X, y):
    y\_pred \= estimator.predict(X)
    pos\_lr, neg\_lr \= [class\_likelihood\_ratios](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
(y, y\_pred, replace\_undefined\_by\=1.0)
    return {"positive\_likelihood\_ratio": pos\_lr, "negative\_likelihood\_ratio": neg\_lr}

def extract\_score(cv\_results):
    lr \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
        {
            "positive": cv\_results\["test\_positive\_likelihood\_ratio"\],
            "negative": cv\_results\["test\_negative\_likelihood\_ratio"\],
        }
    )
    return lr.aggregate(\["mean", "std"\])

Copy to clipboard

We first validate the [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 model with default hyperparameters as used in the previous section.

from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

estimator \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
extract\_score([cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(estimator, X, y, scoring\=scoring, cv\=10))

Copy to clipboard

|     | positive | negative |
| --- | --- | --- |
| mean | 16.661086 | 0.724702 |
| std | 4.383973 | 0.054045 |

  
  

We confirm that the model is useful: the post-test odds are between 12 and 20 times larger than the pre-test odds.

On the contrary, let’s consider a dummy model that will output random predictions with similar odds as the average disease prevalence in the training set:

from sklearn.dummy import [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")

estimator \= [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
(strategy\="stratified", random\_state\=1234)
extract\_score([cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(estimator, X, y, scoring\=scoring, cv\=10))

Copy to clipboard

|     | positive | negative |
| --- | --- | --- |
| mean | 1.108843 | 0.986989 |
| std | 0.268147 | 0.034278 |

  
  

Here both class likelihood ratios are compatible with 1.0 which makes this classifier useless as a diagnostic tool to improve disease detection.

Another option for the dummy model is to always predict the most frequent class, which in this case is “no-disease”.

estimator \= [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
(strategy\="most\_frequent")
extract\_score([cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(estimator, X, y, scoring\=scoring, cv\=10))

Copy to clipboard

/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: No samples were predicted for the positive class and \`positive\_likelihood\_ratio\` is set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)

Copy to clipboard

|     | positive | negative |
| --- | --- | --- |
| mean | 1.0 | 1.0 |
| std | 0.0 | 0.0 |

  
  

The absence of positive predictions means there will be no true positives nor false positives, leading to an undefined `LR+` that by no means should be interpreted as an infinite `LR+` (the classifier perfectly identifying positive cases). In such situation the [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
 function returns `nan` and raises a warning by default. Indeed, the value of `LR-` helps us discard this model.

A similar scenario may arise when cross-validating highly imbalanced data with few samples: some folds will have no samples with the disease and therefore they will output no true positives nor false negatives when used for testing. Mathematically this leads to an infinite `LR+`, which should also not be interpreted as the model perfectly identifying positive cases. Such event leads to a higher variance of the estimated likelihood ratios, but can still be interpreted as an increment of the post-test odds of having the condition.

estimator \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=300, weights\=\[0.9, 0.1\], random\_state\=0)
extract\_score([cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(estimator, X, y, scoring\=scoring, cv\=10))

Copy to clipboard

/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: \`positive\_likelihood\_ratio\` is ill-defined and set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: \`positive\_likelihood\_ratio\` is ill-defined and set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: \`positive\_likelihood\_ratio\` is ill-defined and set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: \`positive\_likelihood\_ratio\` is ill-defined and set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)
/home/circleci/project/sklearn/utils/\_param\_validation.py:218: UndefinedMetricWarning: \`positive\_likelihood\_ratio\` is ill-defined and set to \`np.nan\`. Use the \`replace\_undefined\_by\` param to
  return func(\*args, \*\*kwargs)

Copy to clipboard

|     | positive | negative |
| --- | --- | --- |
| mean | 9.400000 | 0.373333 |
| std | 10.532489 | 0.235430 |

  
  

Invariance with respect to prevalence[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html#invariance-with-respect-to-prevalence "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The likelihood ratios are independent of the disease prevalence and can be extrapolated between populations regardless of any possible class imbalance, **as long as the same model is applied to all of them**. Notice that in the plots below **the decision boundary is constant** (see [SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-unbalanced-py)
 for a study of the boundary decision for unbalanced classes).

Here we train a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 base model on a case-control study with a prevalence of 50%. It is then evaluated over populations with varying prevalence. We use the [`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
 function to ensure the data-generating process is always the same as shown in the plots below. The label `1` corresponds to the positive class “disease”, whereas the label `0` stands for “no-disease”.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

import matplotlib.pyplot as plt
import numpy as np

from sklearn.inspection import DecisionBoundaryDisplay

populations \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
common\_params \= {
    "n\_samples": 10\_000,
    "n\_features": 2,
    "n\_informative": 2,
    "n\_redundant": 0,
    "random\_state": 0,
}
weights \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 0.8, 6)
weights \= weights\[::\-1\]

\# fit and evaluate base model on balanced classes
X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(\*\*common\_params, weights\=\[0.5, 0.5\])
estimator \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
().fit(X, y)
lr\_base \= extract\_score([cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(estimator, X, y, scoring\=scoring, cv\=10))
pos\_lr\_base, pos\_lr\_base\_std \= lr\_base\["positive"\].values
neg\_lr\_base, neg\_lr\_base\_std \= lr\_base\["negative"\].values

Copy to clipboard

We will now show the decision boundary for each level of prevalence. Note that we only plot a subset of the original data to better assess the linear model decision boundary.

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, ncols\=2, figsize\=(15, 12))

for ax, (n, weight) in zip(axs.ravel(), enumerate(weights)):
    X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
        \*\*common\_params,
        weights\=\[weight, 1 \- weight\],
    )
    prevalence \= y.mean()
    populations\["prevalence"\].append(prevalence)
    populations\["X"\].append(X)
    populations\["y"\].append(y)

    \# down-sample for plotting
    rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
    plot\_indices \= rng.choice([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[0\]), size\=500, replace\=True)
    X\_plot, y\_plot \= X\[plot\_indices\], y\[plot\_indices\]

    \# plot fixed decision boundary of base model with varying prevalence
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        estimator,
        X\_plot,
        response\_method\="predict",
        alpha\=0.5,
        ax\=ax,
    )
    scatter \= disp.ax\_.scatter(X\_plot\[:, 0\], X\_plot\[:, 1\], c\=y\_plot, edgecolor\="k")
    disp.ax\_.set\_title(f"prevalence = {y\_plot.mean():.2f}")
    disp.ax\_.legend(\*scatter.legend\_elements())

Copy to clipboard

![prevalence = 0.22, prevalence = 0.34, prevalence = 0.45, prevalence = 0.60, prevalence = 0.76, prevalence = 0.88](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_001.png)

We define a function for bootstrapping.

def scoring\_on\_bootstrap(estimator, X, y, rng, n\_bootstrap\=100):
    results\_for\_prevalence \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
    for \_ in range(n\_bootstrap):
        bootstrap\_indices \= rng.choice(
            [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[0\]), size\=X.shape\[0\], replace\=True
        )
        for key, value in scoring(
            estimator, X\[bootstrap\_indices\], y\[bootstrap\_indices\]
        ).items():
            results\_for\_prevalence\[key\].append(value)
    return [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results\_for\_prevalence)

Copy to clipboard

We score the base model for each prevalence using bootstrapping.

results \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
n\_bootstrap \= 100
rng \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(seed\=0)

for prevalence, X, y in zip(
    populations\["prevalence"\], populations\["X"\], populations\["y"\]
):
    results\_for\_prevalence \= scoring\_on\_bootstrap(
        estimator, X, y, rng, n\_bootstrap\=n\_bootstrap
    )
    results\["prevalence"\].append(prevalence)
    results\["metrics"\].append(
        results\_for\_prevalence.aggregate(\["mean", "std"\]).unstack()
    )

results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results\["metrics"\], index\=results\["prevalence"\])
results.index.name \= "prevalence"
results

Copy to clipboard

|     | positive\_likelihood\_ratio |     | negative\_likelihood\_ratio |     |
| --- | --- | --- | --- | --- |
|     | mean | std | mean | std |
| --- | --- | --- | --- | --- |
| prevalence |     |     |     |     |
| --- | --- | --- | --- | --- |
| 0.2039 | 4.507943 | 0.113516 | 0.207667 | 0.009778 |
| 0.3419 | 4.443238 | 0.125140 | 0.198766 | 0.008915 |
| 0.4809 | 4.421087 | 0.123828 | 0.192913 | 0.006360 |
| 0.6196 | 4.409717 | 0.164009 | 0.193949 | 0.005861 |
| 0.7578 | 4.334795 | 0.175298 | 0.189267 | 0.005840 |
| 0.8963 | 4.197666 | 0.238955 | 0.185654 | 0.005027 |

  
  

In the plots below we observe that the class likelihood ratios re-computed with different prevalences are indeed constant within one standard deviation of those computed with on balanced classes.

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(15, 6))
results\["positive\_likelihood\_ratio"\]\["mean"\].plot(
    ax\=ax1, color\="r", label\="extrapolation through populations"
)
ax1.axhline(y\=pos\_lr\_base + pos\_lr\_base\_std, color\="r", linestyle\="--")
ax1.axhline(
    y\=pos\_lr\_base \- pos\_lr\_base\_std,
    color\="r",
    linestyle\="--",
    label\="base model confidence band",
)
ax1.fill\_between(
    results.index,
    results\["positive\_likelihood\_ratio"\]\["mean"\]
    \- results\["positive\_likelihood\_ratio"\]\["std"\],
    results\["positive\_likelihood\_ratio"\]\["mean"\]
    + results\["positive\_likelihood\_ratio"\]\["std"\],
    color\="r",
    alpha\=0.3,
)
ax1.set(
    title\="Positive likelihood ratio",
    ylabel\="LR+",
    ylim\=\[0, 5\],
)
ax1.legend(loc\="lower right")

ax2 \= results\["negative\_likelihood\_ratio"\]\["mean"\].plot(
    ax\=ax2, color\="b", label\="extrapolation through populations"
)
ax2.axhline(y\=neg\_lr\_base + neg\_lr\_base\_std, color\="b", linestyle\="--")
ax2.axhline(
    y\=neg\_lr\_base \- neg\_lr\_base\_std,
    color\="b",
    linestyle\="--",
    label\="base model confidence band",
)
ax2.fill\_between(
    results.index,
    results\["negative\_likelihood\_ratio"\]\["mean"\]
    \- results\["negative\_likelihood\_ratio"\]\["std"\],
    results\["negative\_likelihood\_ratio"\]\["mean"\]
    + results\["negative\_likelihood\_ratio"\]\["std"\],
    color\="b",
    alpha\=0.3,
)
ax2.set(
    title\="Negative likelihood ratio",
    ylabel\="LR-",
    ylim\=\[0, 0.5\],
)
ax2.legend(loc\="lower right")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Positive likelihood ratio, Negative likelihood ratio](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_002.png)

**Total running time of the script:** (0 minutes 3.290 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_likelihood_ratios.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_likelihood_ratios.ipynb)

[`Download Jupyter notebook: plot_likelihood_ratios.ipynb`](https://scikit-learn.org/stable/_downloads/a396baaf1f191c4fd27c35ae5b37420c/plot_likelihood_ratios.ipynb)

[`Download Python source code: plot_likelihood_ratios.py`](https://scikit-learn.org/stable/_downloads/883c6b4b0cc369a10ddb336c09a9e4dd/plot_likelihood_ratios.py)

[`Download zipped: plot_likelihood_ratios.zip`](https://scikit-learn.org/stable/_downloads/248a4cae89eb02703d4ab8c58361c523/plot_likelihood_ratios.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)

[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

SVM: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/883c6b4b0cc369a10ddb336c09a9e4dd/plot_likelihood_ratios.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a396baaf1f191c4fd27c35ae5b37420c/plot_likelihood_ratios.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/248a4cae89eb02703d4ab8c58361c523/plot_likelihood_ratios.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_likelihood_ratios.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_likelihood_ratios.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)