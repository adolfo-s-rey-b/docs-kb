[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/banded_triangular_solve#main-content)

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
    

tf.linalg.banded\_triangular\_solve Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L350-L443)

Solve triangular systems of equations with a banded solver.

tf.linalg.banded_triangular_solve(
        bands, rhs, lower=True, adjoint=False, name=None
    )

`bands` is a tensor of shape `[..., K, M]`, where `K` represents the number of bands stored. This corresponds to a batch of `M` by `M` matrices, whose `K` subdiagonals (when `lower` is `True`) are stored.

This operator broadcasts the batch dimensions of `bands` and the batch dimensions of `rhs`.

#### Examples:

Storing 2 bands of a 3x3 matrix. Note that first element in the second row is ignored due to the 'LEFT\_RIGHT' padding.

    x = [[2., 3., 4.], [1., 2., 3.]]

Storing 2 superdiagonals of a 4x4 matrix. Because of the 'LEFT\_RIGHT' padding the last element of the first row is ignored.

    x = [[2., 3., 4., 5.], [-1., -2., -3., -4.]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bands` | A `Tensor` describing the bands of the left hand side, with shape `[..., K, M]`. The `K` rows correspond to the diagonal to the `K - 1`\-th diagonal (the diagonal is the top row) when `lower` is `True` and otherwise the `K - 1`\-th superdiagonal to the diagonal (the diagonal is the bottom row) when `lower` is `False`. The bands are stored with 'LEFT\_RIGHT' alignment, where the superdiagonals are padded on the right and subdiagonals are padded on the left. This is the alignment cuSPARSE uses. See [`tf.linalg.set_diag`](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag)<br> for more details. |
| `rhs` | A `Tensor` of shape \[..., M\] or \[..., M, N\] and with the same dtype as `diagonals`. Note that if the shape of `rhs` and/or `diags` isn't known statically, `rhs` will be treated as a matrix rather than a vector. |
| `lower` | An optional `bool`. Defaults to `True`. Boolean indicating whether `bands` represents a lower or upper triangular matrix. |
| `adjoint` | An optional `bool`. Defaults to `False`. Boolean indicating whether to solve with the matrix's block-wise adjoint. |
| `name` | A name to give this `Op` (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape \[..., M\] or \[..., M, N\] containing the solutions. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.