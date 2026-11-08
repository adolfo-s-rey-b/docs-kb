[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.accumulate\_n Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4057-L4140)

Returns the element-wise sum of a list of tensors. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.accumulate_n`](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n)
, [`tf.compat.v1.math.accumulate_n`](https://www.tensorflow.org/api_docs/python/tf/math/accumulate_n)

tf.math.accumulate_n(
        inputs, shape=None, tensor_dtype=None, name=None
    )

Optionally, pass `shape` and `tensor_dtype` for shape and type checking, otherwise, these are inferred.

#### For example:

    a = tf.constant([[1, 2], [3, 4]])

    # Explicitly pass shape and type

#### See Also:

*   [`tf.reduce_sum(inputs, axis=0)`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)
     - This performe the same mathematical operation, but [`tf.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
     may be more efficient because it sums the tensors directly. `reduce_sum` on the other hand calls [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
     on the list of tensors, unncessairly stacking them into a single tensor before summing.
*   [`tf.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
     - This is another python wrapper for the same Op. It has nearly identical functionality.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A list of `Tensor` objects, each with same shape and type. |
| `shape` | Expected shape of elements of `inputs` (optional). Also controls the output shape of this op, which may affect type inference in other ops. A value of `None` means "infer the input shape from the shapes in `inputs`". |
| `tensor_dtype` | Expected data type of `inputs` (optional). A value of `None` means "infer the input dtype from `inputs[0]`". |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of same shape and type as the elements of `inputs`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `inputs` don't all have same shape and dtype or the shape cannot be inferred. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.