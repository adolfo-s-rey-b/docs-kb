[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/minimum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.minimum Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2780-L2821)

Returns the element-wise min of two SparseTensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.minimum`](https://www.tensorflow.org/api_docs/python/tf/sparse/minimum)
, [`tf.compat.v1.sparse_minimum`](https://www.tensorflow.org/api_docs/python/tf/sparse/minimum)

tf.sparse.minimum(
        sp_a, sp_b, name=None
    )

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

|     |
| --- |
| Example<br>------- |     |
| >>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])<br>    >>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])<br>    >>> res = tf.sparse.minimum(sp_zero, sp_one)<br>    >>> res.indices<br>    <tf.Tensor: shape=(2, 1), dtype=int64, numpy=<br>    array([[0],<br>           [1]])><br>    >>> res.values<br>    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 0], dtype=int32)><br>    >>> res.dense_shape<br>    <tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])> |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_a` | a `SparseTensor` operand whose dtype is real, and indices lexicographically ordered. |
| `sp_b` | the other `SparseTensor` operand with the same requirements (and the same shape). |
| `name` | optional name of the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | the output SparseTensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.