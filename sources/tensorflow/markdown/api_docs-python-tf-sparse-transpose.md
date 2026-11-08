[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.transpose Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2824-L2929)

Transposes a `SparseTensor`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.transpose`](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose)
, [`tf.compat.v1.sparse_transpose`](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose)

tf.sparse.transpose(
        sp_input, perm=None, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) |

Permutes the dimensions according to the value of `perm`. This is the sparse version of [`tf.transpose`](https://www.tensorflow.org/api_docs/python/tf/transpose)
.

The returned tensor's dimension `i` will correspond to the input dimension `perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank of the input tensor. Hence, by default, this operation performs a regular matrix transpose on 2-D input Tensors.

#### For example:

    x = tf.SparseTensor(indices=[[0, 1], [0, 3], [2, 3], [3, 1]],

    x_transpose = tf.sparse.transpose(x)

Equivalently, you could call `tf.sparse.transpose(x, perm=[1, 0])`. The `perm` argument is more useful for n-dimensional tensors where n > 2.

    x = tf.SparseTensor(indices=[[0, 0, 1], [0, 0, 3], [1, 2, 3], [1, 3, 1]],

As above, simply calling [`tf.sparse.transpose`](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose)
 will default to `perm=[2,1,0]`.

To take the transpose of a batch of sparse matrices, where 0 is the batch dimension, you would set `perm=[0,2,1]`.

    x_transpose = tf.sparse.transpose(x, perm=[0, 2, 1])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `perm` | A permutation vector of the dimensions of `sp_input`. |
| `name` | A name prefix for the returned tensors (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A transposed `SparseTensor`. |     |

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