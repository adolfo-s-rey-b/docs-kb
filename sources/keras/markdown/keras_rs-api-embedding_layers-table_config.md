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
 / TableConfig configuration class

TableConfig configuration class
===============================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/distributed_embedding_config.py#L12)

### `TableConfig` class

Copied!

`keras_rs.layers.TableConfig(     name: str,     vocabulary_size: int,     embedding_dim: int,     initializer: (         str | keras.src.initializers.initializer.Initializer     ) = keras.src.initializers.random_initializers.VarianceScaling(mode="fan_out"),     optimizer: str | keras.src.optimizers.optimizer.Optimizer = "adam",     combiner: str = "mean",     placement: str = "auto",     max_ids_per_partition: int = 256,     max_unique_ids_per_partition: int = 256, )`

Configuration for one embedding table.

Configures one table for use by one or more [`keras_rs.layers.FeatureConfig`](https://keras.io/keras_rs/api/embedding_layers/feature_config#featureconfig-class)
, which in turn is used to configure a [`keras_rs.layers.DistributedEmbedding`](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding#distributedembedding-class)
.

**Attributes**

*   **name**: The name of the table. Must be defined.
*   **vocabulary\_size**: Size of the table's vocabulary (number of rows).
*   **embedding\_dim**: The embedding dimension (width) of the table.
*   **initializer**: The initializer for the embedding weights. If not specified, defaults to `truncated_normal_initializer` with mean `0.0` and standard deviation `1 / sqrt(embedding_dim)`.
*   **optimizer**: The optimizer for the embedding table. Only SGD, Adagrad, Adam, and FTRL are supported. Note that not all of the optimizer's parameters are supported. Defaults to Adam.
*   **combiner**: Specifies how to reduce if there are multiple entries in a single row. `mean`, `sqrtn` and `sum` are supported. `mean` is the default. `sqrtn` often achieves good accuracy, in particular with bag-of-words columns.
*   **placement**: Where to place the embedding table. `"auto"`, which is the default, means that the table is placed on SparseCore if available, otherwise on the default device where the rest of the model is placed. A value of `"sparsecore"` means the table will be placed on the SparseCore chips and an error is raised if SparseCore is not available. A value of `"default_device"` means the table will be placed on the default device where the rest of the model is placed, even if SparseCore is available. The default device for the rest of the model is the TPU's TensorCore on TPUs, otherwise the GPU or CPU.
*   **max\_ids\_per\_partition**: The max number of ids per partition for the table. This is an input data dependent value and is required by the compiler to appropriately allocate memory.
*   **max\_unique\_ids\_per\_partition**: The max number of unique ids per partition for the table. This is an input data dependent value and is required by the compiler to appropriately allocate memory.

* * *

[TableConfig configuration class](https://keras.io/keras_rs/api/embedding_layers/table_config/#tableconfig-configuration-class)

[`TableConfig` class](https://keras.io/keras_rs/api/embedding_layers/table_config/#tableconfig-class)