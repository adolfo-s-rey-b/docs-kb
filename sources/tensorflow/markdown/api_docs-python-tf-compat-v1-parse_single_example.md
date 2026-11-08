[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.parse\_single\_example Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L370-L402)

Parses a single `Example` proto.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.parse_single_example`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example)

tf.compat.v1.parse_single_example(
        serialized, features, name=None, example_names=None
    )

Similar to `parse_example`, except:

For dense tensors, the returned `Tensor` is identical to the output of `parse_example`, except there is no batch dimension, the output shape is the same as the shape given in `dense_shape`.

For `SparseTensor`s, the first (batch) column of the indices matrix is removed (the indices matrix is a column vector), the values vector is unchanged, and the first (`batch_size`) entry of the shape vector is removed (it is now a single element vector).

One might see performance advantages by batching `Example` protos with `parse_example` instead of using this function directly.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized` | A scalar string Tensor, a single serialized Example. |
| `features` | A mapping of feature keys to `FixedLenFeature` or `VarLenFeature` values. |
| `name` | A name for this operation (optional). |
| `example_names` | (Optional) A scalar string Tensor, the associated name. |

|     |
| --- |
| Returns<br>------- |     |
| A `dict` mapping feature keys to `Tensor` and `SparseTensor` values. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if any feature is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.