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
 / GroupQueryAttention

GroupQueryAttention
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/grouped_query_attention.py#L16)

### `GroupedQueryAttention` class

Copied!

`keras.layers.GroupQueryAttention(     head_dim,     num_query_heads,     num_key_value_heads,     dropout=0.0,     use_bias=True,     sliding_window=None,     flash_attention=None,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     use_gate=False,     seed=None,     **kwargs )`

Grouped Query Attention layer.

This is an implementation of grouped-query attention introduced by [Ainslie et al., 2023](https://arxiv.org/abs/2305.13245)
. Here `num_key_value_heads` denotes number of groups, setting `num_key_value_heads` to 1 is equivalent to multi-query attention, and when `num_key_value_heads` is equal to `num_query_heads` it is equivalent to multi-head attention.

This layer first projects `query`, `key`, and `value` tensors. Then, `key` and `value` are repeated to match the number of heads of `query`.

Then, the `query` is scaled and dot-producted with `key` tensors. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities and concatenated back to a single tensor.

**Arguments**

*   **head\_dim**: Size of each attention head.
*   **num\_query\_heads**: Number of query attention heads.
*   **num\_key\_value\_heads**: Number of key and value attention heads.
*   **dropout**: Dropout probability.
*   **use\_bias**: Boolean, whether the dense layers use bias vectors/matrices.
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

*   **query**: Query tensor of shape `(batch_dim, target_seq_len, feature_dim)`, where `batch_dim` is batch size, `target_seq_len` is the length of target sequence, and `feature_dim` is dimension of feature.
*   **value**: Value tensor of shape `(batch_dim, source_seq_len, feature_dim)`, where `batch_dim` is batch size, `source_seq_len` is the length of source sequence, and `feature_dim` is dimension of feature.
*   **key**: Optional key tensor of shape `(batch_dim, source_seq_len, feature_dim)`. If not given, will use `value` for both `key` and `value`, which is most common case.
*   **attention\_mask**: A boolean mask of shape `(batch_dim, target_seq_len, source_seq_len)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, where 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension.
*   **return\_attention\_scores**: A boolean to indicate whether the output should be `(attention_output, attention_scores)` if `True`, or `attention_output` if `False`. Defaults to `False`.
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Will go with either using the training mode of the parent layer/model or `False` (inference) if there is no parent layer.
*   **use\_causal\_mask**: A boolean to indicate whether to apply a causal mask to prevent tokens from attending to future tokens (e.g., used in a decoder Transformer).

**Returns**

*   **attention\_output**: Result of the computation, of shape `(batch_dim, target_seq_len, feature_dim)`, where `target_seq_len` is for target sequence length and `feature_dim` is the query input last dim.
*   **attention\_scores**: (Optional) attention coefficients of shape `(batch_dim, num_query_heads, target_seq_len, source_seq_len)`.

* * *

[GroupQueryAttention](https://keras.io/api/layers/attention_layers/group_query_attention/#groupqueryattention)

[`GroupedQueryAttention` class](https://keras.io/api/layers/attention_layers/group_query_attention/#groupedqueryattention-class)