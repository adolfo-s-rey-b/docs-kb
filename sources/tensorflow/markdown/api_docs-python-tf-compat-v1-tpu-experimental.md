[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.tpu.experimental Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental#functions)
    

Public API for tf.\_api.v2.tpu.experimental namespace

Modules
-------

[`embedding`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding)
 module: Public API for tf.\_api.v2.tpu.experimental.embedding namespace

Classes
-------

[`class DeviceAssignment`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment)
: Mapping from logical cores in a computation to the physical TPU topology.

[`class DeviceOrderMode`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceOrderMode)
: The way of determining device orders when computing device assignment.

[`class HardwareFeature`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/HardwareFeature)
: class holds all the feature info about the TPU.

[`class TPUSystemMetadata`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/TPUSystemMetadata)
: Describes some metadata about the TPU system.

[`class Topology`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/Topology)
: Describes a set of TPU devices.

Functions
---------

[`embedding_column(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column)
: TPU version of [`tf.compat.v1.feature_column.embedding_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)
.

[`initialize_tpu_system(...)`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system)
: Initialize the TPU devices.

[`shared_embedding_columns(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/shared_embedding_columns)
: TPU version of [`tf.compat.v1.feature_column.shared_embedding_columns`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns)
.

[`shutdown_tpu_system(...)`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/shutdown_tpu_system)
: Shuts down the TPU devices.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.