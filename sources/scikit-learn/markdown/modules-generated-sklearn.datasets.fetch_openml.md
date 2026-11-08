[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_openml.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_openml.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_openml.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_openml.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_openml.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_openml.html)

Collapse Sidebar Expand Sidebar

fetch\_openml[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#fetch-openml "Link to this heading")

===========================================================================================================================================

sklearn.datasets.fetch\_openml(_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _\*_, _version: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 \= 'active'_, _data\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _data\_home: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _target\_column: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= 'default-target'_, _cache: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _return\_X\_y: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _as\_frame: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= 'auto'_, _n\_retries: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 \= 3_, _delay: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
 \= 1.0_, _parser: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= 'auto'_, _read\_csv\_kwargs: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_openml.py#L785)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "Link to this definition")

Fetch dataset from openml by name or dataset id.

Datasets are uniquely identified by either an integer ID or by a combination of name and version (i.e. there might be multiple versions of the ‘iris’ dataset). Please give either name or data\_id (not both). In case a name is given, a version can also be provided.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#openml)
.

Added in version 0.20.

Note

EXPERIMENTAL

The API is experimental (particularly the return value structure), and might have small backward-incompatible changes without notice or warning in future releases.

Parameters:

**name**str, default=None

String identifier of the dataset. Note that OpenML can have multiple datasets with the same name.

**version**int or ‘active’, default=’active’

Version of the dataset. Can only be provided if also `name` is given. If ‘active’ the oldest version that’s still active is used. Since there may be more than one active version of a dataset, and those versions may fundamentally be different from one another, setting an exact version is highly recommended.

**data\_id**int, default=None

OpenML ID of the dataset. The most specific way of retrieving a dataset. If data\_id is not given, name (and potential version) are used to obtain a dataset.

**data\_home**str or path-like, default=None

Specify another download and cache folder for the data sets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**target\_column**str, list or None, default=’default-target’

Specify the column name in the data to use as target. If ‘default-target’, the standard target column a stored on the server is used. If `None`, all columns are returned as data and the target is `None`. If list (of strings), all columns with these names are returned as multi-target (Note: not all scikit-learn classifiers can handle all types of multi-output combinations).

**cache**bool, default=True

Whether to cache the downloaded datasets into `data_home`.

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

**as\_frame**bool or ‘auto’, default=’auto’

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric, string or categorical). The target is a pandas DataFrame or Series depending on the number of target\_columns. The Bunch will contain a `frame` attribute with the target and the data. If `return_X_y` is True, then `(data, target)` will be pandas DataFrames or Series as describe above.

If `as_frame` is ‘auto’, the data and target will be converted to DataFrame or Series as if `as_frame` is set to True, unless the dataset is stored in sparse format.

If `as_frame` is False, the data and target will be NumPy arrays and the `data` will only contain numerical values when `parser="liac-arff"` where the categories are provided in the attribute `categories` of the `Bunch` instance. When `parser="pandas"`, no ordinal encoding is made.

Changed in version 0.24: The default value of `as_frame` changed from `False` to `'auto'` in 0.24.

**n\_retries**int, default=3

Number of retries when HTTP errors or network timeouts are encountered. Error with status code 412 won’t be retried as they represent OpenML generic errors.

**delay**float, default=1.0

Number of seconds between retries.

**parser**{“auto”, “pandas”, “liac-arff”}, default=”auto”

Parser used to load the ARFF file. Two parsers are implemented:

*   `"pandas"`: this is the most efficient parser. However, it requires pandas to be installed and can only open dense datasets.
    
*   `"liac-arff"`: this is a pure Python ARFF parser that is much less memory- and CPU-efficient. It deals with sparse ARFF datasets.
    

If `"auto"`, the parser is chosen automatically such that `"liac-arff"` is selected for sparse ARFF datasets, otherwise `"pandas"` is selected.

Added in version 1.2.

Changed in version 1.4: The default value of `parser` changes from `"liac-arff"` to `"auto"`.

**read\_csv\_kwargs**dict, default=None

Keyword arguments passed to [`pandas.read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv "(in pandas v3.0.5)")
 when loading the data from an ARFF file and using the pandas parser. It can allow to overwrite some default parameters.

Added in version 1.3.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datanp.array, scipy.sparse.csr\_matrix of floats, or pandas DataFrame

The feature matrix. Categorical features are encoded as ordinals.

targetnp.array, pandas Series or DataFrame

The regression target or classification labels, if applicable. Dtype is float if numeric, and object if categorical. If `as_frame` is True, `target` is a pandas object.

DESCRstr

The full description of the dataset.

feature\_nameslist

The names of the dataset columns.

target\_names: list

The names of the target columns.

Added in version 0.22.

categoriesdict or None

Maps each categorical feature name to a list of values, such that the value encoded as i is ith in the list. If `as_frame` is True, this is None.

detailsdict

More metadata from OpenML.

framepandas DataFrame

Only present when `as_frame=True`. DataFrame with `data` and `target`.

**(data, target)**tuple if `return_X_y` is True

Note

EXPERIMENTAL

This interface is **experimental** and subsequent releases may change attributes without notice (although there should only be minor changes to `data` and `target`).

Missing values in the ‘data’ are represented as NaN’s. Missing values in ‘target’ are represented as NaN’s (numerical target) or None (categorical target).

Notes

The `"pandas"` and `"liac-arff"` parsers can lead to different data types in the output. The notable differences are the following:

*   The `"liac-arff"` parser always encodes categorical features as `str` objects. To the contrary, the `"pandas"` parser instead infers the type while reading and numerical categories will be casted into integers whenever possible.
    
*   The `"liac-arff"` parser uses float64 to encode numerical features tagged as ‘REAL’ and ‘NUMERICAL’ in the metadata. The `"pandas"` parser instead infers if these numerical features corresponds to integers and uses panda’s Integer extension dtype.
    
*   In particular, classification datasets with integer categories are typically loaded as such `(0, 1, ...)` with the `"pandas"` parser while `"liac-arff"` will force the use of string encoded class labels such as `"0"`, `"1"` and so on.
    
*   The `"pandas"` parser will not strip single quotes - i.e. `'` - from string columns. For instance, a string `'my string'` will be kept as is while the `"liac-arff"` parser will strip the single quotes. For categorical columns, the single quotes are stripped from the values.
    

In addition, when `as_frame=False` is used, the `"liac-arff"` parser returns ordinally encoded data where the categories are provided in the attribute `categories` of the `Bunch` instance. Instead, `"pandas"` returns a NumPy array were the categories are not encoded.

Examples

\>>> from sklearn.datasets import fetch\_openml
\>>> adult \= fetch\_openml("adult", version\=2)
\>>> adult.frame.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 48842 entries, 0 to 48841
Data columns (total 15 columns):
 #   Column          Non-Null Count  Dtype
\---  ------          --------------  -----
 0   age             48842 non-null  int64
 1   workclass       46043 non-null  category
 2   fnlwgt          48842 non-null  int64
 3   education       48842 non-null  category
 4   education-num   48842 non-null  int64
 5   marital-status  48842 non-null  category
 6   occupation      46033 non-null  category
 7   relationship    48842 non-null  category
 8   race            48842 non-null  category
 9   sex             48842 non-null  category
 10  capital-gain    48842 non-null  int64
 11  capital-loss    48842 non-null  int64
 12  hours-per-week  48842 non-null  int64
 13  native-country  47985 non-null  category
 14  class           48842 non-null  category
dtypes: category(9), int64(6)
memory usage: 2.7 MB

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_thumb.png)

[Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_thumb.png)

[Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)

Early stopping of Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mnist_filters_thumb.png)

[Visualization of MLP weights on MNIST](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)

Visualization of MLP weights on MNIST

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)

[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)

Comparing Target Encoder with Other Encoders

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)