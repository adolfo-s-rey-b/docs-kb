[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Finput_producer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.input\_producer Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/input_producer#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L115-L200)

Output the rows of `input_tensor` to a queue for an input pipeline. (deprecated)

tf.compat.v1.train.input_producer(
        input_tensor,
        element_shape=None,
        num_epochs=None,
        shuffle=True,
        seed=None,
        capacity=32,
        shared_name=None,
        summary_name=None,
        name=None,
        cancel_op=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | A tensor with the rows to produce. Must be at least one-dimensional. Must either have a fully-defined shape, or `element_shape` must be defined. |
| `element_shape` | (Optional.) A `TensorShape` representing the shape of a row of `input_tensor`, if it cannot be inferred. |
| `num_epochs` | (Optional.) An integer. If specified `input_producer` produces each row of `input_tensor` `num_epochs` times before generating an `OutOfRange` error. If not specified, `input_producer` can cycle through the rows of `input_tensor` an unlimited number of times. |
| `shuffle` | (Optional.) A boolean. If true, the rows are randomly shuffled within each epoch. |
| `seed` | (Optional.) An integer. The seed to use if `shuffle` is true. |
| `capacity` | (Optional.) The capacity of the queue to be used for buffering the input. |
| `shared_name` | (Optional.) If set, this queue will be shared under the given name across multiple sessions. |
| `summary_name` | (Optional.) If set, a scalar summary for the current queue size will be generated, using this name as part of the tag. |
| `name` | (Optional.) A name for queue. |
| `cancel_op` | (Optional.) Cancel op for the queue |

|     |
| --- |
| Returns<br>------- |     |
| A queue with the output rows. A `QueueRunner` for the queue is added to the current `QUEUE_RUNNER` collection of the current graph. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shape of the input cannot be inferred from the arguments. |
| `RuntimeError` | If called with eager execution enabled. |

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