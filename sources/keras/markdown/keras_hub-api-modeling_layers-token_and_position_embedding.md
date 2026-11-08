None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 / TokenAndPositionEmbedding layer

TokenAndPositionEmbedding layer
===============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/token_and_position_embedding.py#L11)

### `TokenAndPositionEmbedding` class

Copied!

`keras_hub.layers.TokenAndPositionEmbedding(     vocabulary_size,     sequence_length,     embedding_dim,     tie_weights=True,     embeddings_initializer="uniform",     mask_zero=False,     **kwargs )`

A layer which sums a token and position embedding.

Token and position embeddings are ways of representing words and their order in a sentence. This layer creates a [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 token embedding and a [`keras_hub.layers.PositionEmbedding`](https://keras.io/keras_hub/api/modeling_layers/position_embedding#positionembedding-class)
 position embedding and sums their output when called. This layer assumes that the last dimension in the input corresponds to the sequence dimension.

**Arguments**

*   **vocabulary\_size**: The size of the vocabulary.
*   **sequence\_length**: The maximum length of input sequence
*   **embedding\_dim**: The output dimension of the embedding layer
*   **tie\_weights**: Boolean, whether or not the matrix for embedding and the matrix for the `reverse` projection should share the same weights.
*   **embeddings\_initializer**: The initializer to use for the Embedding Layers
*   **mask\_zero**: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is True, then all subsequent layers in the model need to support masking or an exception will be raised. If mask\_zero\` is set to True, as a consequence, index 0 cannot be used in the vocabulary (input\_dim should equal size of vocabulary + 1).
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Example**

Copied!

`inputs = np.ones(shape=(1, 50), dtype="int32") embedding_layer = keras_hub.layers.TokenAndPositionEmbedding(     vocabulary_size=10_000,     sequence_length=50,     embedding_dim=128, ) outputs = embedding_layer(inputs)`

* * *

[TokenAndPositionEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/token_and_position_embedding/#tokenandpositionembedding-layer)

[`TokenAndPositionEmbedding` class](https://keras.io/keras_hub/api/modeling_layers/token_and_position_embedding/#tokenandpositionembedding-class)