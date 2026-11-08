[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/data/experimental#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/data/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/data/experimental#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/data/experimental#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.data.experimental Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/data/experimental#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/data/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/data/experimental#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/data/experimental#other-members)
    

Public API for tf.\_api.v2.data.experimental namespace

Modules
-------

[`service`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service)
 module: Public API for tf.\_api.v2.data.experimental.service namespace

Classes
-------

[`class AutoShardPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)
: Represents the type of auto-sharding to use.

[`class AutotuneAlgorithm`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm)
: Represents the type of autotuning algorithm to use.

[`class AutotuneOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions)
: Represents options for autotuning dataset performance.

[`class CsvDataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/CsvDataset)
: A Dataset comprising lines from one or more CSV files.

[`class DatasetInitializer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer)
: Creates a table initializer from a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

[`class DistributeOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)
: Represents options for distributed data processing.

[`class ExternalStatePolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ExternalStatePolicy)
: Represents how to handle external state during serialization.

[`class OptimizationOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions)
: Represents options for dataset optimizations.

[`class Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
: Represents a value that may or may not be present.

[`class RandomDataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset)
: A `Dataset` of pseudorandom values. (deprecated)

[`class Reducer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/Reducer)
: A reducer is used for reducing a set of elements.

[`class ServiceOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions)
: Represents options for tf.data service.

[`class SqlDataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/SqlDataset)
: A `Dataset` consisting of the results from a SQL query.

[`class TFRecordWriter`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/TFRecordWriter)
: Writes a dataset to a TFRecord file. (deprecated)

[`class ThreadingOptions`](https://www.tensorflow.org/api_docs/python/tf/data/ThreadingOptions)
: Represents options for dataset threading.

Functions
---------

[`Counter(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/Counter)
: Creates a `Dataset` that counts from `start` in steps of size `step`. (deprecated)

[`assert_cardinality(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality)
: Asserts the cardinality of the input dataset.

[`at(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at)
: Returns the element at a specific index in a datasest.

[`bucket_by_sequence_length(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length)
: A transformation that buckets elements in a `Dataset` by length. (deprecated)

[`cardinality(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality)
: Returns the cardinality of `dataset`, if known.

[`choose_from_datasets(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets)
: Creates a dataset that deterministically chooses elements from `datasets`. (deprecated)

[`copy_to_device(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/copy_to_device)
: A transformation that copies dataset elements to the given `target_device`.

[`dense_to_ragged_batch(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch)
: A transformation that batches ragged elements into [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s. (deprecated)

[`dense_to_sparse_batch(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_sparse_batch)
: A transformation that batches ragged elements into [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
s. (deprecated)

[`distributed_save(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/distributed_save)
: Initiates the process of saving a dataset to disk using tf.data service.

[`enable_debug_mode(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enable_debug_mode)
: Enables debug mode for tf.data.

[`enumerate_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/enumerate_dataset)
: A transformation that enumerates the elements of a dataset. (deprecated)

[`from_list(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list)
: Creates a `Dataset` comprising the given list of elements.

[`from_variant(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant)
: Constructs a dataset from the given variant and (nested) structure.

[`get_model_proto(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto)
: Gets the analytical model inside of `iterator` as `model_pb2.ModelProto`.

[`get_next_as_optional(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_next_as_optional)
: Returns a [`tf.experimental.Optional`](https://www.tensorflow.org/api_docs/python/tf/experimental/Optional)
 with the next element of the iterator. (deprecated)

[`get_single_element(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element)
: Returns the single element of the `dataset` as a nested structure of tensors. (deprecated)

[`get_structure(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure)
: Returns the type signature for elements of the input dataset / iterator.

[`group_by_reducer(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer)
: A transformation that groups elements and performs a reduction.

[`group_by_window(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window)
: A transformation that groups windows of elements by key and reduces them. (deprecated)

[`ignore_errors(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ignore_errors)
: Creates a `Dataset` from another `Dataset` and silently ignores any errors. (deprecated)

[`index_table_from_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/index_table_from_dataset)
: Returns an index lookup table based on the given dataset.

[`load(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/load)
: Loads a previously saved dataset. (deprecated)

[`make_batched_features_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_batched_features_dataset)
: Returns a `Dataset` of feature dictionaries from `Example` protos.

[`make_csv_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_csv_dataset)
: Reads CSV files into a dataset.

[`make_saveable_from_iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_saveable_from_iterator)
: Returns a SaveableObject for saving/restoring iterator state using Saver. (deprecated)

[`map_and_batch(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/map_and_batch)
: Fused implementation of `map` and `batch`. (deprecated)

[`pad_to_cardinality(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/pad_to_cardinality)
: Pads a dataset with fake elements to reach the desired cardinality.

[`parallel_interleave(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave)
: A parallel version of the [`Dataset.interleave()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
 transformation. (deprecated)

[`parse_example_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parse_example_dataset)
: A transformation that parses `Example` protos into a `dict` of tensors. (deprecated)

[`prefetch_to_device(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device)
: A transformation that prefetches dataset values to the given `device`.

[`rejection_resample(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/rejection_resample)
: A transformation that resamples a dataset to achieve a target distribution. (deprecated)

[`sample_from_datasets(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/sample_from_datasets)
: Samples elements at random from the datasets in `datasets`. (deprecated)

[`save(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/save)
: Saves the content of the given dataset. (deprecated)

[`scan(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/scan)
: A transformation that scans a function across an input dataset. (deprecated)

[`shuffle_and_repeat(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat)
: Shuffles and repeats a Dataset, reshuffling with each repetition. (deprecated)

[`snapshot(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/snapshot)
: API to persist the output of the input dataset. (deprecated)

[`table_from_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset)
: Returns a lookup table based on the given dataset.

[`take_while(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/take_while)
: A transformation that stops dataset iteration based on a `predicate`. (deprecated)

[`to_variant(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/to_variant)
: Returns a variant representing the given dataset.

[`unbatch(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch)
: Splits elements of a dataset into multiple elements on the batch dimension. (deprecated)

[`unique(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unique)
: Creates a `Dataset` from another `Dataset`, discarding duplicates. (deprecated)

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| AUTOTUNE | `-1` |
| INFINITE\_CARDINALITY | `-1` |
| SHARD\_HINT | `-1` |
| UNKNOWN\_CARDINALITY | `-2` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.