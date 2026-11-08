[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_sparse_batch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.dense\_to\_sparse\_batch Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/batching.py#L94-L142)

A transformation that batches ragged elements into [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
s. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.dense_to_sparse_batch`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_sparse_batch)

tf.data.experimental.dense_to_sparse_batch(
        batch_size, row_shape
    )

Like [`Dataset.padded_batch()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)
, this transformation combines multiple consecutive elements of the dataset, which might have different shapes, into a single element. The resulting element has three components (`indices`, `values`, and `dense_shape`), which comprise a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
 that represents the same data. The `row_shape` represents the dense shape of each row in the resulting [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
, to which the effective batch size is prepended. For example:

# NOTE: The following examples use `{ ... }` to represent the
    # contents of a dataset.
    a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }
    
    a.apply(tf.data.experimental.dense_to_sparse_batch(
        batch_size=2, row_shape=[6])) ==
    {
        ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
         ['a', 'b', 'c', 'a', 'b'],                 # values
         [2, 6]),                                   # dense_shape
        ([[0, 0], [0, 1], [0, 2], [0, 3]],
         ['a', 'b', 'c', 'd'],
         [1, 6])
    }

|     |     |
| --- | --- |
| Args<br>---- |     |
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |
| `row_shape` | A [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> vector tensor-like object representing the equivalent dense shape of a row in the resulting [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>. Each element of this dataset must have the same rank as `row_shape`, and must have size less than or equal to `row_shape` in each dimension. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.