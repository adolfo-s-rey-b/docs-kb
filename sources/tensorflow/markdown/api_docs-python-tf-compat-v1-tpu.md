[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.tpu Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

Public API for tf.\_api.v2.tpu namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental)
 module: Public API for tf.\_api.v2.tpu.experimental namespace

Classes
-------

[`class CrossShardOptimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer)
: An optimizer that averages gradients across TPU shards.

[`class PaddingSpec`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/PaddingSpec)
: Represents the type of padding policies for tpu.replicate.

[`class XLAOptions`](https://www.tensorflow.org/api_docs/python/tf/tpu/XLAOptions)
: XLA compilation options.

Functions
---------

[`batch_parallel(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/batch_parallel)
: Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/bfloat16_scope)
: Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/core)
: Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/cross_replica_sum)
: Sum the input tensor across replicas according to group\_assignment.

[`initialize_system(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/initialize_system)
: Initializes a distributed TPU system for use with TensorFlow.

[`outside_compilation(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/outside_compilation)
: Builds part of a computation outside any current TPU replicate scope.

[`replicate(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/replicate)
: Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/rewrite)
: Rewrites `computation` for execution on a TPU system.

[`shard(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shard)
: Shards `computation` for parallel execution.

[`shutdown_system(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/shutdown_system)
: Shuts down a running a distributed TPU system.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.