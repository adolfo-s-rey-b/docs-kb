[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2FTPUEmbedding&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#apply_gradients)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#build)
        
    *   [dequeue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#dequeue)
        
    *   [enqueue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#enqueue)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.TPUEmbedding Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#apply_gradients)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#build)
        
    *   [dequeue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#dequeue)
        
    *   [enqueue](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding#enqueue)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2.py#L75-L1555)

The TPUEmbedding mid level API.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)

tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config: Union[tf.tpu.experimental.embedding.FeatureConfig, Iterable],
        optimizer: Optional[tpu_embedding_v2_utils._Optimizer],
        pipeline_execution_with_tensor_core: bool = False
    )

This class can be used to support training large embeddings on TPU. When creating an instance of this class, you must specify the complete set of tables and features you expect to lookup in those tables. See the documentation of [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 and [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)
 for more details on the complete set of options. We will cover the basic usage here.

table_config_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...)
    table_config_two = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...)
    feature_config = {
        'feature_one': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_one),
        'feature_two': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_one),
        'feature_three': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_two)}

There are two modes under which the `TPUEmbedding` class can used. This depends on if the class was created under a `TPUStrategy` scope or not.

Under `TPUStrategy`, we allow access to the method `enqueue`, `dequeue` and `apply_gradients`. We will show examples below of how to use these to train and evaluate your model. Under CPU, we only access to the `embedding_tables` property which allow access to the embedding tables so that you can use them to run model evaluation/prediction on CPU.

First lets look at the `TPUStrategy` mode. Initial setup looks like:

strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(
          feature_config=feature_config,
          optimizer=tf.tpu.experimental.embedding.SGD(0.1))

When creating a distributed dataset that is to be passed to the enqueue operation a special input option must be specified:

distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)

Different feature inputs can have different shapes. For dense and sparse tensor, rank 2 and above is supported. For ragged tensor, although only rank 2 is supported, you can specify the output shape to be rank 2 and above. The output shape specified in the FeatureConfig has the first priority. The input shape passed in build method has second priority and the input shapes auto detected from input feature has the lowest priority. The latter two will be converted to output shapes by omitting the last dimension. If the lower priority one has output shapes which don't match the former one. A ValueError will be raised. Only when the former one has undefined output shapes, the latter one can override.

To use this API on TPU you should use a custom training loop. Below is an example of a training and evaluation step:

@tf.function
    def training_step(dataset_iterator, num_steps):
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)
          model_output = model(activations)
          loss = ...  # some function of labels and model_output
    
        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)
        # Insert your model gradient and optimizer application here
    
      for _ in tf.range(num_steps):
        embedding_features, tpu_features = next(dataset_iterator)
        embedding.enqueue(embedding_features, training=True)
        strategy.run(tpu_step, args=(tpu_features, ))
    
    @tf.function
    def evaluation_step(dataset_iterator, num_steps):
      def tpu_step(tpu_features):
        activations = embedding.dequeue()
        model_output = model(activations)
        # Insert your evaluation code here.
    
      for _ in tf.range(num_steps):
        embedding_features, tpu_features = next(dataset_iterator)
        embedding.enqueue(embedding_features, training=False)
        strategy.run(tpu_step, args=(tpu_features, ))

