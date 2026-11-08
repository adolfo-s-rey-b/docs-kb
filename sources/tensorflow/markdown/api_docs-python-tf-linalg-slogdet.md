[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.slogdet Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet#returns)
    

Computes the sign and the log of the absolute value of the determinant of

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.slogdet`](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet)

tf.linalg.slogdet(
        input: Annotated[Any, TV_LogMatrixDeterminant_T], name=None
    )

one or more square matrices.

The input is a tensor of shape `[N, M, M]` whose inner-most 2 dimensions form square matrices. The outputs are two tensors containing the signs and absolute values of the log determinants for all N input submatrices `[..., :, :]` such that `determinant = sign*exp(log_abs_determinant)`. The `log_abs_determinant` is computed as `det(P)*sum(log(diag(LU)))` where `LU` is the `LU` decomposition of the input and `P` is the corresponding permutation matrix.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`. Shape is `[N, M, M]`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (sign, log\_abs\_determinant). |     |
| `sign` | A `Tensor`. Has the same type as `input`. |
| `log_abs_determinant` | A `Tensor`. Has the same type as `input`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.