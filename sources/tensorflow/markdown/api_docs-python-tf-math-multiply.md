[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/multiply#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/multiply?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fmultiply&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/multiply#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/multiply#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/multiply#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/multiply#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.multiply Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/multiply#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/multiply#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/multiply#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/multiply#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L505-L554)

Returns an element-wise x \* y.

#### View aliases

**Main aliases**

[`tf.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)

tf.math.multiply(
        x, y, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model)<br>    <br>*   [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods) | *   [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning)<br>    <br>*   [Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder)<br>    <br>*   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [TFX Estimator Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components) |

#### For example:

    x = tf.constant(([1, 2, 3, 4]))

Since [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
 will convert its arguments to `Tensor`s, you can also pass in non-`Tensor` arguments:

    tf.math.multiply(7,6)

If `x.shape` is not the same as `y.shape`, they will be broadcast to a compatible shape. (More about broadcasting [here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
.)

#### For example:

    x = tf.ones([1, 2]);

The reduction version of this elementwise operation is [`tf.math.reduce_prod`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A Tensor. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

Returns
-------

A `Tensor`. Has the same type as `x`.

|     |
| --- |
| Raises<br>------ |     |
| *   InvalidArgumentError: When `x` and `y` have incompatible shapes or types. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.