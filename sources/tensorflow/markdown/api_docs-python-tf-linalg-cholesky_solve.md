[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.cholesky\_solve Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L147-L193)

Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cholesky_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve)
, [`tf.compat.v1.linalg.cholesky_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve)

tf.linalg.cholesky_solve(
        chol, rhs, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow Probability Case Study: Covariance Estimation](https://www.tensorflow.org/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) |

Specifically, returns `X` from `A X = RHS`, where `A = L L^T`, `L` is the `chol` arg and `RHS` is the `rhs` arg.

# Solve 10 separate 2x2 linear systems:
    A = ... # shape 10 x 2 x 2
    RHS = ... # shape 10 x 2 x 1
    chol = tf.linalg.cholesky(A)  # shape 10 x 2 x 2
    X = tf.linalg.cholesky_solve(chol, RHS)  # shape 10 x 2 x 1
    # tf.matmul(A, X) ~ RHS
    X[3, :, 0]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 0]
    
    # Solve five linear systems (K = 5) for every member of the length 10 batch.
    A = ... # shape 10 x 2 x 2
    RHS = ... # shape 10 x 2 x 5
    ...
    X[3, :, 2]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 2]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `chol` | A `Tensor`. Must be `float32` or `float64`, shape is `[..., M, M]`. Cholesky factorization of `A`, e.g. `chol = tf.linalg.cholesky(A)`. For that reason, only the lower triangular parts (including the diagonal) of the last two dimensions of `chol` are used. The strictly upper part is assumed to be zero and not accessed. |
| `rhs` | A `Tensor`, same type as `chol`, shape is `[..., M, K]`. |
| `name` | A name to give this `Op`. Defaults to `cholesky_solve`. |

|     |
| --- |
| Returns<br>------- |     |
| Solution to `A x = rhs`, shape `[..., M, K]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.