[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.data.experimental.service Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#functions)
    

Public API for tf.\_api.v2.data.experimental.service namespace

Classes
-------

[`class CrossTrainerCache`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/CrossTrainerCache)
: Options related to the tf.data service cross trainer cache.

[`class DispatchServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer)
: An in-process tf.data service dispatch server.

[`class DispatcherConfig`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig)
: Configuration class for tf.data service dispatchers.

[`class ShardingPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/ShardingPolicy)
: Specifies how to shard data among tf.data service workers.

[`class WorkerConfig`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerConfig)
: Configuration class for tf.data service dispatchers.

[`class WorkerServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer)
: An in-process tf.data service worker server.

Functions
---------

[`distribute(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/distribute)
: A transformation that moves dataset processing to the tf.data service.

[`from_dataset_id(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/from_dataset_id)
: Creates a dataset which reads data from the tf.data service.

[`register_dataset(...)`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/register_dataset)
: Registers a dataset with the tf.data service.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.