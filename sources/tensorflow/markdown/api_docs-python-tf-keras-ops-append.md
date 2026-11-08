[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.append Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L653-L692)

Append tensor `x2` to the end of tensor `x1`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.append`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/append)

tf.keras.ops.append(
        x1, x2, axis=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First input tensor. |
| `x2` | Second input tensor. |
| `axis` | Axis along which tensor `x2` is appended to tensor `x1`. If `None`, both tensors are flattened before use. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the values of `x2` appended to `x1`. |     |

#### Examples:

    x1 = keras.ops.convert_to_tensor([1, 2, 3])

When `axis` is specified, `x1` and `x2` must have compatible shapes.

>>> x1 = keras.ops.convert_to_tensor([[1, 2, 3], [4, 5, 6]])
    >>> x2 = keras.ops.convert_to_tensor([[7, 8, 9]])
    >>> keras.ops.append(x1, x2, axis=0)
    array([[1, 2, 3],\
            [4, 5, 6],\
            [7, 8, 9]], dtype=int32)
    >>> x3 = keras.ops.convert_to_tensor([7, 8, 9])
    >>> keras.ops.append(x1, x3, axis=0)
    Traceback (most recent call last):
        ...
    TypeError: Cannot concatenate arrays with different numbers of
    dimensions: got (2, 3), (3,).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.