[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.embedding\_lookup\_sparse Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/embedding_ops.py#L579-L735)

Looks up embeddings for the given ids and weights from a list of tensors.

tf.nn.embedding_lookup_sparse(
        params,
        sp_ids,
        sp_weights,
        combiner=None,
        max_norm=None,
        name=None,
        allow_fast_lookup=False
    )

`params` is a dense tensor or a list of dense tensors, and `sp_ids` is a 2D [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
 or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 indicating the indices of `params` to gather.

This op is best described with an example. Suppose `params` is an embedding table of size `(4, 2)` and `sp_ids` has 3 rows. Since `sp_ids` is sparse or ragged, not every row has the same number of elements. The output has shape (3, 2). Each row of `sp_ids` is a list of indices, where each index selects a row of `params`. For a given row of `sp_ids`, the rows of `params` are gathered based on the indices in `sp_ids`, then combined by taking their sum or mean.

    params = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=tf.float32)

In this example, `sp_ids` has 3 rows, so the output has 3 rows. Row 0 of `sp_ids` has values 0 and 1, so it selects rows 0 and 1 from `params`, which are `[1, 2]` and `[3, 4]`. The rows are summed since `combiner='sum'`, resulting in the output row of `[4, 6]`.

Since row 1 and 2 of `sp_ids` only have one value each, they simply select the corresponding row from `params` as the output row. Row 1 has value `3` so it selects the `params` elements `[7, 8]` and row 2 has the value 2 so it selects the `params` elements `[5, 6]`.

If `sparse_weights` is specified, it must have the same shape as `sp_ids`. `sparse_weights` is used to assign a weight to each slice of `params`. For example:

    params = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=tf.float32)

In general, `params` can have shape `(p0, ..., pn)` and `sp_ids` can have `M` rows, where each row can have any number of elements. The output has shape `(M, p1, ..., pn)`. Each slice of the output `output[i, ...]` is obtained as follows: The `combiner` argument is used to combine the values `params[sp_ids[i, j], ...] * sparse_weights[i, j]` for each `j` in `range(0, len(sp_ids[i]))`, e.g. by taking the sum or mean of the values.

This op assumes that there is at least one id for each row in the dense tensor represented by sp\_ids (i.e. there are no rows with empty features), and that all the indices of sp\_ids are in canonical row-major order.

`sp_ids` and `sp_weights` (if not None) are `SparseTensor`s or `RaggedTensor`s with rank of 2. For `SpareTensor`s with left-aligned non-zero entries which can be described as `RaggedTensor`s, use of `RaggedTensor`s can yield higher performance.

This op assumes that all id values lie in the range \[0, p0), where p0 is `params.shape[0]`. If you want a version of this op that prunes id values less than 0, see [`tf.nn.safe_embedding_lookup_sparse`](https://www.tensorflow.org/api_docs/python/tf/nn/safe_embedding_lookup_sparse)\
\
If `len(params) > 1`, each element of `sp_ids` is partitioned between the elements of `params` according to the "div" partition strategy, which means we assign ids to partitions in a contiguous manner. For instance, 13 ids are split across 5 partitions as: `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.\
\
If the id space does not evenly divide the number of partitions, each of the first `(max_id + 1) % len(params)` partitions will be assigned one more id.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `params` | A single tensor representing the complete embedding tensor, or a list of tensors all of same shape except for the first dimension, representing sharded embedding tensors following "div" partition strategy. |\
| `sp_ids` | N x M `SparseTensor` of int64 ids where N is typically batch size and M is arbitrary or a `RaggedTensor` with rank 2. |\
| `sparse_weights` | `SparseTensor` or `RaggedTensor` of same type and shape as `sparse_ids`, containing float / double weights corresponding to `sparse_ids`, or `None` if all weights are assumed to be 1.0. |\
| `combiner` | A string specifying the reduction op. Currently "mean", "sqrtn" and "sum" are supported. "sum" computes the weighted sum of the embedding results for each row. "mean" is the weighted sum divided by the total weight. "sqrtn" is the weighted sum divided by the square root of the sum of the squares of the weights. Defaults to `mean`. |\
| `max_norm` | If not `None`, each embedding is clipped if its l2-norm is larger than this value, before combining. |\
| `name` | Optional name for the op. |\
| `allow_fast_lookup` | An optional boolean specifying whether to allow simplified embedding lookups when `params` is a single tensor and `max_norm` is `None`. Setting this flag to `True` during training can cause the use of dense gradients with increased memory footprint. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A dense tensor representing the combined embeddings for the sparse ids. For each row in the dense tensor represented by `sp_ids`, the op looks up the embeddings for all ids in that row, multiplies them by the corresponding weight, and combines these embeddings as specified.<br><br>In other words, if<br><br>`shape(combined params) = [p0, p1, ..., pm]`<br><br>and<br><br>`shape(sp_ids) = shape(sp_weights) = [d0, d1]`<br><br>then<br><br>`shape(output) = [d0, p1, ..., pm]`.<br><br>For instance, if params is a 10x20 matrix, and sp\_ids / sp\_weights are<br><br>  [0, 0]: id 1, weight 2.0<br>      [0, 1]: id 3, weight 0.5<br>      [1, 0]: id 0, weight 1.0<br>      [2, 3]: id 1, weight 3.0<br><br>with `combiner`\="mean", then the output will be a 3x20 matrix where<br><br>  output[0, :] = (params[1, :] * 2.0 + params[3, :] * 0.5) / (2.0 + 0.5)<br>      output[1, :] = (params[0, :] * 1.0) / 1.0<br>      output[2, :] = (params[1, :] * 3.0) / 3.0 |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If `sp_ids` is not a `SparseTensor`, or if `sp_weights` is neither `None` nor `SparseTensor`. |\
| `ValueError` | If `combiner` is not one of {"mean", "sqrtn", "sum"}. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-05 UTC.