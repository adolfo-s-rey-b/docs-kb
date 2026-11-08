[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.logical\_xor Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1784-L1833)

Logical XOR function.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.logical_xor`](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor)
, [`tf.compat.v1.math.logical_xor`](https://www.tensorflow.org/api_docs/python/tf/math/logical_xor)

tf.math.logical_xor(
        x, y, name='LogicalXor'
    )

x ^ y = (x | y) & ~(x & y)

Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 shapes. For example, `x` and `y` can be:

*   Two single elements of type `bool`
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     of type `bool` and one single `bool`, where the result will be calculated by applying logical XOR with the single element to each element in the larger Tensor.
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical XOR of the two input tensors.

#### Usage:

    a = tf.constant([True])

    c = tf.constant([True])

    y = tf.constant([False, False, True, True])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> type bool. |
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the same size as that of x or y. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.