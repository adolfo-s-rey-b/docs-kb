[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#build)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#embedding_lookup)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.TPUEmbeddingV0 Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#methods)
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#build)
        
    *   [embedding\_lookup](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#embedding_lookup)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v1.py#L38-L445)

The TPUEmbedding mid level API running on TPU without Embedding accelerator.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.TPUEmbeddingV0`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0)

tf.tpu.experimental.embedding.TPUEmbeddingV0(
        feature_config: Union[tf.tpu.experimental.embedding.FeatureConfig, Iterable],
        optimizer: Optional[tpu_embedding_v2_utils._Optimizer]
    )

This class has to be created under the `TPUStrategy`, Otherwise a RuntimeError will be raised.

strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbeddingV0(
          feature_config=feature_config,
          optimizer=tf.tpu.experimental.embedding.SGD(0.1))

When creating a distributed dataset that is to be passed to the lookup operation a special input option must be specified:

distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)

Below is an example of a training and evaluation step:

optimizer = tf.keras.optimizers.SGD(0.1)
    
    @tf.function
    def training_step(dataset_iterator, num_steps):
      def tpu_step(embedding_features):
        with tf.GradientTape() as tape:
          tape.watch(embedding.embedding_table.values())
          activation = embedding(embedding_features)
          model_output = model(activations)
          loss = ...  # some function of labels and model_output
    
        embedding_gradients = tape.gradient(loss,
                                            embedding.embedding_table.values())
        optimizer.apply_gradients(list(zip(gradients,
                                  mid_level_api.embedding_tables.values())))
        # Insert your model gradient and optimizer application here
    
      for _ in tf.range(num_steps):
        strategy.run(tpu_step, args=(next(dataset_iterator), ))
    
    @tf.function
    def evalution_step(dataset_iterator, num_steps):
      def tpu_step(embedding_features):
        activations = embedding(embedding_features)
        model_output = model(activations)
        # Insert your evaluation code here.
    
      for _ in tf.range(num_steps):
        strategy.run(tpu_step, args=(next(dataset_iterator), ))

optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.1)
    
    def slot_variable_creation_fn(table, slot_names, slot_initializers):
        slots = {}
        for slot, initializer in zip(slot_names, slot_initializers):
          slots[slot] = optimizer.add_slot(table, slot, initializer)
        return slots
    
    embedding_optimizer = tf.experimental.embedding.Adagrad(
        learning_rate=0.1,
        slot_variable_creation_fn=slot_variable_creation_fn)
    
    # Use the embedding optimizer to create mid level api and keras optimizer to
    # apply gradients.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embedding_tables` | Returns a dict of embedding tables, keyed by `TableConfig`. |

Methods
-------

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_base.py#L128-L133)

build()

Create variables and slots variables for TPU embeddings.

### `embedding_lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v1.py#L241-L306)

embedding_lookup(
        features: Any, weights: Optional[Any] = None
    ) -> Any

Apply embedding lookup on TPUs using Tensorcore.

Note that all the sparse and ragged tensors will be converted to dense tensors on CPU and then passed to the TPU to do embedding look up. Large embedding lookup is not supported by this API, use the TPUEmbedding mid level api instead.

|     |     |
| --- | --- |
| Args |     |
| `features` | a nested structure of Tensors, SparseTensors or RaggedTensors. |
| `weights` | a nested structure of Tensors, SparseTensors or RaggedTensors or None for no weights. If not None, structure must match that of inputs, but entries are allowed to be None. |

|     |
| --- |
| Returns |     |
| A nested structure of Tensors with the same structure as inputs. |     |

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