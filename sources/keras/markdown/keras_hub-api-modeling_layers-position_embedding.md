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
 / PositionEmbedding layer

PositionEmbedding layer
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/position_embedding.py#L8)

### `PositionEmbedding` class

Copied!

`keras_hub.layers.PositionEmbedding(     sequence_length, initializer="glorot_uniform", **kwargs )`

A layer which learns a position embedding for inputs sequences.

This class assumes that in the input tensor, the last dimension corresponds to the features, and the dimension before the last corresponds to the sequence.

This layer does not supporting masking, but can be combined with a [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 for padding mask support.

**Arguments**

*   **sequence\_length**: The maximum length of the dynamic sequence.
*   **initializer**: The initializer to use for the embedding weights. Defaults to `"glorot_uniform"`.
*   **seq\_axis**: The axis of the input tensor where we add the embeddings.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Call arguments**

*   **inputs**: The tensor inputs to compute an embedding for, with shape `(batch_size, sequence_length, hidden_dim)`. Only the input shape will be used, as the position embedding does not depend on the input sequence content.
*   **start\_index**: An integer or integer tensor. The starting position to compute the position embedding from. This is useful during cached decoding, where each position is predicted separately in a loop.
*   **positions**: Tensor of shape `(sequence_length,)` or `(batch_size, sequence_length)`. Custom positions for the input sequence. If specified, this tensor will be used to compute the position embedding, and the `start_index` argument will be ignored. This is useful for cases with non-standard positions.

**Example**

Called directly on input.

Copied!

`>>> layer = keras_hub.layers.PositionEmbedding(sequence_length=10) >>> layer(np.zeros((8, 10, 16)))`

Combine with a token embedding.

Copied!

`seq_length = 50 vocab_size = 5000 embed_dim = 128 inputs = keras.Input(shape=(seq_length,)) token_embeddings = keras.layers.Embedding(     input_dim=vocab_size, output_dim=embed_dim )(inputs) position_embeddings = keras_hub.layers.PositionEmbedding(     sequence_length=seq_length )(token_embeddings) outputs = token_embeddings + position_embeddings`

**Reference**

*   [Devlin et al., 2019](https://arxiv.org/abs/1810.04805)
    

* * *

[PositionEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/position_embedding/#positionembedding-layer)

[`PositionEmbedding` class](https://keras.io/keras_hub/api/modeling_layers/position_embedding/#positionembedding-class)