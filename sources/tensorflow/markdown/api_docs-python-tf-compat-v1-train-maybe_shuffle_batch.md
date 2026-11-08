[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.maybe\_shuffle\_batch Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_shuffle_batch#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L1354-L1415)

Creates batches by randomly shuffling conditionally-enqueued tensors. (deprecated)

tf.compat.v1.train.maybe_shuffle_batch(
        tensors,
        batch_size,
        capacity,
        min_after_dequeue,
        keep_input,
        num_threads=1,
        seed=None,
        enqueue_many=False,
        shapes=None,
        allow_smaller_final_batch=False,
        shared_name=None,
        name=None
    )

See docstring in `shuffle_batch` for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors` | The list or dictionary of tensors to enqueue. |
| `batch_size` | The new batch size pulled from the queue. |
| `capacity` | An integer. The maximum number of elements in the queue. |
| `min_after_dequeue` | Minimum number elements in the queue after a dequeue, used to ensure a level of mixing of elements. |
| `keep_input` | A `bool` Tensor. This tensor controls whether the input is added to the queue or not. If it is a scalar and evaluates `True`, then `tensors` are all added to the queue. If it is a vector and `enqueue_many` is `True`, then each example is added to the queue only if the corresponding value in `keep_input` is `True`. This tensor essentially acts as a filtering mechanism. |
| `num_threads` | The number of threads enqueuing `tensor_list`. |
| `seed` | Seed for the random shuffling within the queue. |
| `enqueue_many` | Whether each tensor in `tensor_list` is a single example. |
| `shapes` | (Optional) The shapes for each example. Defaults to the inferred shapes for `tensor_list`. |
| `allow_smaller_final_batch` | (Optional) Boolean. If `True`, allow the final batch to be smaller if there are insufficient items left in the queue. |
| `shared_name` | (Optional) If set, this queue will be shared under the given name across multiple sessions. |
| `name` | (Optional) A name for the operations. |

|     |
| --- |
| Returns<br>------- |     |
| A list or dictionary of tensors with the types as `tensors`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the `shapes` are not specified, and cannot be inferred from the elements of `tensors`. |

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