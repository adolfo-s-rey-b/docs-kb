[Skip to main content](https://scikit-learn.org/stable/api/sklearn.pipeline.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.pipeline.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.pipeline.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.pipeline.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.pipeline.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.pipeline.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.pipeline.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.pipeline.html)

Collapse Sidebar Expand Sidebar

sklearn.pipeline[#](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "Link to this heading")

==============================================================================================================================

Utilities to build a composite estimator as a chain of transforms and estimators.

**User guide.** See the [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html#combining-estimators)
 section for further details.

|     |     |
| --- | --- |
| [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion") | Concatenates results of multiple transformer objects. |
| [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") | A sequence of data transformers with an optional final predictor. |
| [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline") | Construct a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")<br> from the given estimators. |
| [`make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union") | Construct a [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")<br> from the given transformers. |