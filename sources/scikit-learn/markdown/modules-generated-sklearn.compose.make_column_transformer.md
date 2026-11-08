[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.compose.make_column_transformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.compose.make_column_transformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.compose.make_column_transformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.compose.make_column_transformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.compose.make_column_transformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.compose.make_column_transformer.html)

Collapse Sidebar Expand Sidebar

make\_column\_transformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#make-column-transformer "Link to this heading")

============================================================================================================================================================================

sklearn.compose.make\_column\_transformer(_\*transformers_, _remainder\='drop'_, _sparse\_threshold\=0.3_, _n\_jobs\=None_, _verbose\=False_, _verbose\_feature\_names\_out\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/compose/_column_transformer.py#L1312)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "Link to this definition")

Construct a ColumnTransformer from the given transformers.

This is a shorthand for the ColumnTransformer constructor; it does not require, and does not permit, naming the transformers. Instead, they will be given names automatically based on their types. It also does not allow weighting with `transformer_weights`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/compose.html#make-column-transformer)
.

Parameters:

**\*transformers**tuples

Tuples of the form (transformer, columns) specifying the transformer objects to be applied to subsets of the data.

transformer{‘drop’, ‘passthrough’} or estimator

Estimator must support [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
. Special-cased strings ‘drop’ and ‘passthrough’ are accepted as well, to indicate to drop the columns or to pass them through untransformed, respectively.

columnsstr, array-like of str, int, array-like of int, slice, array-like of bool or callable

Indexes the data on its second axis. Integers are interpreted as positional columns, while strings can reference DataFrame columns by name. A scalar string or int should be used where `transformer` expects X to be a 1d array-like (vector), otherwise a 2d array will be passed to the transformer. A callable is passed the input data `X` and can return any of the above. To select multiple columns by name or dtype, you can use [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
.

**remainder**{‘drop’, ‘passthrough’} or estimator, default=’drop’

By default, only the specified columns in `transformers` are transformed and combined in the output, and the non-specified columns are dropped. (default of `'drop'`). By specifying `remainder='passthrough'`, all remaining columns that were not specified in `transformers` will be automatically passed through. This subset of columns is concatenated with the output of the transformers. By setting `remainder` to be an estimator, the remaining non-specified columns will use the `remainder` estimator. The estimator must support [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
.

**sparse\_threshold**float, default=0.3

If the transformed output consists of a mix of sparse and dense data, it will be stacked as a sparse matrix if the density is lower than this value. Use `sparse_threshold=0` to always return dense. When the transformed output consists of all sparse or all dense data, the stacked result will be sparse or dense, respectively, and this keyword will be ignored.

**n\_jobs**int, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**bool, default=False

If True, the time elapsed while fitting each transformer will be printed as it is completed.

**verbose\_feature\_names\_out**bool, default=True

If True, [`ColumnTransformer.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.get_feature_names_out "sklearn.compose.ColumnTransformer.get_feature_names_out")
 will prefix all feature names with the name of the transformer that generated that feature. If False, [`ColumnTransformer.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.get_feature_names_out "sklearn.compose.ColumnTransformer.get_feature_names_out")
 will not prefix any feature names and will error if feature names are not unique.

Added in version 1.0.

Returns:

**ct**ColumnTransformer

Returns a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 object.

See also

[`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")

Class that allows combining the outputs of multiple transformer objects used on column subsets of the data into a single feature space.

Examples

\>>> from sklearn.preprocessing import StandardScaler, OneHotEncoder
\>>> from sklearn.compose import make\_column\_transformer
\>>> make\_column\_transformer(
...     (StandardScaler(), \['numerical\_column'\]),
...     (OneHotEncoder(), \['categorical\_column'\]))
ColumnTransformer(transformers=\[('standardscaler', StandardScaler(...),\
                                 \['numerical\_column'\]),\
                                ('onehotencoder', OneHotEncoder(...),\
                                 \['categorical\_column'\])\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)

[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)

Displaying estimators and complex pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)