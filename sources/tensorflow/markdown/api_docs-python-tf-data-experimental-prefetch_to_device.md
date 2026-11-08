[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2Fprefetch_to_device&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.prefetch\_to\_device Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/prefetching_ops.py#L33-L62)

A transformation that prefetches dataset values to the given `device`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.prefetch_to_device`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/prefetch_to_device)

tf.data.experimental.prefetch_to_device(
        device, buffer_size=None
    )

For example,

>>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    >>> dataset = dataset.apply(tf.data.experimental.prefetch_to_device("/cpu:0"))
    >>> for element in dataset:
    ...   print(f'Tensor {element} is on device {element.device}')
    Tensor 1 is on device /job:localhost/replica:0/task:0/device:CPU:0
    Tensor 2 is on device /job:localhost/replica:0/task:0/device:CPU:0
    Tensor 3 is on device /job:localhost/replica:0/task:0/device:CPU:0

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | A string. The name of a device to which elements will be prefetched. |
| `buffer_size` | (Optional.) The number of elements to buffer on `device`. Defaults to an automatically chosen value. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.