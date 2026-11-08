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
 / [Merging layers](https://keras.io/api/layers/merging_layers/)
 / Dot layer

Dot layer
=========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/dot.py#L198)

### `Dot` class

Copied!

`keras.layers.Dot(axes, normalize=False, **kwargs)`

Computes element-wise dot product of two tensors.

It takes a list of inputs of size 2, and the axes corresponding to each input along with the dot product is to be performed.

Let's say `x` and `y` are the two input tensors with shapes `(2, 3, 5)` and `(2, 10, 3)`. The batch dimension should be of same size for both the inputs, and `axes` should correspond to the dimensions that have the same size in the corresponding inputs. e.g. with `axes=(1, 2)`, the dot product of `x`, and `y` will result in a tensor with shape `(2, 5, 10)`

**Example**

Copied!

`>>> x = np.arange(10).reshape(1, 5, 2) >>> y = np.arange(10, 20).reshape(1, 2, 5) >>> keras.layers.Dot(axes=(1, 2))([x, y])`

Usage in a Keras model:

Copied!

`>>> x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2)) >>> x2 = keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2)) >>> y = keras.layers.Dot(axes=1)([x1, x2])`

**Arguments**

*   **axes**: Integer or tuple of integers, axis or axes along which to take the dot product. If a tuple, should be two integers corresponding to the desired axis from the first input and the desired axis from the second input, respectively. Note that the size of the two selected axes must match, and that axis `0` (the batch axis) cannot be included.
*   **normalize**: Whether to L2-normalize samples along the dot product axis before taking the dot product. If set to `True`, then the output of the dot product is the cosine proximity between the two samples.
*   **\*\*kwargs**: Standard layer keyword arguments.

**Returns**

A tensor, the dot product of the samples from the inputs.

* * *

[Dot layer](https://keras.io/api/layers/merging_layers/dot/#dot-layer)

[`Dot` class](https://keras.io/api/layers/merging_layers/dot/#dot-class)