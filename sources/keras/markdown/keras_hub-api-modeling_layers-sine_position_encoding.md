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
 / SinePositionEncoding layer

SinePositionEncoding layer
==========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/sine_position_encoding.py#L7)

### `SinePositionEncoding` class

Copied!

`keras_hub.layers.SinePositionEncoding(max_wavelength=10000, **kwargs)`

Sinusoidal positional encoding layer.

This layer calculates the position encoding as a mix of sine and cosine functions with geometrically increasing wavelengths. Defined and formulized in [Attention is All You Need](https://arxiv.org/abs/1706.03762)
.

Takes as input an embedded token tensor. The input must have shape \[batch\_size, sequence\_length, feature\_size\]. This layer will return a positional encoding the same size as the embedded token tensor, which can be added directly to the embedded token tensor.

**Arguments**

*   **max\_wavelength**: The maximum angular wavelength of the sine/cosine curves, as described in Attention is All You Need. Defaults to `10000`.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Call arguments**

*   **inputs**: The tensor inputs to compute an embedding for, with shape `(batch_size, sequence_length, hidden_dim)`.
*   **start\_index**: An integer or integer tensor. The starting position to compute the encoding from. This is useful during cached decoding, where each position is predicted separately in a loop.
*   **positions**: Tensor of shape `(sequence_length,)` or `(batch_size, sequence_length)`. Custom positions for the input sequence. If specified, this tensor will be used to compute the position embedding, and the `start_index` argument will be ignored. This is useful for cases with non-standard positions.

**Example**

Copied!

`# create a simple embedding layer with sinusoidal positional encoding seq_len = 100 vocab_size = 1000 embedding_dim = 32 inputs = keras.Input((seq_len,), dtype="float32") embedding = keras.layers.Embedding(     input_dim=vocab_size, output_dim=embedding_dim )(inputs) positional_encoding = keras_hub.layers.SinePositionEncoding()(embedding) outputs = embedding + positional_encoding`

**References**

*   [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
    

* * *

[SinePositionEncoding layer](https://keras.io/keras_hub/api/modeling_layers/sine_position_encoding/#sinepositionencoding-layer)

[`SinePositionEncoding` class](https://keras.io/keras_hub/api/modeling_layers/sine_position_encoding/#sinepositionencoding-class)