In the above examples, we assume that the user has a dataset which returns a tuple where the first element of the tuple matches the structure of what was passed as the `feature_config` argument to the object initializer. Also we utilize [`tf.range`](https://www.tensorflow.org/api_docs/python/tf/range)
 to get a [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
 in order to increase performance.

When checkpointing your model, you should include your [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 object in the checkpoint. It is a trackable object and saving it will save the embedding tables and their optimizer slot variables:

checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
    checkpoint.save(...)

On CPU, only the `embedding_table` property is usable. This will allow you to restore a checkpoint to the object and have access to the table variables:

model = model_fn(...)
    embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config=feature_config,
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))
    checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
    checkpoint.restore(...)
    
    tables = embedding.embedding_tables

You can now use table in functions like [`tf.nn.embedding_lookup`](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup)
 to perform your embedding lookup and pass to your model.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `feature_config` | A nested structure of [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)<br> configs. |
| `optimizer` | An instance of one of [`tf.tpu.experimental.embedding.SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)<br>, [`tf.tpu.experimental.embedding.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adagrad)<br> or [`tf.tpu.experimental.embedding.Adam`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adam)<br>. When not created under TPUStrategy may be set to None to avoid the creation of the optimizer slot variables, useful for optimizing memory consumption when exporting the model for serving where slot variables aren't needed. |
| `pipeline_execution_with_tensor_core` | If True, the TPU embedding computations will overlap with the TensorCore computations (and hence will be one step old). Set to True for improved performance. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If optimizer is not one of tf.tpu.experimental.embedding.(SGD, Adam or Adagrad) or None when created under a TPUStrategy. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embedding_tables` | Returns a dict of embedding tables, keyed by `TableConfig`.<br><br>This property only works when the `TPUEmbedding` object is created under a non-TPU strategy. This is intended to be used to for CPU based lookup when creating a serving checkpoint. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2.py#L617-L722)

apply_gradients(
        gradients, name: Optional[Text] = None
    )

Applies the gradient update to the embedding tables.

If a gradient of `None` is passed in any position of the nested structure, then an gradient update with a zero gradient is applied for that feature. For optimizers like SGD or Adagrad, this is the same as applying no update at all. For lazy Adam and other sparsely applied optimizers with decay, ensure you understand the effect of applying a zero gradient.

strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)
    
    distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)
    
    @tf.function
    def training_step():
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)
    
          loss = ... #  some computation involving activations
    
        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)
    
      embedding_features, tpu_features = next(dataset_iterator)
      embedding.enqueue(embedding_features, training=True)
      strategy.run(tpu_step, args=(tpu_features, ))
    
    training_step()

|     |     |
| --- | --- |
| Args |     |
| `gradients` | A nested structure of gradients, with structure matching the `feature_config` passed to this object. |
| `name` | A name for the underlying op. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If called when object wasn't created under a `TPUStrategy` or if not built (either by manually calling build or calling enqueue). |
| `ValueError` | If a non-[`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> non-`None` gradient is passed in, or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the incorrect shape is passed in. Also if the size of any sequence in `gradients` does not match corresponding sequence in `feature_config`. |
| `TypeError` | If the type of any sequence in `gradients` does not match corresponding sequence in `feature_config`. |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2.py#L353-L421)

build(
        per_replica_input_shapes=None, per_replica_batch_size=None
    )

Create the underlying variables and initializes the TPU for embeddings.

This method creates the underlying variables (including slot variables). If created under a TPUStrategy, this will also initialize the TPU for embeddings.

This function will automatically get called by enqueue, which will try to determine your output shapes. If this fails, you must manually call this method before you call enqueue.

|     |     |
| --- | --- |
| Args |     |
| `per_replica_input_shapes` | A nested structure of The per replica input shapes that matches the structure of the feature config. The input shapes should be the same as the input shape of the feature (except for ragged tensor) Note that it is fixed and the same per replica input shapes must be used for both training and evaluation. If you want to calculate this from the global input shapes, you can use `num_replicas_in_sync` property of your strategy object. May be set to None if not created under a TPUStrategy. |
| `per_replica_batch_size` | (Deprecated) The per replica batch size that you intend to use. Note that is fixed and the same batch size must be used for both training and evaluation. If you want to calculate this from the global batch size, you can use `num_replicas_in_sync` property of your strategy object. May be set to None if not created under a TPUStrategy. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If per\_replica\_input\_shapes is inconsistent with the output shapes stored in the feature config or the output shapes get from the input shapes are not fully defined. |
| `RuntimeError` | If tpu embedding is already initialized on TPU. |

### `dequeue`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2.py#L724-L799)

dequeue(
        name: Optional[Text] = None
    )

Get the embedding results.

Returns a nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 objects, matching the structure of the `feature_config` argument to the `TPUEmbedding` class. The output shape of the tensors is `(*output_shape, dim)`, `dim` is the dimension of the corresponding `TableConfig`. For output\_shape, there are three places where it can be set.

1.  FeatureConfig provided in the **init** function.
2.  Per\_replica\_output\_shapes by directly calling the build method after initializing the tpu embedding class.
3.  Auto detected from the shapes of the input feature. The priority of these places is the exact same order.

strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)
    
    distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)
    
    @tf.function
    def training_step():
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)
    
          loss = ... #  some computation involving activations
    
        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)
    
      embedding_features, tpu_features = next(dataset_iterator)
      embedding.enqueue(embedding_features, training=True)
      strategy.run(tpu_step, args=(tpu_features, ))
    
    training_step()

