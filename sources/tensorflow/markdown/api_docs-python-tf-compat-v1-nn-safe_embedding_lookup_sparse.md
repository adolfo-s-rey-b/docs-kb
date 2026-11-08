[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.safe\_embedding\_lookup\_sparse Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/safe_embedding_lookup_sparse#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/embedding_ops.py#L854-L1034)

Lookup embedding results, accounting for invalid IDs and empty features.

tf.compat.v1.nn.safe_embedding_lookup_sparse(
        embedding_weights,
        sparse_ids,
        sparse_weights=None,
        combiner='mean',
        default_id=None,
        name=None,
        partition_strategy='div',
        max_norm=None,
        allow_fast_lookup=False
    )

The partitioned embedding in `embedding_weights` must all be the same shape except for the first dimension. The first dimension is allowed to vary as the vocabulary size is not necessarily a multiple of `P`. `embedding_weights` may be a `PartitionedVariable` as returned by using [`tf.compat.v1.get_variable()`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)
 with a partitioner.

Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs with non-positive weight. For an entry with no features, the embedding vector for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

The ids and weights may be multi-dimensional `SparseTensor`s or `RaggedTensor`s with rank of 2. For `SpareTensor`s with left-aligned non-zero entries which can be described as `RaggedTensor`s, use of `RaggedTensor`s can yield higher performance. Embeddings are always aggregated along the last dimension.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `embedding_weights` | A single tensor representing the complete embedding tensor, or a list tensors all of same shape except for the first dimension, representing sharded embedding tensors. Alternatively, a `PartitionedVariable`, created by partitioning along dimension 0. Each element must be appropriately sized for the given `partition_strategy`. |
| `sparse_ids` | `SparseTensor` of shape `[d_0, d_1, ..., d_n]` containing the ids, where `d_0` is typically batch size, or a `RaggedTensor` with rank 2. |
| `sparse_weights` | `SparseTensor` or `RaggedTensor` of same type and shape as `sparse_ids`, containing float weights corresponding to `sparse_ids`, or `None` if all weights are assumed to be 1.0. |
| `combiner` | A string specifying how to combine embedding results for each entry. Currently "mean", "sqrtn" and "sum" are supported, with "mean" the default. |
| `default_id` | The id to use for an entry with no features. |
| `name` | A name for this operation (optional). |
| `partition_strategy` | A string specifying the partitioning strategy. Currently `"div"` and `"mod"` are supported. Default is `"div"`. |
| `max_norm` | If not `None`, all embeddings are l2-normalized to max\_norm before combining. |
| `allow_fast_lookup` | An optional boolean specifying whether to allow simplified embedding lookups when `params` is a single tensor and `max_norm` is `None`. Setting this flag to `True` during training can cause the use of dense gradients with increased memory footprint. |

|     |
| --- |
| Returns<br>------- |     |
| A dense tensor representing the combined embeddings for the sparse ids. For each row in the dense tensor represented by `sp_ids`, the op looks up the embeddings for all ids in that row, multiplies them by the corresponding weight, and combines these embeddings as specified.<br><br>In other words, if<br><br>`shape(combined embedding_weights) = [p0, p1, ..., pm]`<br><br>and<br><br>`shape(sparse_ids) = shape(sparse_weights) = [d0, d1, ..., dn]`<br><br>then<br><br>`shape(output) = [d0, d1, ... dn-1, p1, ..., pm]`.<br><br>For instance, if params is a 10x20 matrix, and sp\_ids / sp\_weights are<br><br>  [0, 0]: id 1, weight 2.0<br>      [0, 1]: id 3, weight 0.5<br>      [1, 0]: id -1, weight 1.0<br>      [2, 3]: id 1, weight 3.0<br><br>`default_id` is 0.<br><br>with `combiner`\="mean", then the output will be a 3x20 matrix where<br><br>  output[0, :] = (params[1, :] * 2.0 + params[3, :] * 0.5) / (2.0 + 0.5)<br>      output[1, :] = (params[0, :] * 1.0) / 1.0<br>      output[2, :] = (params[1, :] * 3.0) / 3.0 |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `embedding_weights` is empty. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.