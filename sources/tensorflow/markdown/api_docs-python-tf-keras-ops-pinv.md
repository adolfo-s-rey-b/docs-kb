[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.pinv Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/linalg.py#L750-L778)

Compute the (Moore-Penrose) pseudoinverse of a matrix.

#### View aliases

**Main aliases**

[`tf.keras.ops.linalg.pinv`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pinv)

tf.keras.ops.pinv(
        x, rcond=None
    )

The pseudoinverse is computed via the singular value decomposition (SVD). Singular values smaller than `rcond` times the largest singular value (per matrix, in the batched case) are treated as zero.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor of shape `(..., M, N)`. |
| `rcond` | Cutoff ratio for small singular values. Singular values less than or equal to `rcond * largest_singular_value` are set to zero. If `None` (default), the backend's own default is used. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of shape `(..., N, M)` containing the pseudoinverse of each matrix in `x`. |     |

#### Example:

    a = keras.ops.convert_to_tensor([[1., 2.], [3., 4.], [5., 6.]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.