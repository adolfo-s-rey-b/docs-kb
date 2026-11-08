[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.to\_double Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/to_double#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1201-L1238)

Casts a tensor to type `float64`. (deprecated)

tf.compat.v1.to_double(
        x, name='ToDouble'
    )

Migrate to TF2
--------------

This name was deprecated and removed in TF2, but has an exact replacement [`tf.cast(..., tf.double)`](https://www.tensorflow.org/api_docs/python/tf/cast)
. There are no further issues with eager execution or tf.function.

Before:

    tf.compat.v1.to_double(tf.constant(3.14, dtype=tf.float32))

After:

    tf.cast(tf.constant(3.14, dtype=tf.float32), tf.double)

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` or `SparseTensor` or `IndexedSlices`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with type `float64`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `x` cannot be cast to the `float64`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.