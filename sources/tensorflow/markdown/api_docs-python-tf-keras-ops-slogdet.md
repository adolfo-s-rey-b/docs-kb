[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.slogdet Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9548-L9564)

Compute the sign and natural logarithm of the determinant of a matrix.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.slogdet`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/slogdet)

tf.keras.ops.slogdet(
        x
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input matrix. It must 2D and square. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple `(sign, logabsdet)`. `sign` is a number representing the sign of the determinant. For a real matrix, this is 1, 0, or -1. For a complex matrix, this is a complex number with absolute value 1 (i.e., it is on the unit circle), or else 0. `logabsdet` is the natural log of the absolute value of the determinant. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.