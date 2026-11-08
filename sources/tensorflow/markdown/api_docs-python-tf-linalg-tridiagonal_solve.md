[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.tridiagonal\_solve Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L446-L617)

Solves tridiagonal systems of equations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.tridiagonal_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve)

tf.linalg.tridiagonal_solve(
        diagonals,
        rhs,
        diagonals_format='compact',
        transpose_rhs=False,
        conjugate_rhs=False,
        name=None,
        partial_pivoting=True,
        perturb_singular=False
    )

The input can be supplied in various formats: `matrix`, `sequence` and `compact`, specified by the `diagonals_format` arg.

In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with two inner-most dimensions representing the square tridiagonal matrices. Elements outside of the three diagonals will be ignored.

In `sequence` format, `diagonals` are supplied as a tuple or list of three tensors of shapes `[..., N]`, `[..., M]`, `[..., N]` representing superdiagonals, diagonals, and subdiagonals, respectively. `N` can be either `M-1` or `M`; in the latter case, the last element of superdiagonal and the first element of subdiagonal will be ignored.

In `compact` format the three diagonals are brought together into one tensor of shape `[..., 3, M]`, with last two dimensions containing superdiagonals, diagonals, and subdiagonals, in order. Similarly to `sequence` format, elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

The `compact` format is recommended as the one with best performance. In case you need to cast a tensor into a compact format manually, use [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd)
. An example for a tensor of shape \[m, m\]:

rhs = tf.constant([...])
    matrix = tf.constant([[...]])
    m = matrix.shape[0]
    dummy_idx = [0, 0]  # An arbitrary element to use as a dummy
    indices = [[[i, i + 1] for i in range(m - 1)] + [dummy_idx],  # Superdiagonal\
             [[i, i] for i in range(m)],                          # Diagonal\
             [dummy_idx] + [[i + 1, i] for i in range(m - 1)]]    # Subdiagonal
    diagonals=tf.gather_nd(matrix, indices)
    x = tf.linalg.tridiagonal_solve(diagonals, rhs)

Regardless of the `diagonals_format`, `rhs` is a tensor of shape `[..., M]` or `[..., M, K]`. The latter allows to simultaneously solve K systems with the same left-hand sides and K different right-hand sides. If `transpose_rhs` is set to `True` the expected shape is `[..., M]` or `[..., K, M]`.

The batch dimensions, denoted as `...`, must be the same in `diagonals` and `rhs`.

The output is a tensor of the same shape as `rhs`: either `[..., M]` or `[..., M, K]`.

The op isn't guaranteed to raise an error if the input matrix is not invertible. [`tf.debugging.check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics)
 can be applied to the output to detect invertibility problems.

On CPU, solution is computed via Gaussian elimination with or without partial pivoting, depending on `partial_pivoting` parameter. On GPU, Nvidia's cuSPARSE library is used: [https://docs.nvidia.com/cuda/cusparse/index.html#gtsv](https://docs.nvidia.com/cuda/cusparse/index.html#gtsv)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `diagonals` | A `Tensor` or tuple of `Tensor`s describing left-hand sides. The shape depends of `diagonals_format`, see description above. Must be `float32`, `float64`, `complex64`, or `complex128`. |
| `rhs` | A `Tensor` of shape \[..., M\] or \[..., M, K\] and with the same dtype as `diagonals`. Note that if the shape of `rhs` and/or `diags` isn't known statically, `rhs` will be treated as a matrix rather than a vector. |
| `diagonals_format` | one of `matrix`, `sequence`, or `compact`. Default is `compact`. |
| `transpose_rhs` | If `True`, `rhs` is transposed before solving (has no effect if the shape of rhs is \[..., M\]). |
| `conjugate_rhs` | If `True`, `rhs` is conjugated before solving. |
| `name` | A name to give this `Op` (optional). |
| `partial_pivoting` | whether to perform partial pivoting. `True` by default. Partial pivoting makes the procedure more stable, but slower. Partial pivoting is unnecessary in some cases, including diagonally dominant and symmetric positive definite matrices (see e.g. theorem 9.12 in \[1\]). |
| `perturb_singular` | whether to perturb singular matrices to return a finite result. `False` by default. If true, solutions to systems involving a singular matrix will be computed by perturbing near-zero pivots in the partially pivoted LU decomposition. Specifically, tiny pivots are perturbed by an amount of order `eps * max_{ij} \|U(i,j)\|` to avoid overflow. Here `U` is the upper triangular part of the LU decomposition, and `eps` is the machine precision. This is useful for solving numerically singular systems when computing eigenvectors by inverse iteration. If `partial_pivoting` is `False`, `perturb_singular` must be `False` as well. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape \[..., M\] or \[..., M, K\] containing the solutions. If the input matrix is singular, the result is undefined. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Is raised if any of the following conditions hold:<br><br>1.  An unsupported type is provided as input,<br>2.  the input tensors have incorrect shapes,<br>3.  `perturb_singular` is `True` but `partial_pivoting` is not. |
| `UnimplementedError` | Whenever `partial_pivoting` is true and the backend is XLA, or whenever `perturb_singular` is true and the backend is XLA or GPU. |

\[1\] Nicholas J. Higham (2002). Accuracy and Stability of Numerical Algorithms: Second Edition. SIAM. p. 175. ISBN 978-0-89871-802-7.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.