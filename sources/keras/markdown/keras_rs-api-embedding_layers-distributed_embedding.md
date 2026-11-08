None

[KerasRS](https://keras.io/keras_rs/)

[API documentation](https://keras.io/keras_rs/api/)
 [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 [Losses](https://keras.io/keras_rs/api/losses/)
 [Metrics](https://keras.io/keras_rs/api/metrics/)
 [Examples](https://keras.io/keras_rs/examples/)

► [KerasRS](https://keras.io/keras_rs/)
 / [API documentation](https://keras.io/keras_rs/api/)
 / [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 / DistributedEmbedding layer

DistributedEmbedding layer
==========================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/distributed_embedding.py#L31)

### `DistributedEmbedding` class

Copied!

`keras_rs.layers.DistributedEmbedding(     feature_configs: Union[         keras_rs.src.layers.embedding.distributed_embedding_config.FeatureConfig,         tensorflow.python.tpu.tpu_embedding_v2_utils.FeatureConfig,         Sequence[             Union[                 keras_rs.src.layers.embedding.distributed_embedding_config.FeatureConfig,                 tensorflow.python.tpu.tpu_embedding_v2_utils.FeatureConfig,                 ForwardRef("Nested[T]"),             ]         ],         Mapping[             str,             Union[                 keras_rs.src.layers.embedding.distributed_embedding_config.FeatureConfig,                 tensorflow.python.tpu.tpu_embedding_v2_utils.FeatureConfig,                 ForwardRef("Nested[T]"),             ],         ],     ],     table_stacking: Union[str, Sequence[str], Sequence[Sequence[str]]] = "auto",     update_stats: bool = False,     **kwargs: Any )`

DistributedEmbedding, a layer for accelerated large embedding lookups.

* * *

Note: `DistributedEmbedding` is in Preview.
-------------------------------------------

* * *

`DistributedEmbedding` is a layer optimized for TPU chips with SparseCore and can dramatically improve the speed of embedding lookups and embedding training. It works by combining multiple lookups into one invocation, and by sharding the embedding tables across the available chips. Note that one will only see performance benefits for embedding tables that are large enough to to require sharding because they don't fit on a single chip. More details are provided in the "Placement" section below.

On other hardware, GPUs, CPUs and TPUs without SparseCore, `DistributedEmbedding` provides the same API without any specific acceleration. No particular distribution scheme is applied besides the one set via [`keras.distribution.set_distribution`](https://keras.io/api/distribution/distribution_utils#setdistribution-function)
.

`DistributedEmbedding` embeds sequences of inputs and reduces them to a single embedding by applying a configurable combiner function.

### Configuration

#### Features and tables

A `DistributedEmbedding` embedding layer is configured via a set of [`keras_rs.layers.FeatureConfig`](https://keras.io/keras_rs/api/embedding_layers/feature_config#featureconfig-class)
 objects, which themselves refer to [`keras_rs.layers.TableConfig`](https://keras.io/keras_rs/api/embedding_layers/table_config#tableconfig-class)
 objects.

*   `TableConfig` defines an embedding table with parameters such as its vocabulary size, embedding dimension, as well as a combiner for reduction and optimizer for training.
*   `FeatureConfig` defines what input features the `DistributedEmbedding` will handle and which embedding table to use. Note that multiple features can use the same embedding table.

Copied!

`table1 = keras_rs.layers.TableConfig(     name="table1",     vocabulary_size=TABLE1_VOCABULARY_SIZE,     embedding_dim=TABLE1_EMBEDDING_SIZE,     placement="auto", ) table2 = keras_rs.layers.TableConfig(     name="table2",     vocabulary_size=TABLE2_VOCABULARY_SIZE,     embedding_dim=TABLE2_EMBEDDING_SIZE,     placement="auto", )  feature1 = keras_rs.layers.FeatureConfig(     name="feature1",     table=table1,     input_shape=(GLOBAL_BATCH_SIZE,),     output_shape=(GLOBAL_BATCH_SIZE, TABLE1_EMBEDDING_SIZE), ) feature2 = keras_rs.layers.FeatureConfig(     name="feature2",     table=table2,     input_shape=(GLOBAL_BATCH_SIZE,),     output_shape=(GLOBAL_BATCH_SIZE, TABLE2_EMBEDDING_SIZE), )  feature_configs = {     "feature1": feature1,     "feature2": feature2, }  embedding = keras_rs.layers.DistributedEmbedding(feature_configs)`

#### Optimizers

Each embedding table within `DistributedEmbedding` uses its own optimizer for training, which is independent from the optimizer set on the model via `model.compile()`.

Note that not all optimizers are supported. Currently, the following are supported on all backends and accelerators:

*   [`keras.optimizers.Adagrad`](https://keras.io/api/optimizers/adagrad#adagrad-class)
    
*   [`keras.optimizers.Adam`](https://keras.io/api/optimizers/adam#adam-class)
    
*   [`keras.optimizers.Ftrl`](https://keras.io/api/optimizers/ftrl#ftrl-class)
    
*   [`keras.optimizers.SGD`](https://keras.io/api/optimizers/sgd#sgd-class)
    

Also, not all parameters of the optimizers are supported (e.g. the `nesterov` option of `SGD`). An error is raised when an unsupported optimizer or an unsupported optimizer parameter is used.

#### Placement

Each embedding table within `DistributedEmbedding` can be either placed on the SparseCore chip or the default device placement for the accelerator (e.g. HBM of the Tensor Cores on TPU). This is controlled by the `placement` attribute of [`keras_rs.layers.TableConfig`](https://keras.io/keras_rs/api/embedding_layers/table_config#tableconfig-class)
.

*   A placement of `"sparsecore"` indicates that the table should be placed on the SparseCore chips. An error is raised if this option is selected and there are no SparseCore chips.
*   A placement of `"default_device"` indicates that the table should not be placed on SparseCore, even if available. Instead the table is placed on the device where the model normally goes, i.e. the HBM on TPUs and GPUs. In this case, if applicable, the table is distributed using the scheme set via [`keras.distribution.set_distribution`](https://keras.io/api/distribution/distribution_utils#setdistribution-function)
    . On GPUs, CPUs and TPUs without SparseCore, this is the only placement available, and is the one selected by `"auto"`.
*   A placement of `"auto"` indicates to use `"sparsecore"` if available, and `"default_device"` otherwise. This is the default when not specified.

To optimize performance on TPU:

*   Tables that are so large that they need to be sharded should use the `"sparsecore"` placement.
*   Tables that are small enough should use `"default_device"` and should typically be replicated across TPUs by using the [`keras.distribution.DataParallel`](https://keras.io/api/distribution/data_parallel#dataparallel-class)
     distribution option.

### Usage with TensorFlow on TPU with SpareCore

#### Inputs

In addition to [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
, `DistributedEmbedding` accepts [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 and [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/SparseTensor)
 as inputs for the embedding lookups. Ragged tensors must be ragged in the dimension with index 1. Note that if weights are passed, each weight tensor must be of the same class as the inputs for that particular feature and use the exact same ragged row lenghts for ragged tensors, and the same indices for sparse tensors. All the output of `DistributedEmbedding` are dense tensors.

#### Setup

To use `DistributedEmbedding` on TPUs with TensorFlow, one must use a [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
. The `DistributedEmbedding` layer must be created under the `TPUStrategy`.

Copied!

`resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu="local") topology = tf.tpu.experimental.initialize_tpu_system(resolver) device_assignment = tf.tpu.experimental.DeviceAssignment.build(     topology, num_replicas=resolver.get_tpu_system_metadata().num_cores ) strategy = tf.distribute.TPUStrategy(     resolver, experimental_device_assignment=device_assignment )  with strategy.scope():     embedding = keras_rs.layers.DistributedEmbedding(feature_configs)`

#### Usage in a Keras model

To use Keras' `model.fit()`, one must compile the model under the `TPUStrategy`. Then, `model.fit()`, `model.evaluate()` or `model.predict()` can be called directly. The Keras model takes care of running the model using the strategy and also automatically distributes the dataset.

Copied!

`with strategy.scope():     embedding = keras_rs.layers.DistributedEmbedding(feature_configs)     model = create_model(embedding)     model.compile(loss=keras.losses.MeanSquaredError(), optimizer="adam")  model.fit(dataset, epochs=10)`

#### Direct invocation

`DistributedEmbedding` must be invoked via a `strategy.run` call nested in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

Copied!

`@tf.function def embedding_wrapper(tf_fn_inputs, tf_fn_weights=None):     def strategy_fn(st_fn_inputs, st_fn_weights):         return embedding(st_fn_inputs, st_fn_weights)      return strategy.run(strategy_fn, args=(tf_fn_inputs, tf_fn_weights)))  embedding_wrapper(my_inputs, my_weights)`

When using a dataset, the dataset must be distributed. The iterator can then be passed to the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 that uses `strategy.run`.

Copied!

`dataset = strategy.experimental_distribute_dataset(dataset)  @tf.function def run_loop(iterator):     def step(data):         (inputs, weights), labels = data         with tf.GradientTape() as tape:             result = embedding(inputs, weights)             loss = keras.losses.mean_squared_error(labels, result)         tape.gradient(loss, embedding.trainable_variables)         return result      for _ in tf.range(4):         result = strategy.run(step, args=(next(iterator),))  run_loop(iter(dataset))`

### Usage with JAX on TPU with SpareCore

#### Setup

To use `DistributedEmbedding` on TPUs with JAX, one must create and set a Keras `Distribution`.

Copied!

`distribution = keras.distribution.DataParallel(devices=jax.device("tpu")) keras.distribution.set_distribution(distribution)`

#### Inputs

For JAX, inputs can either be dense tensors, or ragged (nested) NumPy arrays. To enable `jit_compile = True`, one must explicitly call `layer.preprocess(...)` on the inputs, and then feed the preprocessed output to the model. See the next section on preprocessing for details.

Ragged input arrays must be ragged in the dimension with index 1. Note that if weights are passed, each weight tensor must be of the same class as the inputs for that particular feature and use the exact same ragged row lengths for ragged tensors. All the output of `DistributedEmbedding` are dense tensors.

#### Preprocessing

In JAX, SparseCore usage requires specially formatted data that depends on properties of the available hardware. This data reformatting currently does not support jit-compilation, so must be applied _prior_ to passing data into a model.

Preprocessing works on dense or ragged NumPy arrays, or on tensors that are convertible to dense or ragged NumPy arrays like [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
.

One simple way to add preprocessing is to append the function to an input pipeline by using a python generator.

Copied!

`# Create the embedding layer. embedding_layer = DistributedEmbedding(feature_configs)  # Add preprocessing to a data input pipeline. def preprocessed_dataset_generator(dataset):     for (inputs, weights), labels in iter(dataset):         yield embedding_layer.preprocess(             inputs, weights, training=True         ), labels  preprocessed_train_dataset = preprocessed_dataset_generator(train_dataset)`

This explicit preprocessing stage combines the input and optional weights, so the new data can be passed directly into the `inputs` argument of the layer or model.

**NOTE**: When working in a multi-host setting with data parallelism, the data needs to be sharded properly across hosts. If the original dataset is of type [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, it will need to be manually sharded _prior_ to applying the preprocess generator:

Copied!

`# Manually shard the dataset across hosts. train_dataset = distribution.distribute_dataset(train_dataset) distribution.auto_shard_dataset = False  # Dataset is already sharded.  # Add a preprocessing stage to the distributed data input pipeline. train_dataset = preprocessed_dataset_generator(train_dataset)`

If the original dataset is _not_ a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, it must already be pre-sharded across hosts.

#### Usage in a Keras model

Once the global distribution is set and the input preprocessing pipeline is defined, model training can proceed as normal. For example:

Copied!

`# Construct, compile, and fit the model using the preprocessed data. model = keras.Sequential(   [     embedding_layer,     keras.layers.Dense(2),     keras.layers.Dense(3),     keras.layers.Dense(4),   ] ) model.compile(optimizer="adam", loss="mse", jit_compile=True) model.fit(preprocessed_train_dataset, epochs=10)`

#### Direct invocation

The `DistributedEmbedding` layer can also be invoked directly. Explicit preprocessing is required when used with JIT compilation.

Copied!

`# Call the layer directly. activations = embedding_layer(my_inputs, my_weights)  # Call the layer with JIT compilation and explicitly preprocessed inputs. embedding_layer_jit = jax.jit(embedding_layer) preprocessed_inputs = embedding_layer.preprocess(my_inputs, my_weights) activations = embedding_layer_jit(preprocessed_inputs)`

Similarly, for custom training loops, preprocessing must be applied prior to passing the data to the JIT-compiled training step.

Copied!

`# Create an optimizer and loss function. optimizer = keras.optimizers.Adam(learning_rate=1e-3)  def loss_and_updates(trainable_variables, non_trainable_variables, x, y):     y_pred, non_trainable_variables = model.stateless_call(         trainable_variables, non_trainable_variables, x, training=True     )     loss = keras.losses.mean_squared_error(y, y_pred)     return loss, non_trainable_variables  grad_fn = jax.value_and_grad(loss_and_updates, has_aux=True)  # Create a JIT-compiled training step. @jax.jit def train_step(state, x, y):     (       trainable_variables,       non_trainable_variables,       optimizer_variables,     ) = state     (loss, non_trainable_variables), grads = grad_fn(         trainable_variables, non_trainable_variables, x, y     )     trainable_variables, optimizer_variables = optimizer.stateless_apply(         optimizer_variables, grads, trainable_variables     )     return loss, (         trainable_variables,         non_trainable_variables,         optimizer_variables,     )  # Build optimizer variables. optimizer.build(model.trainable_variables)  # Assemble the training state. trainable_variables = model.trainable_variables non_trainable_variables = model.non_trainable_variables optimizer_variables = optimizer.variables state = trainable_variables, non_trainable_variables, optimizer_variables  # Training loop. for (inputs, weights), labels in train_dataset:     # Explicitly preprocess the data.     preprocessed_inputs = embedding_layer.preprocess(inputs, weights)     loss, state = train_step(state, preprocessed_inputs, labels)`

**Arguments**

*   **feature\_configs**: A nested structure of [`keras_rs.layers.FeatureConfig`](https://keras.io/keras_rs/api/embedding_layers/feature_config#featureconfig-class)
    .
*   **table\_stacking**: The table stacking to use. `None` means no table stacking. `"auto"` means to stack tables automatically. A list of table names or list of lists of table names means to stack the tables in the inner lists together. Note that table stacking is not supported on older TPUs, in which case the default value of `"auto"` will be interpreted as no table stacking.
*   **update\_stats**: If True, `'max_ids_per_partition'`, `'max_unique_ids_per_partition'` and `'suggested_coo_buffer_size_per_device'` are updated during training. This argument can be set to True only for the JAX backend.
*   **\*\*kwargs**: Additional arguments to pass to the layer base class.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/base_distributed_embedding.py#L739)

### `call` method

Copied!

`DistributedEmbedding.call(     inputs: Union[         Any,         Sequence[Union[Any, ForwardRef("Nested[T]")]],         Mapping[str, Union[Any, ForwardRef("Nested[T]")]],     ],     weights: Union[         Any,         Sequence[Union[Any, ForwardRef("Nested[T]")]],         Mapping[str, Union[Any, ForwardRef("Nested[T]")]],         NoneType,     ] = None,     training: bool = False, )`

Lookup features in embedding tables and apply reduction.

**Arguments**

*   **inputs**: A nested structure of 2D tensors to embed and reduce. The structure must be the same as the `feature_configs` passed during construction. Alternatively, may consist of already preprocessed inputs (see `preprocess`).
*   **weights**: An optional nested structure of 2D tensors of weights to apply before reduction. When present, the structure must be the same as `inputs` and the shapes must match.
*   **training**: Whether we are training or evaluating the model.

**Returns**

A nested structure of dense 2D tensors, which are the reduced embeddings from the passed features. The structure is the same as `inputs`.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/base_distributed_embedding.py#L629)

### `preprocess` method

Copied!

`DistributedEmbedding.preprocess(     inputs: Union[         Any,         Sequence[Union[Any, ForwardRef("Nested[T]")]],         Mapping[str, Union[Any, ForwardRef("Nested[T]")]],     ],     weights: Union[         Any,         Sequence[Union[Any, ForwardRef("Nested[T]")]],         Mapping[str, Union[Any, ForwardRef("Nested[T]")]],         NoneType,     ] = None,     training: bool = False, )`

Preprocesses and reformats the data for consumption by the model.

For the JAX backend, converts the input data to a hardward-dependent format required for use with SparseCores. Calling `preprocess` explicitly is only necessary to enable `jit_compile = True`.

For non-JAX backends, preprocessing will bundle together the inputs and weights, and separate the inputs by device placement. This step is entirely optional.

**Arguments**

*   **inputs**: Ragged or dense set of sample IDs.
*   **weights**: Optional ragged or dense set of sample weights.
*   **training**: If true, will update internal parameters, such as required buffer sizes for the preprocessed data.

**Returns**

Set of preprocessed inputs that can be fed directly into the `inputs` argument of the layer.

* * *

[DistributedEmbedding layer](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#distributedembedding-layer)

[`DistributedEmbedding` class](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#distributedembedding-class)

[Note: `DistributedEmbedding` is in Preview.](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#note-distributedembedding-is-in-preview)

[Configuration](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#configuration)

[Usage with TensorFlow on TPU with SpareCore](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#usage-with-tensorflow-on-tpu-with-sparecore)

[Usage with JAX on TPU with SpareCore](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#usage-with-jax-on-tpu-with-sparecore)

[`call` method](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#call-method)

[`preprocess` method](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding/#preprocess-method)