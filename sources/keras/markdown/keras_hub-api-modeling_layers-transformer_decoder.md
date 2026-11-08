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
 / TransformerDecoder layer

TransformerDecoder layer
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/transformer_decoder.py#L17)

### `TransformerDecoder` class

Copied!

`keras_hub.layers.TransformerDecoder(     intermediate_dim,     num_heads,     dropout=0,     activation="relu",     layer_norm_epsilon=1e-05,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     normalize_first=False,     **kwargs )`

Transformer decoder.

This class follows the architecture of the transformer decoder layer in the paper [Attention is All You Need](https://arxiv.org/abs/1706.03762)
. Users can instantiate multiple instances of this class to stack up a decoder.

By default, this layer will apply a causal mask to the decoder attention layer. You can also pass padding or attention masks directly to the layer during call, e.g. with `decoder_padding_mask` or `decoder_attention_mask`.

This layer can be called with either one or two inputs. The number of inputs must be consistent across all calls. The options are as follows: `layer(decoder_sequence)`: no cross-attention will be built into the decoder block. This is useful when building a "decoder-only" transformer such as GPT-2. `layer(decoder_sequence, encoder_sequence)`: cross-attention will be built into the decoder block. This is useful when building an "encoder-decoder" transformer, such as the original transformer model described in Attention is All You Need.

**Arguments**

*   **intermediate\_dim**: int, the hidden size of feedforward network.
*   **num\_heads**: int, the number of heads in MultiHeadAttention.
*   **dropout**: float. the dropout value, shared by MultiHeadAttention and feedforward network. Defaults to `0.`.
*   **activation**: string or `keras.activations`. the activation function of feedforward network. Defaults to `"relu"`.
*   **layer\_norm\_epsilon**: float. The eps value in layer normalization components. Defaults to `1e-5`.
*   **kernel\_initializer**: string or `keras.initializers` initializer. The kernel initializer for the dense and multiheaded attention layers. Defaults to `"glorot_uniform"`.
*   **bias\_initializer**: string or `keras.initializers` initializer. The bias initializer for the dense and multiheaded attention layers. Defaults to `"zeros"`.
*   **normalize\_first**: bool. If True, the inputs to the attention layer(s) and the intermediate dense layer are normalized (similar to GPT-2). If set to False, outputs of attention layer and intermediate dense layer are normalized (similar to BERT). Defaults to `False`.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Example**

Copied!

`# Create a single transformer decoder layer. decoder = keras_hub.layers.TransformerDecoder(     intermediate_dim=64, num_heads=8)  # Create a simple model containing the decoder. decoder_input = keras.Input(shape=(10, 64)) encoder_input = keras.Input(shape=(10, 64)) output = decoder(decoder_input, encoder_input) model = keras.Model(     inputs=(decoder_input, encoder_input),     outputs=output, )  # Call decoder on the inputs. decoder_input_data = np.random.uniform(size=(2, 10, 64)) encoder_input_data = np.random.uniform(size=(2, 10, 64)) decoder_output = model((decoder_input_data, encoder_input_data))`

**References**

*   [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/transformer_decoder.py#L241)

### `call` method

Copied!

`TransformerDecoder.call(     decoder_sequence,     encoder_sequence=None,     decoder_padding_mask=None,     decoder_attention_mask=None,     encoder_padding_mask=None,     encoder_attention_mask=None,     self_attention_cache=None,     self_attention_cache_update_index=None,     cross_attention_cache=None,     cross_attention_cache_update_index=None,     use_causal_mask=True,     training=None, )`

Forward pass of the TransformerDecoder.

**Arguments**

*   **decoder\_sequence**: a Tensor. The decoder input sequence.
*   **encoder\_sequence**: a Tensor. The encoder input sequence. For decoder only models (like GPT2), this should be left `None`. Once the model is called once without an encoder\_sequence, you cannot call it again with encoder\_sequence.
*   **decoder\_padding\_mask**: a boolean Tensor, the padding mask of decoder sequence, must be of shape `[batch_size, decoder_sequence_length]`.
*   **decoder\_attention\_mask**: a boolean Tensor. Customized decoder sequence mask, must be of shape `[batch_size, decoder_sequence_length, decoder_sequence_length]`
*   **encoder\_padding\_mask**: a boolean Tensor, the padding mask of encoder sequence, must be of shape `[batch_size, encoder_sequence_length]`.
*   **encoder\_attention\_mask**: a boolean Tensor. Customized encoder sequence mask, must be of shape `[batch_size, encoder_sequence_length, encoder_sequence_length]`
*   **self\_attention\_cache**: a dense float Tensor. The cache of key/values pairs in the self-attention layer. Has shape `[batch_size, 2, max_seq_len, num_heads, key_dims]`.
*   **self\_attention\_cache\_update\_index**: an int or int Tensor, the index at which to update the `self_attention_cache`. Usually, this is the index of the current token being processed during decoding.
*   **cross\_attention\_cache**: a dense float Tensor. The cache of key/value pairs in the cross-attention layer. Has shape `[batch_size, 2, S, num_heads, key_dims]`.
*   **cross\_attention\_cache\_update\_index**: an int or int Tensor, the index at which to update the `cross_attention_cache`. Usually, this is either `0` (compute the entire `cross_attention_cache`), or `None` (reuse a previously computed `cross_attention_cache`).
*   **use\_causal\_mask**: bool, defaults to `True`. If true, a causal mask (masking out future input) is applied \`on the decoder sequence.
*   **training**: a boolean indicating whether the layer should behave in training mode or in inference mode.

**Returns**

*   **One of three things, depending on call arguments**:
*   `outputs`, if `self_attention_cache` is \`None.
*   `(outputs, self_attention_cache)`, if `self_attention_cache` is set and the layer has no cross-attention.
*   `(outputs, self_attention_cache, cross_attention_cache)`, if `self_attention_cache` and `cross_attention_cache` are set and the layer has cross-attention.

* * *

[TransformerDecoder layer](https://keras.io/keras_hub/api/modeling_layers/transformer_decoder/#transformerdecoder-layer)

[`TransformerDecoder` class](https://keras.io/keras_hub/api/modeling_layers/transformer_decoder/#transformerdecoder-class)

[`call` method](https://keras.io/keras_hub/api/modeling_layers/transformer_decoder/#call-method)