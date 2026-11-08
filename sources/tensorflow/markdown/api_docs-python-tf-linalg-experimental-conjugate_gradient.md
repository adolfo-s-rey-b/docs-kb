[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.experimental.conjugate\_gradient Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/sparse/conjugate_gradient.py#L30-L138)

Conjugate gradient solver.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.experimental.conjugate_gradient`](https://www.tensorflow.org/api_docs/python/tf/linalg/experimental/conjugate_gradient)

tf.linalg.experimental.conjugate_gradient(
        operator,
        rhs,
        preconditioner=None,
        x=None,
        tol=1e-05,
        max_iter=20,
        name='conjugate_gradient'
    )

Solves a linear system of equations `A*x = rhs` for self-adjoint, positive definite matrix `A` and right-hand side vector `rhs`, using an iterative, matrix-free algorithm where the action of the matrix A is represented by `operator`. The iteration terminates when either the number of iterations exceeds `max_iter` or when the residual norm has been reduced to `tol` times its initial value, i.e. ||rhs−Axk||<=tol||rhs||.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `operator` | A `LinearOperator` that is self-adjoint and positive definite. |
| `rhs` | A possibly batched vector of shape `[..., N]` containing the right-hand size vector. |
| `preconditioner` | A `LinearOperator` that approximates the inverse of `A`. An efficient preconditioner could dramatically improve the rate of convergence. If `preconditioner` represents matrix `M`(`M` approximates `A^{-1}`), the algorithm uses `preconditioner.apply(x)` to estimate `A^{-1}x`. For this to be useful, the cost of applying `M` should be much lower than computing `A^{-1}` directly. |
| `x` | A possibly batched vector of shape `[..., N]` containing the initial guess for the solution. |
| `tol` | A float scalar convergence tolerance. |
| `max_iter` | An integer giving the maximum number of iterations. |
| `name` | A name scope for the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | A namedtuple representing the final state with fields:<br><br>*   i: A scalar `int32` `Tensor`. Number of iterations executed.<br>*   x: A rank-1 `Tensor` of shape `[..., N]` containing the computed solution.<br>*   r: A rank-1 `Tensor` of shape `[.., M]` containing the residual vector.<br>*   p: A rank-1 `Tensor` of shape `[..., N]`. `A`\-conjugate basis vector.<br>*   gamma: r˙M˙r, equivalent to \|r\|22 when `preconditioner=None`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.