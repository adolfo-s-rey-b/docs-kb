[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.add\_queue\_runner Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/queue_runner_impl.py#L391-L414)

Adds a `QueueRunner` to a collection in the graph. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.queue_runner.add_queue_runner`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/add_queue_runner)

tf.compat.v1.train.add_queue_runner(
        qr, collection=ops.GraphKeys.QUEUE_RUNNERS
    )

Migrate to TF2
--------------

QueueRunners are not compatible with eager execution. Instead, please use [tf.data](https://www.tensorflow.org/guide/data)
 to get data into your model.

Description
-----------

When building a complex model that uses many queues it is often difficult to gather all the queue runners that need to be run. This convenience function allows you to add a queue runner to a well known collection in the graph.

The companion method `start_queue_runners()` can be used to start threads for all the collected queue runners.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `qr` | A `QueueRunner`. |
| `collection` | A `GraphKey` specifying the graph collection to add the queue runner to. Defaults to `GraphKeys.QUEUE_RUNNERS`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.