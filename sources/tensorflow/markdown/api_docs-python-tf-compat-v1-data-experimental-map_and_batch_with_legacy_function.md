[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.data.experimental.map\_and\_batch\_with\_legacy\_function Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental/map_and_batch_with_legacy_function#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/batching.py#L145-L202)

Fused implementation of `map` and `batch`. (deprecated)

tf.compat.v1.data.experimental.map_and_batch_with_legacy_function(
        map_func,
        batch_size,
        num_parallel_batches=None,
        drop_remainder=False,
        num_parallel_calls=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `map_func` | A function mapping a nested structure of tensors to another nested structure of tensors. |
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |
| `num_parallel_batches` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of batches to create in parallel. On one hand, higher values can help mitigate the effect of stragglers. On the other hand, higher values can increase contention if CPU is scarce. |
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in case its size is smaller than desired; the default behavior is not to drop the smaller batch. |
| `num_parallel_calls` | (Optional.) A [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of elements to process in parallel. If not specified, `batch_size * num_parallel_batches` elements will be processed in parallel. If the value [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> is used, then the number of parallel calls is set dynamically based on available CPU. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If both `num_parallel_batches` and `num_parallel_calls` are specified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.