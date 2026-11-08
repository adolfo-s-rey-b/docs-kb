[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2FDistributedValues&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.DistributedValues Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L62-L166)

Base class for representing distributed values.

A subclass instance of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 is created when creating variables within a distribution strategy, iterating a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 or through [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
. This base class should never be instantiated directly. [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 contains a value per replica. Depending on the subclass, the values could either be synced on update, synced on demand, or never synced.

Two representative types of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 are `tf.types.experimental.PerReplica` and `tf.types.experimental.Mirrored` values.

`PerReplica` values exist on the worker devices, with a different value for each replica. They are produced by iterating through a distributed dataset returned by [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)
 (Example 1, below) and [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)
. They are also the typical result returned by [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
 (Example 2).

`Mirrored` values are like `PerReplica` values, except we know that the value on all replicas are the same. `Mirrored` values are kept synchronized by the distribution strategy in use, while `PerReplica` values are left unsynchronized. `Mirrored` values typically represent model weights. We can safely read a `Mirrored` value in a cross-replica context by using the value on any replica, while PerReplica values should not be read or manipulated in a cross-replica context."

[`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 can be reduced via `strategy.reduce` to obtain a single value across replicas (Example 4), used as input into [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
 (Example 3), or collected to inspect the per-replica values using [`tf.distribute.Strategy.experimental_local_results`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_local_results)
 (Example 5).

#### Example usages:

1.  Created from a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
    :

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

1.  Returned by `run`:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

1.  As input into `run`:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

1.  As input into `reduce`:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

1.  How to inspect per-replica values locally:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.