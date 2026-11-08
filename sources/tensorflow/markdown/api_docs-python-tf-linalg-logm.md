[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/logm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/logm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/logm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/logm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/logm#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.logm Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/logm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/logm#returns)
    

Computes the matrix logarithm of one or more square matrices:

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.logm`](https://www.tensorflow.org/api_docs/python/tf/linalg/logm)

tf.linalg.logm(
        input: Annotated[Any, TV_MatrixLogarithm_T], name=None
    ) -> Annotated[Any, TV_MatrixLogarithm_T]

log(exp(A))\=A

This op is only defined for complex matrices. If A is positive-definite and real, then casting to a complex matrix, taking the logarithm and casting back to a real matrix will give the correct result.

This function computes the matrix logarithm using the Schur-Parlett algorithm. Details of the algorithm can be found in Section 11.6.2 of: Nicholas J. Higham, Functions of Matrices: Theory and Computation, SIAM 2008. ISBN 978-0-898716-46-7.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. The output is a tensor of the same shape as the input containing the exponential for all input submatrices `[..., :, :]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. Shape is `[..., M, M]`. |
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