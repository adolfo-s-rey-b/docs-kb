[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.string\_input\_producer Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/string_input_producer#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L203-L275)

Output strings (e.g. filenames) to a queue for an input pipeline. (deprecated)

tf.compat.v1.train.string_input_producer(
        string_tensor,
        num_epochs=None,
        shuffle=True,
        seed=None,
        capacity=32,
        shared_name=None,
        name=None,
        cancel_op=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `string_tensor` | A 1-D string tensor with the strings to produce. |
| `num_epochs` | An integer (optional). If specified, `string_input_producer` produces each string from `string_tensor` `num_epochs` times before generating an `OutOfRange` error. If not specified, `string_input_producer` can cycle through the strings in `string_tensor` an unlimited number of times. |
| `shuffle` | Boolean. If true, the strings are randomly shuffled within each epoch. |
| `seed` | An integer (optional). Seed used if shuffle == True. |
| `capacity` | An integer. Sets the queue capacity. |
| `shared_name` | (optional). If set, this queue will be shared under the given name across multiple sessions. All sessions open to the device which has this queue will be able to access it via the shared\_name. Using this in a distributed setting means each name will only be seen by one of the sessions which has access to this operation. |
| `name` | A name for the operations (optional). |
| `cancel_op` | Cancel op for the queue (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A queue with the output strings. A `QueueRunner` for the Queue is added to the current `Graph`'s `QUEUE_RUNNER` collection. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the string\_tensor is a null Python list. At runtime, will fail with an assertion if string\_tensor becomes a null tensor. |

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