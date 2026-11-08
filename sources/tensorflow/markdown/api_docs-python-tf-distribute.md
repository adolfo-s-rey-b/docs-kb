[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/distribute#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/distribute#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.distribute Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/distribute#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/distribute#functions)
    

Public API for tf.\_api.v2.distribute namespace

Modules
-------

[`cluster_resolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver)
 module: Public API for tf.\_api.v2.distribute.cluster\_resolver namespace

[`coordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator)
 module: Public API for tf.\_api.v2.distribute.coordinator namespace

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental)
 module: Public API for tf.\_api.v2.distribute.experimental namespace

Classes
-------

[`class CrossDeviceOps`](https://www.tensorflow.org/api_docs/python/tf/distribute/CrossDeviceOps)
: Base class for cross-device reduction and broadcasting algorithms.

[`class DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
: Represents a dataset distributed among devices and machines.

[`class DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
: An iterator over [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

[`class DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
: Base class for representing distributed values.

[`class HierarchicalCopyAllReduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce)
: Hierarchical copy all-reduce implementation of CrossDeviceOps.

[`class InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
: A class wrapping information needed by an input function.

[`class InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)
: Run options for `experimental_distribute_dataset(s_from_function)`.

[`class InputReplicationMode`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode)
: Replication mode for input function.

[`class MirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy)
: Synchronous training across multiple replicas on one machine.

[`class MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
: A distribution strategy for synchronous training on multiple workers.

[`class NcclAllReduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/NcclAllReduce)
: NCCL all-reduce implementation of CrossDeviceOps.

[`class OneDeviceStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy)
: A distribution strategy for running on a single device.

[`class ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
: An multi-worker tf.distribute strategy with parameter servers.

[`class ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)
: Indicates how a set of values should be reduced.

[`class ReductionToOneDevice`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReductionToOneDevice)
: A CrossDeviceOps implementation that copies values to one device to reduce.

[`class ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
: A class with a collection of APIs that can be called in a replica context.

[`class RunOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/RunOptions)
: Run options for `strategy.run`.

[`class Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
: An in-process TensorFlow server, for use in distributed training.

[`class Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
: A state & compute distribution policy on a list of devices.

[`class StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)
: Additional APIs for algorithms that need to be distribution-aware.

[`class TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
: Synchronous training on TPUs and TPU Pods.

Functions
---------

[`experimental_set_strategy(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy)
: Set a [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 as current without `with strategy.scope()`.

[`get_replica_context(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)
: Returns the current [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
 or `None`.

[`get_strategy(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)
: Returns the current [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 object.

[`has_strategy(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/has_strategy)
: Return if there is a current non-default [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
.

[`in_cross_replica_context(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/in_cross_replica_context)
: Returns `True` if in a cross-replica context.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.