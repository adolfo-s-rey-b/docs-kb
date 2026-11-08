[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.argsort Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1154-L1189)

Returns the indices that would sort a tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.argsort`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argsort)

tf.keras.ops.argsort(
        x, axis=-1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Axis along which to sort. Defaults to `-1` (the last axis). If `None`, the flattened tensor is used. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of indices that sort `x` along the specified `axis`. |     |

#### Examples:

#### One dimensional array:

    x = keras.ops.array([3, 1, 2])

Two-dimensional array:

>>> x = keras.ops.array([[0, 3], [3, 2], [4, 5]])
    >>> x
    array([[0, 3],\
           [3, 2],\
           [4, 5]], dtype=int32)
    >>> keras.ops.argsort(x, axis=0)
    array([[0, 1],\
           [1, 0],\
           [2, 2]], dtype=int32)
    >>> keras.ops.argsort(x, axis=1)
    array([[0, 1],\
           [1, 0],\
           [0, 1]], dtype=int32)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.