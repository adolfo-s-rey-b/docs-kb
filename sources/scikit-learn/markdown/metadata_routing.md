[Skip to main content](https://scikit-learn.org/stable/metadata_routing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/metadata_routing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/metadata_routing.html)
[1.8.0](https://scikit-learn.org/1.8/metadata_routing.html)
[1.7.2](https://scikit-learn.org/1.7/metadata_routing.html)
[1.6.1](https://scikit-learn.org/1.6/metadata_routing.html)
[1.5.2](https://scikit-learn.org/1.5/metadata_routing.html)
[1.4.2](https://scikit-learn.org/1.4/metadata_routing.html)

Collapse Sidebar Expand Sidebar

4\. Metadata Routing[#](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing "Link to this heading")

=======================================================================================================================

Note

The Metadata Routing API is experimental, and is not yet implemented for all estimators. Please refer to the [list of supported and unsupported models](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing-models)
 for more information. It may change without the usual deprecation cycle. By default this feature is not enabled. You can enable it by setting the `enable_metadata_routing` flag to `True`:

\>>> import sklearn
\>>> sklearn.set\_config(enable\_metadata\_routing\=True)

Copy to clipboard

Note that the methods and requirements introduced in this document are only relevant if you want to pass [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
 (e.g. `sample_weight`) to a method. If you’re only passing `X` and `y` and no other parameter / metadata to methods such as [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
, etc., then you don’t need to set anything.

This guide demonstrates how [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
 can be routed and passed between objects in scikit-learn. If you are developing a scikit-learn compatible estimator or meta-estimator, you can check our related developer guide: [Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

Metadata is data that an estimator, scorer, or CV splitter takes into account if the user explicitly passes it as a parameter. For instance, [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 accepts `sample_weight` in its `fit()` method and considers it to calculate its centroids. `classes` are consumed by some classifiers and `groups` are used in some splitters, but any data that is passed into an object’s methods apart from X and y can be considered as metadata. Prior to scikit-learn version 1.3, there was no single API for passing metadata like that if these objects were used in conjunction with other objects, e.g. a scorer accepting `sample_weight` inside a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
.

With the Metadata Routing API, we can transfer metadata to estimators, scorers, and CV splitters using [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
 (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 or [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
) or functions such as [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 which route data to other objects. In order to pass metadata to a method like `fit` or `score`, the object consuming the metadata, must _request_ it. This is done via `set_{method}_request()` methods, where `{method}` is substituted by the name of the method that requests the metadata. For instance, estimators that use the metadata in their `fit()` method would use `set_fit_request()`, and scorers would use `set_score_request()`. These methods allow us to specify which metadata to request, for instance `set_fit_request(sample_weight=True)`.

For grouped splitters such as [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
, a `groups` parameter is requested by default. This is best demonstrated by the following examples.

4.1. Usage Examples[#](https://scikit-learn.org/stable/metadata_routing.html#usage-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Here we present a few examples to show some common use-cases. Our goal is to pass `sample_weight` and `groups` through [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
, which routes the metadata to [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 and to a custom scorer made with [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
, both of which _can_ use the metadata in their methods. In these examples we want to individually set whether to use the metadata within the different [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
.

The examples in this section require the following imports and data:

\>>> import numpy as np
\>>> from sklearn.metrics import make\_scorer, accuracy\_score
\>>> from sklearn.linear\_model import LogisticRegressionCV, LogisticRegression
\>>> from sklearn.model\_selection import cross\_validate, GridSearchCV, GroupKFold
\>>> from sklearn.feature\_selection import SelectKBest
\>>> from sklearn.pipeline import make\_pipeline
\>>> n\_samples, n\_features \= 100, 4
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.rand(n\_samples, n\_features)
\>>> y \= rng.randint(0, 2, size\=n\_samples)
\>>> my\_groups \= rng.randint(0, 10, size\=n\_samples)
\>>> my\_weights \= rng.rand(n\_samples)
\>>> my\_other\_weights \= rng.rand(n\_samples)

Copy to clipboard

### 4.1.1. Weighted scoring and fitting[#](https://scikit-learn.org/stable/metadata_routing.html#weighted-scoring-and-fitting "Link to this heading")

The splitter used internally in [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
, [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
, requests `groups` by default. However, we need to explicitly request `sample_weight` for it and for our custom scorer by specifying `sample_weight=True` in [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
’s `set_fit_request()` method and in [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
’s `set_score_request()` method. Both [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
 know how to use `sample_weight` in their `fit()` or `score()` methods. We can then pass the metadata in [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 which will route it to any active consumers:

\>>> weighted\_acc \= make\_scorer(accuracy\_score).set\_score\_request(sample\_weight\=True)
\>>> lr \= LogisticRegressionCV(
...     cv\=GroupKFold(),
...     scoring\=weighted\_acc,
...     use\_legacy\_attributes\=False,
... ).set\_fit\_request(sample\_weight\=True)
\>>> cv\_results \= cross\_validate(
...     lr,
...     X,
...     y,
...     params\={"sample\_weight": my\_weights, "groups": my\_groups},
...     cv\=GroupKFold(),
...     scoring\=weighted\_acc,
... )

Copy to clipboard

Note that in this example, [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 routes `my_weights` to both the scorer and [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
.

If we would pass `sample_weight` in the params of [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
, but not set any object to request it, `UnsetMetadataPassedError` would be raised, hinting to us that we need to explicitly set where to route it. The same applies if `params={"sample_weights": my_weights, ...}` were passed (note the typo, i.e. `weights` instead of `weight`), since `sample_weights` was not requested by any of its underlying objects.

### 4.1.2. Weighted scoring and unweighted fitting[#](https://scikit-learn.org/stable/metadata_routing.html#weighted-scoring-and-unweighted-fitting "Link to this heading")

When passing metadata such as `sample_weight` into a [router](https://scikit-learn.org/stable/glossary.html#term-router)
 ([meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
 or routing function), all `sample_weight` [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
 require weights to be either explicitly requested or explicitly not requested (i.e. `True` or `False`). Thus, to perform an unweighted fit, we need to configure [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 to not request sample weights, so that [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 does not pass the weights along:

\>>> weighted\_acc \= make\_scorer(accuracy\_score).set\_score\_request(sample\_weight\=True)
\>>> lr \= LogisticRegressionCV(
...     cv\=GroupKFold(), scoring\=weighted\_acc, use\_legacy\_attributes\=False
... ).set\_fit\_request(sample\_weight\=False)
\>>> cv\_results \= cross\_validate(
...     lr,
...     X,
...     y,
...     cv\=GroupKFold(),
...     params\={"sample\_weight": my\_weights, "groups": my\_groups},
...     scoring\=weighted\_acc,
... )

Copy to clipboard

If [`linear_model.LogisticRegressionCV.set_fit_request`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.set_fit_request "sklearn.linear_model.LogisticRegressionCV.set_fit_request")
 had not been called, [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 would raise an error because `sample_weight` is passed but [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 would not be explicitly configured to recognize the weights.

### 4.1.3. Unweighted feature selection[#](https://scikit-learn.org/stable/metadata_routing.html#unweighted-feature-selection "Link to this heading")

Routing metadata is only possible if the object’s method knows how to use the metadata, which in most cases means they have it as an explicit parameter. Only then we can set request values for metadata using `set_fit_request(sample_weight=True)`, for instance. This makes the object a [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
.

Unlike [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
, [`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
 can’t consume weights and therefore no request value for `sample_weight` on its instance is set and `sample_weight` is not routed to it:

\>>> weighted\_acc \= make\_scorer(accuracy\_score).set\_score\_request(sample\_weight\=True)
\>>> lr \= LogisticRegressionCV(
...     cv\=GroupKFold(), scoring\=weighted\_acc, use\_legacy\_attributes\=False
... ).set\_fit\_request(sample\_weight\=True)
\>>> sel \= SelectKBest(k\=2)
\>>> pipe \= make\_pipeline(sel, lr)
\>>> cv\_results \= cross\_validate(
...     pipe,
...     X,
...     y,
...     cv\=GroupKFold(),
...     params\={"sample\_weight": my\_weights, "groups": my\_groups},
...     scoring\=weighted\_acc,
... )

Copy to clipboard

### 4.1.4. Different scoring and fitting weights[#](https://scikit-learn.org/stable/metadata_routing.html#different-scoring-and-fitting-weights "Link to this heading")

Despite [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
 and [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 both expecting the key `sample_weight`, we can use aliases to pass different weights to different consumers. In this example, we pass `scoring_weight` to the scorer, and `fitting_weight` to [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
:

\>>> weighted\_acc \= make\_scorer(accuracy\_score).set\_score\_request(
...    sample\_weight\="scoring\_weight"
... )
\>>> lr \= LogisticRegressionCV(
...     cv\=GroupKFold(), scoring\=weighted\_acc, use\_legacy\_attributes\=False
... ).set\_fit\_request(sample\_weight\="fitting\_weight")
\>>> cv\_results \= cross\_validate(
...     lr,
...     X,
...     y,
...     cv\=GroupKFold(),
...     params\={
...         "scoring\_weight": my\_weights,
...         "fitting\_weight": my\_other\_weights,
...         "groups": my\_groups,
...     },
...     scoring\=weighted\_acc,
... )

Copy to clipboard

4.2. API Interface[#](https://scikit-learn.org/stable/metadata_routing.html#api-interface "Link to this heading")

------------------------------------------------------------------------------------------------------------------

A [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
 is an object (estimator, meta-estimator, scorer, splitter) which accepts and uses some [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
 in at least one of its methods (for instance `fit`, `predict`, `inverse_transform`, `transform`, `score`, `split`). Meta-estimators which only forward the metadata to other objects (child estimators, scorers, or splitters) and don’t use the metadata themselves are not consumers. (Meta-)Estimators which route metadata to other objects are [routers](https://scikit-learn.org/stable/glossary.html#term-router)
. A(n) (meta-)estimator can be a [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
 and a [router](https://scikit-learn.org/stable/glossary.html#term-router)
 at the same time. (Meta-)Estimators and splitters expose a `set_{method}_request` method for each method which accepts at least one metadata. For instance, if an estimator supports `sample_weight` in `fit` and `score`, it exposes `estimator.set_fit_request(sample_weight=value)` and `estimator.set_score_request(sample_weight=value)`. Here `value` can be:

*   `True`: method requests a `sample_weight`. This means if the metadata is provided, it will be used, otherwise no error is raised.
    
*   `False`: method does not request a `sample_weight`.
    
*   `None`: router will raise an error if `sample_weight` is passed. This is in almost all cases the default value when an object is instantiated and ensures the user sets the metadata requests explicitly when a metadata is passed. The only exception are `Group*Fold` splitters.
    
*   `"param_name"`: alias for `sample_weight` if we want to pass different weights to different consumers. If aliasing is used the meta-estimator should not forward `"param_name"` to the consumer, but `sample_weight` instead, because the consumer will expect a param called `sample_weight`. This means the mapping between the metadata required by the object, e.g. `sample_weight` and the variable name provided by the user, e.g. `my_weights` is done at the router level, and not by the consuming object itself.
    

Metadata are requested in the same way for scorers using `set_score_request`.

If a metadata, e.g. `sample_weight`, is passed by the user, the metadata request for all objects which potentially can consume `sample_weight` should be set by the user, otherwise an error is raised by the router object. For example, the following code raises an error, since it hasn’t been explicitly specified whether `sample_weight` should be passed to the estimator’s scorer or not:

\>>> param\_grid \= {"C": \[0.1, 1\]}
\>>> lr \= LogisticRegression().set\_fit\_request(sample\_weight\=True)
\>>> try:
...     GridSearchCV(
...         estimator\=lr, param\_grid\=param\_grid
...     ).fit(X, y, sample\_weight\=my\_weights)
... except ValueError as e:
...     print(e)
\[sample\_weight\] are passed but are not explicitly set as requested or not
requested for LogisticRegression.score, which is used within GridSearchCV.fit.
Call \`LogisticRegression.set\_score\_request({metadata}=True/False)\` for each metadata
you want to request/ignore. See the Metadata Routing User guide
<https://scikit-learn.org/stable/metadata\_routing.html> for more information.

Copy to clipboard

The issue can be fixed by explicitly setting the request value:

\>>> lr \= LogisticRegression().set\_fit\_request(
...     sample\_weight\=True
... ).set\_score\_request(sample\_weight\=False)

Copy to clipboard

At the end of the **Usage Examples** section, we disable the configuration flag for metadata routing:

\>>> sklearn.set\_config(enable\_metadata\_routing\=False)

Copy to clipboard

4.3. Metadata Routing Support Status[#](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing-support-status "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

All consumers (i.e. simple estimators which only consume metadata and don’t route them) support metadata routing, meaning they can be used inside meta-estimators which support metadata routing. However, development of support for metadata routing for meta-estimators is in progress, and here is a list of meta-estimators and tools which support and don’t yet support metadata routing.

Meta-estimators and functions supporting metadata routing:

*   [`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    
*   [`sklearn.compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    
*   [`sklearn.compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
    
*   [`sklearn.covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
    
*   [`sklearn.ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    
*   [`sklearn.ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    
*   [`sklearn.ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
    
*   [`sklearn.ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
    
*   [`sklearn.ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    
*   [`sklearn.ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    
*   [`sklearn.feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    
*   [`sklearn.feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    
*   [`sklearn.feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    
*   [`sklearn.feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
    
*   [`sklearn.impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
    
*   [`sklearn.linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    
*   [`sklearn.linear_model.LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")
    
*   [`sklearn.linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    
*   [`sklearn.linear_model.LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
    
*   [`sklearn.linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    
*   [`sklearn.linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    
*   [`sklearn.linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    
*   [`sklearn.linear_model.OrthogonalMatchingPursuitCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV")
    
*   [`sklearn.linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    
*   [`sklearn.linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
    
*   [`sklearn.linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    
*   [`sklearn.model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    
*   [`sklearn.model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    
*   [`sklearn.model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
    
*   [`sklearn.model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    
*   [`sklearn.model_selection.permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
    
*   [`sklearn.model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    
*   [`sklearn.model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    
*   [`sklearn.model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    
*   [`sklearn.model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
    
*   [`sklearn.model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
    
*   [`sklearn.multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
    
*   [`sklearn.multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    
*   [`sklearn.multiclass.OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
    
*   [`sklearn.multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
    
*   [`sklearn.multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
    
*   [`sklearn.multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
    
*   [`sklearn.multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
    
*   [`sklearn.preprocessing.TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
    
*   [`sklearn.pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    
*   [`sklearn.pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    
*   [`sklearn.semi_supervised.SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
    

Meta-estimators and tools not supporting metadata routing yet:

*   [`sklearn.ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    
*   [`sklearn.ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)