[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/det#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/det)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/det?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/det#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/det#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.det Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/det#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/det#returns)
    

Computes the determinant of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.det`](https://www.tensorflow.org/api_docs/python/tf/linalg/det)
, [`tf.compat.v1.matrix_determinant`](https://www.tensorflow.org/api_docs/python/tf/linalg/det)

tf.linalg.det(
        input: Annotated[Any, TV_MatrixDeterminant_T], name=None
    ) -> Annotated[Any, TV_MatrixDeterminant_T]

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. The output is a tensor containing the determinants for all input submatrices `[..., :, :]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
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