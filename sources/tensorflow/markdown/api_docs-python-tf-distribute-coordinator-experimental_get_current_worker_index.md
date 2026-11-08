[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.coordinator.experimental\_get\_current\_worker\_index Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/coordinator/experimental_get_current_worker_index#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/coordinator_context.py#L81-L145)

Returns the current worker index, when called within a worker closure.

tf.distribute.coordinator.experimental_get_current_worker_index()

Some parameter server training workloads may require the worker to know its index, for example for data sharding for reduced-variance training.

This method may be used within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 that is executed on a worker. That is, either a `dataset_fn` that runs via [`ClusterCoordinator.create_per_worker_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#create_per_worker_dataset)
, or any other function scheduled via [`ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)
.

Example (sharding data by worker):

strategy = tf.distribute.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = (
        tf.distribute.coordinator.ClusterCoordinator(strategy))
    
    def dataset_fn(context):
      dataset = tf.data.Dataset.range(10)
      worker_index = (
          tf.distribute.coordinator.experimental_get_current_worker_index()
      )
      dataset = dataset.shard(
          num_shards=num_workers,
          index=worker_index,
      )
      return dataset
    
    @tf.function
    def per_worker_dataset_fn():
      return strategy.distribute_datasets_from_function(dataset_fn)
    
    per_worker_dataset = coordinator.create_per_worker_dataset(
        per_worker_dataset_fn)

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if called from outside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> or outside of a remote closure execution context (that is, on a non-worker machine). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.