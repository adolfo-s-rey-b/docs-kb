[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/cast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/cast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/cast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/cast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/cast#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/cast#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.cast Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/cast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/cast#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/cast#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L972-L1054)

Casts a tensor to a new type.

#### View aliases

**Main aliases**

[`tf.dtypes.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
, [`tf.compat.v1.dtypes.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)

tf.cast(
        x, dtype, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

The operation casts `x` (in case of `Tensor`) or `x.values` (in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

#### For example:

    x = tf.constant([1.8, 2.2], dtype=tf.float32)

Notice [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
 has an alias [`tf.dtypes.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
:

    x = tf.constant([1.8, 2.2], dtype=tf.float32)

The operation supports data types (for `x` and `dtype`) of `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`. In case of casting from complex types (`complex64`, `complex128`) to real types, only the real part of `x` is returned. In case of casting from real types to complex types (`complex64`, `complex128`), the imaginary part of the returned value is set to `0`. The handling of complex types here matches the behavior of numpy.

Note casting nan and inf values to integral types has undefined behavior.

Note this operation can lead to a loss of precision when converting native Python `float` and `complex` variables to [`tf.float64`](https://www.tensorflow.org/api_docs/python/tf#float64)
 or [`tf.complex128`](https://www.tensorflow.org/api_docs/python/tf#complex128)
 tensors, since the input is first converted to the `float32` data type and then widened. It is recommended to use [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
 instead of [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
 for any non-tensor inputs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`. |
| `dtype` | The destination type. The list of supported dtypes is the same as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and same type as `dtype`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `x` cannot be cast to the `dtype`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.