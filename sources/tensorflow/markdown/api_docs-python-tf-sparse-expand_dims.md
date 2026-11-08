[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.expand\_dims Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L143-L246)

Returns a tensor with an length 1 axis inserted at index `axis`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.expand_dims`](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims)

tf.sparse.expand_dims(
        sp_input, axis=None, name=None
    )

Given a tensor `input`, this operation inserts a dimension of length 1 at the dimension index `axis` of `input`'s shape. The dimension index follows python indexing rules: It's zero-based, a negative index it is counted backward from the end.

This operation is useful to:

*   Add an outer "batch" dimension to a single element.
*   Align axes for broadcasting.
*   To add an inner vector length axis to a tensor of scalars.

#### For example:

If you have a sparse tensor with shape `[height, width, depth]`:

    sp = tf.sparse.SparseTensor(indices=[[3,4,1]], values=[7,],

You can add an outer `batch` axis by passing `axis=0`:

    tf.sparse.expand_dims(sp, axis=0).shape.as_list()

The new axis location matches Python `list.insert(axis, 1)`:

    tf.sparse.expand_dims(sp, axis=1).shape.as_list()

Following standard python indexing rules, a negative `axis` counts from the end so `axis=-1` adds an inner most dimension:

    tf.sparse.expand_dims(sp, axis=-1).shape.as_list()

    sp.shape.as_list()

This operation requires that `axis` is a valid index for `input.shape`, following python indexing rules:

-1-tf.rank(input) <= axis <= tf.rank(input)

This operation is related to:

*   [`tf.expand_dims`](https://www.tensorflow.org/api_docs/python/tf/expand_dims)
    , which provides this functionality for dense tensors.
*   [`tf.squeeze`](https://www.tensorflow.org/api_docs/python/tf/squeeze)
    , which removes dimensions of size 1, from dense tensors.
*   [`tf.sparse.reshape`](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape)
    , which provides more flexible reshaping capability.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | A `SparseTensor`. |
| `axis` | 0-D (scalar). Specifies the dimension index at which to expand the shape of `input`. Must be in the range `[-rank(sp_input) - 1, rank(sp_input)]`. Defaults to `-1`. |
| `name` | The name of the output `SparseTensor`. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` with the same data as `sp_input`, but its shape has an additional dimension of size 1 added. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.