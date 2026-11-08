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
 / FeatureConfig configuration class

FeatureConfig configuration class
=================================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/distributed_embedding_config.py#L90)

### `FeatureConfig` class

Copied!

`keras_rs.layers.FeatureConfig(     name: str,     table: keras_rs.src.layers.embedding.distributed_embedding_config.TableConfig,     input_shape: Sequence[int | None],     output_shape: Sequence[int | None], )`

Configuration for one embedding feature.

Configures one feature for [`keras_rs.layers.DistributedEmbedding`](https://keras.io/keras_rs/api/embedding_layers/distributed_embedding#distributedembedding-class)
. Each feature uses a table configured via [`keras_rs.layers.TableConfig`](https://keras.io/keras_rs/api/embedding_layers/table_config#tableconfig-class)
 and multiple features can share the same table.

**Attributes**

*   **name**: The name of the feature. Must be defined.
*   **table**: The table in which to look up this feature.
*   **input\_shape**: The input shape of the feature. The feature fed into the layer has to match the shape. Note that for ragged dimensions in the input, the dimension provided here presents the maximum value; anything larger will be truncated. Also note that the first dimension represents the global batch size. For example, on TPU, this represents the total number of samples that are dispatched to all the TPUs connected to the current host.
*   **output\_shape**: The output shape of the feature activation. What is returned by the embedding layer has to match this shape.

* * *

[FeatureConfig configuration class](https://keras.io/keras_rs/api/embedding_layers/feature_config/#featureconfig-configuration-class)

[`FeatureConfig` class](https://keras.io/keras_rs/api/embedding_layers/feature_config/#featureconfig-class)