[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.coordinator.PerWorkerValues Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/values.py#L152-L182)

A container that holds a list of values, one value per worker.

#### View aliases

**Main aliases**

[`tf.distribute.coordinator.PerWorkerValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)

tf.distribute.experimental.coordinator.PerWorkerValues(
        values
    )

[`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
 contains a collection of values, where each of the values is located on its corresponding worker, and upon being used as one of the `args` or `kwargs` of [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule()`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)
, the value specific to a worker will be passed into the function being executed at that corresponding worker.

Currently, the only supported path to create an object of [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
 is through calling `iter` on a [`ClusterCoordinator.create_per_worker_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#create_per_worker_dataset)
\-returned distributed dataset instance. The mechanism to create a custom [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
 is not yet supported.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.