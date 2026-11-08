[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/inv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/inv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/inv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/inv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/inv#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.inv Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/inv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/inv#returns)
    

Computes the inverse of one or more square invertible matrices or their adjoints (conjugate transposes).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.inv`](https://www.tensorflow.org/api_docs/python/tf/linalg/inv)
, [`tf.compat.v1.matrix_inverse`](https://www.tensorflow.org/api_docs/python/tf/linalg/inv)

tf.linalg.inv(
        input: Annotated[Any, TV_MatrixInverse_T], adjoint: bool = False, name=None
    ) -> Annotated[Any, TV_MatrixInverse_T]

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. The output is a tensor of the same shape as the input containing the inverse for all input submatrices `[..., :, :]`.

The op uses LU decomposition with partial pivoting to compute the inverses.

If a matrix is not invertible there is no guarantee what the op does. It may detect the condition and raise an exception or it may simply return a garbage result.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `adjoint` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.