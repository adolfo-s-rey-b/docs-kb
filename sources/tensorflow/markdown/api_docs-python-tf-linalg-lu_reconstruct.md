[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Flu_reconstruct&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.lu\_reconstruct Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L1100-L1171)

The reconstruct one or more matrices from their LU decomposition(s).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.lu_reconstruct`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct)

tf.linalg.lu_reconstruct(
        lower_upper, perm, validate_args=False, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `lower_upper` | `lu` as returned by [`tf.linalg.lu`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)<br>, i.e., if `matmul(P, matmul(L, U)) = X` then `lower_upper = L + U - eye`. |
| `perm` | `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) = X` then `perm = argmax(P)`. |
| `validate_args` | Python `bool` indicating whether arguments should be checked for correctness. Default value: `False` (i.e., don't validate arguments). |
| `name` | Python `str` name given to ops managed by this object. Default value: `None` (i.e., 'lu\_reconstruct'). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `x` | The original input to [`tf.linalg.lu`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)<br>, i.e., `x` as in, `lu_reconstruct(*tf.linalg.lu(x))`. |

#### Examples

import numpy as np
    import tensorflow as tf
    import tensorflow_probability as tfp
    
    x = [[[3., 4], [1, 2]],\
         [[7., 8], [3, 4]]]
    x_reconstructed = tf.linalg.lu_reconstruct(*tf.linalg.lu(x))
    tf.assert_near(x, x_reconstructed)
    # ==> True

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.