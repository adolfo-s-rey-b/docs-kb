[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/eye#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/eye)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/eye?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/eye#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/eye#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.eye Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/eye#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/eye#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L249-L280)

Creates a two-dimensional sparse tensor with ones along the diagonal.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.eye`](https://www.tensorflow.org/api_docs/python/tf/sparse/eye)

tf.sparse.eye(
        num_rows,
        num_columns=None,
        dtype=tf.dtypes.float32,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_rows` | Non-negative integer or `int32` scalar `tensor` giving the number of rows in the resulting matrix. |
| `num_columns` | Optional non-negative integer or `int32` scalar `tensor` giving the number of columns in the resulting matrix. Defaults to `num_rows`. |
| `dtype` | The type of element in the resulting `Tensor`. |
| `name` | A name for this `Op`. Defaults to "eye". |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` of shape \[num\_rows, num\_columns\] with ones along the diagonal. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.