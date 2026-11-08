[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.compose.make_column_selector.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.compose.make_column_selector.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.compose.make_column_selector.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.compose.make_column_selector.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.compose.make_column_selector.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.compose.make_column_selector.html)

Collapse Sidebar Expand Sidebar

make\_column\_selector[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#make-column-selector "Link to this heading")

===================================================================================================================================================================

class sklearn.compose.make\_column\_selector(_pattern\=None_, _\*_, _dtype\_include\=None_, _dtype\_exclude\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/compose/_column_transformer.py#L1427)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "Link to this definition")

Create a callable to select columns to be used with [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
.

[`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
 can select columns based on datatype or the columns name with a regex. When using multiple selection criteria, **all** criteria must match for a column to be selected.

For an example of how to use [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
 within a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 to select columns based on data type (i.e. `dtype`), refer to [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
.

Parameters:

**pattern**str, default=None

Name of columns containing this regex pattern will be included. If None, column selection will not be selected based on pattern.

**dtype\_include**column dtype or list of column dtypes, default=None

A selection of dtypes to include. For more details, see [`pandas.DataFrame.select_dtypes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "(in pandas v3.0.5)")
.

**dtype\_exclude**column dtype or list of column dtypes, default=None

A selection of dtypes to exclude. For more details, see [`pandas.DataFrame.select_dtypes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "(in pandas v3.0.5)")
.

Returns:

**selector**callable

Callable for column selection to be used by a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
.

See also

[`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")

Class that allows combining the outputs of multiple transformer objects used on column subsets of the data into a single feature space.

Examples

\>>> from sklearn.preprocessing import StandardScaler, OneHotEncoder
\>>> from sklearn.compose import make\_column\_transformer
\>>> from sklearn.compose import make\_column\_selector
\>>> import numpy as np
\>>> import pandas as pd
\>>> X \= pd.DataFrame({'city': \['London', 'London', 'Paris', 'Sallisaw'\],
...                   'rating': \[5, 3, 4, 5\]})
\>>> ct \= make\_column\_transformer(
...       (StandardScaler(),
...        make\_column\_selector(dtype\_include\=np.number)),  \# rating
...       (OneHotEncoder(),
...        make\_column\_selector(dtype\_include\=\[object, "string"\])))  \# city
\>>> ct.fit\_transform(X)
array(\[\[ 0.90453403,  1.        ,  0.        ,  0.        \],\
       \[-1.50755672,  1.        ,  0.        ,  0.        \],\
       \[-0.30151134,  0.        ,  1.        ,  0.        \],\
       \[ 0.90453403,  0.        ,  0.        ,  1.        \]\])

Copy to clipboard

\_\_call\_\_(_df_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/compose/_column_transformer.py#L1492)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector.__call__ "Link to this definition")

Callable for column selection to be used by a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
.

Parameters:

**df**dataframe of shape (n\_features, n\_samples)

DataFrame to select columns from.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)