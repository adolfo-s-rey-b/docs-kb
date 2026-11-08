[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.argpartition Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9593-L9617)

Performs an indirect partition along the given axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.argpartition`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argpartition)

tf.keras.ops.argpartition(
        x, kth, axis=-1
    )

It returns an array of indices of the same shape as `x` that index data along the given axis in partitioned order.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Array to sort. |
| `kth` | Element index to partition by. The k-th element will be in its final sorted position and all smaller elements will be moved before it and all larger elements behind it. The order of all elements in the partitions is undefined. If provided with a sequence of k-th it will partition all of them into their sorted position at once. |
| `axis` | Axis along which to sort. The default is -1 (the last axis). If `None`, the flattened array is used. |

|     |
| --- |
| Returns<br>------- |     |
| Array of indices that partition `x` along the specified `axis`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.