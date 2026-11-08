[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_diabetes.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_diabetes.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_diabetes.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_diabetes.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_diabetes.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_diabetes.html)

Collapse Sidebar Expand Sidebar

load\_diabetes[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#load-diabetes "Link to this heading")

==============================================================================================================================================

sklearn.datasets.load\_diabetes(_\*_, _return\_X\_y\=False_, _as\_frame\=False_, _scaled\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L1042)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "Link to this definition")

Load and return the diabetes dataset (regression).

|     |     |
| --- | --- |
| Samples total | 442 |
| Dimensionality | 10  |
| Features | real, -.2 < x < .2 |
| Targets | integer 25 - 346 |

Note

The meaning of each feature (i.e. `feature_names`) might be unclear (especially for `ltg`) as the documentation of the original dataset is not explicit. We provide information that seems correct in regard with the scientific literature in this field of research.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)
.

Parameters:

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

Added in version 0.18.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric). The target is a pandas DataFrame or Series depending on the number of target columns. If `return_X_y` is True, then (`data`, `target`) will be pandas DataFrames or Series as described below.

Added in version 0.23.

**scaled**bool, default=True

If True, the feature variables are mean centered and scaled by the standard deviation times the square root of `n_samples`. If False, raw data is returned for the feature variables.

Added in version 1.1.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data{ndarray, dataframe} of shape (442, 10)

The data matrix. If `as_frame=True`, `data` will be a pandas DataFrame.

target: {ndarray, Series} of shape (442,)

The regression target. If `as_frame=True`, `target` will be a pandas Series.

feature\_names: list

The names of the dataset columns.

frame: DataFrame of shape (442, 11)

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

DESCR: str

The full description of the dataset.

data\_filename: str

The path to the location of the data.

target\_filename: str

The path to the location of the target.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarrays. The first contains a 2D ndarray of shape (442, 10) with each row representing one sample and the columns representing the features. The second ndarray of shape (442,) contains the target samples. If `as_frame=True`, both arrays are pandas objects, i.e. `X` a dataframe and `y` a series.

Added in version 0.18.

Examples

\>>> from sklearn.datasets import load\_diabetes
\>>> diabetes \= load\_diabetes()
\>>> diabetes.target\[:3\]
array(\[151.,  75., 141.\])
\>>> diabetes.data.shape
(442, 10)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)

[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)

Plot individual and voting regression predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_thumb.png)

[Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)

Advanced Plotting With Partial Dependence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lars_ic_thumb.png)

[Lasso model selection via information criteria](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html)

Lasso model selection via information criteria

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)