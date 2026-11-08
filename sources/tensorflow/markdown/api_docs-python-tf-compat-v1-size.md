[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.size Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/size#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L802-L838)

Returns the size of a tensor.

tf.compat.v1.size(
        input, name=None, out_type=None
    )

Returns a 0-D `Tensor` representing the number of elements in `input` of type `out_type`. Defaults to tf.int32.

#### For example:

t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
    tf.size(t)  # 12

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` or `SparseTensor`. |
| `name` | A name for the operation (optional). |
| `out_type` | (Optional) The specified non-quantized numeric output type of the operation. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. (Note: there is an experimental flag, `tf_shape_default_int64` that changes the default to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. This is an unsupported, experimental setting that causes known breakages.) |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `out_type`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |     |

numpy compatibility
-------------------

Equivalent to np.size()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.