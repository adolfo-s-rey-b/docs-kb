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
 / Attention layer

Attention layer
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/attention.py#L8)

### `Attention` class

Copied!

`keras.layers.Attention(     use_scale=False, score_mode="dot", dropout=0.0, seed=None, **kwargs )`

Dot-product attention layer, a.k.a. Luong-style attention.

Inputs are a list with 2 or 3 elements: 1. A `query` tensor of shape `(batch_size, Tq, dim)`. 2. A `value` tensor of shape `(batch_size, Tv, dim)`. 3. A optional `key` tensor of shape `(batch_size, Tv, dim)`. If none supplied, `value` will be used as a `key`.

The calculation follows the steps: 1. Calculate attention scores using `query` and `key` with shape `(batch_size, Tq, Tv)`. 2. Use scores to calculate a softmax distribution with shape `(batch_size, Tq, Tv)`. 3. Use the softmax distribution to create a linear combination of `value` with shape `(batch_size, Tq, dim)`.

**Arguments**

*   **use\_scale**: If `True`, will create a scalar variable to scale the attention scores.
*   **dropout**: Float between 0 and 1. Fraction of the units to drop for the attention scores. Defaults to `0.0`.
*   **seed**: A Python integer to use as random seed in case of `dropout`.
*   **score\_mode**: Function to use to compute attention scores, one of `{"dot", "concat"}`. `"dot"` refers to the dot product between the query and key vectors. `"concat"` refers to the hyperbolic tangent of the concatenation of the `query` and `key` vectors.

**Call arguments**

*   **inputs**: List of the following tensors:
    *   `query`: Query tensor of shape `(batch_size, Tq, dim)`.
    *   `value`: Value tensor of shape `(batch_size, Tv, dim)`.
    *   `key`: Optional key tensor of shape `(batch_size, Tv, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case.
*   **mask**: List of the following tensors:
    *   `query_mask`: A boolean mask tensor of shape `(batch_size, Tq)`. If given, the output will be zero at the positions where `mask==False`.
    *   `value_mask`: A boolean mask tensor of shape `(batch_size, Tv)`. If given, will apply the mask such that values at positions where `mask==False` do not contribute to the result.
*   **return\_attention\_scores**: bool, it `True`, returns the attention scores (after masking and softmax) as an additional output argument.
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout).
*   **use\_causal\_mask**: Boolean. Set to `True` for decoder self-attention. Adds a mask such that position `i` cannot attend to positions `j > i`. This prevents the flow of information from the future towards the past. Defaults to `False`.

Output: Attention outputs of shape `(batch_size, Tq, dim)`. (Optional) Attention scores after masking and softmax with shape `(batch_size, Tq, Tv)`.

* * *

[Attention layer](https://keras.io/api/layers/attention_layers/attention/#attention-layer)

[`Attention` class](https://keras.io/api/layers/attention_layers/attention/#attention-class)