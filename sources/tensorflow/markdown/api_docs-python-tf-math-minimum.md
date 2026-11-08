[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/minimum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/minimum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/minimum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fminimum&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/minimum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/minimum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/minimum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.minimum Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/minimum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/minimum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/minimum#returns)
    

Returns the min of x and y (i.e. x < y ? x : y) element-wise.

#### View aliases

**Main aliases**

[`tf.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)

tf.math.minimum(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) | *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer) |

Both inputs are number-type tensors (except complex). `minimum` expects that both tensors have the same `dtype`.

#### Examples:

    x = tf.constant([0., 0., 0., 0.])

Note that `minimum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 for `x` and `y`.

    x = tf.constant([-5., 0., 0., 0.])

The reduction version of this elementwise operation is [`tf.math.reduce_min`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.