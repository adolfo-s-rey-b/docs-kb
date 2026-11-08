[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fdistribute%2Fexperimental&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.distribute.experimental Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental#classes)
    

Public API for tf.\_api.v2.distribute.experimental namespace

Classes
-------

[`class CentralStorageStrategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental/CentralStorageStrategy)
: A one-machine strategy that puts all variables on a single device.

[`class CollectiveCommunication`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)
: Cross device communication implementation.

[`class CollectiveHints`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CollectiveHints)
: Hints for collective operations like AllReduce.

[`class CommunicationImplementation`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)
: Cross device communication implementation.

[`class CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)
: Options for cross device communications like All-reduce.

[`class MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental/MultiWorkerMirroredStrategy)
: A distribution strategy for synchronous training on multiple workers.

[`class ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental/ParameterServerStrategy)
: An asynchronous multi-worker parameter server tf.distribute strategy.

[`class TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental/TPUStrategy)
: TPU distribution strategy implementation.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.