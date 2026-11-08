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
 / [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 / UpSampling1D layer

UpSampling1D layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/up_sampling1d.py#L7)

### `UpSampling1D` class

Copied!

`keras.layers.UpSampling1D(size=2, **kwargs)`

Upsampling layer for 1D inputs.

Repeats each temporal step `size` times along the time axis.

**Example**

Copied!

`>>> input_shape = (2, 2, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> x [[[ 0  1  2]   [ 3  4  5]]  [[ 6  7  8]   [ 9 10 11]]] >>> y = keras.layers.UpSampling1D(size=2)(x) >>> y [[[ 0.  1.  2.]   [ 0.  1.  2.]   [ 3.  4.  5.]   [ 3.  4.  5.]]  [[ 6.  7.  8.]   [ 6.  7.  8.]   [ 9. 10. 11.]   [ 9. 10. 11.]]]`

**Arguments**

*   **size**: Integer. Upsampling factor.

**Input shape**

3D tensor with shape: `(batch_size, steps, features)`.

**Output shape**

3D tensor with shape: `(batch_size, upsampled_steps, features)`.

* * *

[UpSampling1D layer](https://keras.io/api/layers/reshaping_layers/up_sampling1d/#upsampling1d-layer)

[`UpSampling1D` class](https://keras.io/api/layers/reshaping_layers/up_sampling1d/#upsampling1d-class)