[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.all Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L317-L351)

Test whether all array elements along a given axis evaluate to `True`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.all`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/all)

tf.keras.ops.all(
        x, axis=None, keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | An integer or tuple of integers that represent the axis along which a logical AND reduction is performed. The default (`axis=None`) is to perform a logical AND over all the dimensions of the input array. `axis` may be negative, in which case it counts for the last to the first axis. |
| `keepdims` | If `True`, axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| The tensor containing the logical AND reduction over the `axis`. |     |

#### Examples:

    x = keras.ops.convert_to_tensor([True, False])

    x = keras.ops.convert_to_tensor([[True, False], [True, True]])

`keepdims=True` outputs a tensor with dimensions reduced to one.

>>> x = keras.ops.convert_to_tensor([[True, False], [True, True]])
    >>> keras.ops.all(x, keepdims=True)
    array([[False]], shape=(1, 1), dtype=bool)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.