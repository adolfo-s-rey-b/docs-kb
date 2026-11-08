[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.matrix\_rank Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/linalg.py#L707-L732)

Return the matrix rank of one or more matrices using SVD.

#### View aliases

**Main aliases**

[`tf.keras.ops.linalg.matrix_rank`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/matrix_rank)

tf.keras.ops.matrix_rank(
        x, tol=None
    )

The rank is the number of singular values that exceed `tol`. If `tol` is `None`, each backend uses its own default threshold derived from the largest singular value and the matrix dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor of shape `(..., M, N)`. |
| `tol` | Absolute threshold below which singular values are treated as zero. If `None` (default), the backend's default is used. |

|     |
| --- |
| Returns<br>------- |     |
| An integer tensor of shape `(...,)` with the rank of each matrix in the batch. |     |

#### Example:

    a = keras.ops.convert_to_tensor([[1., 2.], [2., 4.]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.