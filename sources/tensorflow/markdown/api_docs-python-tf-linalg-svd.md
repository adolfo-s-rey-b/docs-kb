[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/svd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/svd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Fsvd&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.svd Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/linalg/svd#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L489-L557)

Computes the singular value decompositions of one or more matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.svd`](https://www.tensorflow.org/api_docs/python/tf/linalg/svd)
, [`tf.compat.v1.svd`](https://www.tensorflow.org/api_docs/python/tf/linalg/svd)

tf.linalg.svd(
        tensor, full_matrices=False, compute_uv=True, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core) |

Computes the SVD of each inner matrix in `tensor` such that `tensor[..., :, :] = u[..., :, :] * diag(s[..., :, :]) * transpose(conj(v[..., :, :]))`

# a is a tensor.
    # s is a tensor of singular values.
    # u is a tensor of left singular vectors.
    # v is a tensor of right singular vectors.
    s, u, v = svd(a)
    s = svd(a, compute_uv=False)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | `Tensor` of shape `[..., M, N]`. Let `P` be the minimum of `M` and `N`. |
| `full_matrices` | If true, compute full-sized `u` and `v`. If false (the default), compute only the leading `P` singular vectors. Ignored if `compute_uv` is `False`. |
| `compute_uv` | If `True` then left and right singular vectors will be computed and returned in `u` and `v`, respectively. Otherwise, only the singular values will be computed, which can be significantly faster. |
| `name` | string, optional name of the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `s` | Singular values. Shape is `[..., P]`. The values are sorted in reverse order of magnitude, so s\[..., 0\] is the largest value, s\[..., 1\] is the second largest, etc. |
| `u` | Left singular vectors. If `full_matrices` is `False` (default) then shape is `[..., M, P]`; if `full_matrices` is `True` then shape is `[..., M, M]`. Not returned if `compute_uv` is `False`. |
| `v` | Right singular vectors. If `full_matrices` is `False` (default) then shape is `[..., N, P]`. If `full_matrices` is `True` then shape is `[..., N, N]`. Not returned if `compute_uv` is `False`. |

numpy compatibility
-------------------

Mostly equivalent to numpy.linalg.svd, except that

*   The order of output arguments here is `s`, `u`, `v` when `compute_uv` is `True`, as opposed to `u`, `s`, `v` for numpy.linalg.svd.
*   full\_matrices is `False` by default as opposed to `True` for numpy.linalg.svd.
*   tf.linalg.svd uses the standard definition of the SVD A\=UΣVH, such that the left singular vectors of `a` are the columns of `u`, while the right singular vectors of `a` are the columns of `v`. On the other hand, numpy.linalg.svd returns the adjoint VH as the third output argument.

import tensorflow as tf
    import numpy as np
    s, u, v = tf.linalg.svd(a)
    tf_a_approx = tf.matmul(u, tf.matmul(tf.linalg.diag(s), v, adjoint_b=True))
    u, s, v_adj = np.linalg.svd(a, full_matrices=False)
    np_a_approx = np.dot(u, np.dot(np.diag(s), v_adj))
    # tf_a_approx and np_a_approx should be numerically close.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.