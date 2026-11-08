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
 / [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 / DotInteraction layer

DotInteraction layer
====================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/feature_interaction/dot_interaction.py#L11)

### `DotInteraction` class

Copied!

`keras_rs.layers.DotInteraction(     self_interaction: bool = False, skip_gather: bool = False, **kwargs: Any )`

Dot interaction layer present in DLRM.

This layer computes distinct dot product ("feature interactions") for every pair of features. If `self_interaction` is True, we calculate dot products of the form `dot(e_i, e_j)` for `i <= j`, and `dot(e_i, e_j)` for `i < j`, otherwise. `e_i` denotes representation of feature `i`. The layer can be used to build the DLRM model.

**Arguments**

*   **self\_interaction**: bool. Indicates whether features should "self-interact". If it is True, then the diagonal entries of the interaction matrix are also taken.
*   **skip\_gather**: bool. If it's set, then the upper triangular part of the interaction matrix is set to 0. The output will be of shape `[batch_size, num_features * num_features]` of which half of the entries will be zeros. Otherwise, the output will be only the lower triangular part of the interaction matrix. The latter saves space but is much slower.
*   **\*\*kwargs**: Args to pass to the base class.

**Example**

Copied!

`# 1. Simple forward pass batch_size = 2 embedding_dim = 32 feature1 = np.random.randn(batch_size, embedding_dim) feature2 = np.random.randn(batch_size, embedding_dim) feature3 = np.random.randn(batch_size, embedding_dim) feature_interactions = keras_rs.layers.DotInteraction()(     [feature1, feature2, feature3] )  # 2. After embedding layer in a model vocabulary_size = 32 embedding_dim = 6  # Create a simple model containing the layer. feature_input_1 = keras.Input(shape=(), name='indices_1', dtype="int32") feature_input_2 = keras.Input(shape=(), name='indices_2', dtype="int32") feature_input_3 = keras.Input(shape=(), name='indices_3', dtype="int32") x1 = keras.layers.Embedding(     input_dim=vocabulary_size,     output_dim=embedding_dim )(feature_input_1) x2 = keras.layers.Embedding(     input_dim=vocabulary_size,     output_dim=embedding_dim )(feature_input_2) x3 = keras.layers.Embedding(     input_dim=vocabulary_size,     output_dim=embedding_dim )(feature_input_3) feature_interactions = keras_rs.layers.DotInteraction()([x1, x2, x3]) output = keras.layers.Dense(units=10)(x2) model = keras.Model(     [feature_input_1, feature_input_2, feature_input_3], output )  # Call the model on the inputs. batch_size = 2 f1 = np.random.randint(0, vocabulary_size, size=(batch_size,)) f2 = np.random.randint(0, vocabulary_size, size=(batch_size,)) f3 = np.random.randint(0, vocabulary_size, size=(batch_size,)) outputs = model([f1, f2, f3])`

**References**

*   [M. Naumov et al.](https://arxiv.org/abs/1906.00091)
    

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/feature_interaction/dot_interaction.py#L134)

### `call` method

Copied!

`DotInteraction.call(inputs: list[typing.Any])`

Forward pass of the dot interaction layer.

**Arguments**

*   **inputs**: list. Every element in the list represents a feature tensor of shape `[batch_size, feature_dim]`. All tensors in the list must have the same shape.

**Returns**

Tensor representing feature interactions. The shape of the tensor is `[batch_size, k]` where `k` is `num_features * num_features` if `skip_gather` is `True`. Otherwise, `k` is `num_features * (num_features + 1) / 2` if `self_interaction` is `True`, and `num_features * (num_features - 1) / 2` if not.

* * *

[DotInteraction layer](https://keras.io/keras_rs/api/feature_interaction_layers/dot_interaction/#dotinteraction-layer)

[`DotInteraction` class](https://keras.io/keras_rs/api/feature_interaction_layers/dot_interaction/#dotinteraction-class)

[`call` method](https://keras.io/keras_rs/api/feature_interaction_layers/dot_interaction/#call-method)