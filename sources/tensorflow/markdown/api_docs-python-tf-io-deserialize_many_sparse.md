[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fio%2Fdeserialize_many_sparse&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.deserialize\_many\_sparse Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2356-L2427)

Deserialize and concatenate `SparseTensors` from a serialized minibatch.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.deserialize_many_sparse`](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse)
, [`tf.compat.v1.io.deserialize_many_sparse`](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse)

tf.io.deserialize_many_sparse(
        serialized_sparse, dtype, rank=None, name=None
    )

The input `serialized_sparse` must be a string matrix of shape `[N x 3]` where `N` is the minibatch size and the rows correspond to packed outputs of `serialize_sparse`. The ranks of the original `SparseTensor` objects must all match. When the final `SparseTensor` is created, it has rank one higher than the ranks of the incoming `SparseTensor` objects (they have been concatenated along a new row dimension).

The output `SparseTensor` object's shape values for all dimensions but the first are the max across the input `SparseTensor` objects' shape values for the corresponding dimensions. Its first shape value is `N`, the minibatch size.

The input `SparseTensor` objects' indices are assumed ordered in standard lexicographic order. If this is not the case, after this step run [`sparse.reorder`](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder)
 to restore index ordering.

For example, if the serialized input is a `[2, 3]` matrix representing two original `SparseTensor` objects:

index = [ 0]
            [10]
            [20]
    values = [1, 2, 3]
    shape = [50]

and

index = [ 2]
            [10]
    values = [4, 5]
    shape = [30]

then the final deserialized `SparseTensor` will be:

index = [0  0]
            [0 10]
            [0 20]
            [1  2]
            [1 10]
    values = [1, 2, 3, 4, 5]
    shape = [2 50]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized_sparse` | 2-D `Tensor` of type `string` of shape `[N, 3]`. The serialized and packed `SparseTensor` objects. |
| `dtype` | The `dtype` of the serialized `SparseTensor` objects. |
| `rank` | (optional) Python int, the rank of the `SparseTensor` objects. |
| `name` | A name prefix for the returned tensors (optional) |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` representing the deserialized `SparseTensor`s, concatenated along the `SparseTensor`s' first dimension.<br><br>All of the serialized `SparseTensor`s must have had the same rank and type. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.