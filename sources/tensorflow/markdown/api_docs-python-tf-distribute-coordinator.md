[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fcoordinator&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.distribute.coordinator Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator#functions)
    

Public API for tf.\_api.v2.distribute.coordinator namespace

Classes
-------

[`class ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator)
: An object to schedule and coordinate remote function execution.

[`class PerWorkerValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
: A container that holds a list of values, one value per worker.

[`class RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
: An asynchronously available value of a scheduled function.

Functions
---------

[`experimental_get_current_worker_index(...)`](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index)
: Returns the current worker index, when called within a worker closure.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.