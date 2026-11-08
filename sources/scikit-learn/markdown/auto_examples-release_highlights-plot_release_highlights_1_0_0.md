[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-0-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.0[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#release-highlights-for-scikit-learn-1-0 "Link to this heading")

===============================================================================================================================================================================================================

We are very pleased to announce the release of scikit-learn 1.0! The library has been stable for quite some time, releasing version 1.0 is recognizing that and signalling it to our users. This release does not include any breaking changes apart from the usual two-release deprecation cycle. For the future, we do our best to keep this pattern.

This release includes some new key features as well as many improvements and bug fixes. We detail below a few of the major features of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.0.html#release-notes-1-0)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

Keyword and positional arguments[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#keyword-and-positional-arguments "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The scikit-learn API exposes many functions and methods which have many input parameters. For example, before this release, one could instantiate a [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 as:

HistGradientBoostingRegressor("squared\_error", 0.1, 100, 31, None,
    20, 0.0, 255, None, None, False, "auto", "loss", 0.1, 10, 1e-7,
    0, None)

Copy to clipboard

Understanding the above code requires the reader to go to the API documentation and to check each and every parameter for its position and its meaning. To improve the readability of code written based on scikit-learn, now users have to provide most parameters with their names, as keyword arguments, instead of positional arguments. For example, the above code would be:

HistGradientBoostingRegressor(
    loss\="squared\_error",
    learning\_rate\=0.1,
    max\_iter\=100,
    max\_leaf\_nodes\=31,
    max\_depth\=None,
    min\_samples\_leaf\=20,
    l2\_regularization\=0.0,
    max\_bins\=255,
    categorical\_features\=None,
    monotonic\_cst\=None,
    warm\_start\=False,
    early\_stopping\="auto",
    scoring\="loss",
    validation\_fraction\=0.1,
    n\_iter\_no\_change\=10,
    tol\=1e-7,
    verbose\=0,
    random\_state\=None,
)

Copy to clipboard

which is much more readable. Positional arguments have been deprecated since version 0.23 and will now raise a `TypeError`. A limited number of positional arguments are still allowed in some cases, for example in [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, where `PCA(10)` is still allowed, but `PCA(10, False)` is not allowed.

Spline Transformers[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#spline-transformers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

One way to add nonlinear terms to a dataset’s feature set is to generate spline basis functions for continuous/numerical features with the new [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
. Splines are piecewise polynomials, parametrized by their polynomial degree and the positions of the knots. The [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
 implements a B-spline basis.

[![../../_images/sphx_glr_plot_polynomial_interpolation_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

The following code shows splines in action, for more information, please refer to the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#spline-transformer)
.

import numpy as np

from sklearn.preprocessing import [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")

X \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(5).reshape(5, 1)
spline \= [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(degree\=2, n\_knots\=3)
spline.fit\_transform(X)

Copy to clipboard

array(\[\[0.5  , 0.5  , 0.   , 0.   \],\
       \[0.125, 0.75 , 0.125, 0.   \],\
       \[0.   , 0.5  , 0.5  , 0.   \],\
       \[0.   , 0.125, 0.75 , 0.125\],\
       \[0.   , 0.   , 0.5  , 0.5  \]\])

Copy to clipboard

Quantile Regressor[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#quantile-regressor "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Quantile regression estimates the median or other quantiles of y conditional on X, while ordinary least squares (OLS) estimates the conditional mean.

As a linear model, the new [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 gives linear predictions y^(w,X)\=Xw for the q\-th quantile, q∈(0,1). The weights or coefficients w are then found by the following minimization problem:

minw1nsamples∑iPBq(yi−Xiw)+α||w||1.

This consists of the pinball loss (also known as linear loss), see also [`mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
,

PBq(t)\=qmax(t,0)+(1−q)max(−t,0)\={qt,t\>0,0,t\=0,(1−q)t,t<0

and the L1 penalty controlled by parameter `alpha`, similar to [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
.

Please check the following example to see how it works, and the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#quantile-regression)
 for more details.

[![../../_images/sphx_glr_plot_quantile_regression_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_002.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)

Feature Names Support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#feature-names-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When an estimator is passed a [pandas’ dataframe](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)
 during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, the estimator will set a `feature_names_in_` attribute containing the feature names. This is a part of [SLEP007](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep007/proposal.html)
. Note that feature names support is only enabled when the column names in the dataframe are all strings. `feature_names_in_` is used to check that the column names of the dataframe passed in non-[fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, such as [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
, are consistent with features in [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
:

import pandas as pd

from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(\[\[1, 2, 3\], \[4, 5, 6\]\], columns\=\["a", "b", "c"\])
scalar \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().fit(X)
scalar.feature\_names\_in\_

Copy to clipboard

array(\['a', 'b', 'c'\], dtype=object)

Copy to clipboard

The support of [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
 is available for transformers that already had `get_feature_names` and transformers with a one-to-one correspondence between input and output such as [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
. [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
 support will be added to all other transformers in future releases. Additionally, [`compose.ColumnTransformer.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.get_feature_names_out "sklearn.compose.ColumnTransformer.get_feature_names_out")
 is available to combine feature names of its transformers:

import pandas as pd

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

X \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
({"pet": \["dog", "cat", "fish"\], "age": \[3, 7, 1\]})
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("numerical", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), \["age"\]),\
        ("categorical", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(), \["pet"\]),\
    \],
    verbose\_feature\_names\_out\=False,
).fit(X)

preprocessor.get\_feature\_names\_out()

Copy to clipboard

array(\['age', 'pet\_cat', 'pet\_dog', 'pet\_fish'\], dtype=object)

Copy to clipboard

When this `preprocessor` is used with a pipeline, the feature names used by the classifier are obtained by slicing and calling [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
:

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

y \= \[1, 0, 1\]
pipe \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(preprocessor, [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
())
pipe.fit(X, y)
pipe\[:\-1\].get\_feature\_names\_out()

Copy to clipboard

array(\['age', 'pet\_cat', 'pet\_dog', 'pet\_fish'\], dtype=object)

Copy to clipboard

A more flexible plotting API[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#a-more-flexible-plotting-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`metrics.ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
, [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
, [`metrics.DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")
, and [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
 now expose two class methods: `from_estimator` and `from_predictions` which allow users to create a plot given the predictions or an estimator. This means the corresponding `plot_*` functions are deprecated. Please check [example one](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py)
 and [example two](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py)
 for how to use the new plotting functionalities.

Online One-Class SVM[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#online-one-class-svm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The new class [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 implements an online linear version of the One-Class SVM using a stochastic gradient descent. Combined with kernel approximation techniques, [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 can be used to approximate the solution of a kernelized One-Class SVM, implemented in [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
, with a fit time complexity linear in the number of samples. Note that the complexity of a kernelized One-Class SVM is at best quadratic in the number of samples. [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 is thus well suited for datasets with a large number of training samples (> 10,000) for which the SGD variant can be several orders of magnitude faster. Please check this [example](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html#sphx-glr-auto-examples-miscellaneous-plot-anomaly-comparison-py)
 to see how it’s used, and the [User Guide](https://scikit-learn.org/stable/modules/sgd.html#sgd-online-one-class-svm)
 for more details.

[![../../_images/sphx_glr_plot_anomaly_comparison_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Histogram-based Gradient Boosting Models are now stable[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#histogram-based-gradient-boosting-models-are-now-stable "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 and [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 are no longer experimental and can simply be imported and used as:

from sklearn.ensemble import HistGradientBoostingClassifier

Copy to clipboard

New documentation improvements[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#new-documentation-improvements "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This release includes many documentation improvements. Out of over 2100 merged pull requests, about 800 of them are improvements to our documentation.

**Total running time of the script:** (0 minutes 0.018 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_0_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_0_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_1_0_0.ipynb`](https://scikit-learn.org/stable/_downloads/f2677dfc7ce435a13dbd8d5fc7298413/plot_release_highlights_1_0_0.ipynb)

[`Download Python source code: plot_release_highlights_1_0_0.py`](https://scikit-learn.org/stable/_downloads/7be24b5c175982744260a2ced8398a5a/plot_release_highlights_1_0_0.py)

[`Download zipped: plot_release_highlights_1_0_0.zip`](https://scikit-learn.org/stable/_downloads/b64609eaa844207d7f926823a464efd3/plot_release_highlights_1_0_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/7be24b5c175982744260a2ced8398a5a/plot_release_highlights_1_0_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f2677dfc7ce435a13dbd8d5fc7298413/plot_release_highlights_1_0_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b64609eaa844207d7f926823a464efd3/plot_release_highlights_1_0_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_0_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_0_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)