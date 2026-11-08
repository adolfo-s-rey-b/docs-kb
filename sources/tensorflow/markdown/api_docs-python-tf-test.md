[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test#main-content)

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
    

Module: tf.test Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

Public API for tf.\_api.v2.test namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/test/experimental)
 module: Public API for tf.\_api.v2.test.experimental namespace

Classes
-------

[`class Benchmark`](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark)
: Abstract class that provides helpers for TensorFlow benchmarks.

[`class TestCase`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)
: Base class for tests that need to test TensorFlow.

Functions
---------

[`assert_equal_graph_def(...)`](https://www.tensorflow.org/api_docs/python/tf/test/assert_equal_graph_def)
: Asserts that two `GraphDef`s are (mostly) the same.

[`benchmark_config(...)`](https://www.tensorflow.org/api_docs/python/tf/test/benchmark_config)
: Returns a tf.compat.v1.ConfigProto for disabling the dependency optimizer.

[`compute_gradient(...)`](https://www.tensorflow.org/api_docs/python/tf/test/compute_gradient)
: Computes the theoretical and numeric Jacobian of `f`.

[`create_local_cluster(...)`](https://www.tensorflow.org/api_docs/python/tf/test/create_local_cluster)
: Create and start local servers and return the associated `Server` objects.

[`disable_with_predicate(...)`](https://www.tensorflow.org/api_docs/python/tf/test/disable_with_predicate)
: Disables the test if pred is true.

[`gpu_device_name(...)`](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name)
: Returns the name of a GPU device if available or a empty string.

[`is_built_with_cuda(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_cuda)
: Returns whether TensorFlow was built with CUDA (GPU) support.

[`is_built_with_gpu_support(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_gpu_support)
: Returns whether TensorFlow was built with GPU (CUDA or ROCm) support.

[`is_built_with_rocm(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm)
: Returns whether TensorFlow was built with ROCm (GPU) support.

[`is_built_with_xla(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_xla)
: Returns whether TensorFlow was built with XLA support.

[`is_cpu_target_available(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_cpu_target_available)
: Indicates whether TensorFlow was built with support for a given CPU target.

[`is_gpu_available(...)`](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available)
: Returns whether TensorFlow can access a GPU. (deprecated)

[`main(...)`](https://www.tensorflow.org/api_docs/python/tf/test/main)
: Runs all unit tests.

[`with_eager_op_as_function(...)`](https://www.tensorflow.org/api_docs/python/tf/test/with_eager_op_as_function)
: Returns the same class. This will be removed once all usages are removed.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.