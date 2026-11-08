[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/shape_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/shape_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/shape_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/shape_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/shape_n#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.shape\_n Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/shape_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/shape_n#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L732-L759)

Returns shape of a list of tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.shape_n`](https://www.tensorflow.org/api_docs/python/tf/shape_n)

tf.shape_n(
        input,
        out_type=tf.dtypes.int32,
        name=None
    )

Given a list of tensors, [`tf.shape_n`](https://www.tensorflow.org/api_docs/python/tf/shape_n)
 is much faster than applying [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape)
 to each tensor individually.

>>> a = tf.ones([1, 2])
    >>> b = tf.ones([2, 3])
    >>> c = tf.ones([3, 4])
    >>> tf.shape_n([a, b, c])
    [<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>,\
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 3], dtype=int32)>,\
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([3, 4], dtype=int32)>]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A list of at least 1 `Tensor` object with the same dtype. |
| `out_type` | The specified output type of the operation (`int32` or `int64`). Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>(optional). |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Tensor` specifying the shape of each input tensor with type of `out_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.