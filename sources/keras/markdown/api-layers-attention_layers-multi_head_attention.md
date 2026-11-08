None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Attention layers](https://keras.io/api/layers/attention_layers/)
 / MultiHeadAttention layer

MultiHeadAttention layer
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/multi_head_attention.py#L19)

### `MultiHeadAttention` class

Copied!

`keras.layers.MultiHeadAttention(     num_heads,     key_dim,     value_dim=None,     dropout=0.0,     use_bias=True,     output_shape=None,     attention_axes=None,     sliding_window=None,     flash_attention=None,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     use_gate=False,     seed=None,     **kwargs )`

MultiHeadAttention layer.

This is an implementation of multi-headed attention as described in the paper "Attention is all you Need" [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
. If `query`, `key,` `value` are the same, then this is self-attention. Each timestep in `query` attends to the corresponding sequence in `key`, and returns a fixed-width vector.

This layer first projects `query`, `key` and `value`. These are (effectively) a list of tensors of length `num_attention_heads`, where the corresponding shapes are `(batch_size, <query dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, value_dim)`.

Then, the query and key tensors are dot-producted and scaled. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities, then concatenated back to a single tensor.

Finally, the result tensor with the last dimension as `value_dim` can take a linear projection and return.

**Arguments**

*   **num\_heads**: Number of attention heads.
*   **key\_dim**: Size of each attention head for query and key.
*   **value\_dim**: Size of each attention head for value.
*   **dropout**: Dropout probability.
*   **use\_bias**: Boolean, whether the dense layers use bias vectors/matrices.
*   **output\_shape**: The expected shape of an output tensor, besides the batch and sequence dims. If not specified, projects back to the query feature dim (the query input's last dimension).
*   **attention\_axes**: axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features.
*   **sliding\_window**: Optional positive integer. If set, restricts each query position to attend only to key positions within `sliding_window - 1` of itself (a symmetric band). Composes naturally with `use_causal_mask=True` to give the causal sliding window used by Mistral, Llama-3 long-context, and Phi-3. Defaults to `None` (full attention).
*   **flash\_attention**: If `None`, the layer attempts to use flash attention for faster and more memory-efficient attention computations when possible. This behavior can be configured using `keras.config.enable_flash_attention()` or `keras.config.disable_flash_attention()`.
*   **kernel\_initializer**: Initializer for dense layer kernels.
*   **bias\_initializer**: Initializer for dense layer biases.
*   **kernel\_regularizer**: Regularizer for dense layer kernels.
*   **bias\_regularizer**: Regularizer for dense layer biases.
*   **activity\_regularizer**: Regularizer for dense layer activity.
*   **kernel\_constraint**: Constraint for dense layer kernels.
*   **bias\_constraint**: Constraint for dense layer kernels.
*   **use\_gate**: Boolean, whether to apply a gated attention mechanism. When True, an additional gating branch is added based on the (Gated Attention for Large Language Models)\[https://arxiv.org/abs/2505.06708\]. It applies a sigmoid-activated linear projection to the query which then gates the attention output. This helps improve training stability and eliminates "attention sinks".
*   **seed**: Optional integer to seed the dropout layer.

**Call arguments**

*   **query**: Query tensor of shape `(B, T, dim)`, where `B` is the batch size, `T` is the target sequence length, and dim is the feature dimension.
*   **value**: Value tensor of shape `(B, S, dim)`, where `B` is the batch size, `S` is the source sequence length, and dim is the feature dimension.
*   **key**: Optional key tensor of shape `(B, S, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case.
*   **attention\_mask**: a boolean mask of shape `(B, T, S)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension.
*   **return\_attention\_scores**: A boolean to indicate whether the output should be `(attention_output, attention_scores)` if `True`, or `attention_output` if `False`. Defaults to `False`.
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Will go with either using the training mode of the parent layer/model, or `False` (inference) if there is no parent layer.
*   **use\_causal\_mask**: A boolean to indicate whether to apply a causal mask to prevent tokens from attending to future tokens (e.g., used in a decoder Transformer).

**Returns**

*   **attention\_output**: The result of the computation, of shape `(B, T, E)`, where `T` is for target sequence shapes and `E` is the query input last dimension if `output_shape` is `None`. Otherwise, the multi-head outputs are projected to the shape specified by `output_shape`.
*   **attention\_scores**: (Optional) multi-head attention coefficients over attention axes.

* * *

[MultiHeadAttention layer](https://keras.io/api/layers/attention_layers/multi_head_attention/#multiheadattention-layer)

[`MultiHeadAttention` class](https://keras.io/api/layers/attention_layers/multi_head_attention/#multiheadattention-class)