|     |     |
| --- | --- |
| Args |     |
| `name` | A name for the underlying op. |

|     |
| --- |
| Returns |     |
| A nested structure of tensors, with the same structure as `feature_config` |     |

passed to this instance of the `TPUEmbedding` object.

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If called when object wasn't created under a `TPUStrategy` or if not built (either by manually calling build or calling enqueue). |

### `enqueue`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2.py#L1108-L1378)

enqueue(
        features,
        weights=None,
        training: bool = True,
        name: Optional[Text] = None,
        device: Optional[Text] = None
    )

Enqueues id tensors for embedding lookup.

This function enqueues a structure of features to be looked up in the embedding tables. We expect that the input shapes of each of the tensors in features matches the output shapes set via FeatureConfig or build method (if any). the output shapes will be auto detected based on the input shapes with the max\_sequence\_length or output shape setting in the FeatureConfig. Note that the output shapes is based on per replica batch size. If your input dataset is batched to the global batch size and you use [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
's `experimental_distribute_dataset` or if you use `distribute_datasets_from_function` and batch to the per core batch size computed by the context passed to your input function, the output shapes should match automatically.

The auto detected the output shapes:

1.  For dense tensor, if rank 2 or above, make sure the tensor has last dimension as 1. The output shape will be the input shape excluding the last dimension.
2.  For sparse tensor, make sure the tensor has rank 2 and above. a. If feature config has max\_sequence\_length equals 0 or output shape set (the max\_sequence\_length setting will be ignored), the output shape will be the input shape excluding the last dimension. b. Otherwise, if the tensor is rank 2, the output shape will be input shape with last dimension set as max\_sequence\_length. If the tensor is above rank 2, the output shape will be the input shape excluding the last dimension and the last dimension of the output shape will be set to max\_sequence\_length.
3.  For ragged tensor, make sure the tensor has rank 2. a. If feature config has max\_sequence\_length equals 0 or output shape set (the max\_sequence\_length setting will be ignored), the output shape will be the input shape excluding the last dimension. b. Otherwise, the output shape will be the input shape excluding the last dimension and the last dimension of the output shape will be set to max\_sequence\_length.

strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)
    
    distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)
    
    @tf.function
    def training_step():
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)
    
          loss = ... #  some computation involving activations
    
        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)
    
      embedding_features, tpu_features = next(dataset_iterator)
      embedding.enqueue(embedding_features, training=True)
      strategy.run(tpu_step, args=(tpu_features,))
    
    training_step()

For finer grained control, in the above example the line

  embedding.enqueue(embedding_features, training=True)

may be replaced with

  per_core_embedding_features = self.strategy.experimental_local_results(
          embedding_features)
    
      def per_core_enqueue(ctx):
        core_id = ctx.replica_id_in_sync_group
        device = strategy.extended.worker_devices[core_id]
        embedding.enqueue(per_core_embedding_features[core_id],
                          device=device)
    
      strategy.experimental_distribute_values_from_function(
          per_core_queue_inputs)

|     |     |
| --- | --- |
| Args |     |
| `features` | A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, with the same structure as `feature_config`. Inputs will be downcast to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. Only one type out of [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> is supported per call. |
| `weights` | If not `None`, a nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s, matching the above, except that the tensors should be of float type (and they will be downcast to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>). For [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>s we assume the `indices` are the same for the parallel entries from `features` and similarly for [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>s we assume the row\_splits are the same. |
| `training` | Defaults to `True`. If `False`, enqueue the batch as inference batch (forward pass only). Do not call `apply_gradients` when this is `False` as this may lead to a deadlock. name: A name for the underlying op. device: The device name (e.g. '/task:0/device:TPU:2') where this batch should be enqueued. This should be set if and only if features is not a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> and enqueue is not being called inside a TPU context (e.g. inside [`TPUStrategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#run)<br>). |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | When called inside a strategy.run call and input is not directly taken from the args of the `strategy.run` call. Also if the size of any sequence in `features` does not match corresponding sequence in `feature_config`. Similarly for `weights`, if not `None`. If input shapes of features is unequal or different from a previous call. |
| `RuntimeError` | When called inside a strategy.run call and inside XLA control flow. If batch\_size is not able to be determined and build was not called. |
| `TypeError` | If the type of any sequence in `features` does not match corresponding sequence in `feature_config`. Similarly for `weights`, if not `None`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.