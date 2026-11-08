[Skip to main content](https://scikit-learn.org/stable/api/sklearn.compose.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.compose.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.compose.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.compose.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.compose.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.compose.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.compose.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.compose.html)

Collapse Sidebar Expand Sidebar

sklearn.compose[#](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "Link to this heading")

===========================================================================================================================

Meta-estimators for building composite models with transformers.

In addition to its current contents, this module will eventually be home to refurbished versions of [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 and [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
.

**User guide.** See the [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html#combining-estimators)
 section for further details.

|     |     |
| --- | --- |
| [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer") | Applies transformers to columns of an array or pandas DataFrame. |
| [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor") | Meta-estimator to regress on a transformed target. |
| [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector") | Create a callable to select columns to be used with [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")<br>. |
| [`make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer") | Construct a ColumnTransformer from the given transformers. |