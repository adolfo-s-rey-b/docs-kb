[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#main-content)

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
    

tf.distribute.experimental.coordinator.ClusterCoordinator Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1397-L1751)

An object to schedule and coordinate remote function execution.

#### View aliases

**Main aliases**

[`tf.distribute.coordinator.ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator)

tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

This class is used to create fault-tolerant resources and dispatch functions to remote TensorFlow servers.

Currently, this class is not supported to be used in a standalone manner. It should be used in conjunction with a [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
 strategy that is designed to work with it. The `ClusterCoordinator` class currently only works [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
.

**The `schedule`/`join` APIs**

The most important APIs provided by this class is the `schedule`/`join` pair. The `schedule` API is non-blocking in that it queues a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 and returns a `RemoteValue` immediately. The queued functions will be dispatched to remote workers in background threads and their `RemoteValue`s will be filled asynchronously. Since `schedule` doesn’t require worker assignment, the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 passed in can be executed on any available worker. If the worker it is executed on becomes unavailable before its completion, it will be migrated to another worker. Because of this fact and function execution is not atomic, a function may be executed more than once.

**Handling Task Failure**

This class when used with [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
, comes with built-in fault tolerance for worker failures. That is, when some workers are not available for any reason to be reached from the coordinator, the training progress continues to be made with the remaining workers. Upon recovery of a failed worker, it will be added for function execution after datasets created by `create_per_worker_dataset` are re-built on it.

When a parameter server fails, a [`tf.errors.UnavailableError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnavailableError)
 is raised by `schedule`, `join` or `done`. In this case, in addition to bringing back the failed parameter server, users should restart the coordinator so that it reconnects to workers and parameter servers, re-creates the variables, and loads checkpoints. If the coordinator fails, after the user brings it back, the program will automatically connect to workers and parameter servers, and continue the progress from a checkpoint.

It is thus essential that in user's program, a checkpoint file is periodically saved, and restored at the start of the program. If an [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 is checkpointed, after restoring from a checkpoiont, its `iterations` property roughly indicates the number of steps that have been made. This can be used to decide how many epochs and steps are needed before the training completion.

