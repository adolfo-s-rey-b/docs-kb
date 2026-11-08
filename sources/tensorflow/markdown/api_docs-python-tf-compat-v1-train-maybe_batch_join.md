[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.maybe\_batch\_join Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/maybe_batch_join#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/input.py#L1194-L1248)

Runs a list of tensors to conditionally fill a queue to create batches. (deprecated)

tf.compat.v1.train.maybe_batch_join(
        tensors_list,
        keep_input,
        batch_size,
        capacity=32,
        enqueue_many=False,
        shapes=None,
        dynamic_pad=False,
        allow_smaller_final_batch=False,
        shared_name=None,
        name=None
    )

See docstring in `batch_join` for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors_list` | A list of tuples or dictionaries of tensors to enqueue. |
| `keep_input` | A `bool` Tensor. This tensor controls whether the input is added to the queue or not. If it is a scalar and evaluates `True`, then `tensors` are all added to the queue. If it is a vector and `enqueue_many` is `True`, then each example is added to the queue only if the corresponding value in `keep_input` is `True`. This tensor essentially acts as a filtering mechanism. |
| `batch_size` | An integer. The new batch size pulled from the queue. |
| `capacity` | An integer. The maximum number of elements in the queue. |
| `enqueue_many` | Whether each tensor in `tensor_list_list` is a single example. |
| `shapes` | (Optional) The shapes for each example. Defaults to the inferred shapes for `tensor_list_list[i]`. |
| `dynamic_pad` | Boolean. Allow variable dimensions in input shapes. The given dimensions are padded upon dequeue so that tensors within a batch have the same shapes. |
| `allow_smaller_final_batch` | (Optional) Boolean. If `True`, allow the final batch to be smaller if there are insufficient items left in the queue. |
| `shared_name` | (Optional) If set, this queue will be shared under the given name across multiple sessions. |
| `name` | (Optional) A name for the operations. |

|     |
| --- |
| Returns<br>------- |     |
| A list or dictionary of tensors with the same number and types as `tensors_list[i]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the `shapes` are not specified, and cannot be inferred from the elements of `tensor_list_list`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.