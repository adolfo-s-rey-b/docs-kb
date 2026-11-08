[Skip to main content](https://scikit-learn.org/stable/api/sklearn.utils.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.utils.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.utils.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.utils.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.utils.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.utils.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.utils.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.utils.html)

Collapse Sidebar Expand Sidebar

sklearn.utils[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "Link to this heading")

=====================================================================================================================

Various utilities to help with development.

**Developer guide.** See the [Utilities for Developers](https://scikit-learn.org/stable/developers/utilities.html#developers-utils)
 section for further details.

|     |     |
| --- | --- |
| [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch") | Container object exposing keys as attributes. |
| [`_safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing") | Return rows, items or columns of X using indices. |
| [`as_float_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#sklearn.utils.as_float_array "sklearn.utils.as_float_array") | Convert an array-like to an array of floats. |
| [`assert_all_finite`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html#sklearn.utils.assert_all_finite "sklearn.utils.assert_all_finite") | Throw a ValueError if X contains NaN or infinity. |
| [`deprecated`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated "sklearn.utils.deprecated") | Decorator to mark a function or class as deprecated. |
| [`estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr") | Build an HTML representation of an estimator. |
| [`gen_batches`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#sklearn.utils.gen_batches "sklearn.utils.gen_batches") | Generator to create slices containing `batch_size` elements from 0 to `n`. |
| [`gen_even_slices`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "sklearn.utils.gen_even_slices") | Generator to create `n_packs` evenly spaced slices going up to `n`. |
| [`indexable`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html#sklearn.utils.indexable "sklearn.utils.indexable") | Make arrays indexable for cross-validation. |
| [`murmurhash3_32`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html#sklearn.utils.murmurhash3_32 "sklearn.utils.murmurhash3_32") | Compute the 32bit murmurhash3 of key at seed. |
| [`resample`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#sklearn.utils.resample "sklearn.utils.resample") | Resample arrays or sparse matrices in a consistent way. |
| [`safe_mask`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html#sklearn.utils.safe_mask "sklearn.utils.safe_mask") | Return an indexing mask compatible with X. |
| [`safe_sqr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html#sklearn.utils.safe_sqr "sklearn.utils.safe_sqr") | Element wise squaring of array-likes and sparse matrices. |
| [`shuffle`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle") | Shuffle arrays or sparse matrices in a consistent way. |
| [`Tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils.Tags") | Tags for the estimator. |
| [`InputTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.InputTags.html#sklearn.utils.InputTags "sklearn.utils.InputTags") | Tags for the input data. |
| [`TargetTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TargetTags.html#sklearn.utils.TargetTags "sklearn.utils.TargetTags") | Tags for the target data. |
| [`ClassifierTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#sklearn.utils.ClassifierTags "sklearn.utils.ClassifierTags") | Tags for the classifier. |
| [`RegressorTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.RegressorTags.html#sklearn.utils.RegressorTags "sklearn.utils.RegressorTags") | Tags for the regressor. |
| [`TransformerTags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.TransformerTags.html#sklearn.utils.TransformerTags "sklearn.utils.TransformerTags") | Tags for the transformer. |
| [`get_tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html#sklearn.utils.get_tags "sklearn.utils.get_tags") | Get estimator tags. |

Input and parameter validation[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.validation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Functions to validate input and parameters within scikit-learn estimators.

|     |     |
| --- | --- |
| [`check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y") | Input validation for standard estimators. |
| [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array") | Input validation on an array, list, sparse matrix or similar. |
| [`check_consistent_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#sklearn.utils.check_consistent_length "sklearn.utils.check_consistent_length") | Check that all arrays have consistent first dimensions. |
| [`check_random_state`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state") | Turn seed into an np.random.RandomState instance. |
| [`check_scalar`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#sklearn.utils.check_scalar "sklearn.utils.check_scalar") | Validate scalar parameters type and value. |
| [`validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted") | Perform is\_fitted validation for estimator. |
| [`validation.check_memory`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "sklearn.utils.validation.check_memory") | Check that `memory` is joblib.Memory-like. |
| [`validation.check_symmetric`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html#sklearn.utils.validation.check_symmetric "sklearn.utils.validation.check_symmetric") | Make sure that array is 2D, square and symmetric. |
| [`validation.column_or_1d`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#sklearn.utils.validation.column_or_1d "sklearn.utils.validation.column_or_1d") | Ravel column or 1d numpy array, else raises an error. |
| [`validation.has_fit_parameter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html#sklearn.utils.validation.has_fit_parameter "sklearn.utils.validation.has_fit_parameter") | Check whether the estimator's fit method supports the given parameter. |
| [`validation.validate_data`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data") | Validate input data and set or check feature names and counts of the input. |

Meta-estimators[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.metaestimators "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Utilities for meta-estimators.

|     |     |
| --- | --- |
| [`metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if") | An attribute that is available only if check returns a truthy value. |

Weight handling based on class labels[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.class_weight "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Utilities for handling weights based on class labels.

|     |     |
| --- | --- |
| [`class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight") | Estimate class weights for unbalanced datasets. |
| [`class_weight.compute_sample_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#sklearn.utils.class_weight.compute_sample_weight "sklearn.utils.class_weight.compute_sample_weight") | Estimate sample weights by class for unbalanced datasets. |

Dealing with multiclass target in classifiers[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.multiclass "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilities to handle multiclass/multioutput target in classifiers.

|     |     |
| --- | --- |
| [`multiclass.is_multilabel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#sklearn.utils.multiclass.is_multilabel "sklearn.utils.multiclass.is_multilabel") | Check if `y` is in a multilabel format. |
| [`multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") | Determine the type of data indicated by the target. |
| [`multiclass.unique_labels`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#sklearn.utils.multiclass.unique_labels "sklearn.utils.multiclass.unique_labels") | Extract an ordered array of unique labels. |

Optimal mathematical operations[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.extmath "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Utilities to perform optimal mathematical operations in scikit-learn.

|     |     |
| --- | --- |
| [`extmath.density`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "sklearn.utils.extmath.density") | Compute density of a sparse vector. |
| [`extmath.fast_logdet`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html#sklearn.utils.extmath.fast_logdet "sklearn.utils.extmath.fast_logdet") | Compute logarithm of determinant of a square matrix. |
| [`extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder") | Compute an orthonormal matrix whose range approximates the range of A. |
| [`extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd") | Compute a truncated randomized SVD. |
| [`extmath.safe_sparse_dot`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "sklearn.utils.extmath.safe_sparse_dot") | Dot product that handle the sparse matrix case correctly. |
| [`extmath.weighted_mode`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html#sklearn.utils.extmath.weighted_mode "sklearn.utils.extmath.weighted_mode") | Return an array of the weighted modal (most common) value in the passed array. |

Working with sparse matrices and arrays[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.sparsefuncs "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

A collection of utilities to work with sparse matrices and arrays.

|     |     |
| --- | --- |
| [`sparsefuncs.incr_mean_variance_axis`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.incr_mean_variance_axis.html#sklearn.utils.sparsefuncs.incr_mean_variance_axis "sklearn.utils.sparsefuncs.incr_mean_variance_axis") | Compute incremental mean and variance along an axis on a CSR or CSC matrix. |
| [`sparsefuncs.inplace_column_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html#sklearn.utils.sparsefuncs.inplace_column_scale "sklearn.utils.sparsefuncs.inplace_column_scale") | Inplace column scaling of a CSC/CSR matrix. |
| [`sparsefuncs.inplace_csr_column_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_csr_column_scale.html#sklearn.utils.sparsefuncs.inplace_csr_column_scale "sklearn.utils.sparsefuncs.inplace_csr_column_scale") | Inplace column scaling of a CSR matrix. |
| [`sparsefuncs.inplace_row_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html#sklearn.utils.sparsefuncs.inplace_row_scale "sklearn.utils.sparsefuncs.inplace_row_scale") | Inplace row scaling of a CSR or CSC matrix. |
| [`sparsefuncs.inplace_swap_column`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_column.html#sklearn.utils.sparsefuncs.inplace_swap_column "sklearn.utils.sparsefuncs.inplace_swap_column") | Swap two columns of a CSC/CSR matrix in-place. |
| [`sparsefuncs.inplace_swap_row`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html#sklearn.utils.sparsefuncs.inplace_swap_row "sklearn.utils.sparsefuncs.inplace_swap_row") | Swap two rows of a CSC/CSR matrix in-place. |
| [`sparsefuncs.mean_variance_axis`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#sklearn.utils.sparsefuncs.mean_variance_axis "sklearn.utils.sparsefuncs.mean_variance_axis") | Compute mean and variance along an axis on a CSR or CSC matrix. |

Utilities to work with sparse matrices and arrays written in Cython.

|     |     |
| --- | --- |
| [`sparsefuncs_fast.inplace_csr_row_normalize_l1`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html#sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1 "sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1") | Normalize inplace the rows of a CSR matrix or array by their L1 norm. |
| [`sparsefuncs_fast.inplace_csr_row_normalize_l2`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2.html#sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2 "sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2") | Normalize inplace the rows of a CSR matrix or array by their L2 norm. |

Working with graphs[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.graph "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Graph utilities and algorithms.

|     |     |
| --- | --- |
| [`graph.single_source_shortest_path_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html#sklearn.utils.graph.single_source_shortest_path_length "sklearn.utils.graph.single_source_shortest_path_length") | Return the length of the shortest path from source to all reachable nodes. |

Random sampling[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.random "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Utilities for random sampling.

|     |     |
| --- | --- |
| [`random.sample_without_replacement`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html#sklearn.utils.random.sample_without_replacement "sklearn.utils.random.sample_without_replacement") | Sample integers without replacement. |

Auxiliary functions that operate on arrays[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.arrayfuncs "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

A small collection of auxiliary functions that operate on arrays.

|     |     |
| --- | --- |
| [`arrayfuncs.min_pos`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html#sklearn.utils.arrayfuncs.min_pos "sklearn.utils.arrayfuncs.min_pos") | Find the minimum value of an array over positive values. |

Metadata routing[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.metadata_routing "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Utilities to route metadata within scikit-learn estimators.

**User guide.** See the [Metadata Routing](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 section for further details.

|     |     |
| --- | --- |
| [`metadata_routing.MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest") | Container for storing metadata request info and an associated consumer (`owner`). |
| [`metadata_routing.MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter") | Coordinates metadata routing for a [router](https://scikit-learn.org/stable/glossary.html#term-router)<br> object. |
| [`metadata_routing.MethodMapping`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping") | Stores the mapping between `caller` and `callee` methods for a [router](https://scikit-learn.org/stable/glossary.html#term-router)<br>. |
| [`metadata_routing.get_routing_for_object`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#sklearn.utils.metadata_routing.get_routing_for_object "sklearn.utils.metadata_routing.get_routing_for_object") | Get a `Metadata{Router, Request}` instance from the given object. |
| [`metadata_routing.process_routing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing") | Validate and route metadata. |

Discovering scikit-learn objects[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.discovery "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Utilities to discover scikit-learn objects.

|     |     |
| --- | --- |
| [`discovery.all_displays`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#sklearn.utils.discovery.all_displays "sklearn.utils.discovery.all_displays") | Get a list of all displays from `sklearn`. |
| [`discovery.all_estimators`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_estimators.html#sklearn.utils.discovery.all_estimators "sklearn.utils.discovery.all_estimators") | Get a list of all estimators from `sklearn`. |
| [`discovery.all_functions`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_functions.html#sklearn.utils.discovery.all_functions "sklearn.utils.discovery.all_functions") | Get a list of all functions from `sklearn`. |

API compatibility checkers[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.estimator_checks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Various utilities to check the compatibility of estimators with scikit-learn API.

|     |     |
| --- | --- |
| [`estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") | Check if estimator adheres to scikit-learn conventions. |
| [`estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") | Pytest specific decorator for parametrizing estimator checks. |
| [`estimator_checks.estimator_checks_generator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#sklearn.utils.estimator_checks.estimator_checks_generator "sklearn.utils.estimator_checks.estimator_checks_generator") | Iteratively yield all check callables for an estimator. |

Parallel computing[#](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.parallel "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Customizations of [`joblib`](https://joblib.readthedocs.io/en/latest/index.html#module-joblib "(in joblib v1.7)")
 and `threadpoolctl` tools for scikit-learn usage.

|     |     |
| --- | --- |
| [`parallel.Parallel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel") | Tweak of [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")<br> that propagates the scikit-learn configuration. |
| [`parallel.delayed`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed") | Decorator used to capture the arguments of a function. |