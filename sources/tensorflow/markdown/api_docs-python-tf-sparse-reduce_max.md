[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.reduce\_max Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1246-L1338)

Computes [`tf.sparse.maximum`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
 of elements across dimensions of a SparseTensor.

tf.sparse.reduce_max(
        sp_input, axis=None, keepdims=None, output_is_sparse=False, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) |

This is the reduction operation for the elementwise [`tf.sparse.maximum`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
 op.

This Op takes a SparseTensor and is the sparse counterpart to [`tf.reduce_max()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)
. In particular, this Op also returns a dense `Tensor` if `output_is_sparse` is `False`, or a `SparseTensor` if `output_is_sparse` is `True`.

Reduces `sp_input` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in `axis`. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a tensor with a single element is returned. Additionally, the axes can be negative, similar to the indexing rules in Python.

The values not defined in `sp_input` don't participate in the reduce max, as opposed to be implicitly assumed 0 -- hence it can return negative values for sparse `axis`. But, in case there are no values in `axis`, it will reduce to 0. See second example below.

|     |
| --- |
| For example<br>----------- |     |
| 'x' represents \[\[1, ?, 2\]<br>============================<br><br>\[?, 3, ?\]\]<br>=============<br><br>where ? is implicitly-zero.<br>===========================<br><br>    x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 2, 3], [2, 3])<br><br>'y' represents \[\[-7, ?\]<br>==========================<br><br>\[ 4, 3\]<br>=========<br><br>\[ ?, ?\]<br>=========<br><br>    y = tf.sparse.SparseTensor([[0, 0,], [1, 0], [1, 1]], [-7, 4, 3], |     |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `sp_input` | The SparseTensor to reduce. Should have numeric type. |\
| `axis` | The dimensions to reduce; list or scalar. If `None` (the default), reduces all dimensions. |\
| `keepdims` | If true, retain reduced dimensions with length 1. |\
| `output_is_sparse` | If true, returns a `SparseTensor` instead of a dense `Tensor` (the default). |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced Tensor or the reduced SparseTensor if `output_is_sparse` is True. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.