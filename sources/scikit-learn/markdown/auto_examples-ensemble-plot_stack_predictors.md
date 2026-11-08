[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_stack_predictors.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_stack_predictors.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_stack_predictors.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_stack_predictors.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_stack_predictors.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_stack_predictors.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#sphx-glr-download-auto-examples-ensemble-plot-stack-predictors-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Combine predictors using stacking[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#combine-predictors-using-stacking "Link to this heading")

=================================================================================================================================================================================

Stacking is an [ensemble method](https://scikit-learn.org/stable/modules/ensemble.html#ensemble)
. In this strategy, the out-of-fold predictions from several base estimators are used to train a meta-model that combines their outputs at inference time. Unlike [`VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
, which averages predictions with fixed (optionally user-specified) weights, [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
 learns the combination through its `final_estimator`.

In this example, we illustrate the use case in which different regressors are stacked together and a final regularized linear regressor is used to output the prediction. We compare the performance of each individual regressor with the stacking strategy. Here, stacking slightly improves the overall performance.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate data[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#generate-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

We use synthetic data generated from a sinusoid plus a linear trend with heteroscedastic Gaussian noise. A sudden drop is introduced, as it cannot be described by a linear model, but a tree-based model can naturally deal with it.

import numpy as np
import pandas as pd

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X \= rng.uniform(\-3, 3, size\=500)
trend \= 2.4 \* X
seasonal \= 3.1 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(3.2 \* X)
drop \= 10.0 \* (X \> 2).astype(float)
sigma \= 0.75 + 0.75 \* X\*\*2
y \= trend + seasonal \- drop + rng.normal(loc\=0.0, scale\=[np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(sigma))

df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
({"X": X, "y": y})
\_ \= df.plot.scatter(x\="X", y\="y")

Copy to clipboard

![plot stack predictors](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_001.png)

Stack of predictors on a single data set[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#stack-of-predictors-on-a-single-data-set "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is sometimes not evident which model is more suited for a given task, as different model families can achieve similar performance while exhibiting different strengths and weaknesses. Stacking combines their outputs to exploit these complementary behaviors and can correct systematic errors that no single model can fix on its own. With appropriate regularization in the `final_estimator`, the [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
 often matches the strongest base model, and can outperform it when base learners’ errors are only partially correlated, allowing the combination to reduce individual bias/variance.

Here, we combine 3 learners (linear and non-linear) and use the default [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 regressor to combine their outputs together.

Note

Although some base learners include preprocessing (such as the [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
), the `final_estimator` does not need additional preprocessing when using the default `passthrough=False`, as it receives only the base learners’ predictions. If `passthrough=True`, `final_estimator` should be a pipeline with proper preprocessing.

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
, [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
from sklearn.linear\_model import [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
, [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

linear\_ridge \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
())

spline\_ridge \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(n\_knots\=6, degree\=3),
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(interaction\_only\=True),
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(),
)

hgbt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(random\_state\=0)

estimators \= \[\
    ("Linear Ridge", linear\_ridge),\
    ("Spline Ridge", spline\_ridge),\
    ("HGBT", hgbt),\
\]

stacking\_regressor \= [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
(estimators\=estimators, final\_estimator\=[RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
())
stacking\_regressor

Copy to clipboard

StackingRegressor(estimators=\[('Linear Ridge',\
                               Pipeline(steps=\[('standardscaler',\
                                                StandardScaler()),\
                                               ('ridgecv', RidgeCV())\])),\
                              ('Spline Ridge',\
                               Pipeline(steps=\[('splinetransformer',\
                                                SplineTransformer(n\_knots=6)),\
                                               ('polynomialfeatures',\
                                                PolynomialFeatures(interaction\_only=True)),\
                                               ('ridgecv', RidgeCV())\])),\
                              ('HGBT',\
                               HistGradientBoostingRegressor(random\_state=0))\],
                  final\_estimator=RidgeCV())

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

StackingRegressor

[?Documentation for StackingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimators estimators: list of (str, estimator)  <br>  <br>Base estimators which will be stacked together. Each element of the  <br>list is defined as a tuple of string (i.e. name) and an estimator  <br>instance. An estimator can be set to 'drop' using \`set\_params\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=estimators,-list%20of%20%28str%2C%20estimator%29) | \[('Linear Ridge', ...), ('Spline Ridge', ...), ...\] |
|     | [final\_estimator final\_estimator: estimator, default=None  <br>  <br>A regressor which will be used to combine the base estimators.  <br>The default regressor is a :class:\`~sklearn.linear\_model.RidgeCV\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=final_estimator,-estimator%2C%20default%3DNone) | RidgeCV() |
|     | [cv cv: int, cross-validation generator, iterable, or "prefit", default=None  <br>  <br>Determines the cross-validation splitting strategy used in  <br>\`cross\_val\_predict\` to train \`final\_estimator\`. Possible inputs for  <br>cv are:  <br>  <br>\* None, to use the default 5-fold cross validation,  <br>\* integer, to specify the number of folds in a (Stratified) KFold,  <br>\* An object to be used as a cross-validation generator,  <br>\* An iterable yielding train, test splits,  <br>\* \`"prefit"\`, to assume the \`estimators\` are prefit. In this case, the  <br>estimators will not be refitted.  <br>  <br>For integer/None inputs, if the estimator is a classifier and y is  <br>either binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used.  <br>In all other cases, :class:\`~sklearn.model\_selection.KFold\` is used.  <br>These splitters are instantiated with \`shuffle=False\` so the splits  <br>will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>If "prefit" is passed, it is assumed that all \`estimators\` have  <br>been fitted already. The \`final\_estimator\_\` is trained on the \`estimators\`  <br>predictions on the full training set and are \*\*not\*\* cross validated  <br>predictions. Please note that if the models have been trained on the same  <br>data to train the stacking model, there is a very high risk of overfitting.  <br>  <br>.. versionadded:: 1.1  <br>The 'prefit' option was added in 1.1  <br>  <br>.. note::  <br>A larger number of split will provide no benefits if the number  <br>of training samples is large enough. Indeed, the training time  <br>will increase. \`\`cv\`\` is not used for model evaluation but for  <br>prediction.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=cv,-int%2C%20cross-validation%20generator%2C%20iterable%2C%20or%20%22prefit%22%2C%20default%3DNone) | None |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel for \`fit\` of all \`estimators\`.  <br>\`None\` means 1 unless in a \`joblib.parallel\_backend\` context. -1 means  <br>using all processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [passthrough passthrough: bool, default=False  <br>  <br>When False, only the predictions of estimators will be used as  <br>training data for \`final\_estimator\`. When True, the  <br>\`final\_estimator\` is trained on the predictions as well as the  <br>original training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=passthrough,-bool%2C%20default%3DFalse) | False |
|     | [verbose verbose: int, default=0  <br>  <br>Verbosity level.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.StackingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |

Linear Ridge

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

RidgeCV

[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | (0.1, ...) |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |

Spline Ridge

SplineTransformer

[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 6   |
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | 'uniform' |
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'constant' |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |

PolynomialFeatures

[?Documentation for PolynomialFeatures](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [interaction\_only interaction\_only: bool, default=False  <br>  <br>If \`True\`, only interaction features are produced: features that are  <br>products of at most \`degree\` \*distinct\* input features, i.e. terms with  <br>power of 2 or higher of the same input feature are excluded:  <br>  <br>\- included: \`x\[0\]\`, \`x\[1\]\`, \`x\[0\] \* x\[1\]\`, etc.  <br>\- excluded: \`x\[0\] \*\* 2\`, \`x\[0\] \*\* 2 \* x\[1\]\`, etc.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=interaction_only,-bool%2C%20default%3DFalse) | True |
|     | [degree degree: int or tuple (min\_degree, max\_degree), default=2  <br>  <br>If a single int is given, it specifies the maximal degree of the  <br>polynomial features. If a tuple \`(min\_degree, max\_degree)\` is passed,  <br>then \`min\_degree\` is the minimum and \`max\_degree\` is the maximum  <br>polynomial degree of the generated features. Note that \`min\_degree=0\`  <br>and \`min\_degree=1\` are equivalent as outputting the degree zero term is  <br>determined by \`include\_bias\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=degree,-int%20or%20tuple%20%28min_degree%2C%20max_degree%29%2C%20default%3D2) | 2   |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If \`True\` (default), then include a bias column, the feature in which  <br>all polynomial powers are zero (i.e. a column of ones - acts as an  <br>intercept term in a linear model).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to  <br>compute, but may slow down subsequent estimators.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |

RidgeCV

[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | (0.1, ...) |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |

HGBT

HistGradientBoostingRegressor

[?Documentation for HistGradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [loss loss: {'squared\_error', 'absolute\_error', 'gamma', 'poisson', 'quantile'}, default='squared\_error'  <br>  <br>The loss function to use in the boosting process. Note that the  <br>"squared error", "gamma" and "poisson" losses actually implement  <br>"half least squares loss", "half gamma deviance" and "half poisson  <br>deviance" to simplify the computation of the gradient. Furthermore,  <br>"gamma" and "poisson" losses internally use a log-link, "gamma"  <br>requires \`\`y > 0\`\` and "poisson" requires \`\`y >= 0\`\`.  <br>"quantile" uses the pinball loss.  <br>  <br>.. versionchanged:: 0.23  <br>Added option 'poisson'.  <br>  <br>.. versionchanged:: 1.1  <br>Added option 'quantile'.  <br>  <br>.. versionchanged:: 1.3  <br>Added option 'gamma'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27gamma%27%2C%20%27poisson%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [quantile quantile: float, default=None  <br>  <br>If loss is "quantile", this parameter specifies which quantile to be estimated  <br>and must be between 0 and 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=quantile,-float%2C%20default%3DNone) | None |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\` and  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_categorical.py\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the :ref:\`coefficient of determination <r2\_score>\`  <br>(:math:\`R^2\`) is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores during early  <br>stopping. The higher the tolerance, the more likely we are to early  <br>stop: higher tolerance means that it will be harder for subsequent  <br>iterations to be considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |

final\_estimator

RidgeCV

[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | (0.1, ...) |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |

  
  

Measure and plot the results[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#measure-and-plot-the-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can directly plot the predictions. Indeed, the sudden drop is correctly described by the [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 model (HGBT), but the spline model is smoother and less overfitting. The stacked regressor then turns to be a smoother version of the HGBT.

import matplotlib.pyplot as plt

X \= X.reshape(\-1, 1)
linear\_ridge.fit(X, y)
spline\_ridge.fit(X, y)
hgbt.fit(X, y)
stacking\_regressor.fit(X, y)

x\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X.min() \- 0.1, X.max() + 0.1, 500).reshape(\-1, 1)
preds \= {
    "Linear Ridge": linear\_ridge.predict(x\_plot),
    "Spline Ridge": spline\_ridge.predict(x\_plot),
    "HGBT": hgbt.predict(x\_plot),
    "Stacking (Ridge final estimator)": stacking\_regressor.predict(x\_plot),
}

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(10, 8), sharex\=True, sharey\=True)
axes \= axes.ravel()
for ax, (name, y\_pred) in zip(axes, preds.items()):
    ax.scatter(
        X\[:, 0\],
        y,
        s\=6,
        alpha\=0.35,
        linewidths\=0,
        label\="observed (sample)",
    )

    ax.plot(x\_plot.ravel(), y\_pred, linewidth\=2, alpha\=0.9, label\=name)
    ax.set\_title(name)
    ax.set\_xlabel("x")
    ax.set\_ylabel("y")
    ax.legend(loc\="lower right")

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Base Models Predictions versus Stacked Predictions", y\=1)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Base Models Predictions versus Stacked Predictions, Linear Ridge, Spline Ridge, HGBT, Stacking (Ridge final estimator)](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_002.png)

We can plot the prediction errors as well and evaluate the performance of the individual predictors and the stack of the regressors.

import time

from sklearn.metrics import PredictionErrorDisplay
from sklearn.model\_selection import [cross\_val\_predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
, [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(9, 7))
axs \= [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
(axs)

for ax, (name, est) in zip(
    axs, estimators + \[("Stacking Regressor", stacking\_regressor)\]
):
    scorers \= {r"$R^2$": "r2", "MAE": "neg\_mean\_absolute\_error"}

    start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    scores \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(est, X, y, scoring\=list(scorers.values()), n\_jobs\=-1)
    elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time

    y\_pred \= [cross\_val\_predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
(est, X, y, n\_jobs\=-1)
    scores \= {
        key: (
            f"{np.abs([np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(scores\[f'test\_{value}'\])):.2f}"
            r" $\\pm$ "
            f"{[np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(scores\[f'test\_{value}'\]):.2f}"
        )
        for key, value in scorers.items()
    }

    display \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
        y\_true\=y,
        y\_pred\=y\_pred,
        kind\="actual\_vs\_predicted",
        ax\=ax,
        scatter\_kwargs\={"alpha": 0.2, "color": "tab:blue"},
        line\_kwargs\={"color": "tab:red"},
    )
    ax.set\_title(f"{name}\\nEvaluation in {elapsed\_time:.2f} seconds")

    for name, score in scores.items():
        ax.plot(\[\], \[\], " ", label\=f"{name}: {score}")
    ax.legend(loc\="upper left")

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Prediction Errors of Base versus Stacked Predictors", y\=1)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(top\=0.9)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Prediction Errors of Base versus Stacked Predictors, Linear Ridge Evaluation in 0.02 seconds, Spline Ridge Evaluation in 0.02 seconds, HGBT Evaluation in 0.24 seconds, Stacking Regressor Evaluation in 1.16 seconds](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_003.png)

Even if the scores overlap considerably after cross-validation, the predictions from the stacked regressor are slightly better.

Once fitted, we can inspect the coefficients (or meta-weights) of the trained `final_estimator_` (as long as it is a linear model). They reveal how much the individual estimators contribute to the stacked regressor:

stacking\_regressor.fit(X, y)
stacking\_regressor.final\_estimator\_.coef\_

Copy to clipboard

array(\[-0.00446216,  0.44878552,  0.54762418\])

Copy to clipboard

We see that in this case, the HGBT model dominates, with the spline ridge also contributing meaningfully. The plain linear model does not add useful signal once those two are included; with [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 as the `final_estimator`, it is not dropped, but receives a small negative weight to correct its residual bias.

If we use [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
 as the `final_estimator`, that small, unhelpful contribution is set exactly to zero, yielding a simpler blend of the spline ridge and HGBT models.

from sklearn.linear\_model import [LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

stacking\_regressor \= [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
(estimators\=estimators, final\_estimator\=[LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
())
stacking\_regressor.fit(X, y)
stacking\_regressor.final\_estimator\_.coef\_

Copy to clipboard

array(\[0.        , 0.41148006, 0.56187293\])

Copy to clipboard

How to mimic SuperLearner with scikit-learn[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#how-to-mimic-superlearner-with-scikit-learn "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `SuperLearner` [\[Polley2010\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#polley2010)
 is a stacking strategy implemented as [an R package](https://cran.r-project.org/web/packages/SuperLearner/index.html)
, but not available off-the-shelf in Python. It is closely related to the [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
, as both train the meta-model on out-of-fold predictions from the base estimators.

The key difference is that `SuperLearner` estimates a convex set of meta-weights (non-negative and summing to 1) and omits an intercept; by contrast, [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
 uses an unconstrained meta-learner with an intercept by default (and can optionally include raw features via passthrough).

Without an intercept, the meta-weights are directly interpretable as fractional contributions to the final prediction.

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

linear\_reg \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
(fit\_intercept\=False, positive\=True)
super\_learner\_like \= [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
(
    estimators\=estimators, final\_estimator\=linear\_reg
)
super\_learner\_like.fit(X, y)
super\_learner\_like.final\_estimator\_.coef\_

Copy to clipboard

array(\[2.41599723e-04, 4.48129539e-01, 5.49327451e-01\])

Copy to clipboard

The sum of meta-weights in the stacked regressor is close to 1.0, but not exactly one:

super\_learner\_like.final\_estimator\_.coef\_.sum()

Copy to clipboard

np.float64(0.9976985896404182)

Copy to clipboard

Beyond interpretability, the normalization to 1.0 constraint in the `SuperLearner` presents the following advantages:

*   Consensus-preserving: if all base models output the same value at a point, the ensemble returns that same value (no artificial amplification or attenuation).
    
*   Translation-equivariant: adding a constant to every base prediction shifts the ensemble by the same constant.
    
*   Removes one degree of freedom: avoiding redundancy with a constant term and modestly stabilizing weights under collinearity.
    

The cleanest way to enforce the coefficient normalization with scikit-learn is by defining a custom estimator, but doing so is beyond the scope of this tutorial.

Conclusions[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#conclusions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

The stacked regressor combines the strengths of the different regressors. However, notice that training the stacked regressor is much more computationally expensive than selecting the best performing model.

References

\[[Polley2010](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#id1)\
\]

Polley, E. C. and van der Laan, M. J., [Super Learner In Prediction](https://biostats.bepress.com/cgi/viewcontent.cgi?article=1269&context=ucbbiostat)
, 2010.

**Total running time of the script:** (0 minutes 5.666 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_stack_predictors.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_stack_predictors.ipynb)

[`Download Jupyter notebook: plot_stack_predictors.ipynb`](https://scikit-learn.org/stable/_downloads/3c9b7bcd0b16f172ac12ffad61f3b5f0/plot_stack_predictors.ipynb)

[`Download Python source code: plot_stack_predictors.py`](https://scikit-learn.org/stable/_downloads/c6ccb1a9c5f82321f082e9767a2706f3/plot_stack_predictors.py)

[`Download zipped: plot_stack_predictors.zip`](https://scikit-learn.org/stable/_downloads/bb1a82e9d9265cd75fea1470589796a9/plot_stack_predictors.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)

[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)

Plot individual and voting regression predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)

[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)

Decision Tree Regression with AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)

[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

Polynomial and Spline interpolation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/c6ccb1a9c5f82321f082e9767a2706f3/plot_stack_predictors.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3c9b7bcd0b16f172ac12ffad61f3b5f0/plot_stack_predictors.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bb1a82e9d9265cd75fea1470589796a9/plot_stack_predictors.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_stack_predictors.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_stack_predictors.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)