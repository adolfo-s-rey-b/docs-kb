[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.softmax Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2671-L2731)

Applies softmax to a batched N-D `SparseTensor`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.softmax`](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax)
, [`tf.compat.v1.sparse_softmax`](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax)

tf.sparse.softmax(
        sp_input, name=None
    )

The inputs represent an N-D SparseTensor with logical shape `[..., B, C]` (where `N >= 2`), and with indices sorted in the canonical lexicographic order.

This op is equivalent to applying the normal [`tf.nn.softmax()`](https://www.tensorflow.org/api_docs/python/tf/nn/softmax)
 to each innermost logical submatrix with shape `[B, C]`, but with the catch that _the implicitly zero elements do not participate_. Specifically, the algorithm is equivalent to:

(1) Applies [`tf.nn.softmax()`](https://www.tensorflow.org/api_docs/python/tf/nn/softmax)
 to a densified view of each innermost submatrix with shape `[B, C]`, along the size-C dimension; (2) Masks out the original implicitly-zero locations; (3) Renormalizes the remaining elements.

Hence, the `SparseTensor` result has exactly the same non-zero indices and shape.

Example using a 3-D SparseTensor:

  `st = tf.sparse.from_dense(`
  `  [[[0., np.e],`\
  `    [1., 0.]],`\
  \
  `   [[np.e, 0.],`\
  `    [np.e, np.e]]])`
  `res = tf.sparse.softmax(st)`
  `res.indices`
  `  <tf.Tensor: shape=(5, 3), dtype=int64, numpy=`
  `  array([[0, 0, 1],`\
  `         [0, 1, 0],`\
  `         [1, 0, 0],`\
  `         [1, 1, 0],`\
  `         [1, 1, 1]])>`
  `res.values`
  `  <tf.Tensor: ... numpy=array([1. , 1. , 1. , 0.5, 0.5], dtype=float32)>`
  `res.dense_shape`
  `  <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 2])>`
  `tf.sparse.to_dense(res)`
  `  <tf.Tensor: shape=(2, 2, 2), dtype=float32, numpy=`
  `  array([[[0. , 1. ],`\
  `          [1. , 0. ]],`\
  `         [[1. , 0. ],`\
  `          [0.5, 0.5]]], dtype=float32)>`
    
  

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | N-D `SparseTensor`, where `N >= 2`. |
| `name` | optional name of the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | N-D `SparseTensor` representing the results. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.