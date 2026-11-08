[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.where Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4364-L4442)

Return the elements, either from `x` or `y`, depending on the `condition`.

tf.compat.v1.where(
        condition, x=None, y=None, name=None
    )

Migrate to TF2
--------------

This API is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. However, this is still a legacy API endpoint originally designed for TF1. To migrate to fully-native TF2, please replace its usage with [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)
 instead, which is directly backwards compatible with [`tf.compat.v1.where`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where)
.

However,[`tf.compat.v1.where`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where)
 is more restrictive than [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)
, requiring `x` and `y` to have the same shape, and returning a `Tensor` with the same type and shape as `x`, `y` (if they are both non-None).

[`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)
 will accept `x`, `y` that are not the same shape as long as they are broadcastable with one another and with `condition`, and will return a `Tensor` with shape broadcast from `condition`, `x`, and `y`.

For example, the following works with [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)
 but not [`tf.compat.v1.where`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/where)
:

    tf.where([True, False, False, True], [1,2,3,4], [100])

    tf.where(True, [1,2,3,4], 100)

Description
-----------

If both `x` and `y` are None, then this operation returns the coordinates of true elements of `condition`. The coordinates are returned in a 2-D tensor where the first dimension (rows) represents the number of true elements, and the second dimension (columns) represents the coordinates of the true elements. Keep in mind, the shape of the output tensor can vary depending on how many true values there are in input. Indices are output in row-major order.

If both non-None, `x` and `y` must have the same shape. The `condition` tensor must be a scalar if `x` and `y` are scalar. If `x` and `y` are tensors of higher rank, then `condition` must be either a vector with size matching the first dimension of `x`, or must have the same shape as `x`.

The `condition` tensor acts as a mask that chooses, based on the value at each element, whether the corresponding element / row in the output should be taken from `x` (if true) or `y` (if false).

If `condition` is a vector and `x` and `y` are higher rank matrices, then it chooses which row (outer dimension) to copy from `x` and `y`. If `condition` has the same shape as `x` and `y`, then it chooses which element to copy from `x` and `y`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `condition` | A `Tensor` of type `bool` |
| `x` | A Tensor which may have the same shape as `condition`. If `condition` is rank 1, `x` may have higher rank, but its first dimension must match the size of `condition`. |
| `y` | A `tensor` with the same shape and type as `x`. |
| `name` | A name of the operation (optional) |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type and shape as `x`, `y` if they are non-None. Otherwise, a `Tensor` with shape `(num_true, rank(condition))`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When exactly one of `x` or `y` is non-None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.