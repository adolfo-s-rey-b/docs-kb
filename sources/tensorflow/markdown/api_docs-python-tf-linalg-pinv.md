[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Fpinv&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.pinv Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L807-L934)

Compute the Moore-Penrose pseudo-inverse of one or more matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.pinv`](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv)

tf.linalg.pinv(
        a, rcond=None, validate_args=False, name=None
    )

Calculate the [generalized inverse of a matrix](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse)
 using its singular-value decomposition (SVD) and including all large singular values.

The pseudo-inverse of a matrix `A`, is defined as: 'the matrix that 'solves' \[the least-squares problem\] `A @ x = b`,' i.e., if `x_hat` is a solution, then `A_pinv` is the matrix such that `x_hat = A_pinv @ b`. It can be shown that if `U @ Sigma @ V.T = A` is the singular value decomposition of `A`, then `A_pinv = V @ inv(Sigma) U^T`. \[(Strang, 1980)\]\[1\]

This function is analogous to [`numpy.linalg.pinv`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.pinv.html)
. It differs only in default value of `rcond`. In `numpy.linalg.pinv`, the default `rcond` is `1e-15`. Here the default is `10. * max(num_rows, num_cols) * np.finfo(dtype).eps`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | (Batch of) `float`\-like matrix-shaped `Tensor`(s) which are to be pseudo-inverted. |
| `rcond` | `Tensor` of small singular value cutoffs. Singular values smaller (in modulus) than `rcond` \* largest\_singular\_value (again, in modulus) are set to zero. Must broadcast against `tf.shape(a)[:-2]`. Default value: `10. * max(num_rows, num_cols) * np.finfo(a.dtype).eps`. |
| `validate_args` | When `True`, additional assertions might be embedded in the graph. Default value: `False` (i.e., no graph assertions are added). |
| `name` | Python `str` prefixed to ops created by this function. Default value: 'pinv'. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `a_pinv` | (Batch of) pseudo-inverse of input `a`. Has same shape as `a` except rightmost two dimensions are transposed. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if input `a` does not have `float`\-like `dtype`. |
| `ValueError` | if input `a` has fewer than 2 dimensions. |

#### Examples

import tensorflow as tf
    import tensorflow_probability as tfp
    
    a = tf.constant([[1.,  0.4,  0.5],\
                     [0.4, 0.2,  0.25],\
                     [0.5, 0.25, 0.35]])
    tf.matmul(tf.linalg.pinv(a), a)
    # ==> array([[1., 0., 0.],\
                 [0., 1., 0.],\
                 [0., 0., 1.]], dtype=float32)
    
    a = tf.constant([[1.,  0.4,  0.5,  1.],\
                     [0.4, 0.2,  0.25, 2.],\
                     [0.5, 0.25, 0.35, 3.]])
    tf.matmul(tf.linalg.pinv(a), a)
    # ==> array([[ 0.76,  0.37,  0.21, -0.02],\
                 [ 0.37,  0.43, -0.33,  0.02],\
                 [ 0.21, -0.33,  0.81,  0.01],\
                 [-0.02,  0.02,  0.01,  1.  ]], dtype=float32)

#### References

\[1\]: G. Strang. 'Linear Algebra and Its Applications, 2nd Ed.' Academic Press, Inc., 1980, pp. 139-142.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.