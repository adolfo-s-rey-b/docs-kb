[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.range\_input\_producer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#returns)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/range_input_producer#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L278-L317)

Produces the integers from 0 to limit-1 in a queue. (deprecated)

tf.compat.v1.train.range_input_producer(
        limit,
        num_epochs=None,
        shuffle=True,
        seed=None,
        capacity=32,
        shared_name=None,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `limit` | An int32 scalar tensor. |
| `num_epochs` | An integer (optional). If specified, `range_input_producer` produces each integer `num_epochs` times before generating an OutOfRange error. If not specified, `range_input_producer` can cycle through the integers an unlimited number of times. |
| `shuffle` | Boolean. If true, the integers are randomly shuffled within each epoch. |
| `seed` | An integer (optional). Seed used if shuffle == True. |
| `capacity` | An integer. Sets the queue capacity. |
| `shared_name` | (optional). If set, this queue will be shared under the given name across multiple sessions. |
| `name` | A name for the operations (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Queue with the output integers. A `QueueRunner` for the Queue is added to the current `Graph`'s `QUEUE_RUNNER` collection. |     |

eager compatibility
-------------------

Input pipelines based on Queues are not supported when eager execution is enabled. Please use the [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 API to ingest data under eager execution.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.