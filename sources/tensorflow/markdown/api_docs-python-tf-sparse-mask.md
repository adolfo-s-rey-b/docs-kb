[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/mask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/mask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/mask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/mask#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.mask Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/mask#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1599-L1640)

Masks elements of `IndexedSlices`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.mask`](https://www.tensorflow.org/api_docs/python/tf/sparse/mask)
, [`tf.compat.v1.sparse_mask`](https://www.tensorflow.org/api_docs/python/tf/sparse/mask)

tf.sparse.mask(
        a, mask_indices, name=None
    )

Given an `IndexedSlices` instance `a`, returns another `IndexedSlices` that contains a subset of the slices of `a`. Only the slices at indices not specified in `mask_indices` are returned.

This is useful when you need to extract a subset of slices in an `IndexedSlices` object.

#### For example:

# `a` contains slices at indices [12, 26, 37, 45] from a large tensor
    # with shape [1000, 10]
    a.indices  # [12, 26, 37, 45]
    tf.shape(a.values)  # [4, 10]
    
    # `b` will be the subset of `a` slices at its second and third indices, so
    # we want to mask its first and last indices (which are at absolute
    # indices 12, 45)
    b = tf.sparse.mask(a, [12, 45])
    
    b.indices  # [26, 37]
    tf.shape(b.values)  # [2, 10]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | An `IndexedSlices` instance. |
| `mask_indices` | Indices of elements to mask. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The masked `IndexedSlices` instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.