[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/lu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/lu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.lu Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu#returns)
    

Computes the LU decomposition of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.lu`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)

tf.linalg.lu(
        input: Annotated[Any, TV_Lu_T],
        output_idx_type: TV_Lu_output_idx_type = tf.dtypes.int32,
        name=None
    )

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices.

The input has to be invertible.

The output consists of two tensors LU and P containing the LU decomposition of all input submatrices `[..., :, :]`. LU encodes the lower triangular and upper triangular factors.

For each input submatrix of shape `[M, M]`, L is a lower triangular matrix of shape `[M, M]` with unit diagonal whose entries correspond to the strictly lower triangular part of LU. U is a upper triangular matrix of shape `[M, M]` whose entries correspond to the upper triangular part, including the diagonal, of LU.

P represents a permutation matrix encoded as a list of indices each between `0` and `M-1`, inclusive. If P\_mat denotes the permutation matrix corresponding to P, then the L, U and P satisfies P\_mat \* input = L \* U.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. A tensor of shape `[..., M, M]` whose inner-most 2 dimensions form matrices of size `[M, M]`. |
| `output_idx_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (lu, p). |     |
| `lu` | A `Tensor`. Has the same type as `input`. |
| `p` | A `Tensor` of type `output_idx_type`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.