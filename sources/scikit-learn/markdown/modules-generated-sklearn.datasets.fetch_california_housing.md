[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_california_housing.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_california_housing.html)

Collapse Sidebar Expand Sidebar

fetch\_california\_housing[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#fetch-california-housing "Link to this heading")

================================================================================================================================================================================

sklearn.datasets.fetch\_california\_housing(_\*_, _data\_home\=None_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _as\_frame\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_california_housing.py#L56)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "Link to this definition")

Load the California housing dataset (regression).

|     |     |
| --- | --- |
| Samples total | 20640 |
| Dimensionality | 8   |
| Features | real |
| Target | real 0.15 - 5. |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(data.data, data.target)` instead of a Bunch object.

Added in version 0.20.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric, string or categorical). The target is a pandas DataFrame or Series depending on the number of target\_columns.

Added in version 0.23.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**dataset**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datandarray, shape (20640, 8)

Each row corresponding to the 8 feature values in order. If `as_frame` is True, `data` is a pandas object.

targetnumpy array of shape (20640,)

Each value corresponds to the median house value in units of 100,000. If `as_frame` is True, `target` is a pandas object.

feature\_nameslist of length 8

Array of ordered feature names used in the dataset.

DESCRstr

Description of the California housing dataset.

framepandas DataFrame

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarray. The first containing a 2D array of shape (n\_samples, n\_features) with each row representing one sample and each column representing the features. The second ndarray of shape (n\_samples,) containing the target samples.

Added in version 0.20.

Notes

This dataset consists of 20,640 samples and 9 features.

Examples

\>>> from sklearn.datasets import fetch\_california\_housing
\>>> housing \= fetch\_california\_housing()
\>>> print(housing.data.shape, housing.target.shape)
(20640, 8) (20640,)
\>>> print(housing.feature\_names\[0:6\])
\['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup'\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)