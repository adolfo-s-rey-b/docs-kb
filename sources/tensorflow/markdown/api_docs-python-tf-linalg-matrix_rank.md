[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.matrix\_rank Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L768-L804)

Compute the matrix rank of one or more matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.matrix_rank`](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank)

tf.linalg.matrix_rank(
        a, tol=None, validate_args=False, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | (Batch of) `float`\-like matrix-shaped `Tensor`(s) which are to be pseudo-inverted. |
| `tol` | Threshold below which the singular value is counted as 'zero'. Default value: `None` (i.e., `eps * max(rows, cols) * max(singular_val)`). |
| `validate_args` | When `True`, additional assertions might be embedded in the graph. Default value: `False` (i.e., no graph assertions are added). |
| `name` | Python `str` prefixed to ops created by this function. Default value: 'matrix\_rank'. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `matrix_rank` | (Batch of) `int32` scalars representing the number of non-zero singular values. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.