See [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
 docstring for an example usage of this API.

This is currently under development, and the API as well as implementation are subject to changes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `strategy` | a supported [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object. Currently, only [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)<br> is supported. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the strategy being used is not supported. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `strategy` | Returns the `Strategy` associated with the `ClusterCoordinator`. |

Methods
-------

### `create_per_worker_dataset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1604-L1664)

create_per_worker_dataset(
        dataset_fn
    )

Create dataset on each worker.

This creates dataset on workers from the input which can be either a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 or a function which returns a dataset, and returns an object that represents the collection of those individual datasets. Calling `iter` on such collection of datasets returns a [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
, which is a collection of iterators, where the iterators have been placed on respective workers.

Calling `next` on a `PerWorkerValues` of iterator is unsupported. The iterator is meant to be passed as an argument into [`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#schedule)
. When the scheduled function is about to be executed by a worker, the function will receive the individual iterator that corresponds to the worker. The `next` method can be called on an iterator inside a scheduled function when the iterator is an input of the function.

Currently the `schedule` method assumes workers are all the same and thus assumes the datasets on different workers are the same, except they may be shuffled differently if they contain a `dataset.shuffle` operation and a random seed is not set. Because of this, we also recommend the datasets to be repeated indefinitely and schedule a finite number of steps instead of relying on the `OutOfRangeError` from a dataset.

#### Example:

strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy=strategy)
    
    @tf.function
    def worker_fn(iterator):
      return next(iterator)
    
    def per_worker_dataset_fn():
      return strategy.distribute_datasets_from_function(
          lambda x: tf.data.Dataset.from_tensor_slices([3] * 3))
    
    per_worker_dataset = coordinator.create_per_worker_dataset(
        per_worker_dataset_fn)
    per_worker_iter = iter(per_worker_dataset)
    remote_value = coordinator.schedule(worker_fn, args=(per_worker_iter,))
    assert remote_value.fetch() == 3

|     |     |
| --- | --- |
| Args |     |
| `dataset_fn` | The dataset function that returns a dataset. This is to be executed on the workers. |

|     |
| --- |
| Returns |     |
| An object that represents the collection of those individual datasets. `iter` is expected to be called on this object that returns a [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)<br> of the iterators (that are on the workers). |     |

### `done`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1586-L1602)

done()

Returns whether all the scheduled functions have finished execution.

If any previously scheduled function raises an error, `done` will fail by raising any one of those errors.

When `done` returns True or raises, it guarantees that there is no function that is still being executed.

|     |
| --- |
| Returns |     |
| Whether all the scheduled functions have finished execution. |     |

|     |     |
| --- | --- |
| Raises |     |
| `Exception` | one of the exceptions caught by the coordinator by any previously scheduled function since the last time an error was thrown or since the beginning of the program. |

### `fetch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1695-L1751)

fetch(
        val
    )

Blocking call to fetch results from the remote values.

This is a wrapper around [`tf.distribute.experimental.coordinator.RemoteValue.fetch`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue#fetch)
 for a `RemoteValue` structure; it returns the execution results of `RemoteValue`s. If not ready, wait for them while blocking the caller.

#### Example:

strategy = ...
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy)
    
    def dataset_fn():
      return tf.data.Dataset.from_tensor_slices([1, 1, 1])
    
    with strategy.scope():
      v = tf.Variable(initial_value=0)
    
    @tf.function
    def worker_fn(iterator):
      def replica_fn(x):
        v.assign_add(x)
        return v.read_value()
      return strategy.run(replica_fn, args=(next(iterator),))
    
    distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)
    distributed_iterator = iter(distributed_dataset)
    result = coordinator.schedule(worker_fn, args=(distributed_iterator,))
    assert coordinator.fetch(result) == 1

|     |     |
| --- | --- |
| Args |     |
| `val` | The value to fetch the results from. If this is structure of [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br>, `fetch()` will be called on the individual [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br> to get the result. |

|     |
| --- |
| Returns |     |
| If `val` is a [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br> or a structure of [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br>s, return the fetched [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br> values immediately if they are available, or block the call until they are available, and return the fetched [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br> values with the same structure. If `val` is other types, return it as-is. |     |

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1565-L1584)

join()

Blocks until all the scheduled functions have finished execution.

If any previously scheduled function raises an error, `join` will fail by raising any one of those errors, and clear the errors collected so far. If this happens, some of the previously scheduled functions may have not been executed. Users can call `fetch` on the returned [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
 to inspect if they have executed, failed, or cancelled. If some that have been cancelled need to be rescheduled, users should call `schedule` with the function again.

When `join` returns or raises, it guarantees that there is no function that is still being executed.

|     |     |
| --- | --- |
| Raises |     |
| `Exception` | one of the exceptions caught by the coordinator by any previously scheduled function since the last time an error was thrown or since the beginning of the program. |

### `schedule`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1493-L1563)

schedule(
        fn, args=None, kwargs=None
    )

Schedules `fn` to be dispatched to a worker for asynchronous execution.

This method is non-blocking in that it queues the `fn` which will be executed later and returns a [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
 object immediately. `fetch` can be called on it to wait for the function execution to finish and retrieve its output from a remote worker. On the other hand, call [`tf.distribute.experimental.coordinator.ClusterCoordinator.join`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator#join)
 to wait for all scheduled functions to finish.

`schedule` guarantees that `fn` will be executed on a worker at least once; it could be more than once if its corresponding worker fails in the middle of its execution. Note that since worker can fail at any point when executing the function, it is possible that the function is partially executed, but [`tf.distribute.experimental.coordinator.ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator)
 guarantees that in those events, the function will eventually be executed on any worker that is available.

If any previously scheduled function raises an error, `schedule` will raise any one of those errors, and clear the errors collected so far. What happens here, some of the previously scheduled functions may have not been executed. User can call `fetch` on the returned [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
 to inspect if they have executed, failed, or cancelled, and reschedule the corresponding function if needed.

When `schedule` raises, it guarantees that there is no function that is still being executed.

At this time, there is no support of worker assignment for function execution, or priority of the workers.

`args` and `kwargs` are the arguments passed into `fn`, when `fn` is executed on a worker. They can be [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
 and in this case, the argument will be substituted with the corresponding component on the target worker. Arguments that are not [`tf.distribute.experimental.coordinator.PerWorkerValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/PerWorkerValues)
 will be passed into `fn` as-is. Currently, [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)
 is not supported to be input `args` or `kwargs`.

|     |     |
| --- | --- |
| Args |     |
| `fn` | A [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>; the function to be dispatched to a worker for execution asynchronously. Regular python function is not supported to be scheduled. |
| `args` | Positional arguments for `fn`. |
| `kwargs` | Keyword arguments for `fn`. |

|     |
| --- |
| Returns |     |
| A [`tf.distribute.experimental.coordinator.RemoteValue`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/RemoteValue)<br> object that represents the output of the function scheduled. |     |

|     |     |
| --- | --- |
| Raises |     |
| `Exception` | one of the exceptions caught by the coordinator from any previously scheduled function, since the last time an error was thrown or since the beginning of the program. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.