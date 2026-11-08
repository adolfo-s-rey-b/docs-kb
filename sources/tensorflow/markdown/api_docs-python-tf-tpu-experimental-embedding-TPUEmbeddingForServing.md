[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2FTPUEmbeddingForServing&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#build)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#embedding_lookup)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.TPUEmbeddingForServing Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#build)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#embedding_lookup)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_for_serving.py#L45-L316)

The TPUEmbedding mid level API running on CPU for serving.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.TPUEmbeddingForServing`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing)

tf.tpu.experimental.embedding.TPUEmbeddingForServing(
        feature_config: Union[tf.tpu.experimental.embedding.FeatureConfig, Iterable],
        optimizer: Optional[tpu_embedding_v2_utils._Optimizer],
        experimental_sparsecore_restore_info: Optional[Dict[str, Any]] = None
    )

You can first train your model using the TPUEmbedding class and save the checkpoint. Then use this class to restore the checkpoint to do serving.

First train a model and save the checkpoint.

model = model_fn(...)
    strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(
          feature_config=feature_config,
          optimizer=tf.tpu.experimental.embedding.SGD(0.1))
    
    # Your custom training code.
    
    checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
    checkpoint.save(...)

Then restore the checkpoint and do serving.

# Restore the model on CPU.
    model = model_fn(...)
    embedding = tf.tpu.experimental.embedding.TPUEmbeddingForServing(
          feature_config=feature_config,
          optimizer=tf.tpu.experimental.embedding.SGD(0.1))
    
    checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
    checkpoint.restore(...)
    
    result = embedding(...)
    table = embedding.embedding_table

|     |     |
| --- | --- |
| Args<br>---- |     |
| `feature_config` | A nested structure of [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)<br> configs. |
| `optimizer` | An instance of one of [`tf.tpu.experimental.embedding.SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)<br>, [`tf.tpu.experimental.embedding.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adagrad)<br> or [`tf.tpu.experimental.embedding.Adam`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adam)<br>. When not created under TPUStrategy may be set to None to avoid the creation of the optimizer slot variables, useful for optimizing memory consumption when exporting the model for serving where slot variables aren't needed. |
| `experimental_sparsecore_restore_info` | Information from the sparse core training, required to restore from checkpoint for serving (like number of TPU devices used `num_tpu_devices`.) |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If created under TPUStrategy. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embedding_tables` | Returns a dict of embedding tables, keyed by `TableConfig`. |
| `variables` | Returns a dict of variables, keyed by `TableConfig`, then by slot name. |

Methods
-------

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_for_serving.py#L181-L184)

build()

Create variables and slots variables for TPU embeddings.

### `embedding_lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_for_serving.py#L294-L316)

embedding_lookup(
        features: Any, weights: Optional[Any] = None
    ) -> Any

Apply standard lookup ops on CPU.

|     |     |
| --- | --- |
| Args |     |
| `features` | A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, with the same structure as `feature_config`. Inputs will be downcast to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. Only one type out of [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> is supported per call. |
| `weights` | If not `None`, a nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, matching the above, except that the tensors should be of float type (and they will be downcast to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>). For [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s we assume the `indices` are the same for the parallel entries from `features` and similarly for [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s we assume the row\_splits are the same. |

|     |
| --- |
| Returns |     |
| A nested structure of Tensors with the same structure as input features. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_base.py#L135-L139)

__call__(
        features: Any, weights: Optional[Any] = None
    ) -> Any

Call the mid level api to do embedding lookup.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.