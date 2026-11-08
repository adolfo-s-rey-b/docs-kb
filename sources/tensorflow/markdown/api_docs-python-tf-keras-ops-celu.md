[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.celu Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L677-L702)

Continuously-differentiable exponential linear unit.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.celu`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/celu)

tf.keras.ops.celu(
        x, alpha=1.0
    )

#### It is defined as:

`f(x) = alpha * (exp(x / alpha) - 1) for x < 0`, `f(x) = x for x >= 0`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `alpha` | the α value for the CELU formulation. Defaults to `1.0`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape as `x`. |     |

#### Example:

    x = np.array([-1., 0., 1.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.