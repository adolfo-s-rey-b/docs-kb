[Skip to main content](https://scikit-learn.org/stable/glossary.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/glossary.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/glossary.html)
[1.8.0](https://scikit-learn.org/1.8/glossary.html)
[1.7.2](https://scikit-learn.org/1.7/glossary.html)
[1.6.1](https://scikit-learn.org/1.6/glossary.html)
[1.5.2](https://scikit-learn.org/1.5/glossary.html)
[1.4.2](https://scikit-learn.org/1.4/glossary.html)

Glossary of Common Terms and API Elements[#](https://scikit-learn.org/stable/glossary.html#glossary-of-common-terms-and-api-elements "Link to this heading")

=============================================================================================================================================================

This glossary hopes to definitively represent the tacit and explicit conventions applied in Scikit-learn and its API, while providing a reference for users and contributors. It aims to describe the concepts and either detail their corresponding API or link to other relevant parts of the documentation which do so. By linking to glossary entries from the API Reference and User Guide, we may minimize redundancy and inconsistency.

We begin by listing general concepts (and any that didn’t fit elsewhere), but more specific sets of related terms are listed below: [Class APIs and Estimator Types](https://scikit-learn.org/stable/glossary.html#glossary-estimator-types)
, [Metadata Routing](https://scikit-learn.org/stable/glossary.html#glossary-metadata-routing)
, [Callbacks](https://scikit-learn.org/stable/glossary.html#glossary-callbacks)
, [Target Types](https://scikit-learn.org/stable/glossary.html#glossary-target-types)
, [Methods](https://scikit-learn.org/stable/glossary.html#glossary-methods)
, [Parameters](https://scikit-learn.org/stable/glossary.html#glossary-parameters)
, [Attributes](https://scikit-learn.org/stable/glossary.html#glossary-attributes)
, [Data and sample properties](https://scikit-learn.org/stable/glossary.html#glossary-sample-props)
.

General Concepts[#](https://scikit-learn.org/stable/glossary.html#general-concepts "Link to this heading")

-----------------------------------------------------------------------------------------------------------

1d[#](https://scikit-learn.org/stable/glossary.html#term-1d "Link to this term")

1d array[#](https://scikit-learn.org/stable/glossary.html#term-1d-array "Link to this term")

One-dimensional array. A NumPy array whose `.shape` has length 1. A vector.

2d[#](https://scikit-learn.org/stable/glossary.html#term-2d "Link to this term")

2d array[#](https://scikit-learn.org/stable/glossary.html#term-2d-array "Link to this term")

Two-dimensional array. A NumPy array whose `.shape` has length 2. Often represents a matrix.

API[#](https://scikit-learn.org/stable/glossary.html#term-API "Link to this term")

Refers to both the _specific_ interfaces for estimators implemented in Scikit-learn and the _generalized_ conventions across types of estimators as described in this glossary and [overviewed in the contributor documentation](https://scikit-learn.org/stable/developers/develop.html#api-overview)
.

The specific interfaces that constitute Scikit-learn’s public API are largely documented in [API Reference](https://scikit-learn.org/stable/api/index.html#api-ref)
. However, we less formally consider anything as public API if none of the identifiers required to access it begins with `_`. We generally try to maintain [backwards compatibility](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility)
 for all objects in the public API.

Private API, including functions, modules and methods beginning `_` are not assured to be stable.

array-like[#](https://scikit-learn.org/stable/glossary.html#term-array-like "Link to this term")

The most common data format for _input_ to Scikit-learn estimators and functions, array-like is any type object for which [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
 will produce an array of appropriate shape (usually 1 or 2-dimensional) of appropriate dtype (usually numeric).

This includes:

*   a numpy array
    
*   a list of numbers
    
*   a list of length-k lists of numbers for some fixed length k
    
*   a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
     with all columns numeric
    
*   a numeric [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "(in pandas v3.0.5)")
    

Other array API inputs, but see [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for the preferred way of using these:

*   a [PyTorch](https://pytorch.org/)
     tensor on ‘cpu’ device
    
*   a [JAX](https://docs.jax.dev/en/latest/index.html)
     array
    

It excludes:

*   a [sparse matrix](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix)
    
*   a sparse array
    
*   an iterator
    
*   a generator
    

Note that _output_ from scikit-learn estimators and functions (e.g. predictions) should generally be arrays or sparse matrices, or lists thereof (as in multi-output [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
’s `predict_proba`). An estimator where `predict()` returns a list or a `pandas.Series` is not valid.

attribute[#](https://scikit-learn.org/stable/glossary.html#term-attribute "Link to this term")

attributes[#](https://scikit-learn.org/stable/glossary.html#term-attributes "Link to this term")

We mostly use attribute to refer to how model information is stored on an estimator during fitting. Any public attribute stored on an estimator instance is required to begin with an alphabetic character and end in a single underscore if it is set in [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 or [partial\_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit)
. These are what is documented under an estimator’s _Attributes_ documentation. The information stored in attributes is usually either: sufficient statistics used for prediction or transformation; [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
 outputs such as [labels\_](https://scikit-learn.org/stable/glossary.html#term-labels_)
 or [embedding\_](https://scikit-learn.org/stable/glossary.html#term-embedding_)
; or diagnostic data, such as [feature\_importances\_](https://scikit-learn.org/stable/glossary.html#term-feature_importances_)
. Common attributes are listed [below](https://scikit-learn.org/stable/glossary.html#glossary-attributes)
.

A public attribute may have the same name as a constructor [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
, with a `_` appended. This is used to store a validated or estimated version of the user’s input. For example, [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 is constructed with an `n_components` parameter. From this, together with other parameters and the data, PCA estimates the attribute `n_components_`.

Further private attributes used in prediction/transformation/etc. may also be set when fitting. These begin with a single underscore and are not assured to be stable for public access.

A public attribute on an estimator instance that does not end in an underscore should be the stored, unmodified value of an `__init__` [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
 of the same name. Because of this equivalence, these are documented under an estimator’s _Parameters_ documentation.

backwards compatibility[#](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility "Link to this term")

We generally try to maintain backward compatibility (i.e. interfaces and behaviors may be extended but not changed or removed) from release to release but this comes with some exceptions:

Public API only

The behavior of objects accessed through private identifiers (those beginning `_`) may be changed arbitrarily between versions.

As documented

We will generally assume that the users have adhered to the documented parameter types and ranges. If the documentation asks for a list and the user gives a tuple, we do not assure consistent behavior from version to version.

Deprecation

Behaviors may change following a [deprecation](https://scikit-learn.org/stable/glossary.html#term-deprecation)
 period (usually two releases long). Warnings are issued using Python’s [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python v3.14)")
 module.

Keyword arguments

We may sometimes assume that all optional parameters (other than X and y to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and similar methods) are passed as keyword arguments only and may be positionally reordered.

Bug fixes and enhancements

Bug fixes and – less often – enhancements may change the behavior of estimators, including the predictions of an estimator trained on the same data and [random\_state](https://scikit-learn.org/stable/glossary.html#term-random_state)
. When this happens, we attempt to note it clearly in the changelog.

Serialization

We make no assurances that pickling an estimator in one version will allow it to be unpickled to an equivalent model in the subsequent version. (For estimators in the sklearn package, we issue a warning when this unpickling is attempted, even if it may happen to work.) See [Security & Maintainability Limitations](https://scikit-learn.org/stable/model_persistence.html#persistence-limitations)
.

[`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")

We provide limited backwards compatibility assurances for the estimator checks: we may add extra requirements on estimators tested with this function, usually when these were informally assumed but not formally tested.

Despite this informal contract with our users, the software is provided as is, as stated in the license. When a release inadvertently introduces changes that are not backward compatible, these are known as software regressions.

callable[#](https://scikit-learn.org/stable/glossary.html#term-callable "Link to this term")

A function, class or an object which implements the `__call__` method; anything that returns True when the argument of [callable()](https://docs.python.org/3/library/functions.html#callable)
.

categorical feature[#](https://scikit-learn.org/stable/glossary.html#term-categorical-feature "Link to this term")

A categorical or nominal [feature](https://scikit-learn.org/stable/glossary.html#term-feature)
 is one that has a finite set of discrete values across the population of data. These are commonly represented as columns of integers or strings. Strings will be rejected by most scikit-learn estimators, and integers will be treated as ordinal or count-valued. For the use with most estimators, categorical variables should be one-hot encoded. Notable exceptions include tree-based models such as random forests and gradient boosting models that often work better and faster with integer-coded categorical variables. [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 helps encoding string-valued categorical features as ordinal integers, and [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 can be used to one-hot encode categorical features. See also [Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)
 and the [categorical-encoding](https://github.com/scikit-learn-contrib/category_encoders)
 package for tools related to encoding categorical features.

clone[#](https://scikit-learn.org/stable/glossary.html#term-clone "Link to this term")

cloned[#](https://scikit-learn.org/stable/glossary.html#term-cloned "Link to this term")

To copy an [estimator instance](https://scikit-learn.org/stable/glossary.html#term-estimator-instance)
 and create a new one with identical [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters)
, but without any fitted [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
, using [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
.

When `fit` is called, a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 usually clones a wrapped estimator instance before fitting the cloned instance. (Exceptions, for legacy reasons, include [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 and [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
.)

If the estimator’s `random_state` parameter is an integer (or if the estimator doesn’t have a `random_state` parameter), an _exact clone_ is returned: the clone and the original estimator will give the exact same results. Otherwise, _statistical clone_ is returned: the clone might yield different results from the original estimator. More details can be found in [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness)
.

common tests[#](https://scikit-learn.org/stable/glossary.html#term-common-tests "Link to this term")

This refers to the tests run on almost every estimator class in Scikit-learn to check they comply with basic API conventions. They are available for external use through [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
 or [`utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
, with most of the implementation in `sklearn/utils/estimator_checks.py`.

Note: Some exceptions to the common testing regime are currently hard-coded into the library, but we hope to replace this by marking exceptional behaviours on the estimator using semantic [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags)
.

cross-fitting[#](https://scikit-learn.org/stable/glossary.html#term-cross-fitting "Link to this term")

cross fitting[#](https://scikit-learn.org/stable/glossary.html#term-0 "Link to this term")

A resampling method that iteratively partitions data into mutually exclusive subsets to fit two stages. During the first stage, the mutually exclusive subsets enable predictions or transformations to be computed on data not seen during training. The computed data is then used in the second stage. The objective is to avoid having any overfitting in the first stage introduce bias into the input data distribution of the second stage. For examples of its use, see: [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
, [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
, [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
 and [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
.

cross-validation[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation "Link to this term")

cross validation[#](https://scikit-learn.org/stable/glossary.html#term-1 "Link to this term")

A resampling method that iteratively partitions data into mutually exclusive ‘train’ and ‘test’ subsets so model performance can be evaluated on unseen data. This conserves data as it avoids the need to hold out a ‘validation’ dataset and accounts for variability as multiple rounds of cross validation are generally performed. See [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for more details.

deprecation[#](https://scikit-learn.org/stable/glossary.html#term-deprecation "Link to this term")

We use deprecation to slowly violate our [backwards compatibility](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility)
 assurances, usually to:

*   change the default value of a parameter; or
    
*   remove a parameter, attribute, method, class, etc.
    

We will ordinarily issue a warning when a deprecated element is used, although there may be limitations to this. For instance, we will raise a warning when someone sets a parameter that has been deprecated, but may not when they access that parameter’s attribute on the estimator instance.

See the [Contributors’ Guide](https://scikit-learn.org/stable/developers/contributing.html#contributing-deprecation)
.

dimensionality[#](https://scikit-learn.org/stable/glossary.html#term-dimensionality "Link to this term")

May be used to refer to the number of [features](https://scikit-learn.org/stable/glossary.html#term-features)
 (i.e. [n\_features](https://scikit-learn.org/stable/glossary.html#term-n_features)
), or columns in a 2d feature matrix. Dimensions are, however, also used to refer to the length of a NumPy array’s shape, distinguishing a 1d array from a 2d matrix.

docstring[#](https://scikit-learn.org/stable/glossary.html#term-docstring "Link to this term")

The embedded documentation for a module, class, function, etc., usually in code as a string at the beginning of the object’s definition, and accessible as the object’s `__doc__` attribute.

We try to adhere to [PEP257](https://www.python.org/dev/peps/pep-0257/)
, and follow [NumpyDoc conventions](https://numpydoc.readthedocs.io/en/latest/format.html)
.

double underscore[#](https://scikit-learn.org/stable/glossary.html#term-double-underscore "Link to this term")

double underscore notation[#](https://scikit-learn.org/stable/glossary.html#term-double-underscore-notation "Link to this term")

When specifying parameter names for nested estimators, `__` may be used to separate between parent and child in some contexts. The most common use is when setting parameters through a meta-estimator with [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
 and hence in specifying a search grid in [parameter search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
. See [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
. It is also used in [`pipeline.Pipeline.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit "sklearn.pipeline.Pipeline.fit")
 for passing [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties)
 to the `fit` methods of estimators in the pipeline.

dtype[#](https://scikit-learn.org/stable/glossary.html#term-dtype "Link to this term")

data type[#](https://scikit-learn.org/stable/glossary.html#term-data-type "Link to this term")

NumPy arrays assume a homogeneous data type throughout, available in the `.dtype` attribute of an array (or sparse matrix). We generally assume simple data types for scikit-learn data: float or integer. We may support object or string data types for arrays before encoding or vectorizing. Our estimators do not work with struct arrays, for instance.

Our documentation can sometimes give information about the dtype precision, e.g. `np.int32`, `np.int64`, etc. When the precision is provided, it refers to the NumPy dtype. If an arbitrary precision is used, the documentation will refer to dtype `integer` or `floating`. Note that in this case, the precision can be platform dependent. The `numeric` dtype refers to accepting both `integer` and `floating`.

When it comes to choosing between 64-bit dtype (i.e. `np.float64` and `np.int64`) and 32-bit dtype (i.e. `np.float32` and `np.int32`), it boils down to a trade-off between efficiency and precision. The 64-bit types offer more accurate results due to their lower floating-point error, but demand more computational resources, resulting in slower operations and increased memory usage. In contrast, 32-bit types promise enhanced operation speed and reduced memory consumption, but introduce a larger floating-point error. The efficiency improvements are dependent on lower level optimization such as vectorization, single instruction multiple dispatch (SIMD), or cache optimization but crucially on the compatibility of the algorithm in use.

Specifically, the choice of precision should account for whether the employed algorithm can effectively leverage `np.float32`. Some algorithms, especially certain minimization methods, are exclusively coded for `np.float64`, meaning that even if `np.float32` is passed, it triggers an automatic conversion back to `np.float64`. This not only negates the intended computational savings but also introduces additional overhead, making operations with `np.float32` unexpectedly slower and more memory-intensive due to this extra conversion step.

duck typing[#](https://scikit-learn.org/stable/glossary.html#term-duck-typing "Link to this term")

We try to apply [duck typing](https://en.wikipedia.org/wiki/Duck_typing)
 to determine how to handle some input values (e.g. checking whether a given estimator is a classifier). That is, we avoid using `isinstance` where possible, and rely on the presence or absence of attributes to determine an object’s behaviour. Some nuance is required when following this approach:

*   For some estimators, an attribute may only be available once it is [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
    . For instance, we cannot a priori determine if [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
     is available in a grid search where the grid includes alternating between a probabilistic and a non-probabilistic predictor in the final step of the pipeline. In the following, we can only determine if `clf` is probabilistic after fitting it on some data:
    
    \>>> from sklearn.model\_selection import GridSearchCV
    \>>> from sklearn.linear\_model import SGDClassifier
    \>>> clf \= GridSearchCV(SGDClassifier(),
    ...                    param\_grid\={'loss': \['log\_loss', 'hinge'\]})
    
    Copy to clipboard
    
    This means that we can only check for duck-typed attributes after fitting, and that we must be careful to make [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
     only present attributes according to the state of the underlying estimator after fitting.
    
*   Checking if an attribute is present (using `hasattr`) is in general just as expensive as getting the attribute (`getattr` or dot notation). In some cases, getting the attribute may indeed be expensive (e.g. for some implementations of [feature\_importances\_](https://scikit-learn.org/stable/glossary.html#term-feature_importances_)
    , which may suggest this is an API design flaw). So code which does `hasattr` followed by `getattr` should be avoided; `getattr` within a try-except block is preferred.
    
*   For determining some aspects of an estimator’s expectations or support for some feature, we use [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags)
     instead of duck typing.
    

early stopping[#](https://scikit-learn.org/stable/glossary.html#term-early-stopping "Link to this term")

This consists in stopping an iterative optimization method before the convergence of the training loss, to avoid over-fitting. This is generally done by monitoring the generalization score on a validation set. When available, it is activated through the parameter `early_stopping` or by setting a positive [n\_iter\_no\_change](https://scikit-learn.org/stable/glossary.html#term-n_iter_no_change)
.

estimator instance[#](https://scikit-learn.org/stable/glossary.html#term-estimator-instance "Link to this term")

We sometimes use this terminology to distinguish an [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 class from a constructed instance. For example, in the following, `cls` is an estimator class, while `est1` and `est2` are instances:

cls \= RandomForestClassifier
est1 \= cls()
est2 \= RandomForestClassifier()

Copy to clipboard

examples[#](https://scikit-learn.org/stable/glossary.html#term-examples "Link to this term")

We try to give examples of basic usage for most functions and classes in the API:

*   as doctests in their docstrings (i.e. within the `sklearn/` library code itself).
    
*   as examples in the [example gallery](https://scikit-learn.org/stable/auto_examples/index.html#general-examples)
     rendered (using [sphinx-gallery](https://sphinx-gallery.readthedocs.io/)
    ) from scripts in the `examples/` directory, exemplifying key features or parameters of the estimator/function. These should also be referenced from the User Guide.
    
*   sometimes in the [User Guide](https://scikit-learn.org/stable/user_guide.html#user-guide)
     (built from `doc/`) alongside a technical description of the estimator.
    

experimental[#](https://scikit-learn.org/stable/glossary.html#term-experimental "Link to this term")

An experimental tool is already usable but its public API, such as default parameter values or fitted attributes, is still subject to change in future versions without the usual [deprecation](https://scikit-learn.org/stable/glossary.html#term-deprecation)
 warning policy.

evaluation metric[#](https://scikit-learn.org/stable/glossary.html#term-evaluation-metric "Link to this term")

evaluation metrics[#](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics "Link to this term")

Evaluation metrics give a measure of how well a model performs. We may use this term specifically to refer to the functions in [`metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
 (disregarding [`pairwise`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.pairwise "sklearn.metrics.pairwise")
), as distinct from the [score](https://scikit-learn.org/stable/glossary.html#term-score)
 method and the [scoring](https://scikit-learn.org/stable/glossary.html#term-scoring)
 API used in cross validation. See [Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation)
.

These functions usually accept a ground truth (or the raw data where the metric evaluates clustering without a ground truth) and a prediction, be it the output of [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 (`y_pred`), of [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 (`y_proba`), or of an arbitrary score function including [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 (`y_score`). Functions are usually named to end with `_score` if a greater score indicates a better model, and `_loss` if a lesser score indicates a better model. This diversity of interface motivates the scoring API.

Note that some estimators can calculate metrics that are not included in [`metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
 and are estimator-specific, notably model likelihoods.

estimator tags[#](https://scikit-learn.org/stable/glossary.html#term-estimator-tags "Link to this term")

Estimator tags describe certain capabilities of an estimator. This would enable some runtime behaviors based on estimator inspection, but it also allows each estimator to be tested for appropriate invariances while being excepted from other [common tests](https://scikit-learn.org/stable/glossary.html#term-common-tests)
.

Some aspects of estimator tags are currently determined through the [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing)
 of methods like `predict_proba` and through some special attributes on estimator objects:

For more detailed info, see [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
.

feature[#](https://scikit-learn.org/stable/glossary.html#term-feature "Link to this term")

features[#](https://scikit-learn.org/stable/glossary.html#term-features "Link to this term")

feature vector[#](https://scikit-learn.org/stable/glossary.html#term-feature-vector "Link to this term")

In the abstract, a feature is a function (in its mathematical sense) mapping a sampled object to a numeric or categorical quantity. “Feature” is also commonly used to refer to these quantities, being the individual elements of a vector representing a sample. In a data matrix, features are represented as columns: each column contains the result of applying a feature function to a set of samples.

Elsewhere features are known as attributes, predictors, regressors, or independent variables.

Nearly all estimators in scikit-learn assume that features are numeric, finite and not missing, even when they have semantically distinct domains and distributions (categorical, ordinal, count-valued, real-valued, interval). See also [categorical feature](https://scikit-learn.org/stable/glossary.html#term-categorical-feature)
 and [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values)
.

`n_features` indicates the number of features in a dataset.

fitting[#](https://scikit-learn.org/stable/glossary.html#term-fitting "Link to this term")

Calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 (or [fit\_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform)
, [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
, etc.) on an estimator.

fitted[#](https://scikit-learn.org/stable/glossary.html#term-fitted "Link to this term")

The state of an estimator after [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
.

There is no conventional procedure for checking if an estimator is fitted. However, an estimator that is not fitted:

*   should raise [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
     when a prediction method ([predict](https://scikit-learn.org/stable/glossary.html#term-predict)
    , [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
    , etc.) is called. ([`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
     is used internally for this purpose.)
    
*   should not have any [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
     beginning with an alphabetic character and ending with an underscore. (Note that a descriptor for the attribute may still be present on the class, but hasattr should return False)
    

function[#](https://scikit-learn.org/stable/glossary.html#term-function "Link to this term")

We provide ad hoc function interfaces for many algorithms, while [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 classes provide a more consistent interface.

In particular, Scikit-learn may provide a function interface that fits a model to some data and returns the learnt model parameters, as in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
. For transductive models, this also returns the embedding or cluster labels, as in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
 or [`cluster.dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan")
. Many preprocessing transformers also provide a function interface, akin to calling [fit\_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform)
, as in [`preprocessing.maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale")
. Users should be careful to avoid [data leakage](https://scikit-learn.org/stable/glossary.html#term-data-leakage)
 when making use of these `fit_transform`\-equivalent functions.

We do not have a strict policy about when to or when not to provide function forms of estimators, but maintainers should consider consistency with existing interfaces, and whether providing a function would lead users astray from best practices (as regards data leakage, etc.)

gallery[#](https://scikit-learn.org/stable/glossary.html#term-gallery "Link to this term")

See [examples](https://scikit-learn.org/stable/glossary.html#term-examples)
.

hyperparameter[#](https://scikit-learn.org/stable/glossary.html#term-hyperparameter "Link to this term")

hyper-parameter[#](https://scikit-learn.org/stable/glossary.html#term-hyper-parameter "Link to this term")

See [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
.

impute[#](https://scikit-learn.org/stable/glossary.html#term-impute "Link to this term")

imputation[#](https://scikit-learn.org/stable/glossary.html#term-imputation "Link to this term")

Most machine learning algorithms require that their inputs have no [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values)
, and will not work if this requirement is violated. Algorithms that attempt to fill in (or impute) missing values are referred to as imputation algorithms.

indexable[#](https://scikit-learn.org/stable/glossary.html#term-indexable "Link to this term")

An [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like)
, [sparse matrix](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix)
, pandas DataFrame or sequence (usually a list).

induction[#](https://scikit-learn.org/stable/glossary.html#term-induction "Link to this term")

inductive[#](https://scikit-learn.org/stable/glossary.html#term-inductive "Link to this term")

Inductive (contrasted with [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
) machine learning builds a model of some data that can then be applied to new instances. Most estimators in Scikit-learn are inductive, having [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 and/or [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
 methods.

joblib[#](https://scikit-learn.org/stable/glossary.html#term-joblib "Link to this term")

A Python library ([https://joblib.readthedocs.io](https://joblib.readthedocs.io/)
) used in Scikit-learn to facilitate simple parallelism and caching. Joblib is oriented towards efficiently working with numpy arrays, such as through use of [memory mapping](https://scikit-learn.org/stable/glossary.html#term-memory-mapping)
. See [Parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
 for more information.

label indicator format[#](https://scikit-learn.org/stable/glossary.html#term-label-indicator-format "Link to this term")

label indicator matrix[#](https://scikit-learn.org/stable/glossary.html#term-label-indicator-matrix "Link to this term")

multilabel indicator matrix[#](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrix "Link to this term")

multilabel indicator matrices[#](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrices "Link to this term")

This format can be used to represent binary or multilabel data. Each row of a 2d array or sparse matrix corresponds to a sample, each column corresponds to a class, and each element is 1 if the sample is labeled with the class and 0 if not.

[LabelBinarizer](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
 can be used to create a multilabel indicator matrix from [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 labels.

leakage[#](https://scikit-learn.org/stable/glossary.html#term-leakage "Link to this term")

data leakage[#](https://scikit-learn.org/stable/glossary.html#term-data-leakage "Link to this term")

A problem in cross validation where generalization performance can be over-estimated since knowledge of the test data was inadvertently included in training a model. This is a risk, for instance, when applying a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer)
 to the entirety of a dataset rather than each training portion in a cross validation split.

We aim to provide interfaces (such as [`pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
 and [`model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
) that shield the user from data leakage.

memmapping[#](https://scikit-learn.org/stable/glossary.html#term-memmapping "Link to this term")

memory map[#](https://scikit-learn.org/stable/glossary.html#term-memory-map "Link to this term")

memory mapping[#](https://scikit-learn.org/stable/glossary.html#term-memory-mapping "Link to this term")

A memory efficiency strategy that keeps data on disk rather than copying it into main memory. Memory maps can be created for arrays that can be read, written, or both, using [`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "(in NumPy v2.5)")
. When using [joblib](https://scikit-learn.org/stable/glossary.html#term-joblib)
 to parallelize operations in Scikit-learn, it may automatically memmap large arrays to reduce memory duplication overhead in multiprocessing.

missing values[#](https://scikit-learn.org/stable/glossary.html#term-missing-values "Link to this term")

Most Scikit-learn estimators do not work with missing values. When they do (e.g. in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
), NaN is the preferred representation of missing values in float arrays. If the array has integer dtype, NaN cannot be represented. For this reason, we support specifying another `missing_values` value when [imputation](https://scikit-learn.org/stable/glossary.html#term-imputation)
 or learning can be performed in integer space. [Unlabeled data](https://scikit-learn.org/stable/glossary.html#term-unlabeled-data)
 is a special case of missing values in the [target](https://scikit-learn.org/stable/glossary.html#term-target)
.

`n_features`[#](https://scikit-learn.org/stable/glossary.html#term-n_features "Link to this term")

The number of [features](https://scikit-learn.org/stable/glossary.html#term-features)
.

`n_outputs`[#](https://scikit-learn.org/stable/glossary.html#term-n_outputs "Link to this term")

The number of [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs)
 in the [target](https://scikit-learn.org/stable/glossary.html#term-target)
.

`n_samples`[#](https://scikit-learn.org/stable/glossary.html#term-n_samples "Link to this term")

The number of [samples](https://scikit-learn.org/stable/glossary.html#term-samples)
.

`n_targets`[#](https://scikit-learn.org/stable/glossary.html#term-n_targets "Link to this term")

Synonym for [n\_outputs](https://scikit-learn.org/stable/glossary.html#term-n_outputs)
.

narrative docs[#](https://scikit-learn.org/stable/glossary.html#term-narrative-docs "Link to this term")

narrative documentation[#](https://scikit-learn.org/stable/glossary.html#term-narrative-documentation "Link to this term")

An alias for [User Guide](https://scikit-learn.org/stable/user_guide.html#user-guide)
, i.e. documentation written in `doc/modules/`. Unlike the [API reference](https://scikit-learn.org/stable/api/index.html#api-ref)
 provided through docstrings, the User Guide aims to:

*   group tools provided by Scikit-learn together thematically or in terms of usage;
    
*   motivate why someone would use each particular tool, often through comparison;
    
*   provide both intuitive and technical descriptions of tools;
    
*   provide or link to [examples](https://scikit-learn.org/stable/glossary.html#term-examples)
     of using key features of a tool.
    

np[#](https://scikit-learn.org/stable/glossary.html#term-np "Link to this term")

A shorthand for Numpy due to the conventional import statement:

import numpy as np

Copy to clipboard

ovo[#](https://scikit-learn.org/stable/glossary.html#term-ovo "Link to this term")

One-vs-one[#](https://scikit-learn.org/stable/glossary.html#term-One-vs-one "Link to this term")

one-vs-one[#](https://scikit-learn.org/stable/glossary.html#term-one-vs-one "Link to this term")

Method of decomposing a [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 problem into `n_classes * (n_classes - 1) / 2` [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 problems, one for each pairwise combination of classes. A metric is computed or a classifier is fitted for each pair combination. [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
 implements this method for binary classifiers.

ovr[#](https://scikit-learn.org/stable/glossary.html#term-ovr "Link to this term")

One-vs-Rest[#](https://scikit-learn.org/stable/glossary.html#term-One-vs-Rest "Link to this term")

one-vs-rest[#](https://scikit-learn.org/stable/glossary.html#term-one-vs-rest "Link to this term")

Method for decomposing a [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 problem into `n_classes` [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 problems. For each class a metric is computed or classifier fitted, with that class being treated as the positive class while all other classes are negative. [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 implements this method for binary classifiers.

online learning[#](https://scikit-learn.org/stable/glossary.html#term-online-learning "Link to this term")

Where a model is iteratively updated by receiving each batch of ground truth [targets](https://scikit-learn.org/stable/glossary.html#term-targets)
 soon after making predictions on corresponding batch of data. Intrinsically, the model must be usable for prediction after each batch. See [partial\_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit)
.

out-of-core[#](https://scikit-learn.org/stable/glossary.html#term-out-of-core "Link to this term")

An efficiency strategy where not all the data is stored in main memory at once, usually by performing learning on batches of data. See [partial\_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit)
.

outputs[#](https://scikit-learn.org/stable/glossary.html#term-outputs "Link to this term")

Individual scalar/categorical variables per sample in the [target](https://scikit-learn.org/stable/glossary.html#term-target)
. For example, in multilabel classification each possible label corresponds to a binary output. Also called _responses_, _tasks_ or _targets_. See [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput)
 and [continuous multioutput](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput)
.

pair[#](https://scikit-learn.org/stable/glossary.html#term-pair "Link to this term")

A tuple of length two.

parameter[#](https://scikit-learn.org/stable/glossary.html#term-parameter "Link to this term")

parameters[#](https://scikit-learn.org/stable/glossary.html#term-parameters "Link to this term")

param[#](https://scikit-learn.org/stable/glossary.html#term-param "Link to this term")

params[#](https://scikit-learn.org/stable/glossary.html#term-params "Link to this term")

We mostly use _parameter_ to refer to the aspects of an estimator that can be specified in its construction. For example, `max_depth` and `random_state` are parameters of [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
. Parameters to an estimator’s constructor are stored unmodified as attributes on the estimator instance, and conventionally start with an alphabetic character and end with an alphanumeric character. Each estimator’s constructor parameters are described in the estimator’s docstring.

We do not use parameters in the statistical sense, where parameters are values that specify a model and can be estimated from data. What we call parameters might be what statisticians call hyperparameters to the model: aspects for configuring model structure that are often not directly learnt from data. However, our parameters are also used to prescribe modeling operations that do not affect the learnt model, such as [n\_jobs](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for controlling parallelism.

When talking about the parameters of a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
, we may also be including the parameters of the estimators wrapped by the meta-estimator. Ordinarily, these nested parameters are denoted by using a [double underscore](https://scikit-learn.org/stable/glossary.html#term-double-underscore)
 (`__`) to separate between the estimator-as-parameter and its parameter. Thus `clf = BaggingClassifier(estimator=DecisionTreeClassifier(max_depth=3))` has a deep parameter `estimator__max_depth` with value `3`, which is accessible with `clf.estimator.max_depth` or `clf.get_params()['estimator__max_depth']`.

The list of parameters and their current values can be retrieved from an [estimator instance](https://scikit-learn.org/stable/glossary.html#term-estimator-instance)
 using its [get\_params](https://scikit-learn.org/stable/glossary.html#term-get_params)
 method.

Between construction and fitting, parameters may be modified using [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
. To enable this, parameters are not ordinarily validated or altered when the estimator is constructed, or when each parameter is set. Parameter validation is performed when [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 is called.

Common parameters are listed [below](https://scikit-learn.org/stable/glossary.html#glossary-parameters)
.

pairwise metric[#](https://scikit-learn.org/stable/glossary.html#term-pairwise-metric "Link to this term")

pairwise metrics[#](https://scikit-learn.org/stable/glossary.html#term-pairwise-metrics "Link to this term")

In its broad sense, a pairwise metric defines a function for measuring similarity or dissimilarity between two samples (with each ordinarily represented as a [feature vector](https://scikit-learn.org/stable/glossary.html#term-feature-vector)
). We particularly provide implementations of distance metrics (as well as improper metrics like Cosine Distance) through [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
, and of kernel functions (a constrained class of similarity functions) in [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
. These can compute pairwise distance matrices that are symmetric and hence store data redundantly.

See also [precomputed](https://scikit-learn.org/stable/glossary.html#term-precomputed)
 and [metric](https://scikit-learn.org/stable/glossary.html#term-metric)
.

Note that for most distance metrics, we rely on implementations from [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
, but may reimplement for efficiency in our context. The [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
 interface is used to implement distance metrics for integration with efficient neighbors search.

pd[#](https://scikit-learn.org/stable/glossary.html#term-pd "Link to this term")

A shorthand for [Pandas](https://pandas.pydata.org/)
 due to the conventional import statement:

import pandas as pd

Copy to clipboard

precomputed[#](https://scikit-learn.org/stable/glossary.html#term-precomputed "Link to this term")

Where algorithms rely on [pairwise metrics](https://scikit-learn.org/stable/glossary.html#term-pairwise-metrics)
, and can be computed from pairwise metrics alone, we often allow the user to specify that the [X](https://scikit-learn.org/stable/glossary.html#term-X)
 provided is already in the pairwise (dis)similarity space, rather than in a feature space. That is, when passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, it is a square, symmetric matrix, with each vector indicating (dis)similarity to every sample, and when passed to prediction/transformation methods, each row corresponds to a testing sample and each column to a training sample.

Use of precomputed X is usually indicated by setting a `metric`, `affinity` or `kernel` parameter to the string ‘precomputed’. If this is the case, then the estimator should set the `pairwise` estimator tag as True.

rectangular[#](https://scikit-learn.org/stable/glossary.html#term-rectangular "Link to this term")

Data that can be represented as a matrix with [samples](https://scikit-learn.org/stable/glossary.html#term-samples)
 on the first axis and a fixed, finite set of [features](https://scikit-learn.org/stable/glossary.html#term-features)
 on the second is called rectangular.

This term excludes samples with non-vectorial structures, such as text, an image of arbitrary size, a time series of arbitrary length, a set of vectors, etc. The purpose of a [vectorizer](https://scikit-learn.org/stable/glossary.html#term-vectorizer)
 is to produce rectangular forms of such data.

sample[#](https://scikit-learn.org/stable/glossary.html#term-sample "Link to this term")

samples[#](https://scikit-learn.org/stable/glossary.html#term-samples "Link to this term")

We usually use this term as a noun to indicate a single feature vector. Elsewhere a sample is called an instance, data point, or observation. `n_samples` indicates the number of samples in a dataset, being the number of rows in a data array [X](https://scikit-learn.org/stable/glossary.html#term-X)
. Note that this definition is standard in machine learning and deviates from statistics where it means _a set of individuals or objects collected or selected_.

sample property[#](https://scikit-learn.org/stable/glossary.html#term-sample-property "Link to this term")

sample properties[#](https://scikit-learn.org/stable/glossary.html#term-sample-properties "Link to this term")

A sample property is data for each sample (e.g. an array of length n\_samples) passed to an estimator method or a similar function, alongside but distinct from the [features](https://scikit-learn.org/stable/glossary.html#term-features)
 (`X`) and [target](https://scikit-learn.org/stable/glossary.html#term-target)
 (`y`). The most prominent example is [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
; see others at [Data and sample properties](https://scikit-learn.org/stable/glossary.html#glossary-sample-props)
.

As of version 0.19 we do not have a consistent approach to handling sample properties and their routing in [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
, though a `fit_params` parameter is often used.

scikit-learn-contrib[#](https://scikit-learn.org/stable/glossary.html#term-scikit-learn-contrib "Link to this term")

A venue for publishing Scikit-learn-compatible libraries that are broadly authorized by the core developers and the contrib community, but not maintained by the core developer team. See [https://scikit-learn-contrib.github.io](https://scikit-learn-contrib.github.io/)
.

scikit-learn enhancement proposals[#](https://scikit-learn.org/stable/glossary.html#term-scikit-learn-enhancement-proposals "Link to this term")

SLEP[#](https://scikit-learn.org/stable/glossary.html#term-SLEP "Link to this term")

SLEPs[#](https://scikit-learn.org/stable/glossary.html#term-SLEPs "Link to this term")

Changes to the API principles and changes to dependencies or supported versions happen via a [SLEP](https://scikit-learn.org/stable/governance.html#slep)
 and follows the decision-making process outlined in [Scikit-learn governance and decision-making](https://scikit-learn.org/stable/governance.html#governance)
. For all votes, a proposal must have been made public and discussed before the vote. Such a proposal must be a consolidated document, in the form of a “Scikit-Learn Enhancement Proposal” (SLEP), rather than a long discussion on an issue. A SLEP must be submitted as a pull-request to [enhancement proposals](https://scikit-learn-enhancement-proposals.readthedocs.io/)
 using the [SLEP template](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep_template.html)
.

semi-supervised[#](https://scikit-learn.org/stable/glossary.html#term-semi-supervised "Link to this term")

semi-supervised learning[#](https://scikit-learn.org/stable/glossary.html#term-semi-supervised-learning "Link to this term")

semisupervised[#](https://scikit-learn.org/stable/glossary.html#term-semisupervised "Link to this term")

Learning where the expected prediction (label or ground truth) is only available for some samples provided as training data when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 the model. We conventionally apply the label `-1` to [unlabeled](https://scikit-learn.org/stable/glossary.html#term-unlabeled)
 samples in semi-supervised classification.

sparse matrix[#](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix "Link to this term")

sparse graph[#](https://scikit-learn.org/stable/glossary.html#term-sparse-graph "Link to this term")

A representation of two-dimensional numeric data that is more memory efficient than the corresponding dense numpy array where almost all elements are zero. We use the [`scipy.sparse`](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse "(in SciPy v1.18.0)")
 framework, which provides several underlying sparse data representations, or _formats_. Some formats are more efficient than others for particular tasks, and when a particular format provides especial benefit, we try to document this fact in Scikit-learn parameter descriptions.

Some sparse matrix formats (notably CSR, CSC, COO and LIL) distinguish between _implicit_ and _explicit_ zeros. Explicit zeros are stored (i.e. they consume memory in a `data` array) in the data structure, while implicit zeros correspond to every element not otherwise defined in explicit storage.

Two semantics for sparse matrices are used in Scikit-learn:

matrix semantics

The sparse matrix is interpreted as an array with implicit and explicit zeros being interpreted as the number 0. This is the interpretation most often adopted, e.g. when sparse matrices are used for feature matrices or [multilabel indicator matrices](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrices)
.

graph semantics

As with [`scipy.sparse.csgraph`](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html#module-scipy.sparse.csgraph "(in SciPy v1.18.0)")
, explicit zeros are interpreted as the number 0, but implicit zeros indicate a masked or absent value, such as the absence of an edge between two vertices of a graph, where an explicit value indicates an edge’s weight. This interpretation is adopted to represent connectivity in clustering, in representations of nearest neighborhoods (e.g. [`neighbors.kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
), and for precomputed distance representation where only distances in the neighborhood of each point are required.

When working with sparse matrices, we assume that it is sparse for a good reason, and avoid writing code that densifies a user-provided sparse matrix, instead maintaining sparsity or raising an error if not possible (i.e. if an estimator does not / cannot support sparse matrices).

stateless[#](https://scikit-learn.org/stable/glossary.html#term-stateless "Link to this term")

An estimator is stateless if it does not store any information that is obtained during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. This information can be either parameters learned during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 or statistics computed from the training data. An estimator is stateless if it has no [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
 apart from ones set in `__init__`. Calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 for these estimators will only validate the public [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
 passed in `__init__`.

supervised[#](https://scikit-learn.org/stable/glossary.html#term-supervised "Link to this term")

supervised learning[#](https://scikit-learn.org/stable/glossary.html#term-supervised-learning "Link to this term")

Learning where the expected prediction (label or ground truth) is available for each sample when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 the model, provided as [y](https://scikit-learn.org/stable/glossary.html#term-y)
. This is the approach taken in a [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier)
 or [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor)
 among other estimators.

target[#](https://scikit-learn.org/stable/glossary.html#term-target "Link to this term")

targets[#](https://scikit-learn.org/stable/glossary.html#term-targets "Link to this term")

The _dependent variable_ in [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised)
 (and [semisupervised](https://scikit-learn.org/stable/glossary.html#term-semisupervised)
) learning, passed as [y](https://scikit-learn.org/stable/glossary.html#term-y)
 to an estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method. Also known as _dependent variable_, _outcome variable_, _response variable_, _ground truth_ or _label_. Scikit-learn works with targets that have minimal structure: a class from a finite set, a finite real-valued number, multiple classes, or multiple numbers. See [Target Types](https://scikit-learn.org/stable/glossary.html#glossary-target-types)
.

transduction[#](https://scikit-learn.org/stable/glossary.html#term-transduction "Link to this term")

transductive[#](https://scikit-learn.org/stable/glossary.html#term-transductive "Link to this term")

A transductive (contrasted with [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)
) machine learning method is designed to model a specific dataset, but not to apply that model to unseen data. Examples include [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
, [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
 and [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
.

unlabeled[#](https://scikit-learn.org/stable/glossary.html#term-unlabeled "Link to this term")

unlabeled data[#](https://scikit-learn.org/stable/glossary.html#term-unlabeled-data "Link to this term")

Samples with an unknown ground truth when fitting; equivalently, [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values)
 in the [target](https://scikit-learn.org/stable/glossary.html#term-target)
. See also [semisupervised](https://scikit-learn.org/stable/glossary.html#term-semisupervised)
 and [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised)
 learning.

unsupervised[#](https://scikit-learn.org/stable/glossary.html#term-unsupervised "Link to this term")

unsupervised learning[#](https://scikit-learn.org/stable/glossary.html#term-unsupervised-learning "Link to this term")

Learning where the expected prediction (label or ground truth) is not available for each sample when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 the model, as in [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers)
 and [outlier detectors](https://scikit-learn.org/stable/glossary.html#term-outlier-detectors)
. Unsupervised estimators ignore any [y](https://scikit-learn.org/stable/glossary.html#term-y)
 passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Class APIs and Estimator Types[#](https://scikit-learn.org/stable/glossary.html#class-apis-and-estimator-types "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

classifier[#](https://scikit-learn.org/stable/glossary.html#term-classifier "Link to this term")

classifiers[#](https://scikit-learn.org/stable/glossary.html#term-classifiers "Link to this term")

A [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised)
 (or [semi-supervised](https://scikit-learn.org/stable/glossary.html#term-semi-supervised)
) [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
 with a finite set of discrete possible output values.

A classifier supports modeling some of [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
, [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
, [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
, or [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput)
 targets. Within scikit-learn, all classifiers support multi-class classification, defaulting to using a one-vs-rest strategy over the binary classification problem.

Classifiers must store a [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
 attribute after fitting, and inherit from [`base.ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
, which sets their corresponding [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags)
 correctly.

A classifier can be distinguished from other estimators with [`is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier")
.

A classifier must implement:

*   [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    
*   [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
    
*   [score](https://scikit-learn.org/stable/glossary.html#term-score)
    

It may also be appropriate to implement [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 and [predict\_log\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_log_proba)
.

clusterer[#](https://scikit-learn.org/stable/glossary.html#term-clusterer "Link to this term")

clusterers[#](https://scikit-learn.org/stable/glossary.html#term-clusterers "Link to this term")

A [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised)
 [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
 with a finite set of discrete output values.

A clusterer usually stores [labels\_](https://scikit-learn.org/stable/glossary.html#term-labels_)
 after fitting, and must do so if it is [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
.

A clusterer must implement:

*   [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    
*   [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
     if [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
    
*   [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
     if [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)
    

density estimator[#](https://scikit-learn.org/stable/glossary.html#term-density-estimator "Link to this term")

An [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised)
 estimation of input probability density function. Commonly used techniques are:

*   [Kernel Density Estimation](https://scikit-learn.org/stable/modules/density.html#kernel-density)
     - uses a kernel function, controlled by the bandwidth parameter to represent density;
    
*   [Gaussian mixture](https://scikit-learn.org/stable/modules/mixture.html#mixture)
     - uses mixture of Gaussian models to represent density.
    

estimator[#](https://scikit-learn.org/stable/glossary.html#term-estimator "Link to this term")

estimators[#](https://scikit-learn.org/stable/glossary.html#term-estimators "Link to this term")

An object which manages the estimation and decoding of a model. The model is estimated as a deterministic function of:

*   [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters)
     provided in object construction or with [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
    ;
    
*   the global [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "(in NumPy v2.5)")
     random state if the estimator’s [random\_state](https://scikit-learn.org/stable/glossary.html#term-random_state)
     parameter is set to None; and
    
*   any data or [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties)
     passed to the most recent call to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    , [fit\_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform)
     or [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
    , or data similarly passed in a sequence of calls to [partial\_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit)
    .
    

The estimated model is stored in public and private [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
 on the estimator instance, facilitating decoding through prediction and transformation methods.

Estimators must provide a [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method, and should provide [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
 and [get\_params](https://scikit-learn.org/stable/glossary.html#term-get_params)
, although these are usually provided by inheritance from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
.

The core functionality of some estimators may also be available as a [function](https://scikit-learn.org/stable/glossary.html#term-function)
.

feature extractor[#](https://scikit-learn.org/stable/glossary.html#term-feature-extractor "Link to this term")

feature extractors[#](https://scikit-learn.org/stable/glossary.html#term-feature-extractors "Link to this term")

A [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer)
 which takes input where each sample is not represented as an [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like)
 object of fixed length, and produces an [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like)
 object of [features](https://scikit-learn.org/stable/glossary.html#term-features)
 for each sample (and thus a 2-dimensional array-like for a set of samples). In other words, it (lossily) maps a non-rectangular data representation into [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular)
 data.

Feature extractors must implement at least:

*   [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    
*   [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
    
*   [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
    

meta-estimator[#](https://scikit-learn.org/stable/glossary.html#term-meta-estimator "Link to this term")

meta-estimators[#](https://scikit-learn.org/stable/glossary.html#term-meta-estimators "Link to this term")

metaestimator[#](https://scikit-learn.org/stable/glossary.html#term-metaestimator "Link to this term")

metaestimators[#](https://scikit-learn.org/stable/glossary.html#term-metaestimators "Link to this term")

An [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 which takes another estimator as a parameter. Examples include [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
, [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 and [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
.

In a meta-estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method, any contained estimators should be [cloned](https://scikit-learn.org/stable/glossary.html#term-cloned)
 before they are fit.

An exception to this is that an estimator may explicitly document that it accepts a pre-fitted estimator (e.g. using `prefit=True` in [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
). One known issue with this is that the pre-fitted estimator will lose its model if the meta-estimator is cloned. A meta-estimator should have `fit` called before prediction, even if all contained estimators are pre-fitted.

In cases where a meta-estimator’s primary behaviors (e.g. [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 or [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
 implementation) are functions of prediction/transformation methods of the provided _base estimator_ (or multiple base estimators), a meta-estimator should provide at least the standard methods provided by the base estimator. It may not be possible to identify which methods are provided by the underlying estimator until the meta-estimator has been [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
 (see also [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing)
), for which [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
 may help. It should also provide (or modify) the [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags)
 and [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
 attribute provided by the base estimator.

Meta-estimators should be careful to validate data as minimally as possible before passing it to an underlying estimator. This saves computation time, and may, for instance, allow the underlying estimator to easily work with data that is not [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular)
.

outlier detector[#](https://scikit-learn.org/stable/glossary.html#term-outlier-detector "Link to this term")

outlier detectors[#](https://scikit-learn.org/stable/glossary.html#term-outlier-detectors "Link to this term")

An [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised)
 binary [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
 which models the distinction between core and outlying samples.

Outlier detectors must implement:

*   [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    
*   [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
     if [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
    
*   [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
     if [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)
    

Inductive outlier detectors may also implement [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 to give a normalized inlier score where outliers have score below 0. [score\_samples](https://scikit-learn.org/stable/glossary.html#term-score_samples)
 may provide an unnormalized score per sample.

predictor[#](https://scikit-learn.org/stable/glossary.html#term-predictor "Link to this term")

predictors[#](https://scikit-learn.org/stable/glossary.html#term-predictors "Link to this term")

An [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 supporting [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 and/or [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
. This encompasses [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier)
, [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor)
, [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector)
 and [clusterer](https://scikit-learn.org/stable/glossary.html#term-clusterer)
.

In statistics, “predictors” refers to [features](https://scikit-learn.org/stable/glossary.html#term-features)
.

regressor[#](https://scikit-learn.org/stable/glossary.html#term-regressor "Link to this term")

regressors[#](https://scikit-learn.org/stable/glossary.html#term-regressors "Link to this term")

A [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised)
 (or [semi-supervised](https://scikit-learn.org/stable/glossary.html#term-semi-supervised)
) [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
 with [continuous](https://scikit-learn.org/stable/glossary.html#term-continuous)
 output values.

Regressors inherit from [`base.RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
, which sets their [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags)
 correctly.

A regressor can be distinguished from other estimators with [`is_regressor`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_regressor.html#sklearn.base.is_regressor "sklearn.base.is_regressor")
.

A regressor must implement:

*   [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    
*   [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
    
*   [score](https://scikit-learn.org/stable/glossary.html#term-score)
    

transformer[#](https://scikit-learn.org/stable/glossary.html#term-transformer "Link to this term")

transformers[#](https://scikit-learn.org/stable/glossary.html#term-transformers "Link to this term")

An estimator supporting [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
 and/or [fit\_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform)
. A purely [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
 transformer, such as [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
, may not implement `transform`.

vectorizer[#](https://scikit-learn.org/stable/glossary.html#term-vectorizer "Link to this term")

vectorizers[#](https://scikit-learn.org/stable/glossary.html#term-vectorizers "Link to this term")

See [feature extractor](https://scikit-learn.org/stable/glossary.html#term-feature-extractor)
.

There are further APIs specifically related to a small family of estimators, such as:

cross-validation splitter[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-splitter "Link to this term")

CV splitter[#](https://scikit-learn.org/stable/glossary.html#term-CV-splitter "Link to this term")

cross-validation generator[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-generator "Link to this term")

A non-estimator family of classes used to split a dataset into a sequence of train and test portions (see [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
), by providing [split](https://scikit-learn.org/stable/glossary.html#term-split)
 and [get\_n\_splits](https://scikit-learn.org/stable/glossary.html#term-get_n_splits)
 methods. Note that unlike estimators, these do not have [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 methods and do not provide [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
 or [get\_params](https://scikit-learn.org/stable/glossary.html#term-get_params)
. Parameter validation may be performed in `__init__`.

cross-validation estimator[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator "Link to this term")

An estimator that has built-in cross-validation capabilities to automatically select the best hyper-parameters (see the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
). Some example of cross-validation estimators are [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
 and [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
. Cross-validation estimators are named `EstimatorCV` and tend to be roughly equivalent to `GridSearchCV(Estimator(), ...)`. The advantage of using a cross-validation estimator over the canonical [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 class along with [grid search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
 is that they can take advantage of warm-starting by reusing precomputed results in the previous steps of the cross-validation process. This generally leads to speed improvements. An exception is the [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 class, which can instead perform efficient Leave-One-Out (LOO) CV. By default, all these estimators, apart from [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 with an LOO-CV, will be refitted on the full training dataset after finding the best combination of hyper-parameters.

scorer[#](https://scikit-learn.org/stable/glossary.html#term-scorer "Link to this term")

A non-estimator callable object which evaluates an estimator on given test data, returning a number. Unlike [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics)
, a greater returned number must correspond with a _better_ score. See [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
.

Further examples:

*   [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
    
*   [`gaussian_process.kernels.Kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel")
    
*   `tree.Criterion`
    

Metadata Routing[#](https://scikit-learn.org/stable/glossary.html#metadata-routing "Link to this heading")

-----------------------------------------------------------------------------------------------------------

consumer[#](https://scikit-learn.org/stable/glossary.html#term-consumer "Link to this term")

An object which consumes [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
. This object is usually an [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
, a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
, or a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
. Consuming metadata means using it in calculations, e.g. using [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
 to calculate a certain type of score. Being a consumer doesn’t mean that the object always receives a certain metadata, rather it means it can use it if it is provided.

metadata[#](https://scikit-learn.org/stable/glossary.html#term-metadata "Link to this term")

Data which is related to the given [X](https://scikit-learn.org/stable/glossary.html#term-X)
 and [y](https://scikit-learn.org/stable/glossary.html#term-y)
 data, but is not directly a part of the data, e.g. [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
 or [groups](https://scikit-learn.org/stable/glossary.html#term-groups)
, and is passed along to different objects and methods, e.g. to a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
 or a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
.

router[#](https://scikit-learn.org/stable/glossary.html#term-router "Link to this term")

An object which routes metadata to [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
. This object is usually a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
, e.g. [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 or [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
. Some routers can also be a consumer. This happens for example when a meta-estimator uses the given [groups](https://scikit-learn.org/stable/glossary.html#term-groups)
, and it also passes it along to some of its sub-objects, such as a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
.

Please refer to [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more information.

Callbacks[#](https://scikit-learn.org/stable/glossary.html#callbacks "Link to this heading")

---------------------------------------------------------------------------------------------

auto-propagated[#](https://scikit-learn.org/stable/glossary.html#term-auto-propagated "Link to this term")

autopropagated[#](https://scikit-learn.org/stable/glossary.html#term-autopropagated "Link to this term")

A [callback](https://scikit-learn.org/stable/glossary.html#term-callback)
 is auto-propagated if, when registered on a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
, it can be propagated to the sub-estimators of that meta-estimator. This propagation means that the callback gets automatically registered on the sub-estimators, and thus it will have its [hooks](https://scikit-learn.org/stable/glossary.html#term-hooks)
 called during their [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 too.

callback[#](https://scikit-learn.org/stable/glossary.html#term-callback "Link to this term")

callbacks[#](https://scikit-learn.org/stable/glossary.html#term-callbacks "Link to this term")

An object which can be registered on a compatible [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 to have its [hooks](https://scikit-learn.org/stable/glossary.html#term-hooks)
 called during the [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 of that estimator. Registering a callback on an estimator makes it possible to add functionalities to the fitting process, such as displaying a progress bar or logging a score at each step of the fitting. A callback can also interrupt the fitting, for example to perform early stopping.

hook[#](https://scikit-learn.org/stable/glossary.html#term-hook "Link to this term")

hooks[#](https://scikit-learn.org/stable/glossary.html#term-hooks "Link to this term")

The methods of a [callback](https://scikit-learn.org/stable/glossary.html#term-callback)
 which are called during the [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 of the estimator(s) the callback is registered on. The different hooks of a callback are:

*   [`setup`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.setup "sklearn.callback.FitCallback.setup")
     called once at the start of [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    .
    
*   [`on_fit_task_begin`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_begin "sklearn.callback.FitCallback.on_fit_task_begin")
     called at the beginning of each [fit task](https://scikit-learn.org/stable/glossary.html#term-fit-task)
    .
    
*   [`on_fit_task_end`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.on_fit_task_end "sklearn.callback.FitCallback.on_fit_task_end")
     called at the end of each [fit task](https://scikit-learn.org/stable/glossary.html#term-fit-task)
    .
    
*   [`teardown`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.FitCallback.html#sklearn.callback.FitCallback.teardown "sklearn.callback.FitCallback.teardown")
     called once at the end of [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    .
    

fit task[#](https://scikit-learn.org/stable/glossary.html#term-fit-task "Link to this term")

fit tasks[#](https://scikit-learn.org/stable/glossary.html#term-fit-tasks "Link to this term")

In the context of callbacks, a fit task is an arbitrary unit of work performed during the [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
 of an estimator. These tasks are typically an iteration of a loop, with nested loop corresponding to nested tasks. The tasks have an inherent tree structure, with the root task being the whole fitting process itself. For a more detailed description of the task tree, see the [task tree section](https://scikit-learn.org/stable/developers/callback_support.html#callback-task-definition)
 of the developer documentation on callbacks.

Please refer to the [Callbacks User Guide](https://scikit-learn.org/stable/callbacks.html#callbacks-user)
 for more information.

Target Types[#](https://scikit-learn.org/stable/glossary.html#target-types "Link to this heading")

---------------------------------------------------------------------------------------------------

binary[#](https://scikit-learn.org/stable/glossary.html#term-binary "Link to this term")

A classification problem consisting of two classes. A binary target may be represented as for a [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 problem but with only two labels. A binary decision function is represented as a 1d array.

Semantically, one class is often considered the “positive” class. Unless otherwise specified (e.g. using [pos\_label](https://scikit-learn.org/stable/glossary.html#term-pos_label)
 in [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics)
), we consider the class label with the greater value (numerically or lexicographically) as the positive class: of labels \[0, 1\], 1 is the positive class; of \[1, 2\], 2 is the positive class; of \[‘no’, ‘yes’\], ‘yes’ is the positive class; of \[‘no’, ‘YES’\], ‘no’ is the positive class. This affects the output of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
, for instance.

Note that a dataset sampled from a multiclass `y` or a continuous `y` may appear to be binary.

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘binary’ for binary input, or a similar array with only a single class present.

continuous[#](https://scikit-learn.org/stable/glossary.html#term-continuous "Link to this term")

A regression problem where each sample’s target is a finite floating point number represented as a 1-dimensional array of floats (or sometimes ints).

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘continuous’ for continuous input, but if the data is all integers, it will be identified as ‘multiclass’.

continuous multioutput[#](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput "Link to this term")

continuous multi-output[#](https://scikit-learn.org/stable/glossary.html#term-continuous-multi-output "Link to this term")

multioutput continuous[#](https://scikit-learn.org/stable/glossary.html#term-multioutput-continuous "Link to this term")

multi-output continuous[#](https://scikit-learn.org/stable/glossary.html#term-multi-output-continuous "Link to this term")

A regression problem where each sample’s target consists of `n_outputs` [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs)
, each one a finite floating point number, for a fixed int `n_outputs > 1` in a particular dataset.

Continuous multioutput targets are represented as multiple [continuous](https://scikit-learn.org/stable/glossary.html#term-continuous)
 targets, horizontally stacked into an array of shape `(n_samples, n_outputs)`.

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘continuous-multioutput’ for continuous multioutput input, but if the data is all integers, it will be identified as ‘multiclass-multioutput’.

multiclass[#](https://scikit-learn.org/stable/glossary.html#term-multiclass "Link to this term")

multi-class[#](https://scikit-learn.org/stable/glossary.html#term-multi-class "Link to this term")

A classification problem consisting of more than two classes. A multiclass target may be represented as a 1-dimensional array of strings or integers. A 2d column vector of integers (i.e. a single output in [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
 terms) is also accepted.

We do not officially support other orderable, hashable objects as class labels, even if estimators may happen to work when given classification targets of such type.

For semi-supervised classification, [unlabeled](https://scikit-learn.org/stable/glossary.html#term-unlabeled)
 samples should have the special label -1 in `y`.

Within scikit-learn, all estimators supporting binary classification also support multiclass classification, using One-vs-Rest by default.

A [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
 helps to canonicalize multiclass targets as integers.

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘multiclass’ for multiclass input. The user may also want to handle ‘binary’ input identically to ‘multiclass’.

multiclass multioutput[#](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput "Link to this term")

multi-class multi-output[#](https://scikit-learn.org/stable/glossary.html#term-multi-class-multi-output "Link to this term")

multioutput multiclass[#](https://scikit-learn.org/stable/glossary.html#term-multioutput-multiclass "Link to this term")

multi-output multi-class[#](https://scikit-learn.org/stable/glossary.html#term-multi-output-multi-class "Link to this term")

A classification problem where each sample’s target consists of `n_outputs` [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs)
, each a class label, for a fixed int `n_outputs > 1` in a particular dataset. Each output has a fixed set of available classes, and each sample is labeled with a class for each output. An output may be binary or multiclass, and in the case where all outputs are binary, the target is [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
.

Multiclass multioutput targets are represented as multiple [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 targets, horizontally stacked into an array of shape `(n_samples, n_outputs)`.

Note: For simplicity, we may not always support string class labels for multiclass multioutput, and integer class labels should be used.

[`multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
 provides estimators which estimate multi-output problems using multiple single-output estimators. This may not fully account for dependencies among the different outputs, which methods natively handling the multioutput case (e.g. decision trees, nearest neighbors, neural networks) may do better.

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘multiclass-multioutput’ for multiclass multioutput input.

multilabel[#](https://scikit-learn.org/stable/glossary.html#term-multilabel "Link to this term")

multi-label[#](https://scikit-learn.org/stable/glossary.html#term-multi-label "Link to this term")

A [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput)
 target where each output is [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
. This may be represented as a 2d (dense) array or sparse matrix of integers, such that each column is a separate binary target, where positive labels are indicated with 1 and negative labels are usually -1 or 0. Sparse multilabel targets are not supported everywhere that dense multilabel targets are supported.

Semantically, a multilabel target can be thought of as a set of labels for each sample. While not used internally, [`preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
 is provided as a utility to convert from a list of sets representation to a 2d array or sparse matrix. One-hot encoding a multiclass target with [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
 turns it into a multilabel problem.

[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will return ‘multilabel-indicator’ for multilabel input, whether sparse or dense.

multioutput[#](https://scikit-learn.org/stable/glossary.html#term-multioutput "Link to this term")

multi-output[#](https://scikit-learn.org/stable/glossary.html#term-multi-output "Link to this term")

A target where each sample has multiple classification/regression labels. See [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput)
 and [continuous multioutput](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput)
. We do not currently support modelling mixed classification and regression targets.

Methods[#](https://scikit-learn.org/stable/glossary.html#methods "Link to this heading")

-----------------------------------------------------------------------------------------

`decision_function`[#](https://scikit-learn.org/stable/glossary.html#term-decision_function "Link to this term")

In a fitted [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier)
 or [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector)
, predicts a “soft” score for each sample in relation to each class, rather than the “hard” categorical prediction produced by [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
. Its input is usually only some observed data, [X](https://scikit-learn.org/stable/glossary.html#term-X)
.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

Output conventions:

binary classification

A 1-dimensional array, where values strictly greater than zero indicate the positive class (i.e. the last class in [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
).

multiclass classification

A 2-dimensional array, where the row-wise arg-maximum is the predicted class. Columns are ordered according to [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

multilabel classification

Scikit-learn is inconsistent in its representation of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 decision functions. It may be represented one of two ways:

*   List of 2d arrays, each array of shape: (`n_samples`, 2), like in multiclass multioutput. List is of length `n_labels`.
    
*   Single 2d array of shape (`n_samples`, `n_labels`), with each ‘column’ in the array corresponding to the individual binary classification decisions. This is identical to the multiclass classification format, though its semantics differ: it should be interpreted, like in the binary case, by thresholding at 0.
    

multioutput classification

A list of 2d arrays, corresponding to each multiclass decision function.

outlier detection

A 1-dimensional array, where a value greater than or equal to zero indicates an inlier.

`fit`[#](https://scikit-learn.org/stable/glossary.html#term-fit "Link to this term")

The `fit` method is provided on every estimator. It usually takes some [samples](https://scikit-learn.org/stable/glossary.html#term-samples)
 `X`, [targets](https://scikit-learn.org/stable/glossary.html#term-targets)
 `y` if the model is supervised, and potentially other [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties)
 such as [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
. It should:

*   clear any prior [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
     stored on the estimator, unless [warm\_start](https://scikit-learn.org/stable/glossary.html#term-warm_start)
     is used;
    
*   validate and interpret any [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters)
    , ideally raising an error if invalid;
    
*   validate the input data;
    
*   estimate and store model attributes from the estimated parameters and provided data; and
    
*   return the now [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
     estimator to facilitate method chaining.
    

[Target Types](https://scikit-learn.org/stable/glossary.html#glossary-target-types)
 describes possible formats for `y`.

`fit_predict`[#](https://scikit-learn.org/stable/glossary.html#term-fit_predict "Link to this term")

Used especially for [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised)
, [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
 estimators, this fits the model and returns the predictions (similar to [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
) on the training data. In clusterers, these predictions are also stored in the [labels\_](https://scikit-learn.org/stable/glossary.html#term-labels_)
 attribute, and the output of `.fit_predict(X)` is usually equivalent to `.fit(X).predict(X)`. The parameters to `fit_predict` are the same as those to `fit`.

`fit_transform`[#](https://scikit-learn.org/stable/glossary.html#term-fit_transform "Link to this term")

A method on [transformers](https://scikit-learn.org/stable/glossary.html#term-transformers)
 which fits the estimator and returns the transformed training data. It takes parameters as in [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and its output should have the same shape as calling `.fit(X, ...).transform(X)`. There are nonetheless rare cases where `.fit_transform(X, ...)` and `.fit(X, ...).transform(X)` do not return the same value, wherein training data needs to be handled differently (due to model blending in stacked ensembles, for instance; such cases should be clearly documented). [Transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
 transformers may also provide `fit_transform` but not [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
.

One reason to implement `fit_transform` is that performing `fit` and `transform` separately would be less efficient than together. [`base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
 provides a default implementation, providing a consistent interface across transformers where `fit_transform` is or is not specialized.

In [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)
 learning – where the goal is to learn a generalized model that can be applied to new data – users should be careful not to apply `fit_transform` to the entirety of a dataset (i.e. training and test data together) before further modelling, as this results in [data leakage](https://scikit-learn.org/stable/glossary.html#term-data-leakage)
.

`get_feature_names_out`[#](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out "Link to this term")

Primarily for [feature extractors](https://scikit-learn.org/stable/glossary.html#term-feature-extractors)
, but also used for other transformers to provide string names for each column in the output of the estimator’s [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
 method. It outputs an array of strings and may take an array-like of strings as input, corresponding to the names of input columns from which output column names can be generated. If `input_features` is not passed in, then the `feature_names_in_` attribute will be used. If the `feature_names_in_` attribute is not defined, then the input names are named `[x0, x1, ..., x(n_features_in_ - 1)]`.

`get_n_splits`[#](https://scikit-learn.org/stable/glossary.html#term-get_n_splits "Link to this term")

On a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
 (not an estimator), returns the number of elements one would get if iterating through the return value of [split](https://scikit-learn.org/stable/glossary.html#term-split)
 given the same parameters. Takes the same parameters as split.

`get_params`[#](https://scikit-learn.org/stable/glossary.html#term-get_params "Link to this term")

Gets all [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters)
, and their values, that can be set using [set\_params](https://scikit-learn.org/stable/glossary.html#term-set_params)
. A parameter `deep` can be used, when set to False to only return those parameters not including `__`, i.e. not due to indirection via contained estimators.

Most estimators adopt the definition from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, which simply adopts the parameters defined for `__init__`. [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
, among others, reimplements `get_params` to declare the estimators named in its `steps` parameters as themselves being parameters.

`partial_fit`[#](https://scikit-learn.org/stable/glossary.html#term-partial_fit "Link to this term")

Facilitates fitting an estimator in an online fashion. Unlike `fit`, repeatedly calling `partial_fit` does not clear the model, but updates it with the data provided. The portion of data provided to `partial_fit` may be called a mini-batch. Each mini-batch must be of consistent shape, etc. In iterative estimators, `partial_fit` often only performs a single iteration.

`partial_fit` may also be used for [out-of-core](https://scikit-learn.org/stable/glossary.html#term-out-of-core)
 learning, although usually limited to the case where learning can be performed online, i.e. the model is usable after each `partial_fit` and there is no separate processing needed to finalize the model. [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
 introduces the convention that calling `partial_fit(X)` will produce a model that is not finalized, but the model can be finalized by calling `partial_fit()` i.e. without passing a further mini-batch.

Generally, estimator parameters should not be modified between calls to `partial_fit`, although `partial_fit` should validate them as well as the new mini-batch of data. In contrast, `warm_start` is used to repeatedly fit the same estimator with the same data but varying parameters.

Like `fit`, `partial_fit` should return the estimator object.

To clear the model, a new estimator should be constructed, for instance with [`base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
.

Note: Using `partial_fit` after `fit` results in undefined behavior.

`predict`[#](https://scikit-learn.org/stable/glossary.html#term-predict "Link to this term")

Makes a prediction for each sample, usually only taking [X](https://scikit-learn.org/stable/glossary.html#term-X)
 as input (but see under regressor output conventions below). In a [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier)
 or [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor)
, this prediction is in the same target space used in fitting (e.g. one of {‘red’, ‘amber’, ‘green’} if the `y` in fitting consisted of these strings). Despite this, even when `y` passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 is a list or other array-like, the output of `predict` should always be an array or sparse matrix. In a [clusterer](https://scikit-learn.org/stable/glossary.html#term-clusterer)
 or [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector)
 the prediction is an integer.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

Output conventions:

classifier

An array of shape `(n_samples,)` `(n_samples, n_outputs)`. [Multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 data may be represented as a sparse matrix if a sparse matrix was used in fitting. Each element should be one of the values in the classifier’s [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
 attribute.

clusterer

An array of shape `(n_samples,)` where each value is from 0 to `n_clusters - 1` if the corresponding sample is clustered, and -1 if the sample is not clustered, as in [`cluster.dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan")
.

outlier detector

An array of shape `(n_samples,)` where each value is -1 for an outlier and 1 otherwise.

regressor

A numeric array of shape `(n_samples,)`, usually float64. Some regressors have extra options in their `predict` method, allowing them to return standard deviation (`return_std=True`) or covariance (`return_cov=True`) relative to the predicted value. In this case, the return value is a tuple of arrays corresponding to (prediction mean, std, cov) as required.

`predict_log_proba`[#](https://scikit-learn.org/stable/glossary.html#term-predict_log_proba "Link to this term")

The natural logarithm of the output of [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
, provided to facilitate numerical stability.

`predict_proba`[#](https://scikit-learn.org/stable/glossary.html#term-predict_proba "Link to this term")

A method in [classifiers](https://scikit-learn.org/stable/glossary.html#term-classifiers)
 and [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers)
 that can return probability estimates for each class/cluster. Its input is usually only some observed data, [X](https://scikit-learn.org/stable/glossary.html#term-X)
.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

Output conventions are like those for [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 except in the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 classification case, where one column is output for each class (while `decision_function` outputs a 1d array). For binary and multiclass predictions, each row should add to 1.

Like other methods, `predict_proba` should only be present when the estimator can make probabilistic predictions (see [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing)
). This means that the presence of the method may depend on estimator parameters (e.g. in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
) or training data (e.g. in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
) and may only appear after fitting.

`score`[#](https://scikit-learn.org/stable/glossary.html#term-score "Link to this term")

A method on an estimator, usually a [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
, which evaluates its predictions on a given dataset, and returns a single numerical score. A greater return value should indicate better predictions; accuracy is used for classifiers and R^2 for regressors by default.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

Some estimators implement a custom, estimator-specific score function, often the likelihood of the data under the model.

`score_samples`[#](https://scikit-learn.org/stable/glossary.html#term-score_samples "Link to this term")

A method that returns a score for each given sample. The exact definition of _score_ varies from one class to another. In the case of density estimation, it can be the log density model on the data, and in the case of outlier detection, it can be the opposite of the outlier factor of the data.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

`set_params`[#](https://scikit-learn.org/stable/glossary.html#term-set_params "Link to this term")

Available in any estimator, takes keyword arguments corresponding to keys in [get\_params](https://scikit-learn.org/stable/glossary.html#term-get_params)
. Each is provided a new value to assign such that calling `get_params` after `set_params` will reflect the changed [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters)
. Most estimators use the implementation in [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, which handles nested parameters and otherwise sets the parameter as an attribute on the estimator. The method is overridden in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 and related estimators.

`split`[#](https://scikit-learn.org/stable/glossary.html#term-split "Link to this term")

On a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
 (not an estimator), this method accepts parameters ([X](https://scikit-learn.org/stable/glossary.html#term-X)
, [y](https://scikit-learn.org/stable/glossary.html#term-y)
, [groups](https://scikit-learn.org/stable/glossary.html#term-groups)
), where all may be optional, and returns an iterator over `(train_idx, test_idx)` pairs. Each of {train,test}\_idx is a 1d integer array, with values from 0 from `X.shape[0] - 1` of any length, such that no values appear in both some `train_idx` and its corresponding `test_idx`.

`transform`[#](https://scikit-learn.org/stable/glossary.html#term-transform "Link to this term")

In a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer)
, transforms the input, usually only [X](https://scikit-learn.org/stable/glossary.html#term-X)
, into some transformed space (conventionally notated as [Xt](https://scikit-learn.org/stable/glossary.html#term-Xt)
). Output is an array or sparse matrix of length [n\_samples](https://scikit-learn.org/stable/glossary.html#term-n_samples)
 and with the number of columns fixed after [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting)
.

If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
, calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
.

Parameters[#](https://scikit-learn.org/stable/glossary.html#parameters "Link to this heading")

-----------------------------------------------------------------------------------------------

These common parameter names, specifically used in estimator construction (see concept [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
), sometimes also appear as parameters of functions or non-estimator constructors.

`class_weight`[#](https://scikit-learn.org/stable/glossary.html#term-class_weight "Link to this term")

Used to specify sample weights when fitting classifiers as a function of the [target](https://scikit-learn.org/stable/glossary.html#term-target)
 class. Where [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
 is also supported and given, it is multiplied by the `class_weight` contribution. Similarly, where `class_weight` is used in a [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
 (including [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
) tasks, the weights are multiplied across outputs (i.e. columns of `y`).

By default, all samples have equal weight such that classes are effectively weighted by their prevalence in the training data. This could be achieved explicitly with `class_weight={label1: 1, label2: 1, ...}` for all class labels.

More generally, `class_weight` is specified as a dict mapping class labels to weights (`{class_label: weight}`), such that each sample of the named class is given that weight.

`class_weight='balanced'` can be used to give all classes equal weight by giving each sample a weight inversely related to its class’s prevalence in the training data: `n_samples / (n_classes * np.bincount(y))`. Class weights will be used differently depending on the algorithm: for linear models (such as linear SVM or logistic regression), the class weights will alter the loss function by weighting the loss of each sample by its class weight. For tree-based algorithms, the class weights will be used for reweighting the splitting criterion. **Note** however that this rebalancing does not take the weight of samples in each class into account.

For multioutput classification, a list of dicts is used to specify weights for each output. For example, for four-class multilabel classification weights should be `[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}]` instead of `[{1:1}, {2:5}, {3:1}, {4:1}]`.

The `class_weight` parameter is validated and interpreted with [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
.

`cv`[#](https://scikit-learn.org/stable/glossary.html#term-cv "Link to this term")

Determines a cross validation splitting strategy, as used in cross-validation based routines. `cv` is also available in estimators such as [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
 or [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
 which use the predictions of one estimator as training data for another, to not overfit the training supervision.

Possible inputs for `cv` are usually:

*   An integer, specifying the number of folds in K-fold cross validation. K-fold will be stratified over classes if the estimator is a classifier (determined by [`base.is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier")
    ) and the [targets](https://scikit-learn.org/stable/glossary.html#term-targets)
     may represent a binary or multiclass (but not multioutput) classification problem (determined by [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
    ).
    
*   A [cross-validation splitter](https://scikit-learn.org/stable/glossary.html#term-cross-validation-splitter)
     instance. Refer to the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
     for splitters available within Scikit-learn.
    
*   An iterable yielding train/test splits.
    

With some exceptions (especially where not using cross validation at all is an option), the default is 5-fold.

`cv` values are validated and interpreted with [`model_selection.check_cv`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv")
.

`kernel`[#](https://scikit-learn.org/stable/glossary.html#term-kernel "Link to this term")

Specifies the kernel function to be used by Kernel Method algorithms. For example, the estimators [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
 both have a `kernel` parameter that takes the name of the kernel to use as string or a callable kernel function used to compute the kernel matrix. For more reference, see the [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)
 and the [Gaussian Processes](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process)
 user guides.

`max_iter`[#](https://scikit-learn.org/stable/glossary.html#term-max_iter "Link to this term")

For estimators involving iterative optimization, this determines the maximum number of iterations to be performed in [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. If `max_iter` iterations are run without convergence, a [`exceptions.ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
 should be raised. Note that the interpretation of “a single iteration” is inconsistent across estimators: some, but not all, use it to mean a single epoch (i.e. a pass over every sample in the data).

`memory`[#](https://scikit-learn.org/stable/glossary.html#term-memory "Link to this term")

Some estimators make use of [`joblib.Memory`](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "(in joblib v1.7)")
 to store partial solutions during fitting. Thus when `fit` is called again, those partial solutions have been memoized and can be reused.

A `memory` parameter can be specified as a string with a path to a directory, or a [`joblib.Memory`](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "(in joblib v1.7)")
 instance (or an object with a similar interface, i.e. a `cache` method) can be used.

`memory` values are validated and interpreted with [`utils.validation.check_memory`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "sklearn.utils.validation.check_memory")
.

`metric`[#](https://scikit-learn.org/stable/glossary.html#term-metric "Link to this term")

As a parameter, this is the scheme for determining the distance between two data points. See [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. In practice, for some algorithms, an improper distance metric (one that does not obey the triangle inequality, such as Cosine Distance) may be used.

Note: Hierarchical clustering uses `affinity` with this meaning.

We also use _metric_ to refer to [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics)
, but avoid using this sense as a parameter name.

`n_components`[#](https://scikit-learn.org/stable/glossary.html#term-n_components "Link to this term")

The number of features which a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer)
 should transform the input into. See [components\_](https://scikit-learn.org/stable/glossary.html#term-components_)
 for the special case of affine projection.

`n_iter_no_change`[#](https://scikit-learn.org/stable/glossary.html#term-n_iter_no_change "Link to this term")

Number of iterations with no improvement to wait before stopping the iterative procedure. This is also known as a _patience_ parameter. It is typically used with [early stopping](https://scikit-learn.org/stable/glossary.html#term-early-stopping)
 to avoid stopping too early.

`n_jobs`[#](https://scikit-learn.org/stable/glossary.html#term-n_jobs "Link to this term")

This parameter is used to specify how many concurrent processes or threads should be used for routines that are parallelized with [joblib](https://scikit-learn.org/stable/glossary.html#term-joblib)
.

`n_jobs` is an integer, specifying the maximum number of concurrently running workers. If 1 is given, no joblib parallelism is used at all, which is useful for debugging. If set to -1, all CPUs are used. For `n_jobs` below -1, (n\_cpus + 1 + n\_jobs) are used. For example with `n_jobs=-2`, all CPUs but one are used.

`n_jobs` is `None` by default, which means _unset_; it will generally be interpreted as `n_jobs=1`, unless the current [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 backend context specifies otherwise.

Note that even if `n_jobs=1`, low-level parallelism (via Numpy and OpenMP) might be used in some configuration.

For more details on the use of `joblib` and its interactions with scikit-learn, please refer to our [parallelism notes](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
.

`pos_label`[#](https://scikit-learn.org/stable/glossary.html#term-pos_label "Link to this term")

Value with which positive labels must be encoded in binary classification problems in which the positive class is not assumed. This value is typically required to compute asymmetric evaluation metrics such as precision and recall.

`random_state`[#](https://scikit-learn.org/stable/glossary.html#term-random_state "Link to this term")

Whenever randomization is part of a Scikit-learn algorithm, a `random_state` parameter may be provided to control the random number generator used. Note that the mere presence of `random_state` doesn’t mean that randomization is always used, as it may be dependent on another parameter, e.g. `shuffle`, being set.

The passed value will have an effect on the reproducibility of the results returned by the function ([fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, [split](https://scikit-learn.org/stable/glossary.html#term-split)
, or any other function like [`k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means")
). `random_state`’s value may be:

None (default)

Use the global random state instance from [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "(in NumPy v2.5)")
. Calling the function multiple times will reuse the same instance, and will produce different results.

An integer

Use a new random number generator seeded by the given integer. Using an int will produce the same results across different calls. However, it may be worthwhile checking that your results are stable across a number of different distinct random seeds. Popular integer random seeds are 0 and [42](https://en.wikipedia.org/wiki/Answer_to_the_Ultimate_Question_of_Life%2C_the_Universe%2C_and_Everything)
. Integer values must be in the range `[0, 2**32 - 1]`.

A [`numpy.random.RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.5)")
 instance

Use the provided random state, only affecting other users of that same random state instance. Calling the function multiple times will reuse the same instance, and will produce different results.

[`utils.check_random_state`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
 is used internally to validate the input `random_state` and return a [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.5)")
 instance.

For more details on how to control the randomness of scikit-learn objects and avoid common pitfalls, you may refer to [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness)
.

`scoring`[#](https://scikit-learn.org/stable/glossary.html#term-scoring "Link to this term")

Depending on the object, can specify:

*   the score function to be maximized (usually by [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
    ),
    
*   the multiple score functions to be reported,
    
*   the score function to be used to check early stopping, or
    
*   for visualization related objects, the score function to output or plot
    

The score function can be a string accepted by [`metrics.get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")
 or a callable [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
, not to be confused with an [evaluation metric](https://scikit-learn.org/stable/glossary.html#term-evaluation-metric)
, as the latter have a more diverse API. `scoring` may also be set to None, in which case the estimator’s [score](https://scikit-learn.org/stable/glossary.html#term-score)
 method is used. See [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
 in the User Guide.

Where multiple metrics can be evaluated, `scoring` may be given either as a list of unique strings, a dictionary with names as keys and callables as values or a callable that returns a dictionary. Note that this does _not_ specify which score function is to be maximized, and another parameter such as `refit` may be used for this purpose.

The `scoring` parameter is validated and interpreted using [`metrics.check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring")
.

`verbose`[#](https://scikit-learn.org/stable/glossary.html#term-verbose "Link to this term")

Logging is not handled very consistently in Scikit-learn at present, but when it is provided as an option, the `verbose` parameter is usually available to choose no logging (set to False). Any True value should enable some logging, but larger integers (e.g. above 10) may be needed for full verbosity. Verbose logs are usually printed to Standard Output. Estimators should not produce any output on Standard Output with the default `verbose` setting.

`warm_start`[#](https://scikit-learn.org/stable/glossary.html#term-warm_start "Link to this term")

When fitting an estimator repeatedly on the same dataset, but for multiple parameter values (such as to find the value maximizing performance as in [grid search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
), it may be possible to reuse aspects of the model learned from the previous parameter value, saving time. When `warm_start` is true, the existing [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
 model [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
 are used to initialize the new model in a subsequent call to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Note that this is only applicable for some models and some parameters, and even some orders of parameter values. In general, there is an interaction between `warm_start` and the parameter controlling the number of iterations of the estimator.

For estimators imported from [`ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
, `warm_start` will interact with `n_estimators` or `max_iter`. For these models, the number of iterations, reported via `len(estimators_)` or `n_iter_`, corresponds the total number of estimators/iterations learnt since the initialization of the model. Thus, if a model was already initialized with `N` estimators, and `fit` is called with `n_estimators` or `max_iter` set to `M`, the model will train `M - N` new estimators.

Other models, usually using gradient-based solvers, have a different behavior. They all expose a `max_iter` parameter. The reported `n_iter_` corresponds to the number of iterations done during the last call to `fit` and will be at most `max_iter`. Thus, we do not consider the state of the estimator since the initialization.

[partial\_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit)
 also retains the model between calls, but differs: with `warm_start` the parameters change and the data is (more-or-less) constant across calls to `fit`; with `partial_fit`, the mini-batch of data changes and model parameters stay fixed.

There are cases where you want to use `warm_start` to fit on different, but closely related data. For example, one may initially fit to a subset of the data, then fine-tune the parameter search on the full dataset. For classification, all data in a sequence of `warm_start` calls to `fit` must include samples from each class.

Attributes[#](https://scikit-learn.org/stable/glossary.html#attributes "Link to this heading")

-----------------------------------------------------------------------------------------------

See concept [attribute](https://scikit-learn.org/stable/glossary.html#term-attribute)
.

`classes_`[#](https://scikit-learn.org/stable/glossary.html#term-classes_ "Link to this term")

A list of class labels known to the [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier)
, mapping each label to a numerical index used in the model representation our output. For instance, the array output from [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 has columns aligned with `classes_`. For [multi-output](https://scikit-learn.org/stable/glossary.html#term-multi-output)
 classifiers, `classes_` should be a list of lists, with one class listing for each output. For each output, the classes should be sorted (numerically, or lexicographically for strings).

`classes_` and the mapping to indices is often managed with [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
.

`components_`[#](https://scikit-learn.org/stable/glossary.html#term-components_ "Link to this term")

An affine transformation matrix of shape `(n_components, n_features)` used in many linear [transformers](https://scikit-learn.org/stable/glossary.html#term-transformers)
 where [n\_components](https://scikit-learn.org/stable/glossary.html#term-n_components)
 is the number of output features and [n\_features](https://scikit-learn.org/stable/glossary.html#term-n_features)
 is the number of input features.

See also [coef\_](https://scikit-learn.org/stable/glossary.html#term-coef_)
 which is a similar attribute for linear predictors.

`coef_`[#](https://scikit-learn.org/stable/glossary.html#term-coef_ "Link to this term")

The weight/coefficient matrix of a generalized linear model [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
, of shape `(n_features,)` for binary classification and single-output regression, `(n_classes, n_features)` for multiclass classification and `(n_targets, n_features)` for multi-output regression. Note this does not include the intercept (or bias) term, which is stored in `intercept_`.

When available, `feature_importances_` is not usually provided as well, but can be calculated as the norm of each feature’s entry in `coef_`.

See also [components\_](https://scikit-learn.org/stable/glossary.html#term-components_)
 which is a similar attribute for linear transformers.

`embedding_`[#](https://scikit-learn.org/stable/glossary.html#term-embedding_ "Link to this term")

An embedding of the training data in [manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold)
 estimators, with shape `(n_samples, n_components)`, identical to the output of [fit\_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform)
. See also [labels\_](https://scikit-learn.org/stable/glossary.html#term-labels_)
.

`n_iter_`[#](https://scikit-learn.org/stable/glossary.html#term-n_iter_ "Link to this term")

The number of iterations actually performed when fitting an iterative estimator that may stop upon convergence. See also [max\_iter](https://scikit-learn.org/stable/glossary.html#term-max_iter)
.

`feature_importances_`[#](https://scikit-learn.org/stable/glossary.html#term-feature_importances_ "Link to this term")

A vector of shape `(n_features,)` available in some [predictors](https://scikit-learn.org/stable/glossary.html#term-predictors)
 to provide a relative measure of the importance of each feature in the predictions of the model.

`labels_`[#](https://scikit-learn.org/stable/glossary.html#term-labels_ "Link to this term")

A vector containing a cluster label for each sample of the training data in [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers)
, identical to the output of [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
. See also [embedding\_](https://scikit-learn.org/stable/glossary.html#term-embedding_)
.

Data and sample properties[#](https://scikit-learn.org/stable/glossary.html#data-and-sample-properties "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

See concept [sample property](https://scikit-learn.org/stable/glossary.html#term-sample-property)
.

`groups`[#](https://scikit-learn.org/stable/glossary.html#term-groups "Link to this term")

Used in cross-validation routines to identify samples that are correlated. Each value is an identifier such that, in a supporting [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
, samples from some `groups` value may not appear in both a training set and its corresponding test set. See [Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#group-cv)
.

`sample_weight`[#](https://scikit-learn.org/stable/glossary.html#term-sample_weight "Link to this term")

A weight for each data point. Intuitively, if all weights are integers, using them in an estimator or a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
 is like duplicating each data point as many times as the weight value. Weights can also be specified as floats, and can have the same effect as above, as many estimators and scorers are scale invariant. For example, weights `[1, 2, 3]` would be equivalent to weights `[0.1, 0.2, 0.3]` as they differ by a constant factor of 10. Note however that several estimators are not invariant to the scale of weights.

`sample_weight` can be both an argument of the estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method for model training or a parameter of a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
 for model evaluation. These callables are said to _consume_ the sample weights while other components of scikit-learn can _route_ the weights to the underlying estimators or scorers (see [Metadata Routing](https://scikit-learn.org/stable/glossary.html#glossary-metadata-routing)
).

Weighting samples can be useful in several contexts. For instance, if the training data is not uniformly sampled from the target population, it can be corrected by weighting the training data points based on the [inverse probability](https://en.wikipedia.org/wiki/Inverse_probability_weighting)
 of their selection for training (e.g. inverse propensity weighting).

Some model hyper-parameters are expressed in terms of a discrete number of data points in a region of the feature space. When fitting with sample weights, a count of data points is often automatically converted to a sum of their weights, but this is not always the case. Please refer to the model docstring for details.

In classification, weights can also be specified for all samples belonging to a given target class with the [class\_weight](https://scikit-learn.org/stable/glossary.html#term-class_weight)
 estimator [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)
. If both `sample_weight` and `class_weight` are provided, the final weight assigned to a sample is the product of the two.

At the time of writing (version 1.8), not all scikit-learn estimators correctly implement the weight-repetition equivalence property. The [#16298 meta issue](https://github.com/scikit-learn/scikit-learn/issues/16298)
 tracks ongoing work to detect and fix remaining discrepancies.

Furthermore, some estimators have a stochastic fit method. For instance, [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 depends on a random initialization, bagging models randomly resample from the training data, etc. In this case, the sample weight-repetition equivalence property described above does not hold exactly. However, it should hold at least in expectation over the randomness of the fitting procedure.

`X`[#](https://scikit-learn.org/stable/glossary.html#term-X "Link to this term")

Denotes data that is observed at training and prediction time, used as independent variables in learning. The notation is uppercase to denote that it is ordinarily a matrix (see [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular)
). When a matrix, each sample may be represented by a [feature](https://scikit-learn.org/stable/glossary.html#term-feature)
 vector, or a vector of [precomputed](https://scikit-learn.org/stable/glossary.html#term-precomputed)
 (dis)similarity with each training sample. `X` may also not be a matrix, and may require a [feature extractor](https://scikit-learn.org/stable/glossary.html#term-feature-extractor)
 or a [pairwise metric](https://scikit-learn.org/stable/glossary.html#term-pairwise-metric)
 to turn it into one before learning a model.

`Xt`[#](https://scikit-learn.org/stable/glossary.html#term-Xt "Link to this term")

Shorthand for “transformed [X](https://scikit-learn.org/stable/glossary.html#term-X)
”.

`y`[#](https://scikit-learn.org/stable/glossary.html#term-y "Link to this term")

`Y`[#](https://scikit-learn.org/stable/glossary.html#term-Y "Link to this term")

Denotes data that may be observed at training time as the dependent variable in learning, but which is unavailable at prediction time, and is usually the [target](https://scikit-learn.org/stable/glossary.html#term-target)
 of prediction. The notation may be uppercase to denote that it is a matrix, representing [multi-output](https://scikit-learn.org/stable/glossary.html#term-multi-output)
 targets, for instance; but usually we use `y` and sometimes do so even when multiple outputs are assumed.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)