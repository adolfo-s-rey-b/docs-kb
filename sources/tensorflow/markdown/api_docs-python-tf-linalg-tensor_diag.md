[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.tensor\_diag Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

Returns a diagonal tensor with a given diagonal values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.diag`](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag)
, [`tf.compat.v1.linalg.tensor_diag`](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag)

tf.linalg.tensor_diag(
        diagonal: Annotated[Any, TV_Diag_T], name=None
    ) -> Annotated[Any, TV_Diag_T]

Given a `diagonal`, this operation returns a tensor with the `diagonal` and everything else padded with zeros. The diagonal is computed as follows:

Assume `diagonal` has dimensions \[D1,..., Dk\], then the output is a tensor of rank 2k with dimensions \[D1,..., Dk, D1,..., Dk\] where:

`output[i1,..., ik, i1,..., ik] = diagonal[i1, ..., ik]` and 0 everywhere else.

#### For example:

# 'diagonal' is [1, 2, 3, 4]
    tf.diag(diagonal) ==> [[1, 0, 0, 0]\
                           [0, 2, 0, 0]\
                           [0, 0, 3, 0]\
                           [0, 0, 0, 4]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `diagonal` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`. Rank k tensor where k is at most 1. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `diagonal`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.