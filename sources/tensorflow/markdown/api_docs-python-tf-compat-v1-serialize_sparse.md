[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fserialize_sparse&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.serialize\_sparse Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2176-L2194)

Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.serialize_sparse`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse)

tf.compat.v1.serialize_sparse(
        sp_input,
        name=None,
        out_type=tf.dtypes.string
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `name` | A name prefix for the returned tensors (optional). |
| `out_type` | The `dtype` to use for serialization. |

|     |
| --- |
| Returns<br>------- |     |
| A 3-vector (1-D `Tensor`), with each column representing the serialized `SparseTensor`'s indices, values, and shape (respectively). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.