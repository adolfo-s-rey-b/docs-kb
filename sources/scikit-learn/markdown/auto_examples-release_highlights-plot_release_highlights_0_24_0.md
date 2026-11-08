[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-0-24-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 0.24[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#release-highlights-for-scikit-learn-0-24 "Link to this heading")

==================================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 0.24! Many bug fixes and improvements were added, as well as some new key features. We detail below a few of the major features of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v0.24.html#release-notes-0-24)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

Successive Halving estimators for tuning hyper-parameters[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#successive-halving-estimators-for-tuning-hyper-parameters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Successive Halving, a state of the art method, is now available to explore the space of the parameters and identify their best combination. [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 and [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
 can be used as drop-in replacement for [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 and [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
. Successive Halving is an iterative selection process illustrated in the figure below. The first iteration is run with a small amount of resources, where the resource typically corresponds to the number of training samples, but can also be an arbitrary integer parameter such as `n_estimators` in a random forest. Only a subset of the parameter candidates are selected for the next iteration, which will be run with an increasing amount of allocated resources. Only a subset of candidates will last until the end of the iteration process, and the best parameter candidate is the one that has the highest score on the last iteration.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#successive-halving-user-guide)
 (note: the Successive Halving estimators are still [experimental](https://scikit-learn.org/stable/glossary.html#term-experimental)
).

[![../../_images/sphx_glr_plot_successive_halving_iterations_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_iterations_001.png)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html)

import numpy as np
from scipy.stats import [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401
from sklearn.model\_selection import [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=700, random\_state\=rng)

clf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=10, random\_state\=rng)

param\_dist \= {
    "max\_depth": \[3, None\],
    "max\_features": [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")
(1, 11),
    "min\_samples\_split": [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")
(2, 11),
    "bootstrap": \[True, False\],
    "criterion": \["gini", "entropy"\],
}

rsh \= [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
(
    estimator\=clf, param\_distributions\=param\_dist, factor\=2, random\_state\=rng
)
rsh.fit(X, y)
rsh.best\_params\_

Copy to clipboard

{'bootstrap': True, 'criterion': 'gini', 'max\_depth': None, 'max\_features': 10, 'min\_samples\_split': 10}

Copy to clipboard

Native support for categorical features in HistGradientBoosting estimators[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#native-support-for-categorical-features-in-histgradientboosting-estimators "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 now have native support for categorical features: they can consider splits on non-ordered, categorical data. Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#categorical-support-gbdt)
.

[![../../_images/sphx_glr_plot_gradient_boosting_categorical_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_001.png)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

The plot shows that the new native support for categorical features leads to fitting times that are comparable to models where the categories are treated as ordered quantities, i.e. simply ordinal-encoded. Native support is also more expressive than both one-hot encoding and ordinal encoding. However, to use the new `categorical_features` parameter, it is still required to preprocess the data within a pipeline as demonstrated in this [example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-categorical-py)
.

Improved performances of HistGradientBoosting estimators[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#improved-performances-of-histgradientboosting-estimators "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The memory footprint of [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 has been significantly improved during calls to `fit`. In addition, histogram initialization is now done in parallel which results in slight speed improvements. See more in the [Benchmark page](https://scikit-learn.org/scikit-learn-benchmarks/)
.

New self-training meta-estimator[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#new-self-training-meta-estimator "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new self-training implementation, based on [Yarowski’s algorithm](https://doi.org/10.3115/981658.981684)
 can now be used with any classifier that implements [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
. The sub-classifier will behave as a semi-supervised classifier, allowing it to learn from unlabeled data. Read more in the [User guide](https://scikit-learn.org/stable/modules/semi_supervised.html#self-training)
.

import numpy as np

from sklearn import datasets
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.semi\_supervised import [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
random\_unlabeled\_points \= rng.rand(iris.target.shape\[0\]) < 0.3
iris.target\[random\_unlabeled\_points\] \= \-1
clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
self\_training\_model \= [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
(clf)
self\_training\_model.fit(iris.data, iris.target)

Copy to clipboard

/home/circleci/project/sklearn/linear\_model/\_logistic.py:599: ConvergenceWarning: lbfgs failed to converge after 100 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max\_iter=100).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear\_model.html#logistic-regression
  n\_iter\_i = \_check\_optimize\_result(
/home/circleci/project/sklearn/linear\_model/\_logistic.py:599: ConvergenceWarning: lbfgs failed to converge after 100 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max\_iter=100).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear\_model.html#logistic-regression
  n\_iter\_i = \_check\_optimize\_result(

Copy to clipboard

SelfTrainingClassifier(estimator=LogisticRegression())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

SelfTrainingClassifier

[?Documentation for SelfTrainingClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>An estimator object implementing \`fit\` and \`predict\_proba\`.  <br>Invoking the \`fit\` method will fit a clone of the passed estimator,  <br>which will be stored in the \`estimator\_\` attribute.  <br>  <br>.. versionadded:: 1.6  <br>\`estimator\` was added to replace \`base\_estimator\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=estimator,-estimator%20object) | LogisticRegression() |
|     | [threshold threshold: float, default=0.75  <br>  <br>The decision threshold for use with \`criterion='threshold'\`.  <br>Should be in \[0, 1). When using the \`'threshold'\` criterion, a  <br>:ref:\`well calibrated classifier <calibration>\` should be used.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=threshold,-float%2C%20default%3D0.75) | 0.75 |\
|     | [criterion criterion: {'threshold', 'k\_best'}, default='threshold'  <br>  <br>The selection criterion used to select which labels to add to the  <br>training set. If \`'threshold'\`, pseudo-labels with prediction  <br>probabilities above \`threshold\` are added to the dataset. If \`'k\_best'\`,  <br>the \`k\_best\` pseudo-labels with highest prediction probabilities are  <br>added to the dataset. When using the 'threshold' criterion, a  <br>:ref:\`well calibrated classifier <calibration>\` should be used.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=criterion,-%7B%27threshold%27%2C%20%27k_best%27%7D%2C%20default%3D%27threshold%27) | 'threshold' |\
|     | [k\_best k\_best: int, default=10  <br>  <br>The amount of samples to add in each iteration. Only used when  <br>\`criterion='k\_best'\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=k_best,-int%2C%20default%3D10) | 10  |\
|     | [max\_iter max\_iter: int or None, default=10  <br>  <br>Maximum number of iterations allowed. Should be greater than or equal  <br>to 0. If it is \`None\`, the classifier will continue to predict labels  <br>until no new pseudo-labels are added, or all unlabeled samples have  <br>been labeled.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=max_iter,-int%20or%20None%2C%20default%3D10) | 10  |\
|     | [verbose verbose: bool, default=False  <br>  <br>Enable verbose output.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray or list of ndarray of shape (n\_classes,)  <br>  <br>Class labels for each output. (Taken from the trained  <br>\`estimator\_\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=classes_,-ndarray%20or%20list%20of%20ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](3,) | \[0,1,2\] |\
| [estimator\_ estimator\_: estimator object  <br>  <br>The fitted estimator.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=estimator_,-estimator%20object) | LogisticRegression | LogisticRegression() |\
| [labeled\_iter\_ labeled\_iter\_: ndarray of shape (n\_samples,)  <br>  <br>The iteration in which each sample was labeled. When a sample has  <br>iteration 0, the sample was already labeled in the original dataset.  <br>When a sample has iteration -1, the sample was not labeled in any  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=labeled_iter_,-ndarray%20of%20shape%20%28n_samples%2C%29) | ndarray\[int64\](150,) | \[0,0,0,...,0,1,1\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=n_features_in_,-int) | int | 4   |\
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of rounds of self-training, that is the number of times the  <br>base estimator is fitted on relabeled variants of the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=n_iter_,-int) | int | 2   |\
| [termination\_condition\_ termination\_condition\_: {'max\_iter', 'no\_change', 'all\_labeled'}  <br>  <br>The reason that fitting was stopped.  <br>  <br>\- \`'max\_iter'\`: \`n\_iter\_\` reached \`max\_iter\`.  <br>\- \`'no\_change'\`: no new labels were predicted.  <br>\- \`'all\_labeled'\`: all unlabeled samples were labeled before \`max\_iter\`  <br>was reached.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=termination_condition_,-%7B%27max_iter%27%2C%20%27no_change%27%2C%20%27all_labeled%27%7D) | str | 'no...ge' |\
| [transduction\_ transduction\_: ndarray of shape (n\_samples,)  <br>  <br>The labels used for the final fit of the classifier, including  <br>pseudo-labels added during fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#:~:text=transduction_,-ndarray%20of%20shape%20%28n_samples%2C%29) | ndarray\[int64\](150,) | \[0,0,0,...,2,2,2\] |\
\
estimator: LogisticRegression\
\
LogisticRegression()\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
  \
  \
\
New SequentialFeatureSelector transformer[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#new-sequentialfeatureselector-transformer "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
A new iterative transformer to select features is available: [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")\
. Sequential Feature Selection can add features one at a time (forward selection) or remove features from the list of the available features (backward selection), based on a cross-validated score maximization. See the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#sequential-feature-selection)\
.\
\
from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")\
from sklearn.feature\_selection import [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")\
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
\
X, y \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")\
(return\_X\_y\=True, as\_frame\=True)\
feature\_names \= X.columns\
knn \= [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
(n\_neighbors\=3)\
sfs \= [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")\
(knn, n\_features\_to\_select\=2)\
sfs.fit(X, y)\
print(\
    "Features selected by forward sequential selection: "\
    f"{feature\_names\[sfs.get\_support()\].tolist()}"\
)\
\
Copy to clipboard\
\
Features selected by forward sequential selection: \['sepal length (cm)', 'petal width (cm)'\]\
\
Copy to clipboard\
\
New PolynomialCountSketch kernel approximation function[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#new-polynomialcountsketch-kernel-approximation-function "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The new [`PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")\
 approximates a polynomial expansion of a feature space when used with linear models, but uses much less memory than [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")\
.\
\
from sklearn.datasets import [fetch\_covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")\
from sklearn.kernel\_approximation import [PolynomialCountSketch](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")\
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")\
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
\
X, y \= [fetch\_covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")\
(return\_X\_y\=True)\
pipe \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(),\
    [PolynomialCountSketch](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")\
(degree\=2, n\_components\=300),\
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=1000),\
)\
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")\
(\
    X, y, train\_size\=5000, test\_size\=10000, random\_state\=42\
)\
pipe.fit(X\_train, y\_train).score(X\_test, y\_test)\
\
Copy to clipboard\
\
0.7365\
\
Copy to clipboard\
\
For comparison, here is the score of a linear baseline for the same data:\
\
linear\_baseline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
([MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=1000))\
linear\_baseline.fit(X\_train, y\_train).score(X\_test, y\_test)\
\
Copy to clipboard\
\
0.7135\
\
Copy to clipboard\
\
Individual Conditional Expectation plots[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#individual-conditional-expectation-plots "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
A new kind of partial dependence plot is available: the Individual Conditional Expectation (ICE) plot. ICE plots visualize the dependence of the prediction on a feature for each sample separately, with one line per sample. See the [User Guide](https://scikit-learn.org/stable/modules/partial_dependence.html#individual-conditional)\
\
from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")\
from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")\
\
\# from sklearn.inspection import plot\_partial\_dependence\
from sklearn.inspection import PartialDependenceDisplay\
\
X, y \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")\
(return\_X\_y\=True, as\_frame\=True)\
features \= \["MedInc", "AveOccup", "HouseAge", "AveRooms"\]\
est \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")\
(n\_estimators\=10)\
est.fit(X, y)\
\
\# plot\_partial\_dependence has been removed in version 1.2. From 1.2, use\
\# PartialDependenceDisplay instead.\
\# display = plot\_partial\_dependence(\
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
(\
    est,\
    X,\
    features,\
    kind\="individual",\
    subsample\=50,\
    n\_jobs\=3,\
    grid\_resolution\=20,\
    random\_state\=0,\
)\
display.figure\_.suptitle(\
    "Partial dependence of house value on non-location features\\n"\
    "for the California housing dataset, with BayesianRidge"\
)\
display.figure\_.subplots\_adjust(hspace\=0.3)\
\
Copy to clipboard\
\
![Partial dependence of house value on non-location features for the California housing dataset, with BayesianRidge](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_001.png)\
\
New Poisson splitting criterion for DecisionTreeRegressor[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#new-poisson-splitting-criterion-for-decisiontreeregressor "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The integration of Poisson regression estimation continues from version 0.23. [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
 now supports a new `'poisson'` splitting criterion. Setting `criterion="poisson"` might be a good choice if your target is a count or a frequency.\
\
import numpy as np\
\
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")\
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
\
n\_samples, n\_features \= 1000, 20\
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
(0)\
X \= rng.randn(n\_samples, n\_features)\
\# positive integer target correlated with X\[:, 5\] with many zeros:\
y \= rng.poisson(lam\=[np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")\
(X\[:, 5\]) / 2)\
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")\
(X, y, random\_state\=rng)\
regressor \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
(criterion\="poisson", random\_state\=0)\
regressor.fit(X\_train, y\_train)\
\
Copy to clipboard\
\
DecisionTreeRegressor(criterion='poisson', random\_state=0)\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
DecisionTreeRegressor\
\
[?Documentation for DecisionTreeRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [criterion criterion: {"squared\_error", "absolute\_error", "poisson"}, default="squared\_error"  <br>  <br>The function to measure the quality of a split. Supported criteria  <br>are "squared\_error" for the mean squared error, which is equal to  <br>variance reduction as feature selection criterion and minimizes the L2  <br>loss using the mean of each terminal node, "absolute\_error" for the mean  <br>absolute error, which minimizes the L1 loss using the median of each terminal  <br>node, and "poisson" which uses reduction in Poisson deviance to find splits,  <br>also using the mean of each terminal node.  <br>  <br>.. versionadded:: 0.18  <br>Mean Absolute Error (MAE) criterion.  <br>  <br>.. versionadded:: 0.24  <br>Poisson deviance criterion.  <br>  <br>.. versionchanged:: 1.9  <br>Criterion \`"friedman\_mse"\` was deprecated.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=criterion,-%7B%22squared_error%22%2C%20%22absolute_error%22%2C%20%22poisson%22%7D%2C%20default%3D%22squared_error%22) | 'poisson' |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of the estimator. The features are always  <br>randomly permuted at each split, even if \`\`splitter\`\` is set to  <br>\`\`"best"\`\`. When \`\`max\_features < n\_features\`\`, the algorithm will  <br>select \`\`max\_features\`\` at random at each split before finding the best  <br>split among them. But the best found split may vary across different  <br>runs, even if \`\`max\_features=n\_features\`\`. That is the case, if the  <br>improvement of the criterion is identical for several splits and one  <br>split has to be selected at random. To obtain a deterministic behaviour  <br>during fitting, \`\`random\_state\`\` has to be fixed to an integer.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [splitter splitter: {"best", "random"}, default="best"  <br>  <br>The strategy used to choose the split at each node. Supported  <br>strategies are "best" to choose the best split and "random" to choose  <br>the best random split among considered features for this split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=splitter,-%7B%22best%22%2C%20%22random%22%7D%2C%20default%3D%22best%22) | 'best' |\
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.  <br>  <br>For an example of how \`\`max\_depth\`\` influences the model, see  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_tree\_regression.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_features max\_features: int, float or {"sqrt", "log2"}, default=None  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>Note: splitting may inspect more than \`\`max\_features\`\` features if  <br>needed to find a valid split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features,-int%2C%20float%20or%20%7B%22sqrt%22%2C%20%22log2%22%7D%2C%20default%3DNone) | None |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow a tree with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multioutput regressions (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the  <br>(normalized) total reduction of the criterion brought  <br>by that feature. It is also known as the Gini importance \[4\]\_.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](20,) | \[0.02,0.02,0.02,...,0.02,0.06,0.02\] |\
| [max\_features\_ max\_features\_: int  <br>  <br>The inferred value of max\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features_,-int) | int | 20  |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_features_in_,-int) | int | 20  |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_outputs_,-int) | int | 1   |\
| [tree\_ tree\_: Tree instance  <br>  <br>The underlying Tree object. Please refer to  <br>\`\`help(sklearn.tree.\_tree.Tree)\`\` for attributes of Tree object and  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_unveil\_tree\_structure.py\`  <br>for basic usage of these attributes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=tree_,-Tree%20instance) | Tree | <sklearn.tree...x7e1de4921d80> |\
\
  \
  \
\
New documentation improvements[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#new-documentation-improvements "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
New examples and documentation pages have been added, in a continuous effort to improve the understanding of machine learning practices:\
\
*   a new section about [common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html#common-pitfalls)\
    ,\
    \
*   an example illustrating how to [statistically compare the performance of models](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#sphx-glr-auto-examples-model-selection-plot-grid-search-stats-py)\
     evaluated using [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
    ,\
    \
*   an example on how to [interpret coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py)\
    ,\
    \
*   an [example](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#sphx-glr-auto-examples-cross-decomposition-plot-pcr-vs-pls-py)\
     comparing Principal Component Regression and Partial Least Squares.\
    \
\
**Total running time of the script:** (0 minutes 12.132 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_0_24_0.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_0_24_0.ipynb)\
\
[`Download Jupyter notebook: plot_release_highlights_0_24_0.ipynb`](https://scikit-learn.org/stable/_downloads/2e6d841155147c9fbce4ea3837b924b9/plot_release_highlights_0_24_0.ipynb)\
\
[`Download Python source code: plot_release_highlights_0_24_0.py`](https://scikit-learn.org/stable/_downloads/d20432c5cccdd8b208184031b83a8cf9/plot_release_highlights_0_24_0.py)\
\
[`Download zipped: plot_release_highlights_0_24_0.zip`](https://scikit-learn.org/stable/_downloads/3d40c54d0288de1437e5299f8039b95a/plot_release_highlights_0_24_0.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)\
\
Release Highlights for scikit-learn 0.23\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)\
\
Release Highlights for scikit-learn 0.22\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)\
\
Release Highlights for scikit-learn 1.0\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)\
\
Release Highlights for scikit-learn 1.2\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/d20432c5cccdd8b208184031b83a8cf9/plot_release_highlights_0_24_0.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2e6d841155147c9fbce4ea3837b924b9/plot_release_highlights_0_24_0.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/3d40c54d0288de1437e5299f8039b95a/plot_release_highlights_0_24_0.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_0_24_0.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_0_24_0.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)