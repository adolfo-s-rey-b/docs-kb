[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Flstsq&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.lstsq Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L244-L379)

Solves one or more linear least-squares problems.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.lstsq`](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq)
, [`tf.compat.v1.matrix_solve_ls`](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq)

tf.linalg.lstsq(
        matrix, rhs, l2_regularizer=0.0, fast=True, name=None
    )

`matrix` is a tensor of shape `[..., M, N]` whose inner-most 2 dimensions form `M`\-by-`N` matrices. Rhs is a tensor of shape `[..., M, K]` whose inner-most 2 dimensions form `M`\-by-`K` matrices. The computed output is a `Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form `M`\-by-`K` matrices that solve the equations `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least squares sense.

Below we will use the following notation for each pair of matrix and right-hand sides in the batch:

`matrix`\=A∈ℜm×n, `rhs`\=B∈ℜm×k, `output`\=X∈ℜn×k, `l2_regularizer`\=λ.

If `fast` is `True`, then the solution is computed by solving the normal equations using Cholesky decomposition. Specifically, if m≥n then X\=(ATA+λI)−1ATB, which solves the least-squares problem X\=argminZ∈ℜn×k||AZ−B||2F+λ||Z||2F. If m<n then `output` is computed as X\=AT(AAT+λI)−1B, which (for λ\=0) is the minimum-norm solution to the under-determined linear system, i.e. X\=argminZ∈ℜn×k||Z||2F, subject to AZ\=B. Notice that the fast path is only numerically stable when A is numerically full rank and has a condition number cond(A)<1√ϵmach orλ is sufficiently large.

If `fast` is `False` an algorithm based on the numerically robust complete orthogonal decomposition is used. This computes the minimum-norm least-squares solution, even when A is rank deficient. This path is typically 6-7 times slower than the fast path. If `fast` is `False` then `l2_regularizer` is ignored.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `matrix` | `Tensor` of shape `[..., M, N]`. |
| `rhs` | `Tensor` of shape `[..., M, K]`. |
| `l2_regularizer` | 0-D `double` `Tensor`. Ignored if `fast=False`. |
| `fast` | bool. Defaults to `True`. |
| `name` | string, optional name of the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | `Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form `M`\-by-`K` matrices that solve the equations `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least squares sense. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `NotImplementedError` | linalg.lstsq is currently disabled for complex128 and l2\_regularizer != 0 due to poor accuracy. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.