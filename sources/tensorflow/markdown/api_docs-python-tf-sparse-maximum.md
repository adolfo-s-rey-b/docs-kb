[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.maximum Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2734-L2777)

Returns the element-wise max of two SparseTensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.maximum`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
, [`tf.compat.v1.sparse_maximum`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)

tf.sparse.maximum(
        sp_a, sp_b, name=None
    )

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

|     |
| --- |
| Example<br>------- |     |
| >>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])<br>    >>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])<br>    >>> res = tf.sparse.maximum(sp_zero, sp_one)<br>    >>> res.indices<br>    <tf.Tensor: shape=(2, 1), dtype=int64, numpy=<br>    array([[0],<br>           [1]])><br>    >>> res.values<br>    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 1], dtype=int32)><br>    >>> res.dense_shape<br>    <tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])> |     |

The reduction version of this elementwise operation is [`tf.sparse.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max)

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