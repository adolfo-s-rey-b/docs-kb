[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.gammainc Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/gammainc#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/math.py#L656-L681)

Computes the regularized lower incomplete gamma function.

tf.keras.ops.gammainc(
        x1, x2
    )

The regularized lower incomplete gamma function is defined as: P(x1, x2) = 1 / Γ(x1) \* ∫₀ˣ² t^(x1 - 1) e^(-t) dt where `Γ(x1)` is the gamma function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | A tensor containing the shape parameter. |
| `x2` | A tensor containing the upper limit of integration. Must be broadcast-compatible with `x1`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the regularized lower incomplete gamma function evaluated elementwise. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([1.0, 2.0, 3.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.