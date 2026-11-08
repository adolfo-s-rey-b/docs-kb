[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fstart_queue_runners&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.start\_queue\_runners Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners#raises_1)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L417-L484)

Starts all queue runners collected in the graph. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.queue_runner.start_queue_runners`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners)

tf.compat.v1.train.start_queue_runners(
        sess=None,
        coord=None,
        daemon=True,
        start=True,
        collection=ops.GraphKeys.QUEUE_RUNNERS
    )

Migrate to TF2
--------------

QueueRunners are not compatible with eager execution. Instead, please use [tf.data](https://www.tensorflow.org/guide/data)
 to get data into your model.

Description
-----------

This is a companion method to `add_queue_runner()`. It just starts threads for all queue runners collected in the graph. It returns the list of all threads.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sess` | `Session` used to run the queue ops. Defaults to the default session. |
| `coord` | Optional `Coordinator` for coordinating the started threads. |
| `daemon` | Whether the threads should be marked as `daemons`, meaning they don't block program exit. |
| `start` | Set to `False` to only create the threads, not start them. |
| `collection` | A `GraphKey` specifying the graph collection to get the queue runners from. Defaults to `GraphKeys.QUEUE_RUNNERS`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `sess` is None and there isn't any default session. |
| `TypeError` | if `sess` is not a [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br> object. |

|     |
| --- |
| Returns<br>------- |     |
| A list of threads. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If called with eager execution enabled. |
| `ValueError` | If called without a default [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)<br> registered. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.