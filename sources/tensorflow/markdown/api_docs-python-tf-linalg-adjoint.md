[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Fadjoint&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.adjoint Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L102-L128)

Transposes the last two dimensions of and conjugates tensor `matrix`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.adjoint`](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint)

tf.linalg.adjoint(
        matrix, name=None
    )

#### For example:

x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],\
                     [4 + 4j, 5 + 5j, 6 + 6j]])
    tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],\
                          #  [2 - 2j, 5 - 5j],\
                          #  [3 - 3j, 6 - 6j]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `matrix` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op` (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of matrix. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.