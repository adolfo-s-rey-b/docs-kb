[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#methods)
    *   [fetch](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#fetch)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#get)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.coordinator.RemoteValue Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#methods)
    *   [fetch](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#fetch)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#get)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/remote_value.py#L53-L131)

An asynchronously available value of a scheduled function.

#### View aliases

**Main aliases**

[`tf.distribute.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)

This class is used as the return value of [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)
 where the underlying value becomes available at a later time once the function has been executed.

Using [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
 as an input to a subsequent function scheduled with [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)
 is currently not supported.

#### Example:

strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = (
        tf.distribute.experimental.coordinator.ClusterCoordinator(strategy))
    
    with strategy.scope():
      v1 = tf.Variable(initial_value=0.0)
      v2 = tf.Variable(initial_value=1.0)
    
    @tf.function
    def worker_fn():
      v1.assign_add(0.1)
      v2.assign_sub(0.2)
      return v1.read_value() / v2.read_value()
    
    result = coordinator.schedule(worker_fn)
    # Note that `fetch()` gives the actual result instead of a `tf.Tensor`.
    assert result.fetch() == 0.125
    
    for _ in range(10):
      # `worker_fn` will be run on arbitrary workers that are available. The
      # `result` value will be available later.
      result = coordinator.schedule(worker_fn)

Methods
-------

### `fetch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/remote_value.py#L97-L113)

fetch()

Wait for the result of `RemoteValue` and return the numpy result.

This makes the value concrete by copying the remote value to local.

|     |
| --- |
| Returns |     |
| The numpy array structure of the actual output of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> associated with this `RemoteValue`, previously returned by a [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)<br> call. This can be a single value, or a structure of values, depending on the output of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. |     |

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.CancelledError`](https://www.tensorflow.org/api_docs/python/tf/errors/CancelledError) | If the function that produces this `RemoteValue` is aborted or cancelled due to failure. |

### `get`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/remote_value.py#L115-L131)

get()

Wait for the result of `RemoteValue` and return the tensor result.

This makes the value concrete by copying the remote tensor to local.

|     |
| --- |
| Returns |     |
| The actual output (in the form of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s) of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> associated with this `RemoteValue`, previously returned by a [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)<br> call. This can be a single Tensor, or a structure of Tensors, depending on the output of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. |     |

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.CancelledError`](https://www.tensorflow.org/api_docs/python/tf/errors/CancelledError) | If the function that produces this `RemoteValue` is aborted or cancelled due to failure. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.