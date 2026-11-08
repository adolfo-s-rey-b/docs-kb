[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.reorder Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L821-L873)

Reorders a `SparseTensor` into the canonical, row-major ordering.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.reorder`](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder)
, [`tf.compat.v1.sparse_reorder`](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder)

tf.sparse.reorder(
        sp_input, name=None
    )

Note that by convention, all sparse ops preserve the canonical ordering along increasing dimension number. The only time ordering can be violated is during manual manipulation of the indices and values to add entries.

Reordering does not affect the shape of the `SparseTensor`.

For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

[0, 3]: b
    [0, 1]: a
    [3, 1]: d
    [2, 0]: c

then the output will be a `SparseTensor` of shape `[4, 5]` and `indices` / `values`:

[0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `name` | A name prefix for the returned tensors (optional) |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` with the same shape and non-empty values, but in canonical ordering. |     |

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