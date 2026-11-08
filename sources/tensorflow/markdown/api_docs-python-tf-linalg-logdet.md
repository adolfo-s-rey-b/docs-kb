[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#returns_1)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#numpy-compatibility_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.logdet Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#returns_1)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet?version=stable#numpy-compatibility_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L68-L99)

Computes log of the determinant of a hermitian positive definite matrix.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.logdet`](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet)

tf.linalg.logdet(
        matrix, name=None
    )

# Compute the determinant of a matrix while reducing the chance of over- or
    underflow:
    A = ... # shape 10 x 10
    det = tf.exp(tf.linalg.logdet(A))  # scalar

|     |     |
| --- | --- |
| Args<br>---- |     |
| `matrix` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op`. Defaults to `logdet`. |

|     |
| --- |
| Returns<br>------- |     |
| The natural log of the determinant of `matrix`. |     |

numpy compatibility
-------------------

Equivalent to numpy.linalg.slogdet, although no sign is returned since only hermitian positive definite matrices are supported.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.