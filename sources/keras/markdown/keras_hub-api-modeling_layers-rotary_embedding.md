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
 / RotaryEmbedding layer

RotaryEmbedding layer
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/rotary_embedding.py#L8)

### `RotaryEmbedding` class

Copied!

`keras_hub.layers.RotaryEmbedding(     max_wavelength=10000,     scaling_factor=1.0,     rope_type="linear",     beta_fast=32.0,     beta_slow=1.0,     original_max_position_embeddings=4096,     truncate=True,     sequence_axis=1,     feature_axis=-1,     denominator_dim=None,     attention_factor=None,     **kwargs )`

Rotary positional encoding layer.

This layer encodes absolute positional information with a rotation matrix. It calculates the rotary encoding with a mix of sine and cosine functions with geometrically increasing wavelengths. Defined and formulated in [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864v4)
. The input must be a tensor with shape a sequence dimension and a feature dimension. Typically, this will either an input with shape `(batch_size, sequence_length, feature_length)` or `(batch_size, sequence_length, num_heads, feature_length)`. This layer will return a new tensor with the rotary embedding applied to the input tensor.

**Arguments**

*   **max\_wavelength**: int. The maximum angular wavelength of the sine/cosine curves.
*   **scaling\_factor**: float. The scaling factor used to scale positions of the tokens.
*   **rope\_type**: str. The type of RoPE scaling to apply. Supported types: "linear", "dynamic", "yarn". Defaults to "linear".
*   **beta\_fast**: float. Beta fast parameter for YaRN scaling. Only used when rope\_type="yarn". Defaults to 32.0.
*   **beta\_slow**: float. Beta slow parameter for YaRN scaling. Only used when rope\_type="yarn". Defaults to 1.0.
*   **original\_max\_position\_embeddings**: int. Original maximum position embeddings for YaRN scaling. Only used when rope\_type="yarn". Defaults to 4096.
*   **truncate**: bool. Whether to round the YaRN correction range to whole dimensions. Only used when rope\_type="yarn". Defaults to True, matching the reference YaRN implementation.
*   **attention\_factor**: float. The YaRN temperature scale applied to the cos/sin embeddings. Only used when rope\_type="yarn". Defaults to `None`, which derives the scale as `0.1 * log(scaling_factor) + 1.0`. Pass an explicit value to override this default.
*   **sequence\_axis**: int. Sequence axis in the input tensor.
*   **feature\_axis**: int. Feature axis in the input tensor.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Call arguments**

*   **inputs**: The tensor inputs to apply the embedding to. This can have any shape, but must contain both a sequence and feature axis. The rotary embedding will be applied to `inputs` and returned.
*   **start\_index**: An integer or integer tensor. The starting position to compute the rotary embedding from. This is useful during cached decoding, where each position is predicted separately in a loop.
*   **positions**: Tensor of shape `(sequence_length,)` or `(batch_size, sequence_length)`. Custom positions for the input sequence. If specified, this tensor will be used to compute the rotary embedding, and the `start_index` argument will be ignored. This is useful for cases with non-standard positions.

**Examples**

Copied!

`batch_size = 16 feature_length = 18 sequence_length = 256 num_heads = 8  # No multi-head dimension. tensor = np.ones((batch_size, sequence_length, feature_length)) rot_emb_layer = RotaryEmbedding() tensor_rot = rot_emb_layer(tensor)  # With multi-head dimension. tensor = np.ones((batch_size, sequence_length, num_heads, feature_length)) tensor_rot = rot_emb_layer(tensor)`

**References**

*   [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864v4)
    

* * *

[RotaryEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/rotary_embedding/#rotaryembedding-layer)

[`RotaryEmbedding` class](https://keras.io/keras_hub/api/modeling_layers/rotary_embedding/#rotaryembedding-class)