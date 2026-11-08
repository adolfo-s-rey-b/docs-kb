[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.lstsq Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/linalg.py#L650-L691)

Return the least-squares solution to a linear matrix equation.

#### View aliases

**Main aliases**

[`tf.keras.ops.linalg.lstsq`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/lstsq)

tf.keras.ops.lstsq(
        a, b, rcond=None
    )

Computes the vector x that approximately solves the equation `a @ x = b`. The equation may be under-, well-, or over-determined (i.e., the number of linearly independent rows of a can be less than, equal to, or greater than its number of linearly independent columns). If a is square and of full rank, then `x` (but for round-off error) is the exact solution of the equation. Else, `x` minimizes the L2 norm of `b - a * x`.

If there are multiple minimizing solutions, the one with the smallest L2 norm is returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | "Coefficient" matrix of shape `(M, N)`. |
| `b` | Ordinate or "dependent variable" values, of shape `(M,)` or `(M, K)`. If `b` is two-dimensional, the least-squares solution is calculated for each of the K columns of `b`. |
| `rcond` | Cut-off ratio for small singular values of `a`. For the purposes of rank determination, singular values are treated as zero if they are smaller than rcond times the largest singular value of `a`. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor with shape `(N,)` or `(N, K)` containing the least-squares solutions. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.