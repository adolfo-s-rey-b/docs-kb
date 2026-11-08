[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/tanh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/tanh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.tanh Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/tanh?version=stable#returns_1)
    

See Stable See Nightly

Computes hyperbolic tangent of `x` element-wise.

#### View aliases

**Main aliases**

[`tf.nn.tanh`](https://www.tensorflow.org/api_docs/python/tf/math/tanh)
, [`tf.tanh`](https://www.tensorflow.org/api_docs/python/tf/math/tanh)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tanh`](https://www.tensorflow.org/api_docs/python/tf/math/tanh)

tf.math.tanh(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function) |

Given an input tensor, this function computes hyperbolic tangent of every element in the tensor. Input range is `[-inf, inf]` and output range is `[-1,1]`.

  `x = tf.constant([-float("inf"), -5, -0.5, 1, 1.2, 2, 3, float("inf")])`
  `tf.math.tanh(x)`
  `  <tf.Tensor: shape=(8,), dtype=float32, numpy=`
  `  array([-1.0, -0.99990916, -0.46211717,  0.7615942 ,  0.8336547 ,`\
  `          0.9640276 ,  0.9950547 ,  1.0], dtype=float32)>`
    
  

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`.<br><br>If `x` is a `SparseTensor`, returns `SparseTensor(x.indices, tf.math.tanh(x.values, ...), x.dense_shape)` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.