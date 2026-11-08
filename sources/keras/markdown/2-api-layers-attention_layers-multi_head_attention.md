None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Layers API](https://keras.io/2/api/layers/)
 / [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 / MultiHeadAttention layer

MultiHeadAttention layer
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/attention/multi_head_attention.py#L130)

### `MultiHeadAttention` class

Copied!

`tf_keras.layers.MultiHeadAttention(     num_heads,     key_dim,     value_dim=None,     dropout=0.0,     use_bias=True,     output_shape=None,     attention_axes=None,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

MultiHeadAttention layer.

This is an implementation of multi-headed attention as described in the paper "Attention is all you Need" (Vaswani et al., 2017). If `query`, `key,` `value` are the same, then this is self-attention. Each timestep in `query` attends to the corresponding sequence in `key`, and returns a fixed-width vector.

This layer first projects `query`, `key` and `value`. These are (effectively) a list of tensors of length `num_attention_heads`, where the corresponding shapes are `(batch_size, <query dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, value_dim)`.

Then, the query and key tensors are dot-producted and scaled. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities, then concatenated back to a single tensor.

Finally, the result tensor with the last dimension as value\_dim can take an linear projection and return.

When using `MultiHeadAttention` inside a custom layer, the custom layer must implement its own `build()` method and call `MultiHeadAttention`'s `_build_from_signature()` there. This enables weights to be restored correctly when the model is loaded.

**Examples**

Performs 1D cross-attention over two sequence inputs with an attention mask. Returns the additional attention weights over heads.

Copied!

`>>> layer = MultiHeadAttention(num_heads=2, key_dim=2) >>> target = tf.keras.Input(shape=[8, 16]) >>> source = tf.keras.Input(shape=[4, 16]) >>> output_tensor, weights = layer(target, source, ...                                return_attention_scores=True) >>> print(output_tensor.shape) (None, 8, 16) >>> print(weights.shape) (None, 2, 8, 4)`

Performs 2D self-attention over a 5D input tensor on axes 2 and 3.

Copied!

`>>> layer = MultiHeadAttention( ...     num_heads=2, key_dim=2, attention_axes=(2, 3)) >>> input_tensor = tf.keras.Input(shape=[5, 3, 4, 16]) >>> output_tensor = layer(input_tensor, input_tensor) >>> print(output_tensor.shape) (None, 5, 3, 4, 16)`

**Arguments**

*   **num\_heads**: Number of attention heads.
*   **key\_dim**: Size of each attention head for query and key.
*   **value\_dim**: Size of each attention head for value.
*   **dropout**: Dropout probability.
*   **use\_bias**: Boolean, whether the dense layers use bias vectors/matrices.
*   **output\_shape**: The expected shape of an output tensor, besides the batch and sequence dims. If not specified, projects back to the query feature dim (the query input's last dimension).
*   **attention\_axes**: axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features.
*   **kernel\_initializer**: Initializer for dense layer kernels.
*   **bias\_initializer**: Initializer for dense layer biases.
*   **kernel\_regularizer**: Regularizer for dense layer kernels.
*   **bias\_regularizer**: Regularizer for dense layer biases.
*   **activity\_regularizer**: Regularizer for dense layer activity.
*   **kernel\_constraint**: Constraint for dense layer kernels.
*   **bias\_constraint**: Constraint for dense layer kernels.

**Call arguments**

*   **query**: Query `Tensor` of shape `(B, T, dim)`.
*   **value**: Value `Tensor` of shape `(B, S, dim)`.
*   **key**: Optional key `Tensor` of shape `(B, S, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case.
*   **attention\_mask**: a boolean mask of shape `(B, T, S)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension.
*   **return\_attention\_scores**: A boolean to indicate whether the output should be `(attention_output, attention_scores)` if `True`, or `attention_output` if `False`. Defaults to `False`.
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Will go with either using the training mode of the parent layer/model, or False (inference) if there is no parent layer.
*   **use\_causal\_mask**: A boolean to indicate whether to apply a causal mask to prevent tokens from attending to future tokens (e.g., used in a decoder Transformer).

**Returns**

*   **attention\_output**: The result of the computation, of shape `(B, T, E)`, where `T` is for target sequence shapes and `E` is the query input last dimension if `output_shape` is `None`. Otherwise, the multi-head outputs are projected to the shape specified by `output_shape`.
*   **attention\_scores**: \[Optional\] multi-head attention coefficients over attention axes.

* * *

[MultiHeadAttention layer](https://keras.io/2/api/layers/attention_layers/multi_head_attention/#multiheadattention-layer)

[`MultiHeadAttention` class](https://keras.io/2/api/layers/attention_layers/multi_head_attention/#multiheadattention-class)