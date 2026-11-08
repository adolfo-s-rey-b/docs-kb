[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#apply_gradients)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#build)
        
    *   [compute\_sparse\_core\_stats](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#compute_sparse_core_stats)
        
    *   [dequeue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#dequeue)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#embedding_lookup)
        
    *   [enqueue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#enqueue)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#__call__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.TPUEmbeddingV2 Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#apply_gradients)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#build)
        
    *   [compute\_sparse\_core\_stats](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#compute_sparse_core_stats)
        
    *   [dequeue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#dequeue)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#embedding_lookup)
        
    *   [enqueue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#enqueue)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#__call__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L497-L2156)

The TPUEmbedding mid level API running on TPU with sparse core accelerator.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.TPUEmbeddingV2`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2)

tf.tpu.experimental.embedding.TPUEmbeddingV2(
        feature_config: Union[tf.tpu.experimental.embedding.FeatureConfig, Iterable],
        optimizer: Optional[tpu_embedding_v2_utils._Optimizer] = None,
        pipeline_execution_with_tensor_core: bool = False,
        sparse_core_embedding_config: Optional[tf.tpu.experimental.embedding.SparseCoreEmbeddingConfig] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `feature_config` | A nested structure of [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)<br> configs. |
| `optimizer` | An instance of one of [`tf.tpu.experimental.embedding.SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)<br>, [`tf.tpu.experimental.embedding.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adagrad)<br> or [`tf.tpu.experimental.embedding.Adam`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adam)<br>. When not created under TPUStrategy may be set to None to avoid the creation of the optimizer slot variables, useful for optimizing memory consumption when exporting the model for serving where slot variables aren't needed. |
| `pipeline_execution_with_tensor_core` | If True, the TPU embedding computations will overlap with the TensorCore computations (and hence will be one step old). Set to True for improved performance. |
| `sparse_core_embedding_config` | Configs for sparse core embedding including settings for table stacking, input feature static buffer size etc. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If optimizer is not one of tf.tpu.experimental.embedding.(SGD, Adam or Adagrad) or None when created under a TPUStrategy. |
| `RuntimeError` | If not created under TPUStrategy. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embedding_layouts` | Returns how the tables are laid out in the variables.<br><br>The SparseCoreTableLayout describes how a table is stored in its internal state. You need this only if you need to pull apart the internal state. |
| `embedding_table_shards` | Returns a dict of embedding tables, keyed by `TableConfig`. |
| `embedding_tables` | Returns a dict of embedding tables, keyed by stacked table name. |
| `variables` | Returns a dict of variables, keyed by `TableConfig`, then by slot name. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1141-L1345)

apply_gradients(
        gradients: Any, preserved_outputs: Dict[str, PartitionedCsrFormatTensor]
    )

Applies the gradient update to the embedding tables.

If a gradient of `None` is passed in any position of the nested structure, then a gradient update with a zero gradient is applied for that feature. For optimizers like SGD or Adagrad, this is the same as applying no update at all. For lazy Adam and other sparsely applied optimizers with decay, ensure you understand the effect of applying a zero gradient.

|     |     |
| --- | --- |
| Args |     |
| `gradients` | A nested structure of gradients, with structure matching the `feature_config` passed to this object. |
| `preserved_outputs` | A dicts of PartitionedCsrFormatTensor, coming from the second output of the embedding lookup call. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | if not built. |
| `ValueError` | If a non-[`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> non-`None` gradient is passed in, or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the incorrect shape is passed in. Also if the size of any sequence in `gradients` does not match corresponding sequence in `feature_config`. |
| `TypeError` | If the type of any sequence in `gradients` does not match corresponding sequence in `feature_config`. |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1132-L1139)

build()

Create variables and slots variables for TPU embeddings.

### `compute_sparse_core_stats`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1383-L1478)

@classmethod

Computes the max\_ids/unique ids settings from the input features.

### `dequeue`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1605-L1673)

dequeue(
        partitioned_tensors: Tuple[Dict[str, PartitionedCsrFormatTensor], int, int]
    ) -> Tuple[Any, Dict[str, PartitionedCsrFormatTensor]]

Perform embedding lookup.

### `embedding_lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1675-L1718)

embedding_lookup(
        features: Any, weights: Optional[Any] = None
    ) -> Tuple[Any, Dict[str, PartitionedCsrFormatTensor]]

Perform embedding lookup on the input feature.

|     |     |
| --- | --- |
| Args |     |
| `features` | A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, with the same structure as `feature_config`. Inputs will be downcast to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. Only one type out of [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> is supported per call. |
| `weights` | If not `None`, a nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, matching the above, except that the tensors should be of float type (and they will be downcast to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>). For [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s we assume the `indices` are the same for the parallel entries from `features` and similarly for [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s we assume the row\_splits are the same. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the input feature is not one of the Tensor, SparseTensor or RaggedTensor type. |
| `TypeError` | If the type of any sequence in `features` does not match corresponding sequence in `feature_config`. Similarly for `weights`, if not `None`. |

|     |     |
| --- | --- |
| Returns |     |
| `packed_activations` | Embedding lookup results packed as the same sequence of the input feature. |
| `packed_output` | A dict of PartitionedCsrFormatTensors. |

### `enqueue`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1480-L1553)

enqueue(
        features: Any, weights: Optional[Any] = None, device: Optional[str] = None
    ) -> Any

Preprocessing the features on host.

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L1347-L1351)

__call__(
        features: Any, weights: Optional[Any] = None
    ) -> Tuple[Any, Dict[str, PartitionedCsrFormatTensor]]

Call the mid level api to do embedding lookup.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| DEFAULT\_MAX\_IDS\_PER\_TABLE | `256` |
| DEFAULT\_MAX\_UNIQUE\_IDS\_PER\_TABLE | `256` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.