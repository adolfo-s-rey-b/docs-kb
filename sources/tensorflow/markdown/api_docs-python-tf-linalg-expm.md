[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/expm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/expm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Fexpm&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.expm Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#raises)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/expm#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L232-L347)

Computes the matrix exponential of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.expm`](https://www.tensorflow.org/api_docs/python/tf/linalg/expm)

tf.linalg.expm(
        input, name=None
    )

exp(A)\=∞∑n\=0An/n!

The exponential is computed using a combination of the scaling and squaring method and the Pade approximation. Details can be found in: Nicholas J. Higham, "The scaling and squaring method for the matrix exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. The output is a tensor of the same shape as the input containing the exponential for all input submatrices `[..., :, :]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op` (optional). |

|     |
| --- |
| Returns<br>------- |     |
| the matrix exponential of the input. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | An unsupported type is provided as input. |

scipy compatibility
-------------------

Equivalent to scipy.linalg.expm

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.