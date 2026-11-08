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
 / [Core layers](https://keras.io/api/layers/core_layers/)
 / Dense layer

Dense layer
===========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/dense.py#L20)

### `Dense` class

Copied!

`keras.layers.Dense(     units,     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     lora_rank=None,     lora_alpha=None,     quantization_config=None,     **kwargs )`

Just your regular densely-connected NN layer.

`Dense` implements the operation: `output = activation(dot(input, kernel) + bias)` where `activation` is the element-wise activation function passed as the `activation` argument, `kernel` is a weights matrix created by the layer, and `bias` is a bias vector created by the layer (only applicable if `use_bias` is `True`). When this layer is followed by a `BatchNormalization` layer, it is recommended to set `use_bias=False` as `BatchNormalization` has its own bias term.

Note: If the input to the layer has a rank greater than 2, `Dense` computes the dot product between the `inputs` and the `kernel` along the last axis of the `inputs` and axis 0 of the `kernel` (using [`tf.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)
). For example, if input has dimensions `(batch_size, d0, d1)`, then we create a `kernel` with shape `(d1, units)`, and the `kernel` operates along axis 2 of the `input`, on every sub-tensor of shape `(1, 1, d1)` (there are `batch_size * d0` such sub-tensors). The output in this case will have shape `(batch_size, d0, units)`.

**Arguments**

*   **units**: Positive integer, dimensionality of the output space.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **use\_bias**: Boolean, whether the layer uses a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix.
*   **bias\_initializer**: Initializer for the bias vector.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix.
*   **bias\_regularizer**: Regularizer function applied to the bias vector.
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation").
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix.
*   **bias\_constraint**: Constraint function applied to the bias vector.
*   **lora\_rank**: Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's kernel to non-trainable and replaces it with a delta over the original kernel, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large dense layers. You can also enable LoRA on an existing `Dense` layer by calling `layer.enable_lora(rank)`.
*   **lora\_alpha**: Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`.

**Input shape**

N-D tensor with shape: `(batch_size, ..., input_dim)`. The most common situation would be a 2D input with shape `(batch_size, input_dim)`.

**Output shape**

N-D tensor with shape: `(batch_size, ..., units)`. For instance, for a 2D input with shape `(batch_size, input_dim)`, the output would have shape `(batch_size, units)`.

* * *

[Dense layer](https://keras.io/api/layers/core_layers/dense/#dense-layer)

[`Dense` class](https://keras.io/api/layers/core_layers/dense/#dense-class)