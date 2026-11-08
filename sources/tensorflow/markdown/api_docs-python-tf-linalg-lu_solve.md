[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.lu\_solve Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L937-L1032)

Solves systems of linear eqns `A X = RHS`, given LU factorizations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.lu_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve)

tf.linalg.lu_solve(
        lower_upper, perm, rhs, validate_args=False, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `lower_upper` | `lu` as returned by [`tf.linalg.lu`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)<br>, i.e., if `matmul(P, matmul(L, U)) = X` then `lower_upper = L + U - eye`. |
| `perm` | `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) = X` then `perm = argmax(P)`. |
| `rhs` | Matrix-shaped float `Tensor` representing targets for which to solve; `A X = RHS`. To handle vector cases, use: `lu_solve(..., rhs[..., tf.newaxis])[..., 0]`. |
| `validate_args` | Python `bool` indicating whether arguments should be checked for correctness. Note: this function does not verify the implied matrix is actually invertible, even when `validate_args=True`. Default value: `False` (i.e., don't validate arguments). |
| `name` | Python `str` name given to ops managed by this object. Default value: `None` (i.e., 'lu\_solve'). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `x` | The `X` in `A @ X = RHS`. |

#### Examples

import numpy as np
    import tensorflow as tf
    import tensorflow_probability as tfp
    
    x = [[[1., 2],\
          [3, 4]],\
         [[7, 8],\
          [3, 4]]]
    inv_x = tf.linalg.lu_solve(*tf.linalg.lu(x), rhs=tf.eye(2))
    tf.assert_near(tf.matrix_inverse(x), inv_x)
    # ==> True

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.