[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.constant Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/constant_op.py#L111-L174)

Creates a constant tensor.

tf.compat.v1.constant(
        value, dtype=None, shape=None, name='Const', verify_shape=False
    ) -> Union[tf.Operation, ops._EagerTensorBase]

The resulting tensor is populated with values of type `dtype`, as specified by arguments `value` and (optionally) `shape` (see examples below).

The argument `value` can be a constant value, or a list of values of type `dtype`. If `value` is a list, then the length of the list must be less than or equal to the number of elements implied by the `shape` argument (if specified). In the case where the list length is less than the number of elements specified by `shape`, the last element in the list will be used to fill the remaining entries.

The argument `shape` is optional. If present, it specifies the dimensions of the resulting tensor. If not present, the shape of `value` is used.

If the argument `dtype` is not specified, then the type is inferred from the type of `value`.

#### For example:

# Constant 1-D Tensor populated with value list.
    tensor = tf.constant([1, 2, 3, 4, 5, 6, 7]) => [1 2 3 4 5 6 7]
    
    # Constant 2-D tensor populated with scalar value -1.
    tensor = tf.constant(-1.0, shape=[2, 3]) => [[-1. -1. -1.]\
                                                 [-1. -1. -1.]]

[`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
 differs from [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
 in a few ways:

*   [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
     supports arbitrary constants, not just uniform scalar Tensors like [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
    .
*   [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
     creates a `Const` node in the computation graph with the exact value at graph construction time. On the other hand, [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
     creates an Op in the graph that is expanded at runtime.
*   Because [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
     only embeds constant values in the graph, it does not support dynamic shapes based on other runtime Tensors, whereas [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
     does.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A constant value (or list) of output type `dtype`. |
| `dtype` | The type of the elements of the resulting tensor. |
| `shape` | Optional dimensions of resulting tensor. |
| `name` | Optional name for the tensor. |
| `verify_shape` | Boolean that enables verification of a shape of values. |

|     |
| --- |
| Returns<br>------- |     |
| A Constant Tensor. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if shape is incorrectly specified or unsupported. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.