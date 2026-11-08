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
 / EinsumDense layer

EinsumDense layer
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/einsum_dense.py#L26)

### `EinsumDense` class

Copied!

`keras.layers.EinsumDense(     equation,     output_shape,     activation=None,     bias_axes=None,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     lora_rank=None,     lora_alpha=None,     gptq_unpacked_column_size=None,     quantization_config=None,     **kwargs )`

A layer that uses `einsum` as the backing computation.

This layer can perform einsum calculations of arbitrary dimensionality.

**Arguments**

*   **equation**: An equation describing the einsum to perform. This equation must be a valid einsum string of the form `ab,bc->ac`, `...ab,bc->...ac`, or `ab...,bc->ac...` where 'ab', 'bc', and 'ac' can be any valid einsum axis expression sequence.
*   **output\_shape**: The expected shape of the output tensor (excluding the batch dimension and any dimensions represented by ellipses). You can specify `None` for any dimension that is unknown or can be inferred from the input shape.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (that is, a "linear" activation: `a(x) = x`).
*   **bias\_axes**: A string containing the output dimension(s) to apply a bias to. Each character in the `bias_axes` string should correspond to a character in the output portion of the `equation` string.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix.
*   **bias\_initializer**: Initializer for the bias vector.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix.
*   **bias\_regularizer**: Regularizer function applied to the bias vector.
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix.
*   **bias\_constraint**: Constraint function applied to the bias vector.
*   **lora\_rank**: Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's kernel to non-trainable and replaces it with a delta over the original kernel, obtained via multiplying two lower-rank trainable matrices (the factorization happens on the last dimension). This can be useful to reduce the computation cost of fine-tuning large dense layers. You can also enable LoRA on an existing `EinsumDense` layer by calling `layer.enable_lora(rank)`. lora\_alpha: Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`.
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.

**Examples**

**Biased dense layer with einsums**

This example shows how to instantiate a standard Keras dense layer using einsum operations. This example is equivalent to `keras.layers.Dense(64, use_bias=True)`.

Copied!

`>>> layer = keras.layers.EinsumDense("ab,bc->ac", ...                                       output_shape=64, ...                                       bias_axes="c") >>> input_tensor = keras.Input(shape=[32]) >>> output_tensor = layer(input_tensor) >>> output_tensor.shape (None, 64)`

**Applying a dense layer to a sequence**

This example shows how to instantiate a layer that applies the same dense operation to every element in a sequence. Here, the `output_shape` has two values (since there are two non-batch dimensions in the output); the first dimension in the `output_shape` is `None`, because the sequence dimension `b` has an unknown shape.

Copied!

`>>> layer = keras.layers.EinsumDense("abc,cd->abd", ...                                       output_shape=(None, 64), ...                                       bias_axes="d") >>> input_tensor = keras.Input(shape=[32, 128]) >>> output_tensor = layer(input_tensor) >>> output_tensor.shape (None, 32, 64)`

**Applying a dense layer to a sequence using ellipses**

This example shows how to instantiate a layer that applies the same dense operation to every element in a sequence, but uses the ellipsis notation instead of specifying the batch and sequence dimensions.

Because we are using ellipsis notation and have specified only one axis, the `output_shape` arg is a single value. When instantiated in this way, the layer can handle any number of sequence dimensions - including the case where no sequence dimension exists.

Copied!

`>>> layer = keras.layers.EinsumDense("...x,xy->...y", ...                                       output_shape=64, ...                                       bias_axes="y") >>> input_tensor = keras.Input(shape=[32, 128]) >>> output_tensor = layer(input_tensor) >>> output_tensor.shape (None, 32, 64)`

* * *

[EinsumDense layer](https://keras.io/api/layers/core_layers/einsum_dense/#einsumdense-layer)

[`EinsumDense` class](https://keras.io/api/layers/core_layers/einsum_dense/#einsumdense-class)