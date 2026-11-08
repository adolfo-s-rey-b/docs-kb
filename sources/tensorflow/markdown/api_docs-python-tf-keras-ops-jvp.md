[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.jvp Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/linalg.py#L872-L914)

Computes a (forward-mode) Jacobian-vector product of `fun`.

#### View aliases

**Main aliases**

[`tf.keras.ops.linalg.jvp`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/jvp)

tf.keras.ops.jvp(
        fun, primals, tangents, has_aux=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fun` | Function to be differentiated. Its arguments should be arrays, scalars, or standard Python containers of arrays or scalars. It should return an array, scalar, or standard Python container of arrays or scalars. |
| `primals` | The primal values at which the Jacobian of `fun` should be evaluated. Should be either a tuple or a list of arguments, and its length should be equal to the number of positional parameters of `fun`. |
| `tangents` | The tangent vector for which the Jacobian-vector product should be evaluated. Should be either a tuple or a list of tangents, with the same tree structure and array shapes as `primals`. |
| `has_aux` | Optional, bool. Indicates whether `fun` returns a pair where the first element is considered the output of the mathematical function to be differentiated and the second element is auxiliary data. Default is False. |

|     |
| --- |
| Returns<br>------- |     |
| If `has_aux` is False, returns a (`primals_out`, `tangents_out`) pair, where `primals_out` is `fun(*primals)`, and `tangents_out` is the Jacobian-vector product of `fun` evaluated at `primals` with `tangents`. The `tangents_out` value has the same Python tree structure and shapes as `primals_out`.<br><br>If `has_aux` is True, returns a (`primals_out`, `tangents_out`, `aux`) tuple where `aux` is the auxiliary data returned by `fun`. |     |

#### Example:

    from keras import ops

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.