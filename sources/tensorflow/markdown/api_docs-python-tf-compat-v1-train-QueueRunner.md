[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2FQueueRunner&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#methods)
    *   [create\_threads](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#create_threads)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#from_proto)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#to_proto)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.QueueRunner Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#methods)
    *   [create\_threads](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#create_threads)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#from_proto)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner#to_proto)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L33-L388)

Holds a list of enqueue operations for a queue, each to be run in a thread.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.queue_runner.QueueRunner`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/QueueRunner)

tf.compat.v1.train.QueueRunner(
        queue=None,
        enqueue_ops=None,
        close_op=None,
        cancel_op=None,
        queue_closed_exception_types=None,
        queue_runner_def=None,
        import_scope=None
    )

Migrate to TF2
--------------

QueueRunners are not compatible with eager execution. Instead, please use [tf.data](https://www.tensorflow.org/guide/data)
 to get data into your model.

Description
-----------

Queues are a convenient TensorFlow mechanism to compute tensors asynchronously using multiple threads. For example in the canonical 'Input Reader' setup one set of threads generates filenames in a queue; a second set of threads read records from the files, processes them, and enqueues tensors on a second queue; a third set of threads dequeues these input records to construct batches and runs them through training operations.

There are several delicate issues when running multiple threads that way: closing the queues in sequence as the input is exhausted, correctly catching and reporting exceptions, etc.

The `QueueRunner`, combined with the `Coordinator`, helps handle these issues.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `queue` | A `Queue`. |
| `enqueue_ops` | List of enqueue ops to run in threads later. |
| `close_op` | Op to close the queue. Pending enqueue ops are preserved. |
| `cancel_op` | Op to close the queue and cancel pending enqueue ops. |
| `queue_closed_exception_types` | Optional tuple of Exception types that indicate that the queue has been closed when raised during an enqueue operation. Defaults to `(tf.errors.OutOfRangeError,)`. Another common case includes `(tf.errors.OutOfRangeError, tf.errors.CancelledError)`, when some of the enqueue ops may dequeue from other Queues. |
| `queue_runner_def` | Optional `QueueRunnerDef` protocol buffer. If specified, recreates the QueueRunner from its contents. `queue_runner_def` and the other arguments are mutually exclusive. |
| `import_scope` | Optional `string`. Name scope to add. Only used when initializing from protocol buffer. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both `queue_runner_def` and `queue` are both specified. |
| `ValueError` | If `queue` or `enqueue_ops` are not provided when not restoring from `queue_runner_def`. |
| `RuntimeError` | If eager execution is enabled. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `cancel_op` |     |
| `close_op` |     |
| `enqueue_ops` |     |
| `exceptions_raised` | Exceptions raised but not handled by the `QueueRunner` threads.<br><br>Exceptions raised in queue runner threads are handled in one of two ways depending on whether or not a `Coordinator` was passed to `create_threads()`:<br><br>*   With a `Coordinator`, exceptions are reported to the coordinator and forgotten by the `QueueRunner`.<br>    <br>*   Without a `Coordinator`, exceptions are captured by the `QueueRunner` and made available in this `exceptions_raised` property. |
| `name` | The string name of the underlying Queue. |
| `queue` |     |
| `queue_closed_exception_types` |     |

Methods
-------

### `create_threads`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L298-L353)

create_threads(
        sess, coord=None, daemon=False, start=False
    )

Create threads to run the enqueue ops for the given session.

This method requires a session in which the graph was launched. It creates a list of threads, optionally starting them. There is one thread for each op passed in `enqueue_ops`.

The `coord` argument is an optional coordinator that the threads will use to terminate together and report exceptions. If a coordinator is given, this method starts an additional thread to close the queue when the coordinator requests a stop.

If previously created threads for the given session are still running, no new threads will be created.

|     |     |
| --- | --- |
| Args |     |
| `sess` | A `Session`. |
| `coord` | Optional `Coordinator` object for reporting errors and checking stop conditions. |
| `daemon` | Boolean. If `True` make the threads daemon threads. |
| `start` | Boolean. If `True` starts the threads. If `False` the caller must call the `start()` method of the returned threads. |

|     |
| --- |
| Returns |     |
| A list of threads. |     |

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L384-L388)

@staticmethod

Returns a `QueueRunner` object created from `queue_runner_def`.

### `to_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L355-L382)

to_proto(
        export_scope=None
    )

Converts this `QueueRunner` to a `QueueRunnerDef` protocol buffer.

|     |     |
| --- | --- |
| Args |     |
| `export_scope` | Optional `string`. Name scope to remove. |

|     |
| --- |
| Returns |     |
| A `QueueRunnerDef` protocol buffer, or `None` if the `Variable` is not in the specified name scope. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.