[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.embedding\_lookup\_sparse Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/embedding_lookup_sparse#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/embedding_ops.py#L441-L576)

Looks up embeddings for the given ids and weights from a list of tensors.

tf.compat.v1.nn.embedding_lookup_sparse(
        params,
        sp_ids,
        sp_weights,
        partition_strategy='mod',
        name=None,
        combiner=None,
        max_norm=None,
        allow_fast_lookup=False
    )

This op assumes that there is at least one id for each row in the dense tensor represented by sp\_ids (i.e. there are no rows with empty features), and that all the indices of sp\_ids are in canonical row-major order.

`sp_ids` and `sp_weights` (if not None) are `SparseTensor`s or `RaggedTensor`s with rank of 2. For `SpareTensor`s with left-aligned non-zero entries which can be described as `RaggedTensor`s, use of `RaggedTensor`s can yield higher performance.

It also assumes that all id values lie in the range \[0, p0), where p0 is the sum of the size of params along dimension 0.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `params` | A single tensor representing the complete embedding tensor, or a list tensors all of same shape except for the first dimension, representing sharded embedding tensors. Alternatively, a `PartitionedVariable`, created by partitioning along dimension 0. Each element must be appropriately sized for the given `partition_strategy`. |\
| `sp_ids` | N x M `SparseTensor` of int64 ids where N is typically batch size and M is arbitrary or a `RaggedTensor` with rank 2. |\
| `sparse_weights` | `SparseTensor` or `RaggedTensor` of same type and shape as `sparse_ids`, containing float / double weights corresponding to `sparse_ids`, or `None` if all weights are assumed to be 1.0. |\
| `partition_strategy` | A string specifying the partitioning strategy, relevant if `len(params) > 1`. Currently `"div"` and `"mod"` are supported. Default is `"mod"`. See `tf.nn.embedding_lookup` for more details. |\
| `name` | Optional name for the op. |\
| `combiner` | A string specifying the reduction op. Currently "mean", "sqrtn" and "sum" are supported. "sum" computes the weighted sum of the embedding results for each row. "mean" is the weighted sum divided by the total weight. "sqrtn" is the weighted sum divided by the square root of the sum of the squares of the weights. Defaults to `mean`. |\
| `max_norm` | If not `None`, each embedding is clipped if its l2-norm is larger than this value, before combining. |\
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
| `TypeError` | If `sp_ids` is not a `SparseTensor` or `RaggedTensor`, or if `sp_weights` is neither `None` nor of the same type as `sp_ids`. |\
| `ValueError` | If `combiner` is not one of {"mean", "sqrtn", "sum"}